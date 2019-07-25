label dr_debug_sandbox:
    scene black
    show screen dr_debug_interpol_hell

label old_dr_debug_sandbox:
    $ dr_forgeteveryone()
    $ name_dr("Иван")
    $ day_time()
    $ dr_mode_adv()
    scene bg ext_road_day
    dr_uv "Я незнакомка."
    $ dr_meet("dr_uv", "Юля")
    dr_uv "Я Юля."
    $ dr_meet("dr_uv", "Харон")
    dr_uv "Я Харон."
    $ dr_meet("dr_uv", "Юля")
    $ dr_mode_nvl()
    dr_uv "Я Юля в новелле."
    $ dr_meet("dr_uv", "Харон")
    dr_uv "Я Харон в новелле."
    dr_th "Я мысли героя."
    "А я рассказчик."
    "Всё хорошо?"
    menu:
        "Да":
            $ dr_mode_adv()
            dr_uv "Ну и хорошо. Дай поспать-то!"
            $ dr_meet("dr_uv", "Кошка драная")
            ivan "А ну вернись, Кошка драная!"
            dr_uv "Ой, а кто это? Неужели Иван?"
            ivan "Откуда ты... Нет, Я - это Я!"
            $ name_dr("Я")
            dr_uv "Да ну? Прям \"Я?\""
            $ name_dr("Ваня")
            ivan "Ну... Да."
            dr_uv "Понятно всё с тобой. Иди отдыхать, Ваня."

        "Нет":
            dr_uv "Нет?! Так переделывай!"
    $ dr_mode_adv()
    "Рассказчик стреляется."
    return


screen dr_debug_interpol_hell:
    tag menu
    modal True
    add "bg black"

    add "dr_white2"

    add "dr_blacksquare" xalign 0.5 yalign 0.5 xzoom 0.12 yzoom 3.62 xanchor 111

    #add "dr_white2" zoom 0.7 xpos 861

    #text "{font=[source_dr]images/fonts/LemonTuesday.otf}{size=60}З{/font}{font=[source_dr]images/fonts/csn.ttf}аслуженная{/size}{/font}\n {size=50}{font=[source_dr]images/fonts/LemonTuesday.otf}Р{/font}{font=[source_dr]images/fonts/csn.ttf}{/size}{size=60}еальность{/size}{/font}":

        
    # потенциально сделать провекру на хардмод
    vbox:   #Открыть экран сейвов
        textbutton ("•Продолжить_Игру"): # может, только для бабочки?
            xpos 363
            ypos dr_pos1
            background None
            text_style "dr_keys"
            style "dr_keys"
            action NullAction()

        textbutton ("•Новая_Игра"):
            xpos 363
            ypos dr_pos2
            background None
            text_style "dr_keys"
            style "dr_keys"
            #action [Hide("dr_menu"), Jump("dr_newgame")]
            action NullAction()

        textbutton ("•Настройки"):
            xpos 363
            ypos dr_pos3
            background None
            text_style "dr_keys"
            style "dr_keys"
            action NullAction()
        
        textbutton ("•Создатели"):
            xpos 363
            ypos dr_pos4
            background None
            text_style "dr_keys"
            style "dr_keys"
            action NullAction()

    if persistent.cycled_debug:
        vbox:
            textbutton ("•Достижения"):
                xpos 363
                ypos dr_pos5
                background None
                text_style "dr_keys_gray"
                style "dr_keys_gray"
                action NullAction()

    else:
        textbutton ("•Достижения"):
            xpos 363
            ypos dr_pos5
            background None
            text_style "dr_keys"
            style "dr_keys"
            action NullAction()


    

    imagebutton: #Ливнуть
        auto dr_menu("ButtonExit_%s.png")
        xpos 0
        ypos 1008
        action [Hide("dr_debug_interpol_hell", transition = dissolve), Show("dr_exit_promt", transition = dissolve)]