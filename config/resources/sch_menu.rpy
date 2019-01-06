label sch_defaultsettings:
    $ persistent.sch_widget = False # Виджет ОП, надо поработать над ним
    $ persistent.sch_difficulty = False # False для Noraml
    $ persistent.undone_jumper = False # Прыгалка на незаконченные руты, при False герой заведомо не будет выходить
    $ persistent.sch_launched = True # Проверка на запуск, при нём применяются настройки выше и больше не трогаются

    return

init 999:
    $ style.sch_keys = Style(style.default)
    $ style.sch_keys.color = "#000000"
    $ style.sch_keys.hover_color = "#800000"
    $ style.sch_keys.size = 83
    $ style.sch_keys.font = csn

    $ style.sch_keys_reversed = Style(style.default)
    $ style.sch_keys_reversed.color = "#800000"
    $ style.sch_keys_reversed.hover_color = "#000000"
    $ style.sch_keys_reversed.size = 83
    $ style.sch_keys_reversed.font = dr_font

    $ style.sch_keys_white = Style(style.default) # Объявление
    $ style.sch_keys_white.color = "#ffffff" # Цвет текста
    $ style.sch_keys_white.hover_color = "#800000" # Цвет при наведении
    $ style.sch_keys_white.size = 83 # Размер
    $ style.sch_keys_white.font = csn

    $ style.sch_desc = Style(style.default)
    $ style.sch_desc.color = "#ffffff"
    $ style.sch_desc.hover_color = "#800000"
    $ style.sch_desc.size = 40
    $ style.sch_desc.font = csn

init:
    $ hide_back = False # Убрать кнопку Назад при True

    # Объявляем основные ассеты

    image bg white = "#fff"
    image white2 = "#ffffff"
    image blacksquare = 'deserved_reality/source/images/gui/menu/square.png'
    image whitesquare = im.MatrixColor("deserved_reality/source/images/gui/menu/square.png", im.matrix.colorize("#fff", "#fff"))
    image gray = "#171717"

    # Объявляем текст для анимаций

    # Меню

    image sch_begin = Text("•Продолжить_Игру", style="sch_keys")
    image sch_continue = Text("•Новая_Игра", style="sch_keys")
    image sch_settings = Text("•Настройки", style="sch_keys")
    image sch_achievements = Text("•Достижения", style="sch_keys")


    image sch_settings_reversed = Text("•Настройки", style="sch_keys_reversed")

    # Настройки

    image sch_back_white = Text("/Назад/", style="sch_keys_white", size = 100)

    image sch_placeholder_off = Text("•Заглушки - OFF", style="sch_keys_white")
    image sch_placeholder_on = Text("•Заглушки - ON", style="sch_keys_white")

    image sch_widget_off = Text("•Виджет ОП - OFF", style="sch_keys_white")
    image sch_widget_on = Text("•Виджет ОП - ON", style="sch_keys_white")

    image sch_difficulty_Hard = Text("•Сложность по умолчанию - Hard", style="sch_keys_white")
    image sch_difficulty_Normal = Text("•Сложность по умолчанию - Обычная", style="sch_keys_white")
    image sch_difficulty_undefined = Text("•Сложность по умолчанию - не установлена", style="sch_keys_white")

    image sch_es_settings = Text("•Перейти в настройки игры", style="sch_keys_white")

screen sch_placeholder_desc:
window:
        text "Данная опция позволяет включить заглушки,\nКоторые препятствуют переходу на незаконченный рут."
        style 'sch_desc'
        pos(400, 362)

screen sch_difficulty_desc:
    window:
        text "Данная опция позволяет сменить сложность при выборе по умолчанию.\nНормальная сложность - рекомендуется.\nHardmode - сложный режим, меньше ОП, суровее условия.\nНе установлено - выбор при начале игры.\nПо умолчанию - не установлено."
        style 'sch_desc'
        pos(400, 362)

screen sch_widget_desc:
    window:
        text "Данная опция позволяет включить заглушки,\nКоторые препятствуют переходу на незаконченный рут."
        style 'sch_desc'
        pos(400, 362)

screen sch_es_settings_desc:
    window:
        text "По нажатию этой кнопки\nВы можете перейти в настройки игры,\nЧтобы изменить различные настройки."
        style 'sch_desc'
        pos(400, 362)


screen sch_menu:
    tag menu
    modal True
    add '#fff'
    add 'blacksquare' xalign 0.5 yalign 0.5 xzoom 0.12 yzoom 3.62 xanchor 111


    vbox:   #Продолжить_Игру
        textbutton ("•Продолжить_Игру"):
            xpos 363
            ypos 414
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump("sch_savescreen")]

            #Новая_Игра
        textbutton ("•Новая_Игра"):
            xpos 363
            ypos 484
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump('sch_newgame')]

            #Настройки
        textbutton ("•Настройки"):
            xpos 363
            ypos 554
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump("sch_settings_in")]

            #Ачивки
        textbutton ("•Достижения"):
            xpos 363
            ypos 624
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump("sch_achievements")]


    imagebutton: #Ливнуть
        auto menu_sch("ButtonExit_%s.png")
        xpos 0
        ypos 1008
        action [Hide("sch_menu"), Jump("original_mm")]






















































































label sch_main_menu_intro:

    scene bg white
    show blacksquare:
        xalign 0.5 yalign 0.5
        zoom 20.0
        pause 2.0
        ease 1.0 zoom 1.0
        linear 0.75 xzoom 0.12
        easein 0.75 yzoom 3.62
        linear 0.75 xanchor 111
    pause(5.25)
    show white2:
        xpos 861
    show sch_begin behind white2:
        pos(861, 414)
        linear 0.75 xanchor 498
    show sch_continue behind white2:
        pos(861, 484)
        linear 0.75 xanchor 498
    show sch_settings behind white2:
        pos(861, 554)
        linear 0.75 xanchor 498
    show sch_achievements behind white2:
        pos(861, 624)
        linear 0.75 xanchor 498
    show exit_idle:
        pos (-72, 1008)
        linear 0.75 pos(0, 1008)
    pause(0.75)

    jump screen sch_menu




label sch_newgame: # Новая игра
    scene white
    show blacksquare:
        xalign 0.5 yalign 0.5
        xanchor 111 xzoom 0.12 yzoom 3.62
    show sch_begin:
        pos(363, 414)
    show sch_continue:
        pos(363, 484)
    show sch_achievements:
        pos(363, 624)
    show exit_idle:
        pos(0, 1008)

    show white2:
        xpos 861

    show blacksquare:
        xalign 0.5 yalign 0.5 xanchor 111 xzoom 0.12 yzoom 3.62
        linear 0.75 xanchor 0
        easein 0.75 yzoom 1.0
        linear 0.75 xzoom 1.0
        pause(1.75)
        easein 1.0 zoom 20.0
        pause(1)

    jump sch_game_start

    return




label original_mm: # возвращение в меню
    $ renpy.block_rollback()
    stop sound fadeout 1
    stop music fadeout 1
    stop ambience fadeout 1
    play music music_list["blow_with_the_fires"] fadein 1
    call screen main_menu
    return
