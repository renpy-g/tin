# 히든틴
screen tinBtn3:
    imagebutton:
        idle "images/characters/room/tin_hidden_hover.png"
        hover "images/characters/room/tin_hidden_idle.png"
        action Jump("loop_click")
        focus_mask True
        # hovered [ Play("sound", "audio/sound/tv-static.mp3") ]
        # unhovered [ Play("sound", "<from 1>audio/sound/침묵.mp3") ]
        xpos 419
        yanchor 0.098
        at transform:
            zoom 0.49

screen hidden_days_text:                    # 얘네 둘이 같이 해야함
    imagebutton:
        idle "images/backgrounds/1.png" xpos 60 ypos 60 yanchor 0.57 xanchor 0.26 action Jump("hidden_days_click")
    text "???" size 30 xalign 0.07 yalign 0.09

label hidden_days_click:
    scene black
    hide screen days_text
    hide screen tinBtn3
    hide screen hidden_days_text
    hide screen end_btn
    with dissolve

    if hDay == 1:
        "거긴 손대지 마."
        $ hDay += 1
        jump loop_room
    elif hDay == 2:
        "손대지 말라고 했잖아."
        $ hDay += 1
        jump loop_room
    elif hDay == 3:
        "왜, 왜 내 말을 안 들어줘?"
        $ hDay += 1
        jump loop_room
    elif hDay == 4:
        "... ..."
        "이런 신도는 필요 없어."
        "나가."

        $ renpy.full_restart()  # 강제종료


style end_button_style is default:
    size 22
    color "#888888"
    hover_color "#ffffff"
    xpadding 15
    ypadding 5
    background None

screen end_btn():
    frame:
        xalign 0.98
        yalign 0.94
        background None
        textbutton "끝내기":
            action Jump("loop_close")
            style "end_button_style"

# screen end_btn():
#     vbox:
#         textbutton "끝내기" action Jump("loop_close")

    # frame:
    #     xalign 1.0
    #     yalign 1.0
    #     xsize 100
    #     ysize 50
    #     textbutton _("끝내기"):
    #         action Jump("loop_close")
    #         xalign .5

# 히든
label hidden_event:

    hide screen days_text
    hide screen tinBtn
    scene background1 with dissolve
    show screen hidden_days_text
    with dissolve
    play music "audio/bgm/뭔가불길함_김.mp3" loop

    pause

    $ dj1 = 0
    $ loop_list = ["hidden_story_1", "hidden_story_2", "hidden_story_3", "hidden_story_4", "hidden_story_5", "hidden_story_6", "hidden_story_7", "hidden_story_8"] 

    #그냥 처음부터 순서를 섞는다
    $ renpy.random.shuffle(loop_list) 

    # 스토리 카운터 초기화
    $ story_count = 0
    $ stories_per_group = 3

    # 스토리 리스트를 3등분
    $ story_groups = []
    $ group_size = len(loop_list) // 3
    $ remainder = len(loop_list) % 3
    
    $ start_idx = 0
    $ end_idx = 0
    
    # 첫 번째 그룹
    $ end_idx = start_idx + group_size + (1 if remainder > 0 else 0)
    $ story_groups.append(loop_list[start_idx:end_idx])
    $ start_idx = end_idx
    $ remainder -= 1
    
    # 두 번째 그룹
    $ end_idx = start_idx + group_size + (1 if remainder > 0 else 0)
    $ story_groups.append(loop_list[start_idx:end_idx])
    $ start_idx = end_idx
    $ remainder -= 1
    
    # 세 번째 그룹
    $ end_idx = start_idx + group_size + (1 if remainder > 0 else 0)
    $ story_groups.append(loop_list[start_idx:end_idx])

    $ current_group = 0
    $ current_story_in_group = 0

    T "... 아, 안녕."
    T "미안, 오, 오늘은, 안 될 것, 같... 아."
    T "형제가 너, 너무, 가까워, 무서우니까..."
    T "뭘 할 수 있는... 상태가 아, 아닌데..."
    T "가, 갈 거야...? 나 너랑, 같이 있고 싶어. 버리, 버리지 말아, 줘."

    menu:
        "갈 거야.":
            $ belief -= 10
            T "... 그렇구나. 알겠어. 잘 가."

            hide hide_image
            scene black
            with dissolve
            
            $ day += 1
            $ hidd = 0
            $ h = 0
            jump room

        "있을게.":
            $ belief += 10
            T "... 기쁘다.\n거, 걱정 마. 널 오래 붙, 잡진 않을 테니까..."
            T "... 하, 함께 해 줘서, 고마워."
    
    T "... ..."
    T "저, 정신이 없어서. 우왕자왕 이야, 이야기 할 수도 있어."
    T "가고 싶으면 어, 언제든, 가도 돼.{color=#2E2E2E}\n가지 않길 원하지만...{/color}"
    
    jump loop_room
    
# 랜덤루프코드짜기~~~~

label loop_room:
    show screen end_btn    # 나중에 확인~
    window hide # 대사창을 닫음!!
    show screen hidden_days_text
    scene background1 
    with dissolve
    call screen tinBtn3 with dissolve
    pause
    # 틴을 클릭하면 loop_click 이벤트로 넘어간다


label loop_click:
    if story_count < len(loop_list):
        $ current_story = loop_list[story_count]
        $ story_count += 1
        jump expression current_story
    else:
        jump loop_close
    
####################################

label um:
    if dj1 == 0:
        jump loop_click


label hidden_story_1:
    scene black
    hide screen end_btn
    hide screen hidden_days_text
    with dissolve
    $ change_image('say_2')

    T "처, 처음 형제가 보이기 시작한 건... 열 살, 이었나. 잘은 기억이 안 나."
    T "커튼 뒤에 숨, 어서 나, 나를 보고 있었어."
    T "나도 처음에는, 도망치지 않았어. 어머, 니나 다른 사람들에게, 누가 있다고 말했는데...{w}\n다들 날 이, 이상하게 봤을 뿐이야."

    $ change_image('say_3')
    T "... 아무도 내 말을 믿어주지 않았을 뿐이야..."

    menu:
        "나는 믿어.":
            $ change_image('smail_6')
            $ belief += 5
            T "정말? 여, 역시 내 형제는, 존재하는 거지?"
            T "이것 봐, 내 뒤에 바로 있는, 있잖아."

            menu:
                "그건 아냐.":
                    $ belief -= 5
                    $ change_image('eye_right_4')
                    T "... 아. 그래."

                "맞아.":
                    $ belief += 5
                    $ change_image('smail_2')
                    T "[you]도 인, 정했으니까. 나, 나는 틀리지 않았어. 모두 날 괴롭히려는, 거야."
                    T "형제가 나를 주, 죽이기를, 기대하고 있는 거야..."

        "형제 같은 건 없어.":
            $ change_image('eye_right_4')
            $ belief -= 5
            T "... 아. 그래."
            T "너도 결국 나를 미, 믿어주지, 않는 거구나."

    T "... ..."
    $ change_image('eye_right_4')
    T "... 진리가, 중요할까."
    T "결국 내가 아직도, 두려움에서 벗어, 나지 못하는 게... 나한텐 더 주, 중요해."

    # 3개 스토리마다 룸으로 돌아가기
    if story_count % stories_per_group == 0:
        jump loop_room
    else:
        jump loop_click

label hidden_story_2:
    scene black
    hide screen end_btn
    hide screen hidden_days_text
    with dissolve
    $ change_image('say_3')
    T "내, 내가 병에 걸린 걸까?"
    $ change_image('warry')
    T "아니, 난 미치지 아, 않았어. 나는, 난 정상이야. 그래야만, 해..."
    
    window hide # 대사창을 닫음!!
    # 마우스 좌클릭 불허 설정
    $ use_click(False)
    
    $ change_image('mu_6')
    pause(1)
    $ change_image('mu_7')
    pause(1)    
    # 하나더
    # 힘겹게 뭘 말하려는
    $ change_image('sad_2')
    pause(1)

    # 0.1초뒤에 마우스 좌클릭 허용 설정
    $ threading.Timer(0.1, use_click, [True]).start()

    T "... 예전에, 나, 나를 고쳐준다고, 집에 의사가 온 적이 있었어."
    T "하지만 난 아프, 지 않았는걸. 단지 혀, 형제가 계속 따라다닐, 뿐이야. 그래서 그렇, 게 말했어."
    T "그랬더니 뭐라, 뭐라고 했더라. 기억이... {w}... 어른들이 심, 각하게 얘기하더니 나를 끌, 끌고 갔어."
    $ change_image('scary_2')
    T "시, 싫다고 말했, 말했는데...! 도망치, 치니까 억지로 무, 묶어서, 독방에 나를 가둬, 가둬버렸어...!"
    T "형제, 형제가 너무 마, 많았어... 계속 나를 내려 보고 나, 나를 죽일까 봐, 두려워서..."
    $ change_image('scary_3')    # 바부팅이 수정
    T "정말로... 무서웠는데... ..." # 엉엉

    menu:
        "지금은 괜찮아.":
            $ belief += 7
            $ change_image('mu_8')
            T "으응. 여, 여기는 괜찮아. 가끔 선, 생님이 가둬버린다고 마, 말할 때도 있지만..."
            $ change_image('mu_9')
            T "병원, 병원은 무서워... 의사도 실, 싫어. 나는 아, 아프지 않아."

        "널 버린 거네.":
            $ belief -= 7
            $ change_image('mu_9')
            T "끌려 갈 때, 아버지랑 눈이, 마주쳤는데."
            T "바로 아, 알 수 있었어. 날 포기했다는 걸. 내가, 망가져 버려서, 더는 기대를 하, 할 수 없어서... ..."

    T "... 이후에는 어머니가 날 보러, 와서. 아버지를 설득하고, 꺼내줬어."
    $ change_image('mu_10')
    T "어머니가 그, 그렇게 해 주지 않았다면 아마, 지금도 거기에, 갇혀 있지 않았을까?"
    $ change_image('mu_9')
    T "... 나 무서워 [you]... ..."

    # 3개 스토리마다 룸으로 돌아가기
    if story_count % stories_per_group == 0:
        jump loop_room
    else:
        jump loop_click

label hidden_story_3:
    scene black
    hide screen end_btn
    hide screen hidden_days_text
    with dissolve

    $ change_image('base_1')
    T "점점, 느낄 수 있는 게 줄, 어들고 있어."
    T "냄새도 맛도, 감촉도... 내가 듣는 소리가 맞는지 모르겠고, 내가 보는 광경이 진실인지, 확신할 수 없어."
    T "스스로가 느끼는 감정도 미, 믿을 수 없어서... 내가 정말로 기쁜 건지, 모르겠어."
    T "아. 하나는 확신해. 온전히 남은 거라곤, 두려움뿐이야."
    $ change_image('base_2')
    T "... 다들 내가 틀렸대. 내가 하는 말이 전부 지, 진실되지 못하대."
    T "그럼. 무엇 하나 확신할 수, 없잖아. 도무지 자, 자신을 믿을 수, 없어."
    T "나조차도 나를 못 믿는데, 누가 날 믿어주겠어?"
    T "그래도 사, 살아가야 하니까, 내 기준을 전부 그분으로 맞췄어."

    if lamb == '아그넬로':
        if you == '엘시':
            $ belief += 10
            $ change_image('smail_1')
            T "맞아, 내 기준은 모두 너야 엘시."
            T "이, 이게 너를 불편, 하게 할까?"
            T "아... 그래도 허락은, 받아야 하나..."
            # 아무튼 뭔가 포즈
            T "... 엘시. 이 나약한 어린양의... 목자가 되, 되어 줄래?"  # 목자가 되...  기도하는 포ㅡ즈

        else:
            T "내 신이 그 사실에 기뻐하길 원하는 건, 욕심일까?"

    else:
        T "이게 그분을 불, 편하게 하진, 않겠지?"
        T "만일 허락되지, 않는다면..."
        T "... 그분 대신 네, 네가, 나의 기준이 되어 줄래?"

        menu:
            "어떻게 생각해?"
            "괜찮다고 생각한다.":
                $ belief -= 7
            
            "아니라고 생각한다.":
                $ belief += 5

        $ change_image('smail_1')
        T "답은 드, 들려주지 않아도, 돼. 고마워."

        # 3개 스토리마다 룸으로 돌아가기
    if story_count % stories_per_group == 0:
        jump loop_room
    else:
        jump loop_click

label hidden_story_4:
    scene black
    hide screen end_btn
    hide screen hidden_days_text
    with dissolve

    $ change_image('base_1')
    T "... 가끔은, 있지. 아, 아니, 종종인가... 너무 지쳐서, 끝을 바랄 때가 있어."
    T "무슨 말인지, 이해했어?"
    T "이해 못 했어도 괘, 괜찮아. 그냥 나 혼자, 떠드는 거니까... 무, 무시해도 돼."
    T "이, 이 삶은 그저, 죽음이 두려워서, 이어지는 거야. 단지 지금의 두려움보다, 죽음이 더 무서워서..."

    menu:
        "왜?":
            $ change_image('base_2')
            T "왜 두렵냐고? 그, 글쎄... 감정도 습관이 되나 봐. 늘 두려워서, 계속 두려운 상태를, 유지하나 봐..."
            T "이렇게 되고 싶지, 않았는데..."

        "두려움이 더 커지면?":
            $ change_image('eye_bottom')
            T "더 커지면... 아, 아마 그때는, 정말로 죽지 않을까. 도망칠 방법이, 그것밖에 없잖아."

    T "내가, 죽어버리면. 그럼 넌 나를 애, 애도해 줄까?"
    $ change_image('smail_1')
    T "... 그러면 정말, 행복하겠다."

        # 3개 스토리마다 룸으로 돌아가기
    if story_count % stories_per_group == 0:
        jump loop_room
    else:
        jump loop_click


label hidden_story_5:
    scene black
    hide screen end_btn
    hide screen hidden_days_text
    with dissolve

    $ change_image('base_2')
    T "거, 거울이 무서워."
    T "그냥, 보는 건 상관 없는데... 내가 비치면, 형제가 보이는 것, 가, 같아서, 보고 싶지 않아."
    T "그래서 머리카락도 잘라, 잘라버렸어. 직접 자른, 거라 이상... 하겠지만..."
    T "우리, 집에선 시종들이 정돈을 해 줘서, 괜찮았는데... 지금은, 혼자니까. 어쩔 수 없이 그냥, 이렇, 이렇게 있어."
    $ change_image('say_2')
    T "어차피 여기선 겉치레도 주, 중요하지 않잖아."

    menu:
        "그분에게 잘 보여야지.":
            $ belief += 10
            T "어... ... ..."
            T "그... 그렇, 그렇네... 그렇지... 차, 참된 신도라면, 본을 보여야..."
            T "어, 어떡하지. 부끄러워... 지, 지금이라도 뭐, 뭔가, 어... 목욕이라도, 다시 해, 해야 하나?"

            if love:
                $ belief += 5
                T "엘시도 머, 멀끔한 내가 더 좋은, 아, 좋아...?"
            
            T "으... 지금은 요, 욕조에 들어, 가고 싶지 않은데... {i}형제{/i}가 가, 같이 있을 거 같아..."
            T "빠, 빨리 정리하려고, 할게... ..."

        "지저분해.":
            $ belief -= 5
            T "아... 음... 씨, 씻긴 하는데..."
            T "... ... {w}... 미안..."

        "잘 어울려.":
            $ belief += 3
            $ change_image('base_3')
            T "잘, 어울... 어... 그, 래?"
            T "잘 어울리는진, 모르, 겠는데..."
            T "{이가}[you]{/이가} 그렇다면 그런, 거겠지? 고, 고마워...?"

    T "앞으로는 빗질, 이라도 제대로... 하려고 노력, 노력할게..."

    # 3개 스토리마다 룸으로 돌아가기
    if story_count % stories_per_group == 0:
        jump loop_room
    else:
        jump loop_click


label hidden_story_6:
    scene black
    hide screen end_btn
    hide screen hidden_days_text
    with dissolve

    $ change_image('base_2')
    T "아, 아무도 날 이해하려 하지 않아서, 외로워."
    T "나조차도, 스스로가 이해 안 돼. 내가 왜, 왜 이러는지 모르겠어."
    T "왜 갑자기 이렇게 됐는지 모르겠어..."
    T "... {은는}[you]{/은는}, 날 이해하고픈 의지가 있어?"

    menu:
        "응.":
            $ belief += 7

        "없어.":
            $ belief -= 7

        "어려워.":
            $ belief -= 5

    $ change_image('smail_1')
    T "사실 이, 있다고 해도, 믿진 않을 거야."
    T "결국 이해 받지 못하면... 스, 슬프잖아."
    $ change_image('base_1')
    T "기대해봤자, 실망만 돌아와. 그래서 너에게도 신에, 게도 기대하지 않아."
    T "무엇, 무엇도 날 가, 감당하지 못할 거야. 아무것도, 아무도, 날 원하지 않아."
    T "... ... 그래서 외, 외로워."

    menu:
        "내가 있어 [lamb].":
            $ belief += 5
            if love:
                $ belief += 5
                # 확인이 필요함
                $ change_image('smail_8')
                T "마, 맞아. 나에겐 네가 있지. 엘시..."
                T "지금 이 말이, 널 화나게 했을까?"
                T "혹시 그렇다면 사, 사과할게. 미안해. 힘들, 힘들어서 그랬어. 지금 너무 힘들어서..."
                T "용서해 줘..."
            else:
                $ change_image('smail_5')
                T "... {w}그래. 그래... 네가 있네."
                T "함께해서 기뻐. 아, 아마도..."
                T "그치만 [you]도 언, 젠가... 내게 지쳐서, 떠날 거잖아."
                T "다, 다들 그랬어. 처음엔 좋게, 해 주다가도, 날 감당 못해서, 그래서 가 버렸어."
                T "아... 그러니까 신을, 믿는 거야. 그분은 날 떠나지 아, 않으니까."

        "꼴사나워.":
            $ belief -= 5
            $ change_image('smail_5')
            T "하하, 그래. 나, 나도 그렇게, 생각해."
            T "실망하는 게 두려워서, 시도조차 안 하는 건 바보나 하는, 짓이라고 아버지가 그러, 셨는데..."
            $ change_image('smail_1')
            T "... 나, 나는 바보에, 겁쟁이야."
            T "너를, 대하는 데도 내가 얼, 마나 용기를 내는지, 넌 모르지?"
            T "아, 알 필요 없어. 중요하지도 않잖아. 그치."

        "그분이 있잖아.":
            $ belief += 7
            T "... 맞아. 그분... 그분, 이 있지. 그분은 결코 날 떠, 떠나지 않으니까..."

            if love:
                $ belief += 5
                T "... 엘시는 결코 날 떠나지 않으니까."

            T "마, 맞지? 그렇지? 그렇다고, 말해 줘..."
            T "내가 더 열, 심히 할게. 많이 부족하지만, 그치만, 노력할게."
            T "기, 기도도 열심히 하고, 무엇이든 순종하고, 아, 미련도 안 가질게."
            # 애매하군
            $ change_image('sad_4')
            T "내 모든 걸 바칠게."  # 눈물 줄줄
            T "그러니까 제발, 날 떠나지 않는다고, 그 입으로 말해 줘."


    # 뭔가 더 써야할듯


    # 3개 스토리마다 룸으로 돌아가기
    if story_count % stories_per_group == 0:
        jump loop_room
    else:
        jump loop_click

label hidden_story_7:
    scene black
    hide screen end_btn
    hide screen hidden_days_text
    with dissolve

    $ change_image('base_1')
    T "{은는}[you]{/은는} 사람을 죽, 여본 적 있어?"

    menu:
        "응.":
            $ belief -= 3
            $ change_image('base_2')
            T "어... 그, 그렇구나. 나도 짜증난다고, 죽이지 않으면 좋을, 텐데..."

        "아니.":
            T "보통, 보통은 그렇지...?"

        "죽이고 싶어.":
            $ belief -= 3
            T "어... 지, 지금은 말고... 나 없을 때, 죽여 줘... 나 말고 다른, 사람..."

    $ change_image('base_2')
    T "아, 아무튼 있지, 나는 있, 있거든. 아직도 살아있는 내, {i}형제{/i}..."
    T "어쩔, 수 없었어. 혀, 형제가, 눈 앞까지 와서, 너무 무서, 무서워서."
    T "그, 금방이라도 안구끼리 부딪힐, 것 같았단 말야. 오지 말라고 해, 했는데도 계속 가까이, 오니까."
    T "어, 어쩔 수 없이 목을 졸랐어. 그러지 않으면 나, 날 죽일 것 같았, 같았어."

    menu:
        "기분이 어땠어?":
            $ belief -= 5
            $ change_image('tension_1')
            T "기분... 모, 몰라. 인간은 너무, 쉽게 죽어. 그냥 목, 을 졸라도... 손에 힘만 줘도..."
            T "그 애를 죽이는 걸, 점점 숫자로, 취급하니까... 내, 내가 괴물이 된, 기분이야."
            T "... 이러다 내가 다, 다른 누군가를 죽여, 죽여 버리면, 어쩌지?"

            menu:
                "도와줄게.":
                    $ belief += 3
                    $ change_image('warry')
                    T "어... 뭐, 뭐를? 뒷, 처리를 도와준다는, 말이야?"
                    T "아, 아니면, 어, 죽이지 않도록...?"
                    T "... ... {w}그래도 고, 고마워..."
                
                "어쩔 수 없지.":
                    $ belief -= 3
                    T "... 무, 무책임해..."
                    T "... ... {w}내가, 형제 외에 누군가를 죽이면, ... {w}그때는 {이가}[you]{/이가}... 나를 시, 신고해 줘."
                    T "도망쳐도, 붙잡히게... 다, 다시는 못 나오게, 모두가 날 피, 하도록 소문을 내 줘."
                    T "... 네가, 날 생각한다면."

        "형제는 어땠어?":
            $ belief -= 5
            $ change_image('tension_1')
            T "혀, 형제? 왜 그런, 걸 묻는 거야?"
            T "가까이서 볼 일은, 거의 없긴 하, 하지만..."
            $ change_image('eye_right')
            T "... 목, 소리가 예뻤어."
            T "숨이 막혀서, 죽어가는 소리가 예뻤어."
            T "손바닥에, 닿은 피부도 부드럽고 따, 따듯해서... 분명, 살아있었어. 그래서 제대로 주, 죽였는데 왜 계속, 다시 보이는 걸까?"
            $ change_image('base_2')
            T "다들, 죽을 때조차 시, 시선을 떼지 않는 거야?"
            T "... ..."

        "괜찮아.":
            $ belief += 10
            $ change_image('warry')
            T "... 괜찮아?"
            T "사, 사람을 죽였는데, 괜찮은 거야?"
            T "... 그분이, 이런 나도 바, 받아 주실까?"

            if love:
                $ belief += 5
                T "엘시 넌 내가 사, 람을 죽여도, 괜찮아?"

            menu:
                "응":
                    $ belief += 5
                    # 홍조가 필요할지도
                    $ change_image('smail_5')
                    if love:
                        $ belief += 5
                        T "정말? 에, 엘시는, 어떤 나든... 받아주는, 거야?"
                        T "내, 내가 남을 속이고, 아프게 하고, 죽여, 죽여도 용서해 주는 거구나...!"
                        #그렇게까진말하지않았지만
                        T "기쁘, 다. 네, 네가 나의 신이어서, 기뻐."
                        T "앞으로도 널 섬기게 해 줘..."

                    else:
                        T "그렇, 그렇구나. 그분은 자애로우시니까, 사, 사람을 죽인 것 정도론, 날 버리지 않으셔."
                        T "기, 기쁘다...! 응, 난 정말로, 괜찮은 거야...!"
                        T "알려줘서 고, 고마워, [you]!"

                "아니":
                    $ change_image('sad_2')
                    $ belief -= 5
                    if love:
                        T "... 아... 그, 그럼 어쩌지. 형제가 몸을 붙여도, 참아야 하는, 걸까."
                        T "나, 난 못 버틸, 것 같아. 엘시에게 도와, 달라고 자꾸... 울 것 같은데."
                        T "엘시가, 그런 내가 귀찮, 귀찮아지면 어떡하지?"
                        T "난 네게 사랑받고 싶단 말야..."
                        T "읏, 어, 어떻게든, 노력할게..."

                    else:
                        T "그런, 그런가... 살인자는 그, 그분의 신도에 어울리지, 않으니까..."
                        T "하지만 이, 이미 이렇게 됐는, 데... 나는 그럼, 구원받지 못하는 거야?"
                        T "어쩔 수 없는 일이라고, 이해해주지 않는 거야? 그분마저도..."
                        T "아... 난 도대체 어떻게 해야..."

            $ change_image('smail_5')
            T "하하... ..."

    T "형제를 죽이는 건, 아, 아무리 죽여도 계속 다시 나타, 나니까. 자꾸 살인이 반복 돼."
    T "오늘도 이만, 큼 가까우니까... 아마, 무서워서 또 저, 저지르겠지. \n{color=#2E2E2E}이젠 싫어...{/color}"
    T "... 언제쯤 모, 모든 일이 끝날까?"
    T "이대로 영원히 기적이, 오지 않으면. 죽어서야, 끝나는 걸까?"

    # 3개 스토리마다 룸으로 돌아가기
    if story_count % stories_per_group == 0:
        jump loop_room
    else:
        jump loop_click

label hidden_story_8:
    scene black
    hide screen end_btn
    hide screen hidden_days_text
    with dissolve

    $ change_image('base_1')
    T "모든 종교는, 신을 사랑... 하라고 하던데."
    T "난 사랑이, 뭔지 잘 모르겠어."
    T "으응, 아, 알긴 아는데. 개념, 만 안다고 해야 하나... 뭐라고 하, 하면 좋을까."
    T "... 부모님이 나를, 사랑한다는 건 아, 알아. 특히 어머니가 날 걱정 한, 다는 걸 머리로는, 알고 있어."
    T "친구끼리의 사랑도... 아, 아마 알 거야. 이해는... 하고 있어."
    T "사랑이라는 건... 나 외에 다, 다른 존재를 우선하는, 거잖아? 비록 순간이라도, 그 순간을 모아서, 마음을 키우면... 다들 그게 사랑이란 걸, 알아."
    T "사랑하고 있다는 걸 알아..."

    menu:
        "잘 알고 있는 거 아냐?":
            $ belief -=3

        "어렵네.":
            $ belief +=3

    $ change_image('smail_1')
    T "... 그런데 나는, 이기적이라. 나 외에 다른 걸, 우선할 수가 없어."
    T "내가 제, 제일 중요해. 아마 {과와}[you]{/과와} 나 중에 누, 누군가가 죽어야 한다면, 난 {을를}[you]{/을를} 죽이라고 할, 거야."
    T "그게 신이어도 마찬가지야... ..."
    $ change_image('base_1')
    T "... 사랑이란 기능이 내게 없는 것 같아."
    T "잃어버린 건지, 처음부터 없었, 던 건지는 모르겠어."
    T "하지만 우, 우리는 신을 사랑해야 하잖아. 그분에게 버려, 버려지지 않, 기 위해서라도."
    T "어떻, 게 해야 내가 그, 그분을 사랑할 수 있을까?"

    menu:
        "사랑한다 말해.":
            $ belief += 7
            $ change_image('say_2')
            T "말만으로 괜찮아...?"
            T "그, 그치만 그러면, 거짓말이 되는 거잖아. 거짓 고백은 어, 죄가 되는 거 아냐...?"
            T "느, 늘 진실만 말할, 말할 수는 없지만... 나는 이, 이 말이, 거짓이란 걸 인, 식하고 있어."

            menu:
                "안 할 거야?":
                    $ belief -= 0

                "싫음 말고.":
                    $ belief -= 0

            window hide # 대사창을 닫음!!
            # 마우스 좌클릭 불허 설정
            $ use_click(False)
            # 2초를 기다림!!
            pause(2)    
            # 0.1초뒤에 마우스 좌클릭 허용 설정
            $ threading.Timer(0.1, use_click, [True]).start()

            # 기다리는 동안에 표정변화 넣기
            # 꼭 2초 아니어도 됨
            # 중간에 넣으면 되지 않을까

            T "... 사랑해."

            if love:
                $ belief += 5
                T "... 엘시를, 사랑하고 있어."
                T "사랑해 엘시. 사랑해. 정말로 사랑해. 사랑... ..."
                T "계속 이렇게 말하면, 엘시를 향한 사랑이 어, 언젠가 진심, 이 될까?"
                T "진심이 되, 되고 싶어..."
                $ change_image('sad_6')
                T "엘시를 진심으로, 사랑하고 싶은데."

            else:
                T "그분을 저, 정말 사랑해. 애정하고 있어."
                T "사랑해요. 사랑합니다. 사랑해 주세요..."
                T "계속 이, 이렇게 말하다 보면, 언젠가 진심이 될까?"

        "행동으로 보여.":
            $ belief += 5
            $ change_image('base_2')
            T "행동, 음, 조, 좋아하는 행위...?"
            T "마음 없는 행위가 사, 사랑이 될 수 있어?"
            T "나는 다, 단지 사랑 받고 싶어서, 사랑하는 척을 하는 건데. 그건, 그, 자신만 아는, 거잖아."
            T "자기 자신만, 아는 이기적인 행동이잖아."

            menu:
                "안 할 거야?":
                    $ belief -= 0

                "싫음 말고.":
                    $ belief -= 0

            T "... ..."

            if love:
                $ belief += 5
                $ change_image('say_2')
                T "엘시는 여, 연약한 내가 좋아?"
                T "의존하고, 애원하면서 매달, 리는 걸 좋아해?"
                T "그, 그럼 그렇게 할게. 늘 그래왔, 으니까 할 수 이, 있어."
                T "그치만 다른, 다른 것도 알려주면 안 돼?"
                T "너의 어린양은 바보야. 그, 그치만 알려주면 전부, 따르도록 할게."
                T "아무리 싫은 것도, 해내려고 노력, 할 테니까..."
            
            else:
                $ change_image('eye_right')
                T "그, 그래. 그분이 좋아하는 건 어차, 피 교리서에 써 있고... 따라야 하는, 거니까."
                T "지금도 충분히 하, 하고 있는 거니까..."
                T "비록 감사의 마음은 없어도..."
                T "더 여, 열심히 하면, 되는 거겠지...?"
                $ change_image('base_2')
                T "알려줘서 고마, 고마워 [you]..."

        "그냥 살아.":
            $ belief -= 7
            $ change_image('base_2')
            T "... 무, 무슨 말이야. 내 고민을 들을, 생각이 없는 거야?"
            T "관심, 이 없으면, 그냥 무시하면 되, 되잖아."
            T "내가 떠든 건 맞지만..."
            T "... 됐어. 지금 우, 우리에게 중요한 것도 아니지..."

    T "... 기도, 를 가득, 많이 해야겠어..."
    T "그 정도는, 괘, 괜찮을 거야..."

    if love:
        $ change_image('smail_1')
        T "... 내 기도, 들어줄 거지? 엘시... 입 밖으로 널 찾게 해 줘..."

    T "열심히, 할 테니까..."

    # 3개 스토리마다 룸으로 돌아가기
    if story_count % stories_per_group == 0:
        jump loop_room
    else:
        jump loop_click

# 더는 루프를 돌지 않으면
label loop_close:
    T "있잖아, [you]. 잃기만 하는 삶에도, 얻는 게 있을까?"
    T "하하. 마, 맞아. 널 만난 것도, 뭔가 얻은, 거겠지."
    T "그치만, 나, 난, 끊임없이 잃어가는 것 같아서, 그래서... ..."
    T "... 자신, 이 깎여나가는, 기분이야."
    T "계속해서 까, 깎이고 깎여서, 조각상은 꿈도 못 꾸고, 가루밖에 안 남아서..."
    T "... 언젠가 바람에, 전부 흩어져서 날아갈 것, 같아."
    T "이, 이런 것도 보통의 삶, 일까?"

    window hide # 대사창을 닫음!!
    # 마우스 좌클릭 불허 설정
    $ use_click(False)
    # 2초를 기다림!!
    pause(2)    
    # 0.1초뒤에 마우스 좌클릭 허용 설정
    $ threading.Timer(0.1, use_click, [True]).start()

    T "있지 [you]. 너, 너도 두려운 게 있어?"
    T "너만 괜찮다면, 나에게도 들, 려주지 않을래?"

    menu:
        "없어.":
            T "없... 다는 게 가능해?"
            T "하지만... 그, 그렇구나. 두려운 게, 없구나. 부럽다. 무척..."
            T "... [you]도 어딘가. 망가졌나 보네."

        "싫어.":
            T "아... 그렇다면, 어쩔 수 없고..."
            T "아, 알았, 알았어. 아쉽다."

        "그래.":
            $ horror = renpy.input("[you]의 두려움은...", length=32)
            T "{i}'[horror]'{/i}... ... {w}여기서 내 답, 은 정해져 있으니까, 무, 무슨 뜻인지는 정확힌, 몰라."
            T "하지만 말야..."
            T "우리, 가 무서워하는, 건... 다른 누군가가, 보기에 별것 아닐 수도 있, 지만... 그, 그래도 난 {을를}[you]{/을를} 이해해."
            T "... 너의 두려움을 이해해."

    T "아. 이제 가야 하는구나."
    T "헤, 헤어질 시간이네. 헤헤."
    T "같이, 함께해 줘서, 고마워."
    T "내일 또, 또 보자. 잘 자...!"

    hide hide_image
    hide screen end_btn
    scene black
    with dissolve

    $ day += 1
    $ hidd = 0
    $ h = 0
    jump room


