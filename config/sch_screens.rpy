label sch_defaultsettings:
    $ persistent.sch_widget = False # Виджет ОП, надо поработать над ним
    #$ persistent.sch_butterfly = False # Эффект бабочки
    $ persistent.sch_difficulty = False # False для Noraml
    $ persistent.sch_custom = True # custom для сочетания двух стилей
    $ persistent.undone_jumper = False # Прыгалка на незаконченные руты, при False герой заведомо не будет выходить
    $ persistent.sch_launched = True
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
    $ hide_back = False



    image bg white = "#fff"
    image white2 = "#ffffff"
    image blacksquare = 'deserved_reality/source/images/gui/menu/square.png'
    image whitesquare = im.MatrixColor("deserved_reality/source/images/gui/menu/square.png", im.matrix.colorize("#fff", "#fff"))
    image gray = "#171717"

    image sch_begin = Text("•Продолжить_Игру", style="sch_keys")
    image sch_continue = Text("•Новая_Игра", style="sch_keys")
    image sch_settings = Text("•Настройки", style="sch_keys")
    image sch_achievements = Text("•Достижения", style="sch_keys")

    image sch_settings_reversed = Text("•Настройки", style="sch_keys_reversed")


    image sch_back_white = Text("/Назад/", style="sch_keys_white", size = 100)

    image sch_placeholder_off = Text("•Заглушки - OFF", style="sch_keys_white")
    image sch_placeholder_on = Text("•Заглушки - ON", style="sch_keys_white")

    image sch_sprites_normal = Text("•Спрайты - Оригинал", style="sch_keys_white")
    image sch_sprites_orika = Text("•Спрайты - \"Выбор автора\"", style="sch_keys_white")

    image sch_widget_off = Text("•Виджет ОП - OFF", style="sch_keys_white")
    image sch_widget_on = Text("•Виджет ОП - ON", style="sch_keys_white")

    image sch_es_settings = Text("•Перейти в настройки игры", style="sch_keys_white")



screen sch_placeholder_desc:
    window:
        text "Данная опция позволяет включить заглушки,\nКоторые препятствуют переходу на незаконченный рут."
        style 'sch_desc'
        pos(400, 362)

screen sch_custom_desc:
    window:
        text "Данная опция позволяет сменить внешний вид спрайтов и фонов.\nОригинал - спрайты из оригинальной игры.\nCustom - смесь спрайтов Орики и оригинальной игры."
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



label sch_menu_anim_mm:


    scene bg white
    show blacksquare:
        xalign 0.5 yalign 0.5
        zoom 20.0
        pause 2.0
        ease 1.0 zoom 1.0
        linear 0.75 xzoom 0.12
        easein 0.75 yzoom 3.62
        linear 0.75 xanchor 111
    pause(5.75)
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


    return


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


label original_mm: # возвращение в меню
    $ renpy.block_rollback()
    stop sound fadeout 1
    stop music fadeout 1
    stop ambience fadeout 1
    play music music_list["blow_with_the_fires"] fadein 1
    call screen main_menu
    return

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


label sch_savescreen: # Загрузить игру
    scene undone with dissolve
    $ renpy.pause(3)
    $ sch_ingame = True
    jump sichium

label sch_achievements: # Достижения
    scene undone with dissolve
    $ renpy.pause(3)
    $ sch_ingame = True
    jump sichium

label sch_settings_in: # Переход в настройки

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

    show sch_settings_pressed:
        pos(363, 554)

    with Dissolve(0.001)

    scene gray

    show whitesquare:
        xalign 0.5 yalign 0.5
        xanchor 111 xzoom 0.12 yzoom 3.62

    with Dissolve(0.25)

    pause(0.25)

    show sch_back_white:
        pos(400, 519)

    if persistent.undone_jumper:
        show sch_placeholder_on:
            pos(903, 362)
    else:
        show sch_placeholder_off:
            pos(903, 362)

    if persistent.sch_sprites == 'Default':
        show sch_sprites_normal:
            pos(903, 442)
    elif persistent.sch_sprites == 'Orika':
        show sch_sprites_orika:
            pos(903, 442)

    if persistent.sch_widget:
        show sch_sprites_on:
            pos(903, 522)
    else:
        show sch_sprites_off:
            pos(903, 522)

    show sch_es_settings:
        pos(903, 644)

    with Dissolve(0.25)

    scene screen sch_settings_menu



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

        showif not persistent.sch_custom: # Спрайты
            textbutton ("•Спрайты - Оригинал"):
                xpos 903
                ypos 422
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                hovered [ToggleVariable(hide_back, true_value=False, false_value=True), Show('sch_custom_desc')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_custom', True), Jump("sch_settings_between")]
        elif persistent.sch_custom:
            textbutton ("•Спрайты - \"Выбор автора\""):
                xpos 903
                ypos 422
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                hovered [ToggleVariable(hide_back, true_value=False, false_value=True), Show('sch_custom_desc')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_custom', False), Jump("sch_settings_between")]

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
                ypos 519
                text_style "sch_keys_white"
                style "sch_keys_white"
                action [Hide("sch_menu"), Jump("sch_settings_out")]








label sch_settings_out:
    $ overriding_on = True

    window hide

    scene white
    show square:
        xalign 0.5 yalign 0.5 xzoom 0.12 yzoom 3.62 xanchor 111

    with Dissolve(0.25)
    pause(0.25)

    show sch_begin:
        pos(363, 414)
    show sch_continue:
        pos(363, 484)
    show sch_settings:
        pos(363, 554)
    show sch_achievements:
        pos(363, 624)
    show exit_idle:
        pos (-72, 1008)
        easein 0.25 pos(0, 1008)

    with Dissolve(0.25)

    $ overriding_on = False

    show screen sch_settings_menu
