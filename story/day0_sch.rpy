label sch_day0_prehistory:
    $ prolog_time()
    $ persisent.sprite_time = 'Night'

    play music distant fadein 2
    $ renpy.pause(1, hard = True)

    show unblink

    # Предыстория

    scene bg ext_winterpark with fade

    voice "Ты помнишь, что я переезжаю?"
    ivan "Да, что-то было."
    voice "Проблема в том, что я переезжаю туда, куда ты вряд ли отправишься."
    ivan "В Америку какую-нибудь?"
    voice "В точку. И скорее всего, я вряд ли вернусь сюда после обучения. Сам понимаешь."
    "Нависло неловкое молчание."
    "В холодном воздухе воцарились одинокие снежинки и звуки тяжёлого дыхания."
    ivan "Но мы всё равно сможем общаться через ВК, да?"
    voice "Если не потеряемся."

    scene bg semen_room with fade

    "А всё так хорошо начиналось - встреча в соц. сети после 10 лет разлуки, а через два месяца это?"
    "Ненавижу."

    scene bg ext_winterpark with fade

    ivan "Ненавижу!"
    voice "Что?"
    ivan "Проваливай! Проваливай отсюда!"
    "И я остался один."

    scene anim prolog_2 with fade

    "Непонятные трудности, потом короткие гудки и удалённый аккаунт с изменённым именем."
    "Прошёл год."

    with fade

    "А я не могу забыть."
    "Только воспоминания тускнеют с каждым днём, да деталей становится меньше."
    "Со временем они будут вытесняться другими, и я забуду, из-за чего ненавижу свою жизнь."

    show blink

    if cycled:
        call sch_prologue_default

    show unblink

    if not cycled:
        show bg semen_room behind blink
        hide blink
        show unblink

    "Привет, Реальность."
    "Какой день ты создала для меня сегодня?"
    return





label sch_day0_prehistory:
    $ prolog_time()
    $ persisent.sprite_time = 'Night'

    play music distant fadein 2
    $ renpy.pause(1, hard = True)

    show unblink

    # Предыстория

    scene bg ext_winterpark with fade

    voice "Ты помнишь, что я переезжаю?"
    ivan "Да, что-то было."
    voice "Проблема в том, что я переезжаю туда, куда ты вряд ли отправишься."
    ivan "В Америку какую-нибудь?"
    voice "В точку. И скорее всего, я вряд ли вернусь сюда после обучения. Сам понимаешь."
    ivan "Но мы всё равно сможем общаться через ВК, да?"
    voice "Если не потеряемся."

    scene bg semen_room with fade

    "А всё так хорошо начиналось - встреча в соц. сети после 10 лет разлуки, а через два месяца это?"
    "Ненавижу."

    scene bg ext_winterpark with fade

    ivan "Ненавижу!"
    voice "Что?"
    ivan "Проваливай! Проваливай отсюда!"

    "И я остался один."

    scene anim prolog_2 with fade

    "Непонятные трудности, потом короткие гудки и удалённый аккаунт с изменённым именем."
    "Прошёл год."
    "А я не могу забыть."
    "Только воспоминания тускнеют с каждым днём, да деталей становится меньше."
    "Со временем они будут вытесняться другими, и я забуду, из-за чего ненавижу свою жизнь."


    if not cycled:
        show bg semen_room behind blink

        hide blink
        show unblink

    "Привет, Реальность."
    "Какой день ты создала для меня сегодня?"
    return


label sch_day0_keys:
    $ prolog_time()
    $ persisent.sprite_time = 'Night'

    #TODO

    return

label sch_prologue_chose:
    $ prolog_time()
    $ persisent.sprite_time = 'Night'

    play music cassiopeia fadein 1

    scene anim prolog_2

    with flash

    if sch_true:

        "Яркий свет снова покинул меня."
        "А иногда так хочется в нём раствориться."

        dreamgirl "Ты пойдёшь со мной?"
        ivan "В который раз ты уже спрашиваешь..."
        "И в который раз я отвечаю..."

        menu:
            "Я ничего не обещаю.":

                $ limb = True

                dreamgirl "Я понимаю."

            "Я приду." if sch_true:

                $ prophet = True

                dreamgirl "Я знаю."



    elif cycled:


        "Яркий свет рассеялся, и я всё вспомнил."
        "Мне снова снится тот же сон, тянущийся из глубокого детства, повторяющий про безвыходную ситуацию."
        "{b}Она{/b} говорила отрывисто, уверенно, но я её не слушал."
        "{b}Она{/b} знала что-то, чего не знаю я, и это что-то было очень важным."
        dreamgirl "Ты пойдёшь со мной?"
        ivan "От меня ничего не зависит. Сама знаешь."

        "И я ли тут нахожусь?"
        "И мой ли это сон?"

        ivan "Я ничего не обещаю."

        $ limb = True

        dreamgirl "Я понимаю."

    else:
        $ name_sch('Иван')

        show blink

        show uvao_d0 at cleft behind blink
        show anim prolog_2 behind uvao_d0

        pause(1.5)

        hide blink with dspr

        stop music fadeout 1
        play music cassiopeia fadein 1

        "Мне снова снится тот же сон, тянущийся из глубокого детства."
        "И снова я видел ту девочку в коротком оборванном платьице."

        dreamgirl "Ты пойдёшь со мной?"

        "Куда пойду? О чём она?"

        dreamgirl "Всё или ничего."

        ivan "От меня ничего не зависит. Сама знаешь."

        "Это я?"

        dreamgirl "Так попытайся."

        "И я ли тут нахожусь?"
        "И мой ли это сон?"
        "И сон ли это вообще?"

        $ limb = True

    dreamgirl "Прощай."

    stop music fadeout 1

    return


label sch_prologue_normal:
    $ prolog_time()
    $ persisent.sprite_time = 'Night'

    $ set_mode_nvl()

    scene anim prolog_2 with fade

    play music nullspace fadein 1

    $ nvl show dissolve

    "Мне 7 лет. Я впервые иду в школу."
    "Эта атмосфера счастья и радости, ожидания чего-то неизвестного, и от того это всё больше должно захватывать!"
    "Но не для меня."

    $ name_sch('Ваня')

    ivan "Мама! Мамочка, ты где?"
    iv "Мне очень страшно."
    voice "Эй, малыш, не плачь! Ты в порядке? Спокойно, спокойно. Ты ищешь маму?"
    ivan "Угу..."

    nvl clear

    with dissolve

    "Всхлипывает маленький ребёнок на большом празднике."

    iv "А эта девочка мне помогает. Какая она хорошая!"
    iv "Я бы точно-точно на ней поженился!"

    voice "Давай знакомиться, пока ищем твою маму. Вдруг опять потеряешься?"
    ivan "Меня зовут Иван!"

    iv "Говорю как самый настоящий взрослый, где формальность - признак важности."

    voice "А меня - ... Пойдём искать твою маму?"

    nvl clear

    with dissolve

    iv "Я хожу по лесу из ног и тел, ведомый чей-то милой и тёплой рукой."

    mother "Ой, спасибо, что нашли моего сына. Извините за беспокойство."

    iv "Но я стою и не отпускаю руку этой девочки."

    mother "Что это с тобой?"

    iv "А теперь она смеётся. Но не надо мной же? Она не может надо мной смеяться. Она слишком добрая."
    iv "И она наклоняется ко мне."
    iv "И я наконец вижу её лицо."
    iv "Идеальные черты лица, жёлтые сверкающие глаза... Она плачет? Но из-за кого?"

    ivan "А мы с тобой ещё увидимся?"
    voice "Обязательно, дорогой. А теперь иди к маме, тёте пора."

    iv "Я с неохотой отпускаю руку и бросаюсь в объятия мамы."

    nvl clear

    with Fade(3)

    $ renpy.pause(3, hard = True)

    iv "Как же неохота вставать. А идти в школу вообще не хочется!"
    iv "Опять сидеть за партой и слушать."
    iv "А зачем оно мне? Я и без цифр хорошо жил."

    mother "Пойдём, а то опоздаем."
    ivan "Но я не хочу!"
    mother "А есть такое слово - надо."

    iv "\"Надо\" - слово как слово. И от чего он считается таким особенным? Ведь другие слова тоже важны. Без слова \"Мама\" ты не позовёшь маму, без слова \"Привет\" ты ни с кем не поздороваешься."
    iv "Но иногда слова так несовершенны!"

    nvl clear

    with dissolve

    mother "Мне учитель сказал, что у тебя нет друзей. Совсем-совсем нет? Почему ты ни с кем не общаешься?"
    ivan "А мне никто и не нужен. Кроме мамы."

    iv "И той девочки."

    mother "Если не найдёшь себе друзей, то тебе будет туго в жизни."

    iv "И кто это сказал? Мне и без друзей хорошо живётся."

    nvl clear

    with dissolve

    pause(2)

    chat "Привет! Давай дружить!"

    ivan "Меня зовут Ваня! Давай!"

    nvl clear

    with dissolve

    iv "Мне 12. Шестой класс."
    iv "И я снова один."
    iv "Потому что слишком медленный. Может я чего-то не понимаю?"
    iv "А потом переезд. Коробки, пыль, вечная возня, со знакомыми попрощаться времени нет. Кроме одного."

    nvl clear

    with dissolve

    iv "Далеко не тёплый приём в новой школе, гнобление со стороны сверстников и отчаяние."
    iv "Я все ещё переписываюсь со старыми знакомыми, начинаю пробовать себя в искусстве."

    nvl clear

    with dissolve

    iv "Мне 15 лет. Я чувствую себя взрослым и умным, но розовые очки той хорошей реальности, что создали мне родители и учителя, начали трескаться."
    iv "Рисование отпало почти сразу же, как и фотография. Музыку я писал около года, и тоже забросил. Попробовал себя в писательстве. Кажется, что нашёл себя, но снова провал."

    nvl clear

    with dissolve

    stop music fadeout 1
    play music cassiopeia fadein 1

    iv "А по ночам мне снится та девушка с янтарными глазами."

    nvl clear

    $ set_mode_adv()

    show uv normal

    with dissolve

    $ sch_name('Иван')

    ivan "Она обещала увидиться."
    ivan "Слышишь? Ты обещала."
    ivan "И что теперь? И зачем?"

    scene semen_room_night with dissolve
    $ renpy.pause(2, hard=True)
    scene semen_room_day with dissolve

    "Мне 23 года. Снаружи тяжёлые латы - зимнее чёрное пальто полное пустых карманов, ничего не значащих фраз непробиваемый панцирь, а внутри хрупкий моторчик качает пару литров литров красной краски."
    "Это обо мне."

    scene semen_room_sunset
    $ renpy.pause(1, hard=True)

    "И снова творчество. Правда времени нет почти, всё на работу."
    "Да и нечем восполнять обескровленное сердце, которое уже толкает в организм даже не краску - а лишь пустые, полупрозрачные, с серым оттенком безысходности обещания и слова, забивающиеся и оседающие на стенках сосудов и в мозгу."
    "Потом эта неприятная ситуация с последним человеком, который был мне дорог и покинул меня."
    "А что сейчас? Хочется лишь сбежать от мира во вселенную перенасыщенного басом звука из вакуумных наушников и сине-белого экрана мессенджера, в котором я общаюсь ради того, чтобы просто не сгнить."

    scene bg int_home_lift_sch with fade

    "Засыпает город, \nНикому не спится."

    window hide

    $ renpy.pause(2)

    stop sound_loop fadeout 1
    pause(1)
    play ambience ambience_cold_wind_loop fadein 3
    play sound sfx_intro_bus_stop_steps

    scene anim intro_2

    with fade

    $ renpy.pause(3, hard=True)

    scene anim intro_3

    with fade

    $ renpy.pause(3, hard=True)

    scene anim intro_4

    with fade

    "Каждый получает \nТо, к чему стремится."
    if sch_true == 1:
        "19/1987/last..."
        "С этого всё началось, этим всё и закончится."

    else:
        pass

    $ renpy.pause(1, hard = True)

    window hide

    scene bg bus_stop with dissolve

    "Я снова стою на своей остановке, самой далёкой для маршрута."
    "Куда я еду? Не знаю. Может, туда, где лучше?"

    stop ambience fadeout 1
    stop music fadeout 1
    play sound sfx_intro_bus_engine_start

    $ renpy.pause(3)

    play sound_loop sfx_intro_bus_engine_loop fadein 3

    if (sch_true) or (sch_bound):
        "410. Наш автобус отправляется в ад."

    else:
        pass

    play sound_loop sfx_intro_bus_engine_loop fadein 3

    window hide

    $ renpy.pause(2)

    scene anim intro_10
    with fade

    play sound sfx_intro_bus_door_open

    $ renpy.pause(3, hard=True)
    scene anim intro_11

    with fade

    $ renpy.pause(1, hard=True)

    stop sound_loop fadeout 4

    scene bg intro_xx

    with fade

    stop ambience fadeout 2
    play sound_loop sfx_bus_interior_moving fadein 4

    window show

    play music distant fadein 1

    $ set_mode_nvl()

    nvl show dissolve

    "Наша жизнь - всего лишь бесконечная череда бесконечных событий, происходящих в один момент."
    "Кто-то умирает, кто-то рождается, а кто-то стоит посреди города с растеряным выражением лица и не знает, что делать дальше."
    "Наверное, чтобы окончательно не потеряться в бесконечном течении временных параллелей, люди придумали Время."
    "Оно все упрощает. Но оно беспощадно."
    "И каждый из нас становится медленным самоубийцей, бесцельно растрачивающим свои драгоценные минуты жизни."
    "Момент сменяется моментом."
    "Слова заменяются эмоциями."

    $ renpy.pause(1, hard=True)

    "Мир не стоит на месте."

    pause(0.5)

    "И никто не имеет права этого изменить."

    nvl hide dissolve

    nvl clear

    $ set_mode_adv()

    window hide

    show blink

    show bg intro_xx behind blink

    show unblink
    hide blink

    $ renpy.pause(2, hard=True)

    "Хочется просто взять и уйти."

    ivan "Остановите!"

    stop sound_loop fadeout 1
    play sound sfx_intro_bus_engine_start

    show bg bus_stop with fade

    $ renpy.pause(3)

    play sound wind
    play music connor

    show bg bus_stop_summer with dissolve(.7)

    pause(0.7)

    play sound wind

    show bg bus_stop with dissolve(.7)

    ivan "Что?!"

    show blink

    pause(1)

    show bg bus_stop_summer with dissolve

    show unblink
    hide blink

    play sound wind

    pause(1)

    show blink

    $ name_sch("Иван")

    ivan "А-а-а-а!"

    pause(0.7)

    play sound wind

    scene bg black with fade

    play sound sfx_bodyfall_1

    $ renpy.pause(2)

    return


label sch_prologue_true:
    $ prolog_time()
    $ persisent.sprite_time = 'Night'

    return


label sch_prologue_normal_end:
    $ prolog_time()
    $ persisent.sprite_time = 'Night'

    play ambience ambience_camp_center_night fadein 2

    $ renpy.pause(2)

    play music aire fadein 1

    scene cg uvao_d0 with dspr

    dreamgirl "Ты как?"

    "Меня встретила даже не девушка - девочка - в коротком порванном мини-платье и бинтом на ноге."
    "Её жёлтые глаза кого-то мне напоминали, но кого?"

    show anim prolog_2 behind uvao_d0
    show uv normal at left

    hide cg uvao_d0

    with dissolve

    $ name_sch("Я")

    ivan "Где я?"
    dreamgirl "Там, где тебе нужно оказаться."
    ivan "Дай угадаю - пока я сейчас валяюсь во сне и вижу тебя в качестве плода воспалённого воображения, добрые санитары утирают мне пену и надевают фиременную рубашку с застёжками на спине?"
    dreamgirl "Понятия не имею, о чём ты, но ты не спишь."

    with flash_red

    show uv normal at left

    "Ай!"

    ivan "Ты чего? Могла просто ущипнуть!"
    dreamgirl "Зато ты убедился, что это не сон."
    dreamgirl "Может быть, мы вернёмся к делу?"
    ivan "Кстати о делах - ты кто вообще?"

    show uv upset at left with dspr

    dreamgirl "Перестань притворяться - обратно я тебя всё равно не верну."

    show uv normal at left with dspr

    dreamgirl "Не узнаёшь свой сон? Мне пора обижаться?"

    show bg ext_entrance_night_water_sch behind uv with dspr

    "Передо мной показался вход."
    "Но куда он ведёт? Буквы казались размытыми и от того совсем не читаемыми."

    ivan "Ты можешь не играть в угадайку?"

    "Меня начала раздражать эта нелепая таинтсвенность."

    iv "Сколько я тут вообще нахожусь?"

    "Спрашивать эту странную девочку, похоже, тоже бессмысленно."

    menu:
        "Отпусти меня.":
            ivan "Я не знаю, где я, но я просто хочу вернуться."
            dreamgirl "Дело твоё. Если твои атомы не разбросает по Вселенной, то у тебя хотя бы будет время подумать, что ты натворил."

            with fade

            $ deathflag = True

        "Что тебе нужно?":
            dreamgirl "От тебя? Чтобы ты поверил мне."
            ivan "Допустим, я верю."
            dreamgirl "Тогда пойдём."

            scene cg uvao_d0 with dissolve

            "Она подошла ко мне настолько близко, что я мог слышать её дыхание."

            scene cg uvao_d0_2 with dissolve

            dreamgirl "А теперь..."
            dreamgirl "Спи..."

            stop music fadeout 1


    window hide

    scene bg black with fade

    if not deathflag:
        play sound wind

    pause (0.5)

    play sound sfx_bodyfall_1

    return

label sch_prologue_true_end:
    $ prolog_time()
    $ persisent.sprite_time = 'Night'

    play music finale fadein 1

    scene bg ext_entrance_night_clear_sch
    show uvao_d0

    with dspr

    "Я очнулся."
    "Те же, там же."

    dreamgirl "Снова встретились."
    ivan "Как по таймеру."
    dreamgirl "Ты готов?"

    "Она снова мне протянула свою холодную руку."
    "Я снова взял её и снова не мог её расцепить."
    "Да и не особо хотел - теперь я знал достаточно.."
    "И получил возможность..."

    pause (0.3)

    "Исправить свою жизнь..."
    "И сделать всё правильно с самого начала."

    dreamgirl "Brace yourself, your last chance..."

    "Напевала мне моя подруга."

    ivan "Last summer..."

    $ renpy.pause(3, hard=True)

    play sound wind

    stop ambience fadeout 1
    stop music fadeout 1

    $ volume(1.0, 'music')

    return


label sch_prologue_death:
    $ prolog_time()
    $ persisent.sprite_time = 'Night'

    $ sch_chaper(0, u"Game over.")

    scene bg ext_liaz with dspr

    play music markus fadein 1

    "Меня встретил мой холодный зимний мир со свинцовым небом и несбывшимися мечтами, которым осталось лишь исчезнуть, не подкреплёнными ничем, кроме воспоминаний."
    "В глазах темнело."

    ivan "Прошай, Реальность."

    show bg black with fade

    $ renpy.pause(5, hard=True)

    stop music fadeout 5
    stop ambience fadeout 1

    $ renpy.pause(3)

    $ volume(1.0, 'music')

    return
