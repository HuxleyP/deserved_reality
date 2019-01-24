label sch_savescreen_in: # Загрузить игру
    scene undone with dissolve
    $ renpy.pause(3)
    $ sch_ingame = True

label sch_achievements_in: # Достижения
    scene undone with dissolve
    $ renpy.pause(3)
    $ sch_ingame = True




screen sch_settings_menu:
    tag menu
    modal True
    add 'gray'
    add 'whitesquare' xalign 0.5 yalign 0.5 xzoom 0.12 yzoom 3.62 xanchor 111

    vbox:
        showif persistent.undone_jumper: #Заглушки
            textbutton ("•Заглушки - ON"):
                xpos 903
                ypos 362
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                hovered [ToggleVariable(hide_back, true_value=False, false_value=True), Show('sch_placeholder_desc')]
                action [Hide("sch_menu"), SetField(persistent, 'undone_jumper', False), Jump("sch_settings_between")]
        else:
            textbutton ("•Заглушки - OFF"):
                xpos 903
                ypos 362
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                hovered [ToggleVariable(hide_back, true_value=False, false_value=True)]
                action [Hide("sch_menu"), SetField(persistent, 'undone_jumper', True), Jump("sch_settings_between")]

        showif persistent.sch_difficulty: # Сложность
            textbutton ("•Сложность по умолчанию - Hardmode"):
                xpos 903
                ypos 482
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                hovered [ToggleVariable(hide_back, true_value=False, false_value=True), Show('sch_difficulty_desc')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_difficulty', False), Jump("sch_settings_between")]
        showif persistent.sch_difficulty == False:
            textbutton ("•Сложность по умолчанию - Обычная"):
                xpos 903
                ypos 482
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                hovered [ToggleVariable(hide_back, true_value=False, false_value=True), Show('sch_difficulty_desc')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_difficulty', None), Jump("sch_settings_between")]
        else:
            textbutton ("•Сложность по умолчанию - не установлено"):
                xpos 903
                ypos 482
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                hovered [ToggleVariable(hide_back, true_value=False, false_value=True), Show('sch_difficulty_desc')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_difficulty', True), Jump("sch_settings_between")]

        showif persistent.sch_widget: # Виджет ОП
            textbutton("•Виджет ОП - ON"):
                xpos 903
                ypos 542
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                hovered [ToggleVariable(hide_back, true_value=False, false_value=True), Show('sch_widget_desc')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_widget', False), Jump("sch_settings_between")]
        else:
            textbutton("•Виджет ОП - OFF"):
                xpos 903
                ypos 542
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                hovered [ToggleVariable(hide_back, true_value=False, false_value=True), Show('sch_widget_desc')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_widget', True), Jump("sch_settings_between")]

        textbutton("•Перейти в настройки игры"):
            xpos 903
            ypos 644
            background None
            text_style "sch_keys_white"
            style "sch_keys_white"
            hovered [ToggleVariable(hide_back, true_value=False, false_value=True), Show('sch_es_settings_desc')]
            action [ShowMenu('preferences')]

        showif not hide_back:
            textbutton("/Назад/"):
                xpos 400
                ypos 1000
                text_style "sch_keys_white"
                style "sch_keys_white"
                action [Hide("sch_menu"), Jump("sch_settings_out")]





init 1000:
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
            #action [Hide("sch_menu"), Jump("sch_savescreen_in")]

    vbox:        #Новая_Игра
        textbutton ("•Новая_Игра"):
            xpos 363
            ypos 484
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump('sch_newgame_in')]

    vbox:        #Настройки
        textbutton ("•Настройки"):
            xpos 363
            ypos 554
            background None
            text_style "sch_keys"
            style "sch_keys"
            #action [Hide("sch_menu"), Jump("sch_settings_in")]

    vbox:        #Ачивки
        textbutton ("•Достижения"):
            xpos 363
            ypos 624
            background None
            text_style "sch_keys"
            style "sch_keys"
            #action [Hide("sch_menu"), Jump("sch_achievements_in")]


    imagebutton: #Ливнуть
        auto menu_sch("ButtonExit_%s.png")
        xpos 0
        ypos 1008
        action [Hide("sch_menu"), Jump("original_mm")]






label sch_menu_anim_intro:

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

    scene screen sch_menu




label sch_newgame_in: # Новая игра
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
