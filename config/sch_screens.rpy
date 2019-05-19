
# виджет ЛП и музыки
screen sch_fuchsia_widget:
    modal False
    imagemap:
        ground 'bg_null'
        if (not (persistent.sch_widget or save_name == ("Заслуженная Реальность. Меню.") or sch_hard)):
            add sch_path + 'source/images/gui/arrow.png' anchor(0.5, 0.0) xalign 0.5 yalign 0.0
            alpha False
            hotspot (0, 0, 1920, 50) hovered [SetVariable("sch_WidgetVisible", True), Show("sch_widget_screen", transition=dspr)] action NullAction


screen sch_widget_screen:
    modal False
    imagebutton:
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

    #$ list_sch_screenPos = [26, 242, 458, 674, 890] # 5 позиций
    #$ sch_known = len(list_sch_ch_known) # Надо для скрина
    #$ k = 0
    #for i in range(len(list_sch_ch_known)):
    #    if not ((list_sch_ch_known[i] == 'mt') or list_sch_ch_known[i] == 'cs'):
    #        add gui_sch('icons/[list_sch_ch_known[i]]_widget.png')
    #        text '[list_sch_screenPos[i]]':
    #            xalign list_sch_screenPos[k]
    #            ypos 20
    #            size 36
    #            color '000000'
    #            font font_sch('csn.ttf')
    #        $ k +=1
    #    else:
    #        pass

    add source_sch + 'images/gui/icons/dv_widget.png' xpos 26 ypos 10
    add source_sch + 'images/gui/icons/us_widget.png' xpos 242 ypos 10
    add source_sch + 'images/gui/icons/un_widget.png' xpos 458 ypos 10
    add source_sch + 'images/gui/icons/sl_widget.png' xpos 674 ypos 10
    add source_sch + 'images/gui/icons/mi_widget.png' xpos 890 ypos 10
    text str(dr_dv):
        xpos 26
        ypos 20
        size 36
        color '#ff9600'
        font source_sch + "images/fonts/Roboto.ttf"

    text str(dr_us):
        xpos 242
        ypos 20
        size 36
        color '#ff0000'
        font source_sch + "images/fonts/Roboto.ttf"

    text str(dr_un):
        xpos 458
        ypos 20
        size 36
        color '#c045ff'
        font source_sch + "images/fonts/Roboto.ttf"

    text str(dr_sl):
        xpos 674
        ypos 20
        size 36
        color '#fff600'
        font source_sch + "images/fonts/Roboto.ttf"

    text str(dr_mi):
        xpos 890
        ypos 20
        size 36
        color '#00f6ff'
        font source_sch + "images/fonts/Roboto.ttf"

    showif persistent.sch_karma_shown == True:
        text str(dr_ka):
            xalign 0.67
            ypos 20
            size 36
            color '#000000'
            font source_sch + "images/fonts/Roboto.ttf"

    text str(dr_wi):
            xalign 0.785
            ypos 20
            size 36
            color '#000000'
            font source_sch + "images/fonts/Roboto.ttf"

    text str(dr_pi):
            xalign 0.897
            ypos 20
            size 36
            color '#000000'
            font source_sch + "images/fonts/Roboto.ttf"



screen sch_menu_pre:
    modal False
    key "game_menu":
        action NullAction()
    key "screenshot":
        action NullAction()
    timer 0.1 action (Hide("sch_menu_pre", transition=dissolve), Show("sch_menu"))


# Ниже меню. Нихрена не откалибровано, было заменено по причине дизайна (крайне херового, но ты, копатель по файлам, можешь заменить вызов скринов и посмотреть на это чудо инженегровой мысли)
screen sch_menu:
    tag menu
    modal True
    key "game_menu":
        action NullAction()
    key "screenshot":
        action NullAction()
    add "bg black"
    add "dr_main_menu_atl"
    add 'blacksquare' xalign 0.5 yalign 0.5 xzoom 0.12 yzoom 3.62 xanchor 111

    #add 'white2' zoom 0.7 xpos 861

    # потенциально сделать провекру на хардмод
    vbox:   #Открыть экран сейвов
        textbutton ("•Продолжить_Игру"): # может, только для бабочки?
            xpos 363
            ypos 382
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu", transition=Dissolve(0.5)), ShowMenu('load')] # сделать загрузку свою
            #action [Hide("sch_menu"), Jump("sch_savescreen")]

    vbox:        #Новая_Игра
        textbutton ("•Новая_Игра"):
            xpos 363
            ypos 462
            background None
            text_style "sch_keys"
            style "sch_keys"
            #action [Hide("sch_menu"), Jump('sch_newgame')]
            action [Hide("sch_menu"), Return('sch_newgame')]

    vbox:        #Настройки
        textbutton ("•Настройки"):
            xpos 363
            ypos 542
            background None
            text_style "sch_keys"
            style "sch_keys"
            action [Hide("sch_menu"), Show("sch_settings_menu", transition=Dissolve(0.5))]

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
        action [Hide("sch_menu", transition=dissolve), Show("sch_exit_promt", transition=dissolve)]
        # action [ShowMenu("sch_exit_promt", transition=Dissolve(0.5))] # на случай, если найду лейбл оригинального меню игры
        # action MainMenu() совсем запасной


screen sch_settings_menu:
    tag menu
    modal True
    key "game_menu":
        action NullAction()
    key "screenshot":
        action NullAction()
    add '#171717'
    add 'whitesquare' xalign 0.5 yalign 0.5 xzoom 0.12 yzoom 3.62 xanchor 111

    mousearea:
        area(0, 0, 1920, 1080)
        hovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1))]
        unhovered[Hide('sch_settings_back')]

    vbox:
        showif persistent.undone_jumper: #Заглушки
            textbutton ("•Заглушки - ON"):
                xpos 880
                ypos 382
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_placeholder_desc")]
                hovered[ShowTransient('sch_placeholder_desc', transition=Dissolve(0.1)), Hide('sch_settings_back')]
                action [Hide("sch_menu"), SetField(persistent, 'undone_jumper', False)]
        else:
            textbutton ("•Заглушки - OFF"):
                xpos 880
                ypos 382
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_placeholder_desc")]
                hovered[ShowTransient('sch_placeholder_desc', transition=Dissolve(0.1)), Hide('sch_settings_back')]
                action [Hide("sch_menu"), SetField(persistent, 'undone_jumper', True)]

        showif persistent.sch_difficulty: # Сложность
            textbutton ("•Сложность по умолчанию - Hardmode"):
                xpos 880
                ypos 436
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_difficulty_desc")]
                hovered[ShowTransient('sch_difficulty_desc', transition=Dissolve(0.1)), Hide('sch_settings_back')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_difficulty', False)]
        showif persistent.sch_difficulty == False:
            textbutton ("•Сложность по умолчанию - Обычная"):
                xpos 880
                ypos 436
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_difficulty_desc")]
                hovered[ShowTransient('sch_difficulty_desc', transition=Dissolve(0.1)), Hide('sch_settings_back')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_difficulty', None)]
        showif persistent.sch_difficulty == None:
            textbutton ("•Сложность по умолчанию - не установлено"):
                xpos 880
                ypos 436
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_difficulty_desc")]
                hovered[ShowTransient('sch_difficulty_desc', transition=Dissolve(0.1)), Hide('sch_settings_back')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_difficulty', True)]

        showif persistent.sch_widget: # Виджет ОП
            textbutton("•Виджет ОП - ON"):
                xpos 880
                ypos 492
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_widget_desc")]
                hovered[ShowTransient('sch_widget_desc', transition=Dissolve(0.1)), Hide('sch_settings_back')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_widget', False)]
        else:
            textbutton("•Виджет ОП - OFF"):
                xpos 880
                ypos 492
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_widget_desc")]
                hovered[ShowTransient('sch_widget_desc', transition=Dissolve(0.1)), Hide('sch_settings_back')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_widget', True)]

        showif persistent.sch_chapter_skip:
            textbutton("•Пропуск названий глав - ON"):
                xpos 880
                ypos 522
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_chskip_desc")]
                hovered[ShowTransient('sch_chskip_desc', transition=Dissolve(0.1)), Hide('sch_settings_back')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_chapter_skip', False)]
        else:
            textbutton("•Пропуск названий глав - OFF"):
                xpos 880
                ypos 522
                background None
                text_style "sch_keys_white"
                style "sch_keys_white"
                unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide("sch_widget_desc")]
                hovered[ShowTransient('sch_chskip_desc', transition=Dissolve(0.1)), Hide('sch_settings_back')]
                action [Hide("sch_menu"), SetField(persistent, 'sch_chapter_skip', True)]


        #textbutton("•Перейти в настройки игры"):
        #    xpos 880
        #    ypos 582
        #    background None
        #    text_style "sch_keys_white"
        #    style "sch_keys_white"
        #    unhovered[ShowTransient('sch_settings_back', transition=Dissolve(0.1)), Hide('sch_es_settings_desc')]
        #    hovered[ShowTransient('sch_es_settings_desc'), Hide('sch_settings_back')]
        #    action [ShowMenu('preferences')]

screen sch_settings_back:
            textbutton("/Назад/"):
                xpos 500
                ypos 500
                text_style "sch_keys_white"
                style "sch_keys_white"
                action [Show("sch_menu", transition=Dissolve(0.55)), Hide("sch_settings", transition=Dissolve(0.25)), Hide("sch_settings_back", transition=Dissolve(0.25))]

label sch_achievements:
    "Undone."
    call screen sch_menu
    return

screen sch_exit_promt:
    tag menu
    modal True
    key "game_menu":
        action NullAction()
    key "screenshot":
        action NullAction()
    add "#ffffff"
    if (u"Заслуженная Реальность" in save_name and persistent.prologue_done == 1):
        $ dr_quittext = 'Вы уверены, что хотите\nвернуться в свою реальность?'
    else:
        $ dr_quittext  = "Вы действительно\nхотите выйти из мода?"
    text dr_quittext:
        style "sch_keys"
        size 60
        text_align 0.5
        xalign 0.5
        yalign 0.33
        color "#800000"
        antialias True
        kerning 2
    textbutton "Да":
        text_size 80
        style "sch_keys"
        text_style "sch_keys"
        xalign 0.35
        yalign 0.55
        text_color "#000000"
        text_hover_color "#800000"
        action [Hide("sch_exit_promt", transition=dissolve), Return("sch_exit_final")]
    textbutton "Нет":
        text_size 80
        style "sch_keys"
        text_style "sch_keys"
        xalign 0.66
        yalign 0.55
        text_color "#000000"
        text_hover_color "#006400"
        action [Hide("sch_exit_promt", transition=Dissolve(0.5)), Show("sch_menu", transition=Dissolve(0.5))]
    #action [Hide("sch_menu"), Jump("original_mm")]



screen sch_placeholder_desc:
    textbutton("Данная опция позволяет включить заглушки,\nкоторые препятствуют переходу\nна незаконченный рут."):
        style 'sch_desc'
        text_style "sch_keys_white"
        text_size 44
        pos(250, 500)
        unhovered[Hide('sch_placeholder_desc', transition=Dissolve(0.1))]

screen sch_difficulty_desc:
    textbutton("Данная опция позволяет сменить сложность\nпри выборе по умолчанию.\nНормальная сложность - рекомендуется.\nHardmode - меньше ОП, сложнее выйти на рут."):
        style 'sch_desc'
        text_style "sch_keys_white"
        text_size 44
        pos(250, 480)
        unhovered[Hide('sch_difficulty_desc', transition=Dissolve(0.1))]

screen sch_widget_desc:
    textbutton("Данная опция позволяет включить виджет,\nкоторый показывает очки, получаемые во \nвремя прохождения мода."):
        style 'sch_desc'
        text_style "sch_keys_white"
        text_size 44
        pos(250, 500)
        unhovered[Hide('sch_widget_desc', transition=Dissolve(0.1))]

screen sch_es_settings_desc:
    textbutton("По нажатию этой кнопки\nВы можете перейти в настройки игры,\nЧтобы изменить различные настройки."):
        style 'sch_desc'
        text_style "sch_keys_white"
        text_size 44
        pos(250, 500)
        unhovered[Hide('sch_es_settings_desc', transition=Dissolve(0.1))]

screen sch_chapter_skip_desc:
    textbutton("Данная опция позволяет пропускать\nназвания глав и дней."):
        style 'sch_desc'
        text_style "sch_keys_white"
        text_size 44
        pos(250, 500)
        unhovered[Hide('sch_es_settings_desc', transition=Dissolve(0.1))]
