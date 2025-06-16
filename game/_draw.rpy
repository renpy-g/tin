
init -10 python in draw_logic:

    import os
    import io
    import math
    import hashlib
    import store
    import enum
    import pygame_sdl2 as pygame
    from os import path

    

    class Point(object):

        # __author__ = "Vladya"

        def __init__(self, x, y, st, color, width):

            self.__x, self.__y = map(int, (x, y))
            self.__st = abs(float(st))

            self.__color = renpy.color.Color(color)
            self.__width = abs(2)       # 크기 조절

        @property
        def x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

        @property
        def st(self):
            return self.__st

        @property
        def color(self):
            return self.__color

        @property
        def width(self):
            return self.__width

    class Draw(renpy.Displayable):

        DRAW_BUTTON = 1

        def __init__(self, background, reference=None, **properties):

            super(Draw, self).__init__(**properties)

            self.__background = self._get_displayable(background)

            self.__curves = []
            self.__active_curve = None
            self.__delete_log = []

            self.__color = renpy.color.Color("#000")

            if reference is not None:
                self.__reference = self._get_displayable(reference)
            else:
                self.__reference = None
            self.__show_reference = False

            self.__size = None
            self.__end_interact_request = False

        @classmethod
        def main(
            cls,
            background=None,        # 이미지 넣기 가능?
            reference=None,
            start_width=5,
            start_color=renpy.color.Color("#000"),
            **transform_prop
        ):

            if background is None:
                background = "images/backgrounds/prayBg/wrist_3.png"
                # background = "#fff"
                # 크기 잘 맞추기

            if transform_prop:
                background = store.Transform(background, **transform_prop)

            draw_object = cls(background, reference)
            if start_width:
                draw_object.set_width(start_width)
            if start_color:
                draw_object.set_color(start_color)

            _screen_name = "_draw_screen"

            renpy.mode("screen")
            renpy.show_screen(_screen_name, draw_object, _transient=True)
            # roll_forward = renpy.roll_forward_info()

            try:
                rv = renpy.ui.interact(
                    mouse="screen",
                    type="screen",
                    suppress_overlay=True,
                    suppress_window=True,
                    # roll_forward=roll_forward
                )
            except (renpy.game.JumpException, renpy.game.CallException) as ex:
                rv = ex


            return rv

        # 완료?
        def _disable(self):
            self.__end_interact_request = True
            renpy.redraw(self, .0)

        @staticmethod
        def _get_displayable(data):
            result = renpy.displayable(data)
            if not isinstance(result, renpy.display.core.Displayable):
                raise ValueError("{0} isn't a displayable.".format(data))
            return result

        @property
        def reference(self):
            return self.__reference

        @property
        def reference_switcher(self):
            return self.__show_reference

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, new_width):
            self.__width = int(new_width)

        def draw_all(self, canvas):

            for curve in self.__curves:

                if not curve:
                    continue

                elif len(curve) == 1:
                    point = curve[0]
                    canvas.circle(
                        point.color,
                        (point.x, point.y),
                        (point.width // 2)
                    )

                else:
                    prev = None
                    for point in curve:
                        if prev:
                            canvas.line(
                                prev.color,
                                (prev.x, prev.y),
                                (point.x, point.y),
                                prev.width
                            )
                        prev = point

        def add_point(self, x, y, st):
            point = Point(x, y, st, self.__color, self.__width)
            if self.__active_curve is None:
                self.__active_curve = []
                self.__curves.append(self.__active_curve)
                self.__delete_log.clear()
            self.__active_curve.append(point)
            renpy.redraw(self, .0)


        def set_color(self, color):
            self.__color = renpy.color.Color(color)

        def set_width(self, width):
            self.width = width


        def event(self, ev, x, y, st):

            if not self.__size:
                return

            w, h = self.__size
            in_area = False
            if (0 <= x < w) and (0 <= y < h):
                in_area = True

            if in_area and (ev.type == pygame.MOUSEMOTION):
                if self.__is_pressed:
                    self.add_point(x, y, st)

            elif in_area and (ev.type == pygame.MOUSEBUTTONDOWN):
                if ev.button == self.DRAW_BUTTON:
                    self.__is_pressed = True
                    self.add_point(x, y, st)
                    raise renpy.IgnoreEvent()

            elif ev.type == pygame.MOUSEBUTTONUP:
                if ev.button == self.DRAW_BUTTON:
                    self.__is_pressed = False
                    self.__active_curve = None

        def per_interact(self):
            self.__is_pressed = False
            self.__active_curve = None
            renpy.redraw(self, .0)

        def render(self, *rend_args):

            back = renpy.render(self.__background, *rend_args)
            w, h = self.__size = tuple(map(int, back.get_size()))

            result = renpy.Render(w, h)
            result.blit(back, (0, 0))

            if self.reference and self.reference_switcher:
                rend = renpy.render(self.reference, *rend_args)
                x = (float(result.width) * .5) - (float(rend.width) * .5)
                y = (float(result.height) * .5) - (float(rend.height) * .5)
                x, y = map(int, (x, y))
                result.blit(rend, (x, y))

            canvas = result.canvas()
            self.draw_all(canvas)

            if self.__end_interact_request:
                self.__end_interact_request = False
                # disp = self.get_canvas_as_disp(canvas)
                disp = "yes"      # 이걸 바꾸면 됨
                renpy.end_interaction(disp)


            return result




screen _draw_screen(draw_object):

    # 회색그림판
    frame:
        add draw_object:
            align (.5, .5)

    frame:
        xalign 1.0
        yalign 1.0
        xsize 100
        ysize 50
        textbutton _("Done"):
            action Function(draw_object._disable)
            xalign .5
