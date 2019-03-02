
# виджет ЛП и музыки
screen sch_fuchsia_widget:
    modal False
    imagemap:
        ground 'bg_empty'
        if not (persistent.sch_widget or save_name == ('"Заслуженная Реальность. Меню."') or sch_hard):
            add sch_path + 'source/images/gui/arrow.png' anchor(0.5, 0.0) xalign 0.5 yalign 0.0
            alpha False
            hotspot (0, 0, 1920, 50) hovered [SetVariable("sch_WidgetVisible", True), Show("sch_widget_screen", transition=dspr)] action NullAction


screen sch_widget_screen:
    modal False
    imagemap:
        idle sch_path + "source/images/gui/widget_case.png"
        hover sch_path + "source/images/gui/widget_case.png"
        anchor(0.5, 0.0)
        xalign 0.5
        yalign 0.0
        hovered NullAction
        unhovered [Hide("sch_widget_screen", transition=dspr), SetVariable("sch_WidgetVisible", False)]
        action [Hide("sch_widget_screen", transition=dspr), SetVariable("sch_WidgetVisible", False)]

        if sch_true:
            add gui_sch('icons/karma_widget.png') xalign 0.67 ypos 10
        add gui_sch('icons/will_widget.png') xalign 0.785 ypos 10
        add gui_sch('icons/pioneer_widget.png') xalign 0.897 ypos 10

        $ list_sch_screenPos = [26, 242, 458, 674, 890] # 5 позиций
        $ sch_known = len(list_sch_ch_known) # Надо для скрина
        $ k = 0
        for i in range(len(list_sch_ch_known)):
            if not ((list_sch_ch_known[i] == 'mt') or list_sch_ch_known[i] == 'cs'):
                add gui_sch('icons/[list_sch_ch_known[i]]_widget.png')
                text '[list_sch_screenPos[i]]':
                    xalign list_sch_screenPos[k]
                    ypos 20
                    size 36
                    color '000000'
                    font font_sch('csn.ttf')
                $ k +=1
            else:
                pass






# Ниже меню. Нихрена не откалибровано, было заменено по причине дизайна (крайне херового, но ты, копатель по файлам, можешь заменить вызов скринов и посмотреть на это чудо инженегровой мысли)
screen sch_menu:
    tag menu
    modal True
    add '#fff'
    add 'blacksquare' xalign 0.5 yalign 0.5 xzoom 0.12 yzoom 3.62 xanchor 111

    add 'white2' zoom 0.7 xpos 861


    vbox:   #Продолжить_Игру
        textbutton ("•Продолжить_Игру"):
            xpos 363
            ypos 382
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump("sch_savescreen")]

    vbox:        #Новая_Игра
        textbutton ("•Новая_Игра"):
            xpos 363
            ypos 462
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump('sch_newgame')]

    vbox:        #Настройки
        textbutton ("•Настройки"):
            xpos 363
            ypos 542
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump("sch_settings_in")]

    vbox:        #Ачивки
        textbutton ("•Достижения"):
            xpos 363
            ypos 622
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Jump("sch_achievements")]


    imagebutton: #Ливнуть
        auto menu_sch("ButtonExit_%s.png")
        xpos 0
        ypos 1008
        action [Hide("sch_menu"), Jump("original_mm")]


screen sch_settings_menu:
    tag menu
    modal True
    add '#171717'
    add 'whitesquare' xalign 0.5 yalign 0.5 xzoom 0.12 yzoom 3.62 xanchor 111

    vbox:
        showif persistent.undone_jumper: #Заглушки
            textbutton ("•Заглушки - ON"):
                xpos 880
                ypos 382
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_placeholder_desc", transition=Dissolve(0.1))]
                hovered[ShowTransient('sch_placeholder_desc', transition=Dissolve(0.1)), Hide('sch_settings_back', transition=Dissolve(0.1))]
                action [Hide("sch_menu"), SetField(persistent, 'undone_jumper', False)]
        else:
            textbutton ("•Заглушки - OFF"):
                xpos 880
                ypos 382
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_placeholder_desc", transition=Dissolve(0.1))]
                hovered[ShowTransient('sch_placeholder_desc', transition=Dissolve(0.1)), Hide('sch_settings_back', transition=Dissolve(0.1))]
                action [Hide("sch_menu"), SetField(persistent, 'undone_jumper', True)]

        showif persistent.sch_difficulty: # Сложность
            textbutton ("•Сложность по умолчанию - Hardmode"):
                xpos 880
                ypos 436
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_difficulty_desc", transition=Dissolve(0.1))]
                hovered[ShowTransient('sch_difficulty_desc', transition=Dissolve(0.1)), Hide('sch_settings_back', transition=Dissolve(0.1))]
                action [Hide("sch_menu"), SetField(persistent, 'sch_difficulty', False)]
        showif persistent.sch_difficulty == False:
            textbutton ("•Сложность по умолчанию - Обычная"):
                xpos 880
                ypos 436
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_difficulty_desc", transition=Dissolve(0.1))]
                hovered[ShowTransient('sch_difficulty_desc', transition=Dissolve(0.1)), Hide('sch_settings_back', transition=Dissolve(0.1))]
                action [Hide("sch_menu"), SetField(persistent, 'sch_difficulty', None)]
        showif persistent.sch_difficulty == None:
            textbutton ("•Сложность по умолчанию - не установлено"):
                xpos 880
                ypos 436
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_difficulty_desc", transition=Dissolve(0.1))]
                hovered[ShowTransient('sch_difficulty_desc', transition=Dissolve(0.1)), Hide('sch_settings_back', transition=Dissolve(0.1))]
                action [Hide("sch_menu"), SetField(persistent, 'sch_difficulty', True)]

        showif persistent.sch_widget: # Виджет ОП
            textbutton("•Виджет ОП - ON"):
                xpos 880
                ypos 492
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_widget_desc", transition=Dissolve(0.1))]
                hovered[ShowTransient('sch_widget_desc', transition=Dissolve(0.1)), Hide('sch_settings_back', transition=Dissolve(0.1))]
                action [Hide("sch_menu"), SetField(persistent, 'sch_widget', False)]
        else:
            textbutton("•Виджет ОП - OFF"):
                xpos 880
                ypos 492
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_widget_desc", transition=Dissolve(0.1))]
                hovered[ShowTransient('sch_widget_desc'), Hide('sch_settings_back', transition=Dissolve(0.1))]
                action [Hide("sch_menu"), SetField(persistent, 'sch_widget', True)]

        textbutton("•Перейти в настройки игры"):
            xpos 880
            ypos 582
            background None
            text_style "sch_keys_white"
            style "sch_keys_white"
            unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide('sch_es_settings_desc', transition=Dissolve(0.1))]
            hovered[ShowTransient('sch_es_settings_desc'), Hide('sch_settings_back', transition=Dissolve(0.1))]
            action [ShowMenu('preferences')]

screen sch_settings_back:
            textbutton("/Назад/"):
                xpos 400
                ypos 529
                text_style "sch_keys_white"
                style "sch_keys_white"
                action [Hide("sch_menu"), Jump("sch_settings_out")]





screen sch_placeholder_desc:
    textbutton("Данная опция позволяет включить заглушки,\nКоторые препятствуют переходу на незаконченный рут."):
        style 'sch_desc'
        pos(300, 362)
        unhovered[Hide('sch_placeholder_desc', transition=Dissolve(0.1))]

screen sch_difficulty_desc:
    textbutton("Данная опция позволяет сменить сложность при выборе по умолчанию.\nНормальная сложность - рекомендуется.\nHardmode - сложный режим, меньше ОП, суровее условия.\nНе установлено - выбор при начале игры.\nПо умолчанию - не установлено."):
        style 'sch_desc'
        pos(300, 362)
        unhovered[Hide('sch_difficulty_desc', transition=Dissolve(0.1))]

screen sch_widget_desc:
    textbutton("Данная опция позволяет включить заглушки,\nКоторые препятствуют переходу на незаконченный рут."):
        style 'sch_desc'
        pos(300, 362)
        unhovered[Hide('sch_widget_desc', transition=Dissolve(0.1))]

screen sch_es_settings_desc:
    textbutton("По нажатию этой кнопки\nВы можете перейти в настройки игры,\nЧтобы изменить различные настройки."):
        style 'sch_desc'
        pos(300, 362)
        unhovered[Hide('sch_es_settings_desc', transition=Dissolve(0.1))]
