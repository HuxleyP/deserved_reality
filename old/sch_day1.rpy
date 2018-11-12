label sch_day1_arrival:

    window hide

    $ persistent.sprite_time = "day"
    $ day_time()

    scene bg int_bus with flash_red

    play ambience ambience_camp_entrance_day_people fadein 1

    "Голова раскалывается."
    "Что это вообще было?"

    iv "Где я вообще?"

    if limb:
        "Здесь так жарко и душно... как в Лимбе."

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

            $ name_sch("Я")
            ivan "Кто же ты такой?"

            $ name_sch("Иван")
            ivan "Что, не понравилась легенда прошлого?"

            $ name_sch("Я")
            ivan "Зато нравится идея хорошего будущего."

            show uv normal pioneer with dissolve

            dreamgirl "Как и мне."

            scene bg int_bus with flash_red

    elif prophet:

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


    $ name_sch("Я")

    "И ярко..."
    "Жарко?!"
    "Я оказался в незнакомом мне автобусе."
    "Рядом лежало пальто и рюкзак."

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
    ivan "Икарус? Их же давно списали."

    scene bg ext_road_day with fade

    "А приехал я, похоже, по дороге, идущей из ниоткуда."

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

            scene bg ext_camp_entrance_day with fade

        "Зайти в лагерь":

            "Я подошёл к дверям и решил приоткрыть ворота."


    return

label sch_day1_slavya:

    $ persistent.sprite_time = "day"
    $ day_time()

    play ambience ambience_camp_entrance_day_people fadein 1

    scene bg ext_camp_entrance_day

    "Ворота начали открываться, и из-за них аккуратно, почти на носочках, выбежала какая-то девочка."
    "Ну, девушка."
    "На вид ей было где-то семнадцать-восемнадцать лет, её волосы"

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

            show sl normal pioneer with dspr

            ivan "Я как бы даже не знаю, где я."
            sl "Как не знаешь? Ты приехал в пионерлагерь \"Совёнок!\""

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
        "Это что за пионерская реконструкция ещё?"

    sl "Тебе сейчас надо к вожатой, я тебе скажу, как туда пройти. Хотя, лучше возьми с собой карту!"

    "Девочка дала мне свёрнутый бело-жёлтый листок из плотной бумаги и собиралась убежать по своим важным делам." # скомканно слишком, 30 строк на первую встречу - мало

    ivan "Хоть скажешь, как зовут?"
    sl "А, извини. Нашу вожатую зовут Ольга Дмитриевна."
    ivan "Хорошо...{w=.3} Спасибо."

    menu:
        "Это всё?":

            sl "А тебе нужно узнать что-то ещё?"
            ivan "Нет, я, думаю, разберусь."
            sl "Хорошо. Пока!"

        "И в какой домик идти?":

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

                "Отказаться":

                    ivan "Ещё и ждать? Нет, я лучше сам."

                    show sl normal pioneer with dspr

                    sl "Ну ладно."

                    extend "Надеюсь, тебе здесь понравится! Я побежала! Пока!" # слишком резко смена настроения

    hide sl with dissolve

    return

label sch_day1_loner:
    $ persistent.sprite_time = "day"
    $ day_time()

    play ambience ambience_camp_entrance_day_people fadein 1
    scene ext_clubs_day with fade
    play music sunpatterns fadein 1
    "Мои ожидания по поводу общего вида лагеря изнутри не оправдались."
    "То, что было повреждённым и стёршимся снаружи, выглядело абсолютно новым и чистым внутри." # топорноооо
    "Лес, похоже, почти не вырубали, даже ландшафт выглядит абсолютно нетронутым."
    "И первое здание - клубы." # какие клубы? что за херню ты молишь? одно описание ахуительнее другого
    "На вывеске было какое-то неразличимое расписание, а за дверями слышался шум статики."
    "К тому же из открытого окна доносилось несколько голосов, искажённых ветром."
    "А это значит, что мне лучше туда не входить."
    scene ext_clubs_day with dissolve
    "Дальше дорожка тоже вела прямо, так что я мог идти и рассматривать окружение без размышления, куда идти, пока" # мне не нравится куча "тоже" и прочих союзов, ибо это визуальная новелла и тут по=хорошему описание от лица рассказчика
    show un normal pioneer at cleft with dissolve
    extend "я не увидел на своём пути ещё одну девушку."
    "Сначала не заметив меня, она шла непринуждённо, но, встретившись взглядами, "
    show un shy pioneer at cleft with dspr
    extend "её передернуло и она зацвела." # звучит тупо
    menu:
        "Поздороваться":
            $ sch_day1_un_known = True
            $ pt_un +=1
            $ pt_wi +=10
            ivan "Привет."
            show un surprise pioneer at cleft with dissolve
            un "П-привет."
            ivan "Меня зовут Ваня. А тебя?"
            un "Меня зовут Ле..."
            ivan "Ле...?"
            un "Лена." # опять ГГ слишком резко знакомится, нет малейшего описания
            $ meet('un', u"Лена")
            show un shy pioneer at cleft with dissolve
            "А я уже перерос стесняться перед противоположным полом." # как бы стёб, но сейчас я понял, что вообще-то уже правда
            play sound_loop sfx_bush_leaves
            #TODO Screen с ульяной
            if sch_day1_un_us_spotted:
                menu:
                    "Заступиться":
                        $ pt_us -=1
                        $ pt_un +=1
                        $ sch_day1_us_known = True
                        "Я заметил шуршение в кустах и рыжий отлив волос, и..."
                        ivan "Мелкая, вылезай!"
                        show un surprise pioneer at cright with dissolve
                        ivan "Лена, на тебя чуть не напали только что." #тупо x2
                        show us dontlike pioneer at cright with dissolve
                        us "Ну вот, а ты кто ещё такой?"
                        ivan "Тот же вопрос и к тебе." # вообще диалог не в духе Ульянки, которая бежала и запыхалась, потом пряталась в кустах и теперь так спокойно, как Киборг, говорит (вообще проблема всех диалогов)
                        us "Вопросом на вопрос не отвечают."
                        ivan "Я мимо проходил."
                        show us angry pioneer at cright with dspr
                        us "Ну так и проходи мимо!"
                        hide us
                        show un normal pioneer at center
                        with flash_red
                        "Моя коленка!"
                        ivan "Вот негодяйка..." # тут должны быть маты, но литературный язык сказал нет
                        show un smile pioneer with dspr
                        un "Ульянка такая..."
                        $ meet('us', u"Ульяна")
                        ivan "Спасибо, хоть буду знать, как зовут моего {i}врага!{/i}" # герой не такой жизнерадостный
                        show un shy pioneer with dspr
                        ivan "Пока. Ещё увидимся!"
                        un "Пока." # опять же, Лена должна покрыться краской
                        show un normal pioneer close with dspr
                        pause(0.5)
                        hide un with dspr
                    "Игнорировать":
                        $ pt_un -=1
                        $ pt_us +=1
                        $ sch_day1_un_guilty = True
                        play sound_loop sfx_bush_leaves
                        "Я думал, что шуршание кустов было лишь из-за ветра, но" # опять от лица героя так, будто это рассказчик
                        stop ambience
                        play music music_list["i_want_to_play"] fadein 1
                        window hide
                        scene cg d1_grasshopper with dissolve
                        extend " из них выпрыгнула мелкая хулиганка и напала на девочку с огромной саранчой!"
                        un "А{w=0.35}-а{w=0.17}-a{w=0.09}-a{w=0.7}а!"
                        scene bg ext_clubs_day
                        show us laugh pioneer
                        with dissolve
                        us "Ха-ха-ха-ха!"
                        ivan "И зачем?"
                        us "Да ладно, весело же!"
                        us "Ну ладно, я пошла!" # да ладно - ну ладно
                        hide us with dissolve
                        "Ну и ну..."
                        stop music fadeout 1
                        play ambience ambience_camp_entrance_day_people fadein 1
            else:
                $ sch_day1_un_guilty = True
                $ pt_un -=1
                $ sch_day1_un_guilty = True
                play sound_loop sfx_bush_leaves
                "Я думал, что шуршание кустов было лишь из-за ветра, но"
                stop ambience
                play music music_list["i_want_to_play"] fadein 1
                window hide
                scene cg d1_grasshopper with dissolve
                extend " из них выпрыгнула мелкая хулиганка и напала на девочку с огромной саранчой!"
                un "А{w=0.35}-а{w=0.17}-a{w=0.09}-a{w=0.7}а!"
                scene bg ext_clubs_day
                show us laugh pioneer
                with dissolve
                us "Ха-ха-ха-ха!"
                ivan "И зачем?"
                us "Да ладно, весело же!"
                us "Ну ладно, я пошла!" # тафталогия
                hide us with dissolve
                "Ну и ну..."
                stop music fadeout 1
                play ambience ambience_camp_entrance_day_people fadein 1
        "Идти дальше":
            $ pt_wi +=10
            "Лучше пройти мимо - познакомиться с обитателями я ещё успею, да и потребуется ли." # опять в одном сообщении
    return



label sch_day1_camp_enter_sl:
    $ persistent.sprite_time = "day"
    $ day_time()
    play ambience ambience_camp_entrance_day_people fadein 1
    scene ext_clubs_day with fade
    play music sunpatterns fadein 1
    "Мои ожидания по поводу общего вида лагеря изнутри не оправдались." # описание скомканное
    "То, что было повреждённым и стёршимся снаружи, выглядело абсолютно новым и чистым внутри."
    "Лес, похоже, почти не вырубали, даже ландшафт выглядит абсолютно нетронутым."
    "И первое здание - клубы."
    "На вывеске было какое-то неразличимое расписание, а за дверями слышался шум статики."
    show sl normal pioneer far at cleft with dissolve
    sl "Я скоро вернусь." # С чего бы вообще, кстати, Славе, идти в клубы, если ей не горит? Нужно поджечь
    hide sl with dspr
    iv "И теперь я остался один, как маленький ребёнок, ждущий маму." # плохое сравнение
    iv "Но ведь я не ребёнок?" # x2
    menu:
        "Сбежать":
            $ pt_sl -=1
            "Пока я не потерял свой последний шанс на личную неприкосновенность и свободу, нужно действовать." # опять глупо на фоне полного непонимания всей ситуации
            "И под этим я имею в виду тихий уход из под дверей, пока меня она не заметила."
            $ sch_day1_sl_together = False
        "Ждать":
            "А сбежав я только подтвержу свою ветренность." # WAIT WHAT - ты 5 минут тут, какя ветренность?
            "Отказываться надо было раньше - сейчас поезд уехал."
            with fade
            show sl normal pioneer at cleft with dissolve
            sl "Не заждался?"
            ivan "Нет, всё в порядке."
            show sl smile pioneer at cleft with dspr
            sl "Отлично! Пойдём; Ольга Дмитриевна, наверное, заждалась."
    return

label sch_day1_sl:
    $ persistent.sprite_time = "day"
    $ day_time()
    play ambience ambience_camp_entrance_day_people fadein 1
    scene ext_houses_day with fade
    play music sunpatterns fadein 1
    show sl normal pioneer with dissolve
    ivan "Можешь просвятить меня в том, что тут обычно происходит?" # язык не поворачивается
    sl "Ну, у нас тут определённый распорядок дня - если что, расписание на обратной части карты."
    sl "Подъем в восемь, отбой в полночь, четырёхразовое питание, но никто тебе не мешает не приходить в столовую - только потом не жалуйся."
    sl "Раз в неделю дискотека или концерт. А на этой неделе будет всё сразу, последняя же." # Славя - точно не робот-картонка? Должны быть ивенты, которых она ждёт больше остальныъ
    ivan "Получается, я опоздал на две трети смены?" # КАПИТАН ОЧЕВИДНОСТЬ ВРЫВАЕТСЯ В ЗДАНИЕ
    scene ext_square_day
    show sl sad pioneer
    with dissolve
    sl "Да."
    ivan "Не нужно печалиться насчёт меня."
    sl "Но ты так много пропустил!"
    ivan "Мне без разницы." # тут бы по макушке от неё получить, ибо она вся правильная и вообще нужно ценить
    scene bg ext_house_of_mt_day
    show sl normal pioneer
    with dissolve
    sl "Кстати, а откуда ты?" # разумный вопроос, но опять скомканный, Славя должна иметь какую-то причину о таком спрашивать
    "Не тот ты вопрос задала, девочка."
    ivan "Мы пришли?"
    sl "Угу."
    show dv normal pioneer2 far at cleft with dissolve
    if sch_day1_dv_known:
        ivan "Оперативно у вас тут реагируют на происшествия."
        show sl sad pioneer with dspr
        ivan "Жаль, что не предотвращают."
    hide sl with easeinleft
    play sound sfx_knock_door7_polite
    pause(1)
    return


label sch_day1_dv:
    $ persistent.sprite_time = "day"
    $ day_time()
    play ambience ambience_camp_entrance_day_people fadein 1
    scene ext_clubs_day with fade
    play music sunpatterns fadein 1
    iv "И всё же тут довольно неплохо, люди добрые и не лезут, как у меня... дома." # Славя лезет, ГГ не должен про дом заикаться - хоть он не помнит, почему, но он осознанно его покинул
    show dv normal pioneer2 far at cleft
    show us smile sport far at cright
    with dissolve
    us "Эй, чего такой кислый?" # Опять Уля спокойная и не ребенок
    if sch_day1_us_known:
        us "Нога ещё болит?"
        ivan "Благодаря тебе."
    show dv normal pioneer2 normal at cleft
    show us smile sport normal at cright
    with dissolve
    ivan "Может, пропустите?" # На "Вы" потому что их две, но тут надо более решительно, ибо он понимает, что попал
    show dv normal pioneer2 close at cleft
    show us smile sport close at cright
    with vpunch
    pause(0.4)
    show dv normal pioneer2 normal at cleft
    show us smile sport normal at cright
    with dspr
    iv "Это что ещё за наезды?!" # привет, Кэп
    if not (persistent.dv_good_sch or persistent.dv_reject_sch or persistent.dv_neutral_sch or persistent.dv_true_sch or persistent.dv_transit_good_sch or persistent.dv_transit_bad_sch) or persistent.dv_bad_sch:
        $ meet('dv', u"Алиса")
        $ pt_dv +=1
        iv "А, вижу. Ведро с мутной водой. Специально для меня."
        ivan "Не дождётесь!"
        "Алису в охапку и вперёд!" # Терминатор confirmed, вообще это событие происходит только с героем "в цикле", который уже прошёл через рут и что-то знает, следственно, вспоминает
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
        if sch_day1_us_known:
            "Ульяна не подвела."
        else: # КОРОТКО СЛИШКОМ
            "Мелкая не подвела."
        extend "Побежав за мной с ведром, она споткнулась и облила Алису!" # опять сухое комментирование
    else:
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
            $ sch_day1_dv_fail
        else:
            pass
            # QTE
        if sch_day1_dv_fail:
            play sound waterslpash
            with vpunch
            "На меня вылили несколько литров жидкого и грязного льда и оставили мокнуть в гордом одиночестве." # плохо
            ivan "Я бы понял, если бы меня ещё завели куда подальше, но льдом нахрена обливать?!" # подальше - это куда?
            "Кричал я уже воздуху." # опять сухо
            "Тем не менее, от этого теплее не стало. Пришлось найти скамейку, чтобы отдышаться, скинуть свитер и кое-как отжать джинсы."
        else:
            if sch_day1_us_known:
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
            iv "А чёрт пойми с чего!" # а с чего? опять обрыв мыслей
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
