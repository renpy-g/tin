label ending:
    scene bg1 with dissolve
    hide screen hidden_days_text
    hide screen tinBtn3
    # 다른 거 해
    show screen tinBtn with dissolve

    T "... 버, 벌써, 마지막 날이네.  시간이 무척, 빨리 흐른 것 같아."
    T "[you]도 그렇게, 생각해?"

    menu:
        "응":
            T "네가 즐거웠, 다면 좋을 텐데."
            T "... 고생을 마, 많이 시킨 것 같아. 응, 그랬지... 미안..."

        "아니":
            T "나, 나랑 있는 게, 지루했던 건... 아니지...?"

    T "그래도 지, 지금까지 함께, 해 줘서 정말... 고마워."
    T "언제든 나를 포기할 수 있었잖아."
    T "여기까지 왔으니까, 마지막까지 어울, 려 줘. 부탁이야..."
    T "나도 {이랑}[you]{/이랑} 함께 지, 지내는 동안 마음 먹었거든. 앞으로 어떻게 하, 할지 정했어."

    hide screen tinBtn with dissolve

    if belief >= 200: # 임시수치
        if love:
            jump ending_4
        else:
            # 찐 신도 엔딩
            jump ending_good
    elif belief >= 100: # 임시수치
        # 어정쩡 신도
        jump ending_normal
    else:
        # 바이바이 신도
        jump ending_bad

