label sch_day1_arrival:

    window hide

    $ persistent.sprite_time = "day"
    $ day_time()

    scene bg int_bus with flash_red

    play ambience ambience_camp_entrance_day_people fadein 1

    "Голова раскалывается."
    "Что это вообще было?"
    # ВОЗДУХ СЛИШКОМ ДРУГОЙ НУЖНО ЕМУ АХУЕТЬ

    iv "Где я вообще?"

    if prophet:

        show anim prolog2 with fade

        $ name_sch("Иван")
        ivan "Кто же ты такой?"

        $ name_sch("Я")
        ivan "Я - Пророк."
        ivan "А ты - лишь часть того Лимба, что осталась во мне."
        ivan "Я - твой единственный шанс. И больше никто тебе не поможет."

        $ name_sch("Иван")
        ivan "Я могу сделать всё сам! Я хочу изменить условия сделки!"
        ivan "Харон, ты слышишь меня?! Он предаст нас! Он нас всех уничтожит!"

        scene bg int_bus with flash_red

    elif sch_bound:

        show anim prolog2
        show uv normal pioneer

        with fade

        $ name_sch("Иван")
        ivan "Сделку не отменить?"

        $ name_sch("Я")
        ivan "Мне нечего терять."
        dreamgirl "А мне есть."
        ivan "Так почему ты не откажешься, раз жертвуешь стольким?"

        $ name_sch("Иван")
        ivan "Потому что иначе она потеряет всё."

        $ name_sch('Я')
        ivan "Настоящий Ромео."

        scene bg int_bus with flash_red

        if sch_true:

            show anim prolog2 with fade

            pause(0.5)

            $ name_sch("Я")
            ivan "Кто же ты такой?"

            $ name_sch("Иван")
            ivan "Что, не понравилась легенда прошлого?"

            $ name_sch("Я")
            ivan "Зато нравится идея хорошего будущего."

            show uv normal pioneer with dissolve

            dreamgirl "Как и мне."

            scene bg int_bus with flash_red


    if limb:
        "Здесь так жарко и душно... как в Лимбе."


    $ name_sch("Я")

    "И ярко..."
    "Жарко?!"
    "Я оказался в незнакомом мне автобусе."
    "Рядом лежало моё старое пальто и рюкзак."

    ivan "Посмотрим..."

    "Небольшой рюкзак из непромокаемой ткани и экокожи, в котором лежали наушники, старый зонт с кошками, повербанк и кошелёк с ключами."
    "Определённо мой."

    if not sch_true:
        "Я прошёлся между рядами в несчастных попытках найти ещё что-нибудь полезное, но безрезультатно."
        "Лишь в пустом водительском месте я нашёл зажигалку и пустую пачку \"Космоса\"."
        "А это значит, что тут мне делать больше нечего."

    else:
        "Я прошёлся между рядами в попытках найти ещё что-нибудь полезное, но наткнулся только на записку."

        dreamgirl "Удачи."

        "Интересно, чья она?"

    "А это значит, что тут мне делать больше нечего."

    scene bg ext_bus with dissolve

    "Горячий воздух из душного салона сменился свежим и прохладным, а мне в лицо подул лёгкий ветерок."
    "Я обернулся, чтобы посмотреть, на чём хотя бы приехал."
    "И это был Икарус! Такие же по междугородным рейсам ездили."
    "А это значит, что город не близко. Блин."
    "И вообще - их должны были списать!"

    scene bg ext_road_day with fade

    "А дорога, по которой я приехал, была настолько длинной, что, кажется, вела в никуда, за самый горизонт."

    scene bg ext_camp_entrance_day with fade

    "Зато в конкретное место."
    "Простая кирпичная стена, потрескавшийся асфальт, окруженный двумя гипсовыми пионерами, небольшая арка над железными воротами с выдавленной надписью - вот и весь нехитрый дизайн."
    "Какой-то он знакомый..."

    ivan "\"Совёнок\", пионерлагерь..."
    ivan "И где, извините, я нахожусь?"

    menu:
        "Найти информацию об этом месте":
            $ day1_info_check = True
            show bg ext_road_day with fade

            "Связи нет. Странно? Да не то слово."
            "Wi-fi? Надежды не было, но зато не буду локти грызть."
            "Может, хоть GPS поймаю?"

            ivan "Твою мать!"

            "Где я оказался?!"
            "Илон Маск устроил космическую войну и уничтожил все спутники?"
            "Бррр."
            ivan "Так, вдох-выдох. Не мог же вот так взять и переместиться... Откуда?"
            "Так, ладно, без паники."
            "Без паники, я сказал."
            "Фу-{w=.3}у{w=0.15}-х."

            scene bg ext_camp_entrance_day with fade

        "Зайти в лагерь":

            "Проверять связь не имело смысл даже при всём моём желании - только паниковать начну."
            "Но надо же что-то делать!"
            "Я подошёл к дверям и решил приоткрыть ворота."


    return

label sch_day1_slavya:

    $ persistent.sprite_time = "day"
    $ day_time()

    play ambience ambience_camp_entrance_day_people fadein 1

    scene bg ext_camp_entrance_day

    "Ворота начали открываться, и из-за них аккуратно, почти на носочках, выбежала какая-то девочка."
    "Ну, девушка."
    "На вид ей было где-то семнадцать-восемнадцать лет, её волосы отливались золотым оттенком, " #TODO

    show sl smile pioneer with dissolve

    sl "Привет. Ты новенький?"

    # опять же, меню появляется слишком рано
    menu:

        "Поздороваться":

            if not sch_hard:
                $ pt_sl +=1

            ivan "При{w=0.3}вет?"

            show sl smile pioneer with dspr

            sl "А ты меня спрашиваешь?"

            "Девушка по-детски улыбнулась."

            show sl normal pioneer with dspr

            ivan "Напомни, где я?"
            sl "Ты приехал в пионерлагерь \"Совёнок!\""
            ivan "Территориально это где?"
            sl "С тобой всё в порядке?"

            "Очевидно, что таким вопросом я только заставлю других усомниться в моём состоянии."

        "Игнорировать":

            $ pt_sl -=1

            show sl sad pioneer

            sl "Что-то не так?"

            "Да почему ты не можешь уйти и оставить меня?"
            ivan "Просто скажи, что тебе нужно."

            show sl smile pioneer with dspr

            pause (0.3)

            show sl normal pioneer with dspr

            sl "Так ты всё-таки умеешь говорить!"


    sl "Кстати, моё имя - Славяна. Но все меня зовут Славей, так что ты тоже можешь."

    $ meet('sl', u"Славя")

    sl "Добро пожаловать в наш лагерь!"

    if sch_true and pt_sl == 1:
        "Ощущение, что я БКРР читаю." # отсылочка
    else:
        "За это время я кое-что заметил."
        "На ней же пионерская форма!"
        "Это что за пионерская реконструкция ещё?"

    sl "Тебе сейчас надо к вожатой, я тебе скажу, как туда пройти. Хотя, лучше возьми с собой карту!"

    "Девочка дала мне свёрнутый бело-жёлтый листок из плотной бумаги и собиралась убежать по своим важным делам." # скомканно слишком, 30 строк на первую встречу - мало

    ivan "Хоть скажешь, как её по имени-отчеству?"
    sl "А, извини. Нашу вожатую зовут Ольга Дмитриевна. Идёшь прямо, потом от площади налево, третий ряд "
    ivan "Хорошо...{w=.3} Спасибо."

    menu:
        "Это всё?":

            sl "А тебе нужно узнать что-то ещё?"
            ivan "Нет, я, думаю, разберусь."
            sl "Хорошо. Пока!"

            "Славя убежала за ворота, оставив меня, наконец, в одиночестве."

        "Я не потеряюсь?":

            $ pt_pi +=10

            sl "Её домик под номером 17. Хочешь, я тебя туда свожу?"
            sl "Мне только на несколько минут в клубы сбегать."

            menu:
                "Согласиться":

                    $ pt_sl +=1
                    $ sch_day1_sl_route = True

                    ivan "Ладно."

                    show sl smile pioneer with dspr

                    sl "Отлично! Пойдём?"
                    ivan "Угу."

                    return

                "Отказаться":

                    ivan "Ещё и ждать? Нет, я лучше сам."

                    show sl normal pioneer with dspr

                    sl "Ну ладно."

                    extend "Надеюсь, тебе здесь понравится! Я побежала! Пока!" # слишком резко смена настроения

    hide sl with dissolve

    "Девушка растворилась за воротами, оставив меня в гордом одиночестве."

    return

label sch_day1_loner:
    $ persistent.sprite_time = "day"
    $ day_time()

    play ambience ambience_camp_entrance_day_people fadein 1
    play music sunpatterns fadein 1

    scene ext_clubs_day with fade

    "Мои ожидания по поводу общего вида лагеря изнутри не оправдались."
    "То, что было повреждённым и потёртым снаружи, выглядело ухоженным и чистым внутри."
    "Потресканный асфальт заменился чистой и (почти) целой плиткой, а стены лагеря были недавно покрашены."
    "Лес, похоже, почти не вырубали, даже ландшафт выглядит абсолютно нетронутым."
    "Первое здание, которое меня встретило, гордо красовалось надписью \"Клубы\" над неразличимым расписанием."
    "А за дверями слышался шум статики и треск простивающих колонок."
    "К тому же из открытого окна доносилось несколько голосов, искажённых ветром."

    iv "Вообще, здесь довольно неплохо. Солнце греет голову и душу, трава настолько зелёная, будто её нарисовали, а воздух чист настолько, что мне в первые минуты было сложно дышать."
    iv "Даже слишком сложно..."

    scene ext_clubs_day with dissolve

    "Дальше дорожка тоже вела прямо, так что я мог идти и рассматривать окружение без размышления, куда идти, пока"

    show un normal pioneer at cleft with dissolve

    extend "я не увидел на своём пути ещё одну девушку."

    "Однако при моём виде она смутилась."

    iv "Вот это тут красавица есть."

    show un shy pioneer at cleft with dspr

    menu:

        "Поздороваться":

            $ list_sch_ch_known.append('un')
            $ pt_un +=1
            $ pt_wi +=10

            ivan "Привет."

            show un surprise pioneer at cleft with dissolve

            un "П-привет."

            ivan "Меня зовут Ваня. А тебя?"

            "Похоже, что из-за моего настроя на разговор, ей стало не по себе."

            un "Меня зовут Ле..."
            ivan "Ле...?"
            un "Лена." # опять ГГ слишком резко знакомится, нет малейшего описания

            $ meet('un', u"Лена")

            show un shy pioneer at cleft with dissolve

            "А я уже перерос стесняться перед противоположным полом."

            play sound_loop sfx_bush_leaves

            menu:
                "Заступиться":

                    $ pt_us -=1
                    $ pt_un +=1

                    $ list_sch_ch_known.append('us')

                    "Я заметил шуршение в кустах и рыжий отлив волос, и..."

                    ivan "Мелкая, вылезай!"

                    show un surprise pioneer at cright with dissolve

                    ivan "Лена, на тебя чуть не напали." #тупо x2

                    show us dontlike pioneer at cright with dissolve

                    us "Ну вот, а ты кто ещё такой?!"
                    ivan "Тот же вопрос и к тебе."

                    show us grin pioneer at center with dissolve

                    us "Вопросом на вопрос не отвечают."
                    ivan "Я мимо проходил."

                    show us angry pioneer at cright with dspr

                    us "Ну так и проходи мимо!"

                    hide us
                    show un normal pioneer at center

                    with flash_red

                    iv "Моя коленка!"

                    ivan "Вот {w=1} негодяйка..." # тут должны быть маты, но литературный язык сказал нет

                    show un smile pioneer with dspr

                    un "Ульянка такая..."

                    $ meet('us', u"Ульяна")

                    ivan "Спасибо, хоть буду знать, как зовут моего {i}врага!{/i}" # герой не такой жизнерадостный

                    show un shy pioneer with dspr

                    "М-да, видимо, она боится общения в принципе, или общается лишь тогда, когда рядом кто-то знакомый."

                    ivan "Пока. Ещё увидимся!"
                    un "П-пока." # опять же, Лена должна покрыться краской

                    show un normal pioneer close with dspr

                    pause(0.5)

                    hide un with dspr

                "Игнорировать":

                    $ pt_un -=1
                    $ pt_us +=1
                    $ sch_day1_un_guilty = True

                    play sound_loop sfx_bush_leaves

                    iv "Я думал, что шуршание кустов было лишь из-за ветра, но" # опять от лица героя так, будто это рассказчик

                    stop ambience
                    play music music_list["i_want_to_play"] fadein 1

                    window hide

                    scene cg d1_grasshopper with dissolve

                    extend " из них выпрыгнула мелкая хулиганка в футболке \"СССР\" и напала на девочку с огромной саранчой!"

                    un "А{w=0.35}-а{w=0.17}-a{w=0.09}-a{w=0.7}а!"

                    scene bg ext_clubs_day
                    show us laugh pioneer

                    with dissolve

                    us "Ха-ха-ха-ха!"
                    ivan "И зачем?"
                    us "Да ладно, весело же!"
                    ivan "Пугать людей - весело?"
                    us "Да!"

                    "Рыжая показала мне язык на прощание и снова убежала куда-то за домики. Видимо, там пролегает короткая тропа."

                    hide us with dissolve

                    "Ну и ну..."

                    stop music fadeout 1
                    play ambience ambience_camp_entrance_day_people fadein 1


        "Идти дальше":

            $ pt_wi +=10

            "Хотя, судя по её выражению лица, я был ей совсем не интересен." # опять в одном сообщении
            "Только время обоим сэкономим."

    return



label sch_day1_camp_slavya:
    $ persistent.sprite_time = "day"
    $ day_time()

    play ambience ambience_camp_entrance_day_people fadein 1
    play music sunpatterns fadein 1

    scene ext_clubs_day with fade

    "Мои ожидания по поводу общего вида лагеря изнутри не оправдались." # описание скомканное
    "То, что было повреждённым и стёршимся снаружи, выглядело абсолютно новым и чистым внутри."
    "Лес, похоже, почти не вырубали, даже ландшафт выглядит абсолютно нетронутым."
    "И первое здание - клубы."
    "Похоже, что за этим зданием особо не ухаживали. На фоне чистых дорожек это здание имело совсем печальный вид - треснутые ступеньки, серые перила, слезшая со стен краска и покрытые сантиметрами пыли окна, закрытые ржавой решёткой."
    "На вывеске было какое-то неразличимое расписание, а за дверями стоял шум статики."

    show sl normal pioneer far at cleft with dissolve

    sl "Я скоро вернусь!" # С чего бы вообще, кстати, Славе, идти в клубы, если ей не горит? Нужно поджечь
    hide sl with fade

    $ renpy.pause(2, hard=True)

    with fade

    show sl normal pioneer at cleft with dissolve

    "Наконец двери клубов открылись и Славя выбежала ко мне."
    sl "Не заждался?"
    ivan "Нет, всё в порядке."

    show sl smile pioneer at cleft with dspr

    sl "Отлично! Пойдём, Ольга Дмитриевна, наверное, заждалась."

    play ambience ambience_camp_entrance_day_people fadein 1

    scene ext_houses_day with fade

    show sl normal pioneer with dissolve

    ivan "А вообще, как у вас день проходит?"
    sl "Ну, у нас тут определённый распорядок дня - если что, расписание на обратной части карты."
    sl "Подъем в восемь, отбой в полночь, четырёхразовое питание, но никто тебе не мешает не приходить в столовую - только потом не жалуйся, что тебя не покормят."
    sl "Раз в неделю у нас проводятся концерты и свечки. И дискотека."
    "На последнем слове Славя смутилась или мне показалось?"

    show sl smile pioneer with dspr

    extend "А на этой неделе будет всё сразу, последняя же."
    ivan "Получается, я опоздал на две трети смены?" # КАПИТАН ОЧЕВИДНОСТЬ ВРЫВАЕТСЯ В ЗДАНИЕ УДАРОМ С НОГИ

    scene ext_square_day
    show sl sad pioneer

    with dissolve

    sl "Да."
    ivan "Не нужно печалиться насчёт меня."
    "Пионерка (святой Рандом, куда меня занесло?) удивилась моему ответу так, будто я публично выругался в самой матерной манере."
    sl "Но ты так много пропустил!"
    ivan "Мне без разницы."
    sl "Зачем тогда вообще ехал?"

    scene bg ext_house_of_mt_day
    show sl normal pioneer

    with dissolve

    "Остаток пути мы прошли молча."

    ivan "Мы пришли?"
    sl "Угу."

    show dv normal pioneer2 far at cleft with dissolve

    if 'dv' in list_sch_ch_known:
        ivan "Оперативно у вас тут реагируют на происшествия."

        show sl sad pioneer with dspr

        ivan "Жаль, что не предотвращают."

    hide dv
    with easeinleft

    pause(0.5)

    hide sl

    wuth dissolve

    play sound sfx_knock_door7_polite

    pause(1)

    return


label sch_day1_dv:
    $ persistent.sprite_time = "day"
    $ day_time()

    play ambience ambience_camp_entrance_day_people fadein 1
    play music sunpatterns fadein 1

    scene ext_clubs_day

    with fade

    iv "И всё же тут довольно неплохо, люди добрые и не лезут, как у меня... дома." # Славя лезет, ГГ не должен про дом заикаться - хоть он не помнит, почему, но он осознанно его покинул

    show dv normal pioneer2 far at cleft
    show us smile sport far at cright

    with dissolve

    "И только я сказал про то, как тут хорошо, так мгновенная карма пришла, не постучавшись."

    us "Эй, чего такой кислый?" # Опять Уля спокойная и не ребенок

    if 'us' in list_sch_ch_known:
        show us grin sport far at cleft with dissolve
        us "Нога ещё болит?"
        ivan "Благодаря тебе."

    show dv normal pioneer2 normal at cleft
    show us smile sport normal at cright

    with dissolve

    ivan "Может быть, пропустите?" # На "Вы" потому что их две, но тут надо более решительно, ибо он понимает, что попал

    show dv normal pioneer2 close at cleft
    show us smile sport close at cright

    with vpunch

    pause(0.4)

    show dv normal pioneer2 normal at cleft
    show us smile sport normal at cright

    with dspr

    iv "Это что ещё за наезды?!" # привет, Кэп

    if persistent.dv_good_sch or persistent.true_sch:
        $ meet('dv', u"Алиса")
        $ pt_dv +=1
        iv "А, вижу. Ведро с мутной водой. Специально для меня."
        ivan "Не дождётесь!"
        if 'us' in list_sch_ch_known or persistent.us_true_sch:
            "Разгон, полное игнорирование опешевшей Ульянки, и Алису за пояс!"
        else:
            "Разгон, полное игнорирование опешевшей мелкой, и Алису за пояс!"
        "Вес минимален, хотя сначала и не скажешь."
        "Живой щит, спаси меня!"
        hide us
        show dv shocked pioneer2 close at cleft:
            zoom 1.2 xalign 0.44 yalign 0.33
        with vpunch
        dv "Что делаешь, псих!" # должен быть крик и физическое насилие, ибо она почти такой же силы
        hide dv with vpunch
        ivan "И я тебя тоже помню." # звучит тупо
        with sch_running
        scene ext_square_day
        with vpunch
        if 'us' in list_sch_ch_known:
            "Ульяна не подвела."
        else: # КОРОТКО СЛИШКОМ
            "Мелкая не подвела."
        extend "Побежав за мной с ведром, она споткнулась и облила Алису!" # опять сухое комментирование
        with sch_running
    elif persistent.dv_reject_sch or persistent.dv_neutral_sch or persistent.dv_transit_good_sch or persistent.dv_bad_sch:
        show dv normal pioneer2 close at cleft
        show us smile sport close at cright
        with vpunch
        pause(0.2)
        show dv normal pioneer2 normal at cleft
        show us smile sport normal at cright
        with dspr
        with flash
        dv "Я держу! Давай!"
        if persistent.dv_bad_sch:
            play sound waterslpash
            with vpunch
            "На меня вылили несколько литров жидкого и грязного льда и оставили мокнуть в гордом одиночестве." # плохо
            ivan "Я бы понял, если бы меня ещё завели куда подальше, но льдом нахрена обливать?!" # подальше - это куда?
            "Кричал я уже воздуху." # опять сухо
            "Тем не менее, от этого теплее не стало. Пришлось найти скамейку, чтобы отдышаться, скинуть свитер и кое-как отжать джинсы."
        else:
            if 'us' in list_sch_ch_known:
                "Мне удалось выскользнуть из заключения у увернуться ровно в тот момент, как Ульяна вылила на рыжую несколько литров холодной воды."
            else: # тоже как-нибудь жирнее и активнее
                "Мне удалось выскользнуть из заключения у увернуться ровно в тот момент, как мелкая вылила на рыжую несколько литров холодной воды."
            "А это значит, что мне пора бежать, пока они находятся в непонимании."
            us "Ой, Алис, извини!"
            $ meet('dv', u"Ульяна")
            dv "НОВИЧО-О-К!!!" # вообще, это кличка Семена из 7дл. Надо что-то другое
            with sch_running
            scene ext_square_day
            with sch_running
            pause (0.7)
            scene ext_house_of_mt_day with vpunch
            iv "Вроде бы сбежал."
            ivan "День начинается не с кофе..."
            iv "А чёрт пойми с чего!"
    return


label sch_day1_dv_sl_meet:
    $ persistent.sprite_time = "day"
    $ day_time()
    play ambience ambience_camp_entrance_day_people fadein 1
    scene ext_clubs_day with fade
    play music sunpatterns fadein 1
    return


label sch_day1_mi_meet:
    $ persistent.sprite_time = "day"
    $ day_time()
    play ambience ambience_camp_entrance_day_people fadein 1
    scene ext_clubs_day with fade
    play music sunpatterns fadein 1
    "Но, похоже, что не судьба - за мной бежала ещё одна пионерка." # кривоооо
    show mi normal pioneer with dissolve
    mi "Привет, ты новенький? Конечно, новенький, я ведь раньше тебя не видела, да и формы на тебе нет. Ты, наверное, к вожатой идёшь? Кстати, меня Мику зовут. Никто не верит, но я настоящая японка!"
    $ meet('mi', u"Мику") # Мику тараторка, но не настолько и не глупая
    ivan "Привет. Да, я иду к вожатой."
    ivan "Меня зовут Иван."
    mi "Иван? То есть Ваня? Очень приятно. Какое милое на слух имя. У нас вообще в отряде мальчиков почти нет, а у них имена твёрдые, жёсткие." # СпрОведливА
    "Похоже, что моё имя ей по-настоящему понравилось." # или нет - где здоровый пессимизм от такой ситуации?
    mi "Ваня, ты не можешь мне помочь убрать сцену после вчерашнего концерта? Жаль, тебя не было, было так весело, даже меньшие отряды отличились!"
    menu:
        "Помочь Мику":
            $ pt_mi +=1
            $ sch_day1_mi_inclub = True
            ivan "Конечно, только давай немного быстрее, а то мне ещё идти к Ольге Дмитриевне." # опа, он говорит так, будто две недели знает ОД
            show mi grin pioneer with dspr
            mi "Хорошо-хорошо, сейчас мы быстро перетащим всё, что нужно, и я тебя отведу." # акция невиданной щедрости, реакция ГГ?
        "Отказаться":
            $ pt_mi -=1
            if sch_hard:
                $ pt_pi -=10
            ivan "Извини, Мику, но ты сама сказала, что я к вожатой спешу. Если я успею освободиться пораньше, то приду помочь тебе. Хорошо?"
            show mi sad pioneer with dspr
            mi "Ну ладно. Пока." # не в стиле Мику
            hide mi with dissolve
    return

label sch_day1_mi:
    # БГ сцены
    # это было написано 24.10, но я уже себя блеймлю
    ivan "Мы пришли?"
    mi "Да. Видишь, тут ещё даже немного конфетти осталось?"
    iv "Откуда в СССР конфетти в небольшом лагере?"
    mi "Привезла много, половину использовали ещё на первой неделе."
    mi "Осталось немного, храню к прощальной дискотеке."
    ivan "Это, конечно, всё очень круто, но ты меня зачем сюда привела? Поговорить?"
    mi "А мне молчать? Ладно." # тут типа Мику несколько обижена, хотя какого черта она должна обидиться от слов новичка
    ivan "Лучше скажи, что нужно утащить."
    mi "Сначала отсоедини все провода от колонок и усилителя, потом кинь их мне."
    ivan "Ещё что-то?"

    return








label sch_day1_od:
    $ persistent.sprite_time = "day"
    $ day_time()

    stop music fadeout 1

    pause(1)

    play sound sfx_close_door_1


label sch_day1_med:
    label boom:
        # Уля выпрыгивает
        us "Бу!"
        ivan "А-а-а!"
        #звуки падения
        "Дальше я слышал лишь заглушённые голоса."
        us "Ой, Новенький, ты в порядке? Новенький? Алло?"
        sl "Уля, что тут проис-{w=1} Ой! Что с ним произошло?"
        us "Славушка, извини, я только хотела испытать новенького, а он какой-то совсем не живучим оказался..."
        sl "Эй, парень!"
        sl "Новичок!"
        sl "Уля, ты что натворила? Он без сознания!"
        us "Мне Виолу позвать?"
        sl "Быстро!"
        "Я почувствовал, что поднялся. Но не мне принадлежало тело, чтобы я сделал это по своей воле."
        # окончательно минус глаза и разум
        # Картина маслом - Уля, Славя и Виола
        "Я почувствовал резкий и невыносимый запах, и..."
        ivan "А! Фух-фух..."
        "Так хочется дышать. А вокруг лишь пустота, пустота..."
        #пощёчина
        iv "Верните мне мою тьму!"
        ivan "Что... Где я?"
        cs "Ты? В 1989-м, дружок. На что-нибудь жалобы есть?"
        ivan "Пить хочется."
        cs "Держи."
        # звуки питья воды
        "Я наконец смог различать блеклые оттенки, котоыре приобрели цвет и форму."
        "Я оказался в стерильно белой комнате на какой-то чересчур твёрдой койке, рядом с которой был стол, видимо, местной медсестры, отвернувшейся от меня и сидевшей за каким-то толстым компьютером, играя в... Хоних? Зоникс? Ксоникс? Не важно."
        ivan "Здравствуйте, эм..."
        "Она соизвоила обернуться на меня и удосужиться посмотреть на моё состояние."
        cs "Виолетта Церновна. Для тебя Виола, {w=0.5}пионер. И не называй меня на \"вы\", пионэр. Мне ещё тридцати нет."
        menu:
            "Виолетта Церновна.":
                $ pt_pi +=10
                cs "Попросила же..."
            "Виола.":
                $ pt_wi +=10
                cs "Так-то лучше."
                #улыбка
                "Медсестра по-своему улыбнулась."

        ivan "Погодите, какой сейчас год?"
        cs "Тебе, может, и день сказать? Сегодня... {w} кхем... {w} 5 июля 1989 года."
        "Сестра мельком оглянулась на календарь."
        iv "Я в бреду. Я в бреду."
        ivan "Точно не ошиблись?"
        cs "Точно, пионэр."
        ivan "То есть, сейчас не 2019?"
        cs "2019-ый? Голова точно не болит?"
        cs "У меня есть один способ её решить..."
        ivan "Нет-нет. Просто показалось."
        cs "Да? {w} Слушай, пионер. То, что ты умудрился попасть в медпункт в первый день, конечно, рекорд. Но мне нужно об этом сообщить твоей вожатой, а оставить я тебя не могу."
        cs "Поэтому выбирай. С тобой может посидеть Лена, которая мне помогает и в случае чего не даст тебе снова превратиться в овоща. {w} Или \"твоя\""
        # подмигивание
        extend "Славя."
        ivan "С чего это она \"моя?\""
        cs "Ты хочешь сказать, что вы не знакомы? И почему это она тогда от тебя не отходила, пока я её на скамейку не выгнала?"
        if 'sl' in list_sch_ch_known:
            ivan "С утра буквально."
        else:
            ivan "Я даже не знаю, кто она!"

        cs "Хм, интересно."
        cs "Однако ты её должник. Если бы не она, то ты бы так и лежал на плитке под солнышком."

    label sch_day1_med_chose:

        menu:
            "Я со Славей посижу":
                cs "Хочешь сказать \"спасибо?\""
                cs "Сейчас позову."
                $ sch_day1_med = 'sl'
                $ pt_sl +=1
            "Лена хоть знает, что делать":
                cs "Только не сильно приставай к ней, понял, пионэр?"
                ivan "Угу."
                cs "Вот и отлично. Лен, посидишь за главную, пока я к вашей вожатой сбегаю?"
                un "Да, Виолетта."
                $ pt_sl +=1
            "А одному нельзя?" if not sch_day1_med_asked:
                "Не хотелось бы сейчас сидеть в чей-то компании."
                cs "Нет. Мне нужен кто-то, кто будет смотреть за медпунктом."
                $ sch_day1_med_asked = True
                jump sch_day1_med_chose

        cs "Ну всё, я побежала."
        #Минус Виола
        if sch_day1_med == 'sl':
            "В комнату взамен крайне откровенно одетой докторши вошла Славя."
            if 'sl' in list_sch_ch_known:
                "В комнату вошла Славя и села рядом со мной на койку."
                sl "Сильно от Ульянки досталось?"
                ivan "Как видишь."
                sl "Бедный."
                ivan "Зачем жалеешь-то? Я не лишился руки или головы."
                sl "Так нельзя такое допускать! Надо быть осторожнее?"
                ivan "Извини, но выхлопной трубы мне в комплекте не дали, чтобы я смог привыкнуть."
                sl "Ты откуда-то далеко, что там настолько грязный воздух?"
                ivan "Ещё утром был в Москве."
                sl "Тогда понятно."
                #TODO
            else:
                #Славя незнакома
                #TODO
        else:
            "В комнату аккуратно просочилась Лена."
            ivan "Привет."
            un "П-привет."
            ivan "Мы так и не закончили разговор."
            $ sch_day1_un_guilty = False
            ivan "Продолжим нашу милую беседу или мне стоит замолчать и смотреть в потолок ближайшее время? Кстати, сколько обычно она времени \"гуляет?\""
            un "Минут п-пятнадцать, наверное."
            ivan "Тогда у нас целых пятнадцать минут, чтобы помолчать о своём."
            #Прошло 5 минут тишины
            "Прошло где-то пять минут."
            "Первой, неожиданно, сдалась Лена."
            un "Мне сказали, что ты приехал в довольно тёплой одежде."
            ivan "И насколько тёплой?"
            un "В пальто и с заснеженным рюкзаком." # улыбка
            if sch_true:
                "Вот блин!"
            else:
                ivan "Заснеженным? А-ха-ха!"
            ivan "Кто сказал хоть?"
            un "Ульянка."
            ivan "Это которая?"
            un "С рыжими хвостами и низкая."
            ivan "Так вот, кто меня напугал!"
            un "Ч-что?" #снова смущение
            ivan "Ну, после нашего неудачного диалога я пошёл дальше по улице, и на меня набросилась эта сумасшедшая."
            un "Она не сумасшедшая, она ребёнок!"
            ivan "Кровожадный ребёнок."
            un "И что дальше?"
            ivan "А что ещё может быть? Упал в обморок, по разведданным меня притащила на собственном горбу "
            if not 'sl' in list_sch_ch_known:
                extend "некая Славя."
            else:
                extend "Славя."
            ivan "Вот скажи мне, это норма для неё?"
            # чуть мрачнее Лена
            un "Не знаю."
            "Разговор зашёл в тупик - как обычно и происходит со мной при общении с ней."
            ivan "Лен, можно попросить об одолжении?"
            un "Что?"
            ivan "Я тут новенький, ничего не знаю, а свободного времени на исследование лагеря самостоятельно уже лишился."
            ivan "К тому же мне завтра, наверное, дадут лист на обход всей вашей необъятной территории."
            un "Ты хочешь сказать, что..."
            iv "Так, а тут неловко уже мне."
            menu:
                "Перевести тему":
                    ivan "Нет-нет, я молчу."
                    un "Постой, я..."
                    ivan "Что?"
                    un "Ничего."
                "Предложить прогулку по лагерю":
                    ivan "Как насчёт прогулки по лагерю? Сможешь мне его показать?"
                    # Лена смущение
                    un "Я н-не знаю... Мне нужно подумать."
                    $ sch_day1_un_walk = True
                    $ pt_un +=1
                    ivan "У тебя целый вечер на это."

        "Кстати, а вот и наша Виолетта в сопровождении какой-то девушки врываются без стука."
        ivan "А если я в интимном положении? Постучаться нельзя?"
        mt "А вот и наш новенький. И как ты успел?"
        ivan "Успел что?"
        iv "Переместиться на 30 лет и пару сезонов за глазки с приятным бонусом в виде омоложения? Самому бы знать."
        mt "В медпункт попасть. За два года торжественно заявляю, что ты - первый."
        ivan "Извините, вы надо мной смеяться пришли али по делу?"
        # деловое настроение
        mt "Ну раз ты не в настроенни шутить, тогда позволь представиться - Миронова Ольга Дмитриевна."
        $ meet('mt', 'Ольга Дмитриевна')
        mt "Можно просто по имени-отчеству."
        ivan "И кто вы мне?"
        mt "С тобой всё хорошо?"
        iv "Да вы сговорились! Хотя бы синоним подобрали!"
        ivan "Наверное, нет."
        mt "Тогда я тебе напомню. Ты попал в пионерлагерь \"Совёнок!\""
        ivan "Угу. С СССР и красными галстуками."
        mt "Не зазнавайся! С этого момента я за тебя отвественна перед целью создания из тебя полноценного и примерного пионера!"
        ivan "Я болен. Но не стоит меня винить в этом."
        mt "Если ты так беспокоишься о мести, то Ульянка уже всё получила."
        ivan "Вы это успели узнать за... сколько?"
        mt "А кто ещё это мог сделать?"
        ivan "Так если вы знаете причину, почему я должен страдать? Почему не предотвратить?"
        mt "Потому что не имеем права. Наказывать можно за проступок, а он ничего не делала пока что... До этого момента."
        mt "Виол, что скажешь?"
        cs "Да бегать будет, куда ему."
        if sch_day1_med_chose != 'sl':
            un "Я-я пойду?"
            mt "Да, Тихонова, ты можешь быть свободна."
        else:
            sl "Я могу сопровождать его сегодня."
            mt "Хватит с тебя, Феоктисова. У тебя дел нет?"
            sl "Есть, но..."
            mt "Вот и занимайся ими. А он не беспомощный. Да, пионер?"
            ivan "Да."
        # минус героиня