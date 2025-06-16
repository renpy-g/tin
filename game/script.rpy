define config.name = _('인도')

define gui.show_name = True

# 틴데라이
define T = Character("[lamb]", color="#FA58D0")

# 이미지
image bg1 = "images/backgrounds/background1.jpg"

init python:
    
    # config.keymap['rollback'].clear()   # 스크롤 시 되감기 금지
    hide_image = None
    new = None
    
    def change_image(new_image, with_ = Dissolve(0.2)):
        global hide_image
        global new
        new = new_image
        
        if hide_image is not None:  # 이전 이미지가 있을 때만 숨김
            renpy.hide(hide_image)  # 이전 이미지를 숨김
        renpy.show(new)

        # 전환 효과를 추가할 거냐 말거냐
        if with_:
            renpy.transition(with_)
            
        hide_image = new

        # 이거 $ change_image 밑에 넣으면 됨
        # show expression AlphaMask("black70", At(new, center)) as mask at multiply
        # 숨길 땐 hide mask
    #### 함수퍼옴
    import threading
    
    def use_click(bUseyn):
        if bUseyn:  #마우스 좌클릭 허용
            config.keymap['dismiss'].append('mouseup_1')
            if 'mouseup_1' in config.keymap['button_ignore']:
                config.keymap['button_ignore'].remove('mouseup_1')
            if 'mousedown_1' in config.keymap['button_ignore']:
                config.keymap['button_ignore'].remove('mousedown_1')
                
        else: #마우스 좌클릭 불허
            if 'mouseup_1' in config.keymap['dismiss']:
                config.keymap['dismiss'].remove('mouseup_1')
                
            if 'mouseup_1' not in config.keymap['button_ignore']:
                config.keymap['button_ignore'].append('mouseup_1')
            
            if 'mousedown_1' not in config.keymap['button_ignore']:
                config.keymap['button_ignore'].append('mousedown_1')
            
        renpy.clear_keymap_cache() #설정된 키맵 바로 적용하기


    # label 안에 넣어서 쓰면 된대
    # 마우스 좌클릭 불허 설정
    # $ use_click(False)
    
    # 3초뒤에 마우스 좌클릭 허용 설정
    # $ threading.Timer(3, use_click, [True]).start()
    ##########

    
# 받침유무판별기
# 수정: 파이썬 3.0부터는 유니코드가 기본
    def finalChecker(myname):
        dec = ord(myname[-1]) - ord('가')

        if dec % 28 == 0:
            return False
        else:
            return True

    def ppCommon(tag, argument, contents):
        (kind, str) = contents[-1]
        if finalChecker(str):
            return contents + [(renpy.TEXT_TEXT, tag[0])]
        else:
            return contents + [(renpy.TEXT_TEXT, tag[1])]

    def ppRang(tag, argument, contents):
        (kind, str) = contents[-1]
        if finalChecker(str):
            return contents + [(renpy.TEXT_TEXT, "이랑")]  
        else:
            return contents + [(renpy.TEXT_TEXT, "랑")]  

    config.custom_text_tags["은는"] = ppCommon
    config.custom_text_tags["이가"] = ppCommon
    config.custom_text_tags["을를"] = ppCommon
    config.custom_text_tags["과와"] = ppCommon
    config.custom_text_tags["이랑"] = ppRang  
    config.custom_text_tags["랑"] = ppRang 

init:

    image black70 = "#00000070" #불투명도 70인 검정색

    transform multiply(child): #곱하기
        Transform(child, gl_blend_func=config.gl_blend_func["multiply"])

    $ randtext = 1
    $ you = "you"
    $ lamb = "lamb"
    $ nn = 0  #엔딩크레딧용

    # 아그넬로와 엘시
    $ love = False
    
    $ belief = 30  # 틴의 믿음
    # 일 수
    $ day = 1

    # 히든 조절
    $ hidd = 1
    $ hDay = 1

    # 틴의 혼잣말들 
    define dialogue = ""
    define dialogue_list = ["우리 아버지는, 어, 엄하셨지만,\n많은, 걸 알려주셨어.", "난 정말 바보야...", "어머니. 아, 안타까운 분.", "나도 사랑받고 싶어...", "보, 보여? 형제, 형제가, 날 죽이려 해...", "다 내가 망가져버려서...", "살려주세요.", "저장은 틈틈이 해.", "늘 울어서 계속 목이 말라."]
    
    $ sang = False  # 외출 상 받기
    $ go = False    # 의식에서 쫓겨나기 확인용
    $ sleep = False # 의식 같이 자기
    $ kill = False  # 그애 죽이기

    transform jump_motion:
        yoffset 80  # 아래로 10px 이동
        linear 3   # 0.1초 동안 위로 이동
        yoffset 0    # 다시 원래 위치로 돌아옴
        linear 3   # 0.1초 동안 돌아옴

    # hide hi_1
    # show smail_3 at Position(xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5)
    # show smail_3 at jump_motion
    # 이런 식...

    # 흔들리기이
    # 양옆
    transform shake:
        xalign 0.5 yalign 1.0  # 중심 기준
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        xoffset 0  # 초기 위치로 복원

    # 위아래
    transform ouch_sm:
        xalign 0.5 yalign 1.0  # 중심 기준
        linear 0.05 yoffset -2
        linear 0.05 yoffset 5
        linear 0.05 yoffset -1
        yoffset 0  # 초기 위치로 복원

    transform ouch_big:
        xalign 0.5 yalign 1.0  # 중심 기준
        linear 0.05 yoffset -2
        linear 0.05 yoffset 10
        linear 0.05 yoffset -2
        linear 0.05 yoffset 10
        linear 0.05 yoffset -1
        yoffset 0  # 초기 위치로 복원

    # 쓸 때는 show 이미지 at ouch 이런 식
    # 디졸브를 넣을 수도 있음
            
screen days_text:
    add "images/backgrounds/days.png" xalign 0.05 yalign 0.05
    text "[day]일" size 30 xalign 0.07 yalign 0.09
    text "[belief]" size 13 xalign 0.08 yalign 0.148


# 이미지 버튼
screen imagebuttons:
    imagebutton:
        auto "images/backgrounds/room_menu/select_pray_%s.png" action [Hide("speech"), Hide("tinBtn2", dissolve), Hide("days_text", dissolve), Hide("hidden_days_text", dissolve), Jump("pray")]
        xpos 430
        ypos 150
        at transform:
            zoom 0.8
    imagebutton:
        auto "images/backgrounds/room_menu/select_outing_%s.png" action [Hide("speech"), Hide("tinBtn2", dissolve), Hide("days_text", dissolve), Hide("hidden_days_text", dissolve), Jump("outing")]
        xpos 200
        ypos 320
        at transform:
            zoom 0.8
    imagebutton:
        auto "images/backgrounds/room_menu/select_study_%s.png" action [Hide("speech"), Hide("tinBtn2", dissolve), Hide("days_text", dissolve), Hide("hidden_days_text", dissolve), Jump("study")]
        xpos 350
        ypos 510
        at transform:
            zoom 0.8
    imagebutton:
        auto "images/backgrounds/room_menu/select_rest_%s.png" action [Hide("speech"), Hide("tinBtn2", dissolve), Hide("days_text", dissolve), Hide("hidden_days_text", dissolve), Jump("rest")]
        xpos 1000
        ypos 90
        at transform:
            zoom 0.8
    imagebutton:
        auto "images/backgrounds/room_menu/select_sacrifice_%s.png" action [Hide("speech"), Hide("tinBtn2", dissolve), Hide("days_text", dissolve), Hide("hidden_days_text", dissolve), Jump("sacrifice")]
        xpos 800
        ypos 280
        at transform:
            zoom 0.8
    imagebutton:
        auto "images/backgrounds/room_menu/select_eat_%s.png" action [Hide("speech"), Hide("tinBtn2", dissolve), Hide("days_text", dissolve), Hide("hidden_days_text", dissolve), Jump("eat")]
        xpos 900
        ypos 450
        at transform:
            zoom 0.8
    
    
screen tinBtn:
    imagebutton:
        auto "images/characters/room/tin2_room_%s.png"
        action [ Show("tinBtn2"), Jump("schedule")]
        focus_mask True
        xpos 400
        # ypos 0
        yanchor 0.015
        at transform:
            zoom 0.49

# 랜덤 텍스트
screen speech:
    frame:
        xpadding 40
        ypadding 25
        xalign 0.55 
        yalign 0.05
        background Frame("images/backgrounds/box2.png", tile="integer")
        has vbox
        text "[dialogue]" size 17 xalign 0.55 yalign 0.05
        timer 3.0 action Hide("speech", transition=dissolve)


# 틴과 대화
screen tinBtn2:
    imagebutton:
        auto "images/characters/room/tin2_room_%s.png"
        action [SetVariable("randtext", renpy.random.randint(0, len(dialogue_list) - 1)), SetVariable("dialogue", dialogue_list[randtext]), Show("speech", transition=dissolve)]
        focus_mask True
        xpos 400
        # ypos 0
        yanchor 0.015
        at transform:
            zoom 0.49


label start:

    # 경고문
    call warning_label from _call_warning_label

    "안녕."
    "바, 반가워."
    "나 사실, 기대하고 있었어."
    "네가 같이 시, 신을 믿도록 이끌어준다고 했잖아."

    menu:
        "맞지?"
        "처음 듣는 이야긴데.":
            "뭐? 하, 하지, 하지만 분명, 그렇게 들었... 잠깐, 난 누구, 에게서, 들은 거지...?"
            "{color=#6E6E6E}{i}혼란스러운 중얼임{/i}{/color}"
            "... ..."
        "당연하지":
            "그치? 그럼 네가 내, 선생님, 이네."
        "안 할 거야.":
            "뭐...? 아, 안돼, 부탁이야, 내, 나의 구원을 도와, 줘! 내겐 너밖에 없어, 제발...!"
            "... ..."
            "... 넌 할 수밖에 없어."
    
    "아, 아무튼 결정, 됐으니까... 잘 부탁해. 날 두고 가지 마..."
    "내 이름이 뭔지는 알지...? 한 번만 들려줘..."

    $ lamb = renpy.input("내 이름이 뭐야? {color=#6E6E6E}{i}입력 후 Enter{/i}{/color}", length=32)
    
    if lamb == "틴데라이":
        "맞아, 내 이름은 [lamb]야."
        "아, 알아줘서 기뻐."
    elif lamb == "아그넬로":
        "... 아그넬로."
        "너의 어린양."
        "그래. 그게 내 온전한 이름이지..."
        python:
            lamb = "아그넬로"
    elif lamb ==  '' or lamb == '몰라' or lamb == '몰라요' or lamb == '모르는데' or lamb == '모름':
        "아... 정말 모, 모르는 거야?"
        "아쉽, 아쉽네. 아, 알려줄게. 나는 틴데라이야."
        "잘 부탁해. 헤헤..."
        python:
            lamb = "틴데라이"
    else:
        "뭐? 아, 아냐. 난 틴데라이야."
        python:
            lamb = "틴데라이"
    
    T "이제 네 이름을 드, 들을 차례네."
    
    call you_name from _call_you_name

    T "시작하기 전에 기, 기본적인 설명을, 들을래?"

    menu:
        "응.":
            T "뭐, 뭐부터 말해줘야 하지. 여기는 어떤 신을 섬기는, 기숙시설이야. 하, 학교라고 생각하면, 편해."
            T "아이들이 많고, 어른들이 우리를 가르쳐. 신앙은 우리의 전부야."
            T "너는 음, 음, 신앙이 부족한 나의... 멘토로 왔어. 서, 선생님이지."
            T "특이하게 이곳은 잘 사는, 집의 애들도 많고 고아인 친구들도, 많아. 상류층 사람들은 안 좋아할 텐데 어, 어떻게 가능한 걸까?"
            T "지금은 한창 공장에서 자동차나 기계가 만들어지고 다들 일을 하면서 시끌벅적한, 시대야. 여긴 조용한 편이지만... 우리 아버지도 사업을, 많이 하셨어."
            T "으음 또, 궁금한 거 있어...?"

            menu:
                "너에 대해":
                    T "나... 나? 어, 별로, 재미도 없을 테, 텐데."
                    if love:
                        T "엘시는 이미, 나에 대해 전부 알고 있잖아?"
                        T "나의 전부는 너의 소유야..."
                    T "그래도 설명, 해야겠지... 어, 뭐, 뭘 말해야 할까. 자기소개는 어려워..."
                    T "내, 내가 태어난 집안은, 유구한 귀족이야. 그래서 풍족하게 자란, 편인데. 지금은 나랑 관계 없어."
                    T "가출이냐고? 아, 아니 그런 건 아니라... ... 비슷한가..."
                    T "그리고 아, 으음, 늘 내, 나의 눈에, {i}형제{/i}가 보이는데, 다른 사람들은 아, 안 보인대. 아냐 난 미치지 않았어."
                    if love:
                        T "벗어나고 싶은데 바, 방법이 없어서... 나한텐 너밖에 없어... 그러니까..."
                    else:
                        T "벗어나고 싶은데 바, 방법이 없어서... 나한텐 신 님밖에 없어... 그러니까..."

                "없어":
                    T "조, 좋아..."

        "아니.":
            T "그래..."

    T "간단, 하게 요약하자면"
    T "앞으로 7일 동, 안 나는 {이가}[you]{/이가} 가리키는 대로, 신앙을 쌓을 거, 야."
    T "부, 분명 잘 할 수 있어. 힘내자...!"

    "준비가 되면 마, 말을 걸어 줘."
    jump room

# 여기서부터 일정관리
label room:
    if belief < 0:
        $ belief = 0
    
    play music "audio/bgm/room.mp3" loop fadein 0.1 fadeout 0.2 volume 0.75
    
    if day > 7:
        #엔딩
        jump ending

    # 일상들
    scene bg1 with dissolve
    hide screen hidden_days_text
    hide screen tinBtn3
    with dissolve
    
    # 화면에 배경이랑 틴 그림 나와야함
    # 며칠 째인지도
    if day > 1:
        
        $ hidden = renpy.random.randint(1,100)
        "숫자 [hidden]"
        if hidd == 1:
            $ go = False
            $ sleep = False

            # 7일째에도 히든을 못 보면
            if day == 7:
                jump hidden_event

            # 15로 나중에 수정
            if hidden <= 15:
                "히든시작"
                # 히든 이벤트
                jump hidden_event

    # 의식에서 쫓겨났다면
    if go == True:
        show screen tinBtn with dissolve
        T "어, 어제는 왜 갑자기 사라졌어?"
        T "다신 못 만나는 줄, 알고 걱정했어."
        T "또 봐서 다, 다행이다."
        $ go = False

    # 의식에서 같이 잤다면
    if sleep == True:
        show screen tinBtn with dissolve
        T "눈을 뜨니까 네가 있어서 노, 놀랐어."
        T "어제 일이 잘 기억이, 안 나."
        T "그래, 도 아침부터, {을를}[you]{/을를} 보니까, 좋다. 히히."
        $ sleep = False

    # 이벤트선택지
    show screen days_text
    call screen tinBtn with dissolve
    pause


# 일정 선택
label schedule:
    call screen imagebuttons with dissolve
    pause

label you_name:

    $ you = renpy.input("이름을 들려줘. {color=#6E6E6E}{i}한글 추천!{/i}{/color}", length=32)
    $ cnt = 0
    $ err = False
    $ not_name = True

    if len(you) > 6 or lamb == you:
        $ err = True

    if you == '엘시 슈라우드':
        $ err = False

    while err:
        if len(you) > 6 or lamb == you:
            $ err = True
        else:
            $ err = False

        # you 이름이 6글자 이상이면 반복
        if len(you) > 6:
            $ cnt += 1
            T "음... 너, 너무 긴데... 조금만, 줄여서 알려, 주면 안 될까? 애, 애칭도 좋으니까."
            $ you = renpy.input("이름을 들려줘.", length=32)

        # you 이름이 lamb와 같으면 반복
        if lamb == you:
            $ cnt += 1
            
            if not_name:
                T "... 응? 그건 내, 내 이름이잖아. 왜 그 이름을, 말하는 거야?"
                T "이름... 알려주기 싫어...?"
                $ not_name = False

            T "그, 그러지 말고, 부를 수 있는 이름으로 다시... 알려줘."
            $ you = renpy.input("이름을 들려줘.", length=32)

        # 루프를 5번 반복하면
        if cnt == 5:
            T "... 계속 이 루프에 빠지고 싶은 거야?"
            T "아, 아니면 그냥... 날 놀리는 걸까..."
            T "하하. 그치만 더는 시, 시간을 낭비하고 싶지 않, 아."
            T "그러니 너를 '친구'라고 부를게."
            $ you = "친구"
            $ err = False


    if lamb == "아그넬로": 
        if you == "엘시 슈라우드" or you == "엘시":
            $ you = "엘시"
            T "[you]..."
            T "네가, 와 줄 거라 생각했어."
            T "너, 너는 나의... ... 아."
            T "너는 나의 목자니까."
            T "우린, 여, 영원을 약속했으니까. ... 그렇지?"
            $ love = True
            # python:
            #     dialogue_list.append('엘시는 영원이 뭐라고 생각해?')
                # dialogue_list.append()
                # dialogue_list.append()
                # dialogue_list+['엘시는 영원이 뭐라고 생각해?', '사랑이 뭘까...', '사실 네게서 버려질까봐 늘 두려워.']
        else:
            T "... ..."
            T "... 너 누구야?"
            if lamb == "틴데라이": 
                T "왜 내 것이었던 이름을, 탐내는 걸까..."
            T "... ... 아냐. 그건 지금 중요한 게 아니니까..."
            T "하하......"
    elif you == "엘시 슈라우드" or you == "엘시":
        T "[you]... 엘시?"
        T "네가 겨, 곁에 있어서, 정말 기뻐. 진심이야. {color=#2E2E2E}아마도...{/color}"
        T "이번에도... 함, 께 있, 있어주는 거지? 헤헤... 잘, 부탁해."
        $ you = "엘시"
    elif you == "K" or you == "k" or you == "케이":
        T "[you]... 케이라고, 불러도 돼?"
        T "나, 난 우리가, 친구라고 생각해... 맞지? 맞을 거야... 맞고 싶어..."
        $ you = "케이"
    elif you == "폴라리스":
        T "아... 내 소중한 친구 [you]. 널 다시 봐서 기뻐."
        T "우, 우리 잘 지내, 보자."
    elif you == "":
        T "아, 알려주기 싫어?"
        T "그럼, 어... 일단은, 친구라고 부를게..."
        T "잘 부탁해 친구..."
        $ you = "친구"
    else:
        T "[you]... 반가워. 네가 날, 도와준다니, 참 좋아..."

