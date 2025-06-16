label not_eat1:
    $ change_image('what')
    T "먹지 않는다고? 왜, 왜?? 배고프지 않아??"
    T "아,  아니면 어. 원하는 게, 없는 거야?"
    T "편식, 편식은 안돼...! 저, 정말로 안 먹을 거야? 그분이 너, 너를 위해 준비, 했는데?"
    T "다시 한번만 새, 생각해 봐. [you], 진짜로 안 먹는... 거야...?"

    menu:
        "먹는다.":
            $ belief += 3
            $ change_image('extortion_1')
            T "그러, 그렇지? 같이 먹어주는, 거지?"
            T "[you]라면 그, 그래 줄 거라 생각했어. 그분의 식, 사를 거부하다니 말이, 안 되잖아."
            $ change_image('smail_2')
            T "하하. 다행이다... 벌을 받지, 않아서."
            T "그럼 다시 고, 골라보자."

            $ eatX += 1
            call eat_food from _call_eat_food_1

        "안 먹어.":
            $ belief -= 3
            $ change_image('base_2')
            T "아... 정말, 안 먹어?"
            T "그렇, 구나. 그거 무척... 아쉽네."
            T "싫으면 어, 어쩔 수 없지. 어쩔 수 없어 [lamb]..."
            T "그러면... 돌아갈까? 여기, 서 더는 볼일이 없잖아."
            T "화나지 않았어. 나는 괜찮아... 가자."

            play sound "audio/sound/쿵드럼1.mp3"
            hide hide_image
            scene black
            with dissolve
            "식당의 문이 닫힌다. 무거운 신음이 짧게 울리고 어두컴컴한 복도가 둘을 품었다."
            "배고프진 않니 [you]? 그래도 너는 선택했으니, 돌아가는 길밖에 없다."
            "잘 자렴. 좋은 시간 되기를."

            $ day += 1
            jump room


label not_eat2:
    $ belief -= 5
    $ change_image('contempt')
    T "... 다시 이걸 선택한 이유가 뭐야?"
    T "그분을 모욕하는 거야? 나, 날 놀리는 게 재밌어?"
    $ change_image('base_1')
    T "...... ......"
    T "... 됐어. 어차피 더 이어나갈, 생각 따위 없잖아."
    T "가, 갈래. 나머지는 알, 아서 해."
    T "... 내일 봐."
    # 끼익 쿵
    play sound "audio/sound/쿵드럼1.mp3"
    hide hide_image
    scene black
    with dissolve
    $ day += 1
    jump room