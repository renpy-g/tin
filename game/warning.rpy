screen warning:
    frame:
        xsize 800
        ysize 400
        background "#000"
        padding (20, 20)
        xalign 0.5  
        yalign 0.5  
        vbox:
            spacing 20
            text "주의" style "warning_title"
            text "본 게임에는 사이비, 폭력, 정신 이상 등 일부 플레이어에게 \n불편함을 줄 수 있는 소재가 포함되어 있습니다." style "warning_text"
            text "본 게임은 허구의 세계를 배경으로 하며, 등장하는 모든 \n인물, 사건, 단체는 실제와 관련이 없습니다." style "warning_text"

# 스타일 정의
style warning_title:
    size 50
    color "#FF0000"
    bold True
    align (0.5, 0.5)  # 텍스트 자체 가운데 정렬
    font "GowunDodum-Regular.ttf"

style warning_text:
    size 30
    color "#FFFFFF"
    font "GowunDodum-Regular.ttf"

label warning_label:
    # 밑에 메뉴 없애기
    $ nn = 1

    scene black
    pause 0.5

    show screen warning with dissolve
    pause #3
    hide screen warning with Dissolve(2)

    $ nn = 0

