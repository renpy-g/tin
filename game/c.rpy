transform scrollup_credit:
    ypos 1. yanchor .0
    linear 10. ypos .0 yanchor 1.

screen scrolluptest:
    vbox at scrollup_credit:
        xalign .5
        for n, i in enumerate(displays):
            text i xalign .5


define displays=["{size=40}제작",  "{size=25}모르는아이\n\n",  "{size=40}글", "{size=25}모르는아이\n\n",  "{size=40}그림",  "{size=25}일라",  "{size=25}멩멩멩\n\n",   "{size=40}출연", "{size=25}[you]", "{size=25}[lamb]"]



label credits:
    # 밑에 메뉴 없애기
    $ nn = 1

    image theend = Text("{size=50}The End", text_align=0.5)
    image thanks = Text("{size=50}플레이 해주셔서 감사합니다!", text_align=0.5)

    # 마우스 좌클릭 불허 설정
    $ use_click(False)

    scene black with dissolve

    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend

    show screen scrolluptest
    # 알아서 초 계산하기....
    pause(11)

    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide thanks

    # 0.1초뒤에 마우스 좌클릭 허용 설정
    $ threading.Timer(0.1, use_click, [True]).start()

    # 메인 메뉴 강제 이동
    $ renpy.full_restart()


    