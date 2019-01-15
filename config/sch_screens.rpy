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

    vbox:        #Новая_Игра
        textbutton ("•Новая_Игра"):
            xpos 363
            ypos 484
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump('sch_newgame')]

    vbox:        #Настройки
        textbutton ("•Настройки"):
            xpos 363
            ypos 554
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump("sch_settings")]

    vbox:        #Ачивки
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



label sch_settings: # Переход в настройки



    call screen sch_settings_menu



screen sch_settings_menu:
    tag menu
    modal True
    add '#171717'
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
                ypos 519
                text_style "sch_keys_white"
                style "sch_keys_white"
                action [Hide("sch_menu"), Jump("sch_settings_out")]





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
