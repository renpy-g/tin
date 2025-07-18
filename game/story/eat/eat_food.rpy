screen frame_():
    frame:
        add "images/backgrounds/frame1.png"
        add "images/backgrounds/frame2.png"
        align(0.5, 0.2)
        at transform:
            zoom 0.45

screen stew():
    frame:
        add "images/backgrounds/food/stew.png"
        align(0.5, 0.35)
        at transform:
            zoom 0.09
    

label eat_food:
    $ change_image('smail_5')
    T "그럼 [you]... 어떤, 걸 고를까...?"
    menu:
        "고기":
            T "{은는}[you]{/은는} 고, 고기 좋아해?"
            menu:
                "좋아해.":
                    $ belief += 3
                    T "그렇, 구나. 나, 나는... 무난하게 먹었던, 것 같아."
                    T "잘 기억이 안 나네..."
                "싫어해.":
                    $ belief -= 2
                    $ change_image('base_2')
                    T "으응...? 싫어하는데 왜... 아, 아냐. 받아들일게..."
                "그냥 그래.":
                    $ belief += 1
                    T "그래... 어쩌면 나도, 그냥 그런 것 같아..."
                    T "어릴 때는... 채소를 더 조, 좋아했거든."

                    menu:
                        "토마토?":
                            $ belief += 3
                            $ change_image('base_3')
                            T "맞아. 어, 어떻게 알았어? 전에 말해줬, 던가...?"
                            T "토마토 좋아해. 어릴 때는 어머니랑 같이, 재배도 해 봤어."
                            T "잔뜩 더러워지기만 하고, 공부, 때문에 신경쓰지 못해서 겨, 결국 실패했지만."
                            $ change_image('smail_7')
                            T "즐거웠어."

                        "오렌지?":
                            T "오렌지가... 채소였던가...? 오렌지는 나, 나무에서 열리지 않아?"
                            T "나름 머, 먹긴 했어. 즐기진 않았, 지만. 싫지도 않고..."
                            $ change_image('eye_bottom')
                            T "오렌지가 무슨 맛이었지......"

                        "브로콜리?":
                            $ change_image('base_2')
                            T "음... 아니, 그건 별로 좋아하지 않은, 것 같아. 지금도 그닥..."
                            T "마, 맛없어."

            $ change_image('smail_1')
            T "어... [you], 이, 이건 접시가 2개야. 푸드커버엔 숫자만 쓰여있고..."
            T "어떤, 걸 먹을래? 2개 다 먹으면 남길 수도 있으, 니까. 하나만 고르자. 음식을 남기면 그분에게 호, 혼나."

            menu:
                "뭘 먹을까?"
                "'1'":  # 양고기
                    $ belief += 4
                    $ change_image('panic_2')
                    show expression AlphaMask("black70", At(new, center)) as mask at multiply
                    "식탁 위로 푸드커버에 '1'이라 적힌 접시가 내려온다. [lamb]의 팔이 후들거리는 걸 보니 꽤 무게가 나가나 보다."
                    "뚜껑을 열면..."

                    # 그냥 파일 이름 넣자
                    hide mask
                    hide panic_2
                    with dissolve
                    # show screen frame_()
                    # show screen stew() 
                    show stew:
                        zoom 0.15
                        xalign 0.5
                        yalign 0.3
                    with dissolve

                    "... 모락모락 김을 풍기며 커다란 고기가 듬뿍 들어간 스튜가 나왔다! 달큰한 냄새가 코를 스치고 보기 좋은 붉은 빛이 자태를 뽐낸다. 야채와 고기가 한 데 어우러진 모습을 보면 당장이라도 허기가 지고 침이 고일 수밖에 없다."
                    hide stew with dissolve
                    $ change_image('chim_1')
                    T "우와... 이런 건 오랜만인데... 이, 이건... 토마토 스튜인가 봐. 맛있, 맛있겠다."
                    T "응? 그, 그게... 어릴 때 어머니가 해 주신, 요리랑 비슷해서..."
                    $ change_image('base_3')
                    T "[you]도 추억의 음식, 같은 건 있잖아. 그렇지? 아닌, 가..."
                    T "금방 다, 담아줄게. 잠시만..."
                    show expression AlphaMask("black70", At(new, center)) as mask at multiply
                    "우왕자왕. 허둥지둥. 달그락달그락."
                    "그릇에 담긴 요리의 상태는 양호했다. 만든 지 얼마 되지 않은 것 같고, 낯설면서도 익숙한 향이 코 끝을 찔렀다."
                    "고기를 집어 한 입 먹어보면..."
                    hide mask
                    $ change_image('warry')
                    T "자, 잠깐만 [you]. 기도는 아, 안 해?"

                    menu:
                        "안 해.":
                            $ belief -= 3
                            T "엇... 안 할 거야? 그, 그럼 그분에게 혼날 거야. 감사하지 않는 신도는, 가치가 없댔어."
                            T "진짜로 안 하는 거야...? 그러지 말고 나, 나랑 같이 하자. 잠깐만 참으면 되니, 까."

                            menu:
                                "기도할 거야?"
                                "할게.":
                                    $ belief += 2
                                    $ change_image('smail_3')
                                    T "다행이다... 우, 우린 축복받을 거야."
                                    call eat_pray from _call_eat_pray

                                "안 해.":
                                    T "그런... 아, 알았어. 강요는 안 할, 게. 그냥 먹어도 가끔은, 용서해주시겠지...? 그, 그럴 거야."

                        "할 거야.":
                            $ belief += 3
                            call eat_pray from _call_eat_pray_1

                    T "토마토 스튜..."
                    $ change_image('chim_2')
                    T "그럼... 자, 잘 먹겠습니다."
                    "이제 정말로 고기를 입에 넣으면 {w}소스를 머금어 푹 익힌 고기가 입안을 헤집으며 기분 좋게 감칠맛을 뽐냈다. 고기는 부드러웠고 야채는 씹기 좋았으며 고소하면서 상큼한 소스가 요리를 조화롭게 적셨다."
                    "한 마디로... 맛있다! 너도 맛있다고 느꼈을까?"
                    $ change_image('eat_happy')
                    T "이, 이거 맛있다... 오랜만에 무척, 맛있게 느껴져. 맛이 잘 느껴지는 건 오, 오랜만이야."
                    T "{은는}[you]{/은는} 어때? 마, 맛있어?"

                    menu:
                        "맛있어.":
                            $ belief += 3
                            $ change_image('smail_2')
                            T "헤헤, 그치. 나, 나도 맛있... 아 이건 아까 말했지..."
                            T "혼자 먹는 게 아니라서, 좋아."
                            T "혼자는 다, 다른 게 느껴지니까."

                        "별로야.":
                            $ belief -= 2
                            $ change_image('what')
                            T "어... 혹시 토마토 싫, 어해?"
                            T "어쩌, 지. 내가 [you] 몫까지 여, 열심히 먹을게."

                    $ change_image('eat_1')
                    T "음... 근데 이건 무슨, 고기일까. 뭔가 익숙한, 맛인데..."
                    T "...{w} 양인가?"

                "'2'":  # ???크림소스미트볼
                    $ belief += 7
                    "식탁 위로 푸드커버에 '2'라 적힌 접시가 내려온다. 그릇이 식탁에 부딪히는 소리가 가볍게 울렸다."
                    "뚜껑을 열면..."

                    hide smail_1 with dissolve
                    show meatball:
                        zoom 0.15
                        xalign 0.5
                        yalign 0.3
                    with dissolve

                    "... 모락모락 김을 풍기며 크림 소스에 덮여진 동그란 미트볼들이 나왔다! 식욕을 돋구는 냄새가 코를 찌르고 옆에 같이 담겨진 구운 감자들이 반짝반짝 빛을 냈다. 또한 느끼함을 잡아줄 빨간 링곤베리 잼이 담겨있어 조화로운 색을 뽐냈다."
                    "단촐하지만 정겨움이 느껴지는 요리다."
                    hide meatball with dissolve
                    $ change_image('smail_5')
                    T "아, 이 요리. 예, 예전에 지나가던 가게에서, 본 적 있어."
                    T "서민들이 많이 먹는 음, 식이라고 해서 나, 나도 먹어보고 싶었는데."
                    T "{은는}[you]{/은는} 먹어본 적, 있어? 미트볼 좋아해?"

                    menu:
                        "좋아해.":
                            $ change_image('smail_2')
                            T "그렇구나. 자, 잘 됐다. 좋아하는 요리가 나왔네. 헤헤."
                            T "나는 첨, 처음이지만 {이가}[you]{/이가} 좋아한다고 하니까, 분명 맛있을 거야."
                            "[lamb]의 미소를 눈에 담고 미트볼 하나를 스푼에 올려 한 입 넣으면..."

                        "그닥.":
                            $ change_image('base_3')
                            T "그래...? 그래도 냄새, 는 괜찮은 거 같으니까, 맛없진 아, 않을지도 몰라."
                            T "일단은 배만 채우, 고 다음에 더 맛, 맛난 거, 먹자."
                            "아쉬운대로 미트볼 하나를 스푼에 올려 한 입 넣으면..."

                        "싫어.":
                            $ change_image('what')
                            T "싫어해? 어어 어쩌지, 이, 이미 골라서 먹, 먹어야 되는데..."
                            T "마, 많이 싫어? 굶고 싶을 만큼 싫은 거야? 그, 그런 거 아니라면 한 입이라도, 먹어보자. 응?"
                            T "잘 먹으면 그, 음, 아. 치, 칭찬을, 해 줄게. 그분도 {이가}[you]{/이가} 잘 먹으면 분명 기뻐, 하실 거야...!"
                            "입에 넣는 시늉이라도 하지 않으면 [lamb]는 포기할 생각이 없어 보인다."
                            "어떻게든 미트볼 하나를 스푼에 올려 한 입 넣으면..."

                    $ change_image('warry')
                    T "자, 잠깐만 [you]. 기도는 아, 안 해?"

                    menu:
                        "안 해.":
                            $ belief -= 3
                            T "엇... 안 할 거야? 그, 그럼 그분에게 혼날 거야. 감사하지 않는 신도는, 가치가 없댔어."
                            T "진짜로 안 하는 거야...? 그러지 말고 나, 나랑 같이 하자. 잠깐만 참으면 되니, 까."

                            menu:
                                "기도할 거야?"
                                "할게.":
                                    $ belief += 2
                                    $ change_image('smail_3')
                                    T "다행이다... 우, 우린 축복받을 거야."
                                    call eat_pray from _call_eat_pray_2

                                "안 해.":
                                    T "그런... 아, 알았어. 강요는 안 할, 게. 그냥 먹어도 가끔은, 용서해주시겠지...? 그, 그럴 거야."

                        "할 거야.":
                            $ belief += 3
                            call eat_pray from _call_eat_pray_3

                    $ change_image('chim_2')
                    T "그럼... 자, 잘 먹겠습니다."
                    "이제 정말로 미트볼을 입에 넣으면... {w}고소하고 부드러운 크림이 입안을 적시고 씹을 때마다 육즙이 터졌다. 곱게 다져진 덕분에 불편하지 않게 고기가 입안에서 녹았다."
                    "중간중간 들어있는 양파 같은 야채들이 아삭함을 살리고 서서히 느끼할 때쯤 감자와 링곤베리 잼을 먹으면 적당한 상큼함이 느끼함을 잡아주었다."
                    "한 마디로... 맛있다! 너도 맛있다고 느꼈을까?"
                    $ change_image('eat_2')
                    T "맛있, 다. 기름지고 미끌미끌한 식감이야. 고기 부, 부드러워. 꽤 괜찮네..."
                    T "{은는}[you]{/은는} 머, 먹을 만 해...?"

                    menu:
                        "맛있어.":
                            $ belief += 3
                            $ change_image('smail_2')
                            T "으, 응! 맛있어. 헤헤. 같이 먹어서 조, 좋아."
                            T "[you]도 만족, 스러웠다면 다행이야..."
                            T "다음에도. 같이 먹자. 또 데려, 데려와 줄게."

                        "별로야.":
                            $ belief -= 2
                            $ change_image('warry')
                            T "많이 벼, 별로야? 그런..."
                            T "나, 남긴 건 내가 어떻게든, 먹을게. {color=#2E2E2E}토하면 어쩌지...{color} \n{은는}[you]{/은는} 먹고 싶은 마, 만큼만 먹어도 괜찮, 아."
                            
                    $ change_image('eat_1')
                    T "음... 근데 이건 무슨, 고기일까..."
                    T "...{w} ... 역시 잘 모르겠네."
                    T "크, 크게 중요한 건, 아니겠지? 맛있으니까..."

        "채소": #라따뚜이
            $ belief += 4
            $ change_image('panic_2')
            show expression AlphaMask("black70", At(new, center)) as mask at multiply
            "식탁 위로 동그란 냄비 하나가 올라온다. 아직 뜨거운 건지 두툼한 장갑을 낀 [lamb]가 팔을 후들거렸다."
            "뚜껑을 열면..."

            hide mask
            hide panic_2
            with dissolve
            show ratatouille:
                zoom 0.4
                xalign 0.5
                yalign 0.3
            with dissolve

            "... 납작하게 잘린 다양한 야채들이 겹쳐진 채 일렬로 나열되어 다채로운 색을 뽐냈다. 푹 익혀 깊은 풍미를 담은 향이 증기와 함께 얼굴을 감싼다. 눈도 코도 즐거운 요리다."

            hide ratatouille with dissolve
            $ change_image('smail_3')

            T "아... 이 요리, 책에서 본, 본 적 있어. 이름이 특이, 했는데. 어, 음, 라따뚜이?"
            T "은근히 유명한, 요리라더라. 헤헤. 채소만 먹는 애들도 이, 있어서 이걸 챙겨준, 걸까?"
            T "아...! 얼른 다, 담아줄게. 따뜻할 때 먹으면 더 맛있, 맛있을 거야."
            show expression AlphaMask("black70", At(new, center)) as mask at multiply
            "채소들이 흩어지지 않도록 온 신경을 집중하며 조심조심 [you]의 접시에 담긴 음식들은 보기엔 양호했다."
            "맛도 그럴까. 포크로 음식을 집어 한 입 넣어보면..."

            hide mask
            $ change_image('warry')
            T "자, 잠깐만 [you]. 기도는 아, 안 해?"

            menu:
                "안 해.":
                    $ belief -= 3
                    T "엇... 안 할 거야? 그, 그럼 그분에게 혼날 거야. 감사하지 않는 신도는, 가치가 없댔어."
                    T "진짜로 안 하는 거야...? 그러지 말고 나, 나랑 같이 하자. 잠깐만 참으면 되니, 까."

                    menu:
                        "기도할 거야?"
                        "할게.":
                            $ belief += 2
                            $ change_image('smail_3')
                            T "다행이다... 우, 우린 축복받을 거야."
                            call eat_pray from _call_eat_pray_4

                        "안 해.":
                            T "그런... 아, 알았어. 강요는 안 할, 게. 그냥 먹어도 가끔은, 용서해주시겠지...? 그, 그럴 거야."

                "할 거야.":
                    $ belief += 3
                    call eat_pray from _call_eat_pray_5

            $ change_image('chim_2')
            T "그럼... 자, 잘 먹겠습니다."
            "이제 정말로 음식을 입에 넣으면 {w}조화롭게 섞인 각종 야채의 맛이 깊게 입안에 스며들고 감칠맛이 나는 소스와 아삭아삭한 식감이 입을 즐겁게 한다. 절로 몸이 건강해지고 속이 편안해질 것 같은 맛이다."
            "한 마디로... 맛있다! 너도 맛있다고 느꼈는진 모르겠으나..."
            $ change_image('eat_2')
            T "이건... 책에서만 맛보던 요, 리인데... 생각보다 괘, 괜찮다. 좋아했던 맛이 나서... 어쩐지 그리움이 느껴지는, 것 같아. 이제 처음 먹어봤는데."
            T "{은는}[you]{/은는} 마, 맛있어?"

            menu:
                "고기가 더 좋아.":
                    $ belief -= 2
                    $ change_image('base_2')
                    T "어... 고기가 좋은데 왜, 왜 이걸...?"
                    T "아, 음, 그래도 머, 먹을 수 있다니 다행, 다행이다."
                    T "마, 많이 먹어..!"

                "맛있어.":
                    $ belief += 3
                    $ change_image('smail_2')
                    T "히히 그치. 맛있어... 토마토 소스도, 발라져 있어서. 좋아했던 게 가, 가득하네."
                    T "{이랑}[you]{/이랑} 먹을 수 있어서 행복해."
                    T "... 함께 있어줘서 고, 마워."

        "디저트":   # 호두파이 짱
            $ belief += 4
            $ change_image('warry')
            T "으응? 아, 아직 식사도 안 했는데, 바로 후식을 먹는, 거야?"
            $ change_image('smail_1')
            T "으, 음. 이런 일탈도, 나쁘진 않지만..."
            T "좋아 그럼 가, 가져올게. 잠시만..."
            $ change_image('panic_2')
            show expression AlphaMask("black70", At(new, center)) as mask at multiply
            "곧 식탁 위로 접시 하나가 올라온다. 디저트치곤 묵직한 건지 음식을 옮기는 [lamb]의 얼굴이 힘들어 보였다."
            "이제 뚜껑을 열면..."

            hide mask
            hide panic_2
            with dissolve
            show pie:
                zoom 0.4
                xalign 0.5
                yalign 0.3
            with dissolve
            
            "... 고소한 향을 가득 풍기는 먹음직스런 파이가 나왔다! 달달한 과일이 아닌 견과류가 올려져 있는 것으로 보아 이건 누가 봐도 호두파이다. 파이는 식사인가?"
            hide pie with dissolve
            $ change_image('smail_3')
            T "와. 정말 간, 식이네. 그래도 배는, 부르겠다. 그치."
            T "[you], 이런 파이 좋아해?"

            menu:
                "좋아해.":
                    if lamb == '아그넬로':
                        if you == '엘시':
                            $ belief += 5
                            $ change_image('smail_2')
                            T "하하, 맞아. 엘시는 견과류를 좋아한다고, 했잖아. 이번엔 제대로 기억하고 이, 있어. 언제 들었던 건진, 모르겠지만..."
                            $ change_image('base_2')
                            T "아니, 들었던 게, 맞나?"
                            $ change_image('tension_1')
                            T "... 내가 제대로 알고 있는, 거 맞지? 그렇지? 엘시..."
                        else:
                            $ change_image('base_2')
                            T "... 그렇구나. 사실 내 신도, 호두파이를 좋아해."
                            T "너는 내 신을 따라하는 거야? 왜?"
                    else:
                        $ change_image('smail_2')
                        T "정말? 다행, 다행이다. 좋아하는 걸 먹으면 기, 기분이 좋잖아."
                        T "나, 나는 이런 디저트류는... 집에서 거의 허락, 하지 않아서. 잘 몰라."
                        T "아, 아니 알긴 하는데. 보통보다 많이 아, 안, 접해봤어. 보통이 어느, 어느정도지?"
                        T "그래도 웬, 만하면 잘 먹는 것, 같아. 헤헤."

                "그냥 그래.":
                    $ change_image('base_2')
                    T "혹시 따로 기대한 디저트라도 이, 있던 거야?"
                    T "음... 다음엔 그, 그게 나오면, 좋겠다."

                "싫어해.":
                    $ change_image('what')
                    T "앗, 싫, 싫어? 어... 이제 다시 못, 고르는데..."
                    T "내가 마, 많이 먹을게...! 으음 그치만 한 입이, 라도 먹어 줘... 다는 모, 못 먹어..."

            T "잠시만, 내가 담아, 줄게."
            show expression AlphaMask("black70", At(new, center)) as mask at multiply
            "우왕자왕 칼을 들고. 하지만 나름 반듯하게, 낑낑거리며 조각을 자른다."
            "[you]의 앞에 곱게 잘린 호두파이 조각이 놓여졌다."
            "포크로 조각을 잘라 한 입 넣어보면..."

            hide mask
            $ change_image('warry')
            T "자, 잠깐만 [you]. 기도는 아, 안 해?"

            menu:
                "안 해.":
                    $ belief -= 3
                    T "엇... 안 할 거야? 그, 그럼 그분에게 혼날 거야. 감사하지 않는 신도는, 가치가 없댔어."
                    T "진짜로 안 하는 거야...? 그러지 말고 나, 나랑 같이 하자. 잠깐만 참으면 되니, 까."

                    menu:
                        "기도할 거야?"
                        "할게.":
                            $ belief += 2
                            $ change_image('smail_3')
                            T "다행이다... 우, 우린 축복받을 거야."
                            call eat_pray from _call_eat_pray_6

                        "안 해.":
                            T "그런... 아, 알았어. 강요는 안 할, 게. 그냥 먹어도 가끔은, 용서해주시겠지...? 그, 그럴 거야."

                "할 거야.":
                    $ belief += 3
                    call eat_pray from _call_eat_pray_7

            $ change_image('chim_2')
            T "그럼... 자, 잘 먹겠습니다."
            "이제 정말로 조각을 입에 넣으면 {w}계피 향이 입안에 가득차며 바삭하고 부드러운 호두와 시트가 식감을 즐겁게 했다. 견과류 특유의 고소한 맛이 달달함과 섞여 절로 콧노래를 부르게 한다. 식사가 아닌, 영락없는 디저트다."
            "한 마디로... 맛있다! 너는 어땠을지 모르나..."
            $ change_image('eat_2')
            T "이, 이것도... 괜찮네..."
            T "[you]도 괘, 괜찮아? 나름 맛있, 는 것 같은데."

            menu:
                "맛있어.":
                    $ belief += 3
                    $ change_image('smail_2')
                    T "입맛에 맞는, 다니 다행이네. 헤헤. 나도 좋아."
                    T "좀 달달, 한 건가? 새로운, 맛이야. {이가}[you]{/이가} 좋아하니까 나도 좋아하게 될 거야."
                    T "그러면. 우리 또... 같이 먹자."

                "식사를 하는 게 나았어.":
                    $ belief -= 2
                    $ change_image('what')
                    T "어, 어? 그치만 아, 이미 골랐는데... 이, 이건 {이가}[you]{/이가} 고른, 거잖아. 끝까지 머, 먹어야 돼."
                    T "내가 마, 많이 먹을 테니까, 접시에 담은 거라도 다 먹어 줘. 응?"
                    $ change_image('smail_1')
                    T "잘 먹으면... 음... 칭, 찬을 해 줄게. 그니까 힘내자."

            $ change_image('smail_5')
            T "아... 그, 그분도 좋아하는 간식이, 있을까?"

            if love:
                $ belief += 5
                T "알아. 에, 엘시가 좋아하는 간식. 호두파이, 견과류... 언제 들은 건진 기억, 이 안 나지만..."        
                T "그래도 좀 더 엘시가, 좋아하는 것들을 알아두고 싶어."
                T "그야, 당연히, 내 주인이 좋아하는 걸 아는 게, 어린양의 의무잖아. 그렇지?"
                $ change_image('tension_1')
                T "네가 좋아하는 것들을 잔뜩 바쳐야, 엘시가 날 사랑할 거야. 마, 맞지?"
                T "나 열심히 하, 할 테니까..."
                # 별로면 바꿔
                $ change_image('sad_1')
                T "사랑해 줘. 엘시."
            else:
                T "그분도 맛있는 걸 먹으면 우, 우리처럼 행복하실 거, 아냐."
                T "간식의 종류는 조금, 다를지라도..."
                T "그분이 좋아, 좋아하는 걸 알면, 우리도 그걸 구해서 바치면 되는, 거야."
                T "아... 생각해 보니 그건... 이, 이미 교리서에 나와있구나."
                T "... 그분은 피와 살을 좋아해."
                $ change_image('smail_6')
                T "그래서 피와 살을 취하려고, 아이들을 데려가는 거였구나!"
                $ change_image('smail_2')
                T "[you] 덕분에 깨달음을, 얻었어. 고마워!"

                menu:
                    "갑자기?":
                        $ belief += 2

                    "... ...":
                        $ belief += 1

                    "잘됐네.":
                        $ belief += 3

                T "헤헤. 워, 원래 이런 건, 갑자기 오기도 하잖아."
                T "다 네 덕분이야."

        "먹지 않는다.": # 걍 돌아가기
            $ belief -= 5
            if eatX == 1:
                call not_eat1 from _call_not_eat1
            else:
                call not_eat2 from _call_not_eat2
                
