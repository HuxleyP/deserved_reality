transform out_transition:
    





# Дизайн меню by Лишняя | Запятая, рабочая часть by DeadFox и Huxley

init 999:
    $ style.sch_keys = Style(style.default)
    $ style.sch_keys.color = "#000000"
    $ style.sch_keys.hover_color = "#800000"
    $ style.sch_keys.size = 83
    $ style.sch_keys.font = csn

    $ style.sch_keys_reversed = Style(style.default)
    $ style.sch_keys_reversed.color = "#800000"
    $ style.sch_keys_reversed.hover_color = "#000000"
    $ style.sch_keys_reversed.size = 53
    $ style.sch_keys_reversed.font = dr_font

screen sch_menu:
    tag menu
    modal True
    add menu_sch("white.png")
    add menu_sch("line.png") xpos 849 ypos 375


    vbox: #Продолжить_Игру
        textbutton ("•Продолжить_Игру"):
            xpos 363
            ypos 414
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump("sch_savescreen")]

    vbox: #Новая_Игра
        textbutton ("•Новая_Игра"):
            xpos 363
            ypos 484
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump("day1_cr")]

    vbox: #Настройки
        textbutton ("•Настройки"):
            xpos 363
            ypos 554
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump("sch_options")]

    vbox: #Ачивки
        textbutton ("•Достижения"):
            xpos 363
            ypos 629
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump("sch_achievements")]

    vbox: # TOBEDONE на "настройки"
        textbutton ("#To be done"):
            xpos 863
            ypos 564
            background None
            text_style "sch_keys_reversed"
            style "sch_keys_reversed"
            action [OpenURL("https://vk.com/deserved_reality"), Stop('music', fadeout=2), Return()]

    vbox: # TOBEDONE на "ачивки"
        textbutton ("#To be done"):
            xpos 863
            ypos 639
            background None
            text_style "sch_keys_reversed"
            style "sch_keys_reversed"
            action [Hide("sch_menu"), OpenURL("https://vk.com/deserved_reality"), Stop('music', fadeout=2), Return()]

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

label sch_savescreen: # открывается окошко с сейвами мода
    scene undone with dissolve
    $ renpy.pause(3)
    $ sch_ingame = True
    jump sichium

label sch_achievements: # окошко с ачивками
    scene undone with dissolve
    $ renpy.pause(3)
    $ sch_ingame = True
    jump sichium

label sch_settings:
   screen sch_settings_menu:
