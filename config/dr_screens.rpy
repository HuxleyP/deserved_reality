# виджет ЛП и музыки
screen dr_fuchsia_widget:
    modal False
    imagemap:
        ground "bg_null"
        if (not (persistent.dr_widget or save_name == ("Заслуженная Реальность. Меню.") or dr_hard)):
            add dr_path + "source/images/gui/arrow.png" anchor(0.5, 0.0) xalign 0.5 yalign 0.0
            alpha False
            hotspot (0, 0, 1920, 50) hovered [SetVariable("dr_WidgetVisible", True), Show("dr_widget_screen", transition = dspr)] action NullAction

screen dr_widget_screen:
    modal False
    imagebutton:
        idle dr_path + "source/images/gui/widget_case.png"
        hover dr_path + "source/images/gui/widget_case.png"
        anchor(0.5, 0.0)
        xalign 0.5
        yalign 0.0
        hovered NullAction
        unhovered [Hide("dr_widget_screen", transition=dspr), SetVariable("dr_WidgetVisible", False)]
        action [Hide("dr_widget_screen", transition=dspr), SetVariable("dr_WidgetVisible", False)]

    if dr_true:
        add gui_dr("icons/karma_widget.png") xalign 0.67 ypos 10

    add gui_dr("icons/will_widget.png") xalign 0.785 ypos 10

    add gui_dr("icons/pioneer_widget.png") xalign 0.897 ypos 10

    #$ list_dr_screenPos = [26, 242, 458, 674, 890] # 5 позиций
    #$ dr_known = len(list_dr_ch_known) # Надо для скрина
    #$ k = 0
    #for i in range(len(list_dr_ch_known)):
    #    if not ((list_dr_ch_known[i] == "mt") or list_dr_ch_known[i] == "cs"):
    #        add gui_dr("icons/[list_dr_ch_known[i]]_widget.png")
    #        text "[list_dr_screenPos[i]]":
    #            xalign list_dr_screenPos[k]
    #            ypos 20
    #            size 36
    #            color "000000"
    #            font font_dr("csn.ttf")
    #        $ k +=1
    #    else:
    #        pass

    add source_dr + "images/gui/icons/dv_widget.png" xpos 26 ypos 10

    add source_dr + "images/gui/icons/us_widget.png" xpos 242 ypos 10

    add source_dr + "images/gui/icons/un_widget.png" xpos 458 ypos 10

    add source_dr + "images/gui/icons/sl_widget.png" xpos 674 ypos 10

    add source_dr + "images/gui/icons/mi_widget.png" xpos 890 ypos 10

    text str(dr_dv):
        xpos 26
        ypos 20
        size 36
        color "#ff9600"
        font source_dr + "images/fonts/Roboto.ttf"

    text str(dr_us):
        xpos 242
        ypos 20
        size 36
        color "#ff0000"
        font source_dr + "images/fonts/Roboto.ttf"

    text str(dr_un):
        xpos 458
        ypos 20
        size 36
        color "#c045ff"
        font source_dr + "images/fonts/Roboto.ttf"

    text str(dr_sl):
        xpos 674
        ypos 20
        size 36
        color "#fff600"
        font source_dr + "images/fonts/Roboto.ttf"

    text str(dr_mi):
        xpos 890
        ypos 20
        size 36
        color "#00f6ff"
        font source_dr + "images/fonts/Roboto.ttf"

    showif persistent.dr_karma_shown == True:
        text str(dr_ka):
            xalign 0.67
            ypos 20
            size 36
            color "#000000"
            font source_dr + "images/fonts/Roboto.ttf"

    text str(dr_wi):
            xalign 0.785
            ypos 20
            size 36
            color "#000000"
            font source_dr + "images/fonts/Roboto.ttf"

    text str(dr_pi):
            xalign 0.897
            ypos 20
            size 36
            color "#000000"
            font source_dr + "images/fonts/Roboto.ttf"

screen dr_menu_pre:
    modal False

    key "game_menu":
        action NullAction()

    key "screenshot":
        action NullAction()

    key "K_F1":
        action NullAction()

    timer 0.1 action (Hide("dr_menu_pre", transition=dissolve), Show("dr_menu"))

# Ниже меню. Нихрена не откалибровано, было заменено по причине дизайна (крайне херового, но ты, копатель по файлам, можешь заменить вызов скринов и посмотреть на это чудо инженегровой мысли)
screen dr_menu:
    tag menu
    modal True

    key "game_menu":
        action NullAction()

    key "screenshot":
        action NullAction()

    key "K_F1":
        action NullAction()

    add "bg black"

    if dr_inmenu:
        add "dr_main_menu_atl_short"
    else:
        add "dr_main_menu_atl"

    add "dr_blacksquare" xalign 0.5 yalign 0.5 xzoom 0.12 yzoom 3.62 xanchor 111

    #add "dr_white2" zoom 0.7 xpos 861

    #text "{font=[source_dr]images/fonts/LemonTuesday.otf}{size=60}З{/font}{font=[source_dr]images/fonts/csn.ttf}аслуженная{/size}{/font}\n {size=50}{font=[source_dr]images/fonts/LemonTuesday.otf}Р{/font}{font=[source_dr]images/fonts/csn.ttf}{/size}{size=60}еальность{/size}{/font}":
    ##vbox:
    if not dr_inmenu:
        textbutton "{size=150}Заслуженная{/size}\n  {size=120}Реальность{/color}" at dr_menu_ease:
            yalign 0.5
            style "dr_keys"
            text_style "dr_keys"
            action OpenURL("https://vk.com/public167564386")
    else:
        textbutton "{size=150}Заслуженная{/size}\n  {size=120}Реальность{/color}":
            xpos 1131
            yalign 0.5
            style "dr_keys"
            text_style "dr_keys"
            action OpenURL("https://vk.com/public167564386")
        
    # потенциально сделать провекру на хардмод
    vbox:   #Открыть экран сейвов
        textbutton ("•Продолжить_Игру"): # может, только для бабочки?
            xpos 363
            ypos 357
            background None
            text_style "dr_keys"
            style "dr_keys"
            action [Hide("dr_menu", transition=Dissolve(0.5)), ShowMenu("load", transition=Dissolve(0.5))] # сделать загрузку свою
            #action [Hide("dr_menu"), Jump("dr_savescreen")]

        textbutton ("•Новая_Игра"):
            xpos 363
            ypos 377
            background None
            text_style "dr_keys"
            style "dr_keys"
            #action [Hide("dr_menu"), Jump("dr_newgame")]
            action [Hide("dr_menu"), Return("dr_newgame")]

        textbutton ("•Настройки"):
            xpos 363
            ypos 397
            background None
            text_style "dr_keys"
            style "dr_keys"
            action [Hide("dr_menu"), Show("dr_settings_menu", transition = Dissolve(0.5))]
        
        if persistent.cycled:
            textbutton ("•Достижения"):
                xpos 363
                ypos 417
                background None
                text_style "dr_keys_gray"
                style "dr_keys_gray"
                action [Hide("dr_menu"), Jump("dr_achievements_menu")]

        else:
            textbutton ("•Достижения"):
                xpos 363
                ypos 417
                background None
                text_style "dr_keys"
                style "dr_keys"
                action NullAction()

        textbutton ("•Создатели"):
            xpos 363
            ypos 437
            background None
            text_style "dr_keys"
            style "dr_keys"
            action [Hide("dr_menu"), Show("dr_titles_menu", transition = Dissolve(0.5))]
    
        textbutton("•/Дебаг/"):
            xpos 363
            ypos 457
            background None
            text_style "dr_keys"
            style "dr_keys"
            text_color "#006400"
            text_hover_color "#800000"
            hovered Show('prologue_dream')
            unhovered Hide('prologue_dream')
            action [Hide("dr_menu"), Return("dr_debug")]


    imagebutton: #Ливнуть
        auto dr_menu("ButtonExit_%s.png")
        xpos 0
        ypos 1008
        action [Hide("dr_menu", transition = dissolve), Show("dr_exit_promt", transition = dissolve)]
        # action [ShowMenu("dr_exit_promt", transition=Dissolve(0.5))] # на случай, если найду лейбл оригинального меню игры
        # action MainMenu() совсем запасной

screen dr_titles_menu:
    tag menu
    modal True



screen dr_settings_menu:
    tag menu
    modal True

    key "game_menu":
        action NullAction()

    key "screenshot":
        action NullAction()

    key "K_F1":
        action NullAction()

    add "#171717"

    add "dr_whitesquare" xalign 0.5 yalign 0.5 xzoom 0.12 yzoom 3.62 xanchor 111

    mousearea:
        area(0, 0, 1920, 1080)
        hovered [ShowTransient("dr_settings_back", transition = Dissolve(0.1))]
        unhovered [Hide("dr_settings_back")]

    vbox:
        showif persistent.undone_jumper:
            textbutton ("•Заглушки - ON"):
                xpos 880
                ypos 357
                background None
                text_style "dr_keys_white"
                style "dr_keys_white"
                unhovered[ShowTransient("dr_settings_back", transition = Dissolve(0.1)), Hide("dr_placeholder_desc")]
                hovered[ShowTransient("dr_placeholder_desc", transition = Dissolve(0.1)), Hide("dr_settings_back")]
                action [Hide("dr_menu"), SetField(persistent, "undone_jumper", False)]

        else:
            textbutton ("•Заглушки - OFF"):
                xpos 880
                ypos 357
                background None
                text_style "dr_keys_white"
                style "dr_keys_white"
                unhovered[ShowTransient("dr_settings_back", transition=Dissolve(0.1)), Hide("dr_placeholder_desc")]
                hovered[ShowTransient("dr_placeholder_desc", transition=Dissolve(0.1)), Hide("dr_settings_back")]
                action [Hide("dr_menu"), SetField(persistent, "undone_jumper", True)]

        showif persistent.dr_difficulty:
            textbutton ("•Сложность по умолчанию - Hard"):
                xpos 880
                ypos 377
                background None
                text_style "dr_keys_white"
                style "dr_keys_white"
                unhovered[ShowTransient("dr_settings_back", transition=Dissolve(0.1)), Hide("dr_difficulty_desc")]
                hovered[ShowTransient("dr_difficulty_desc", transition=Dissolve(0.1)), Hide("dr_settings_back")]
                action [Hide("dr_menu"), SetField(persistent, "dr_difficulty", False)]

        elif persistent.dr_difficulty == False:
            textbutton ("•Сложность по умолчанию - Обычная"):
                xpos 880
                ypos 377
                background None
                text_style "dr_keys_white"
                style "dr_keys_white"
                unhovered[ShowTransient("dr_settings_back", transition=Dissolve(0.1)), Hide("dr_difficulty_desc")]
                hovered[ShowTransient("dr_difficulty_desc", transition=Dissolve(0.1)), Hide("dr_settings_back")]
                action [Hide("dr_menu"), SetField(persistent, "dr_difficulty", None)]

        showif persistent.dr_difficulty == None:
            textbutton ("•Сложность по умолчанию - не установлено"):
                xpos 880
                ypos 377
                background None
                text_style "dr_keys_white"
                style "dr_keys_white"
                unhovered [ShowTransient("dr_settings_back", transition = Dissolve(0.1)), Hide("dr_difficulty_desc")]
                hovered [ShowTransient("dr_difficulty_desc", transition = Dissolve(0.1)), Hide("dr_settings_back")]
                action [Hide("dr_menu"), SetField(persistent, "dr_difficulty", True)]

        showif persistent.dr_widget:
            textbutton("•Виджет ОП - ON"):
                xpos 880
                ypos 397
                background None
                text_style "dr_keys_white"
                style "dr_keys_white"
                unhovered [ShowTransient("dr_settings_back", transition = Dissolve(0.1)), Hide("dr_widget_desc")]
                hovered [ShowTransient("dr_widget_desc", transition = Dissolve(0.1)), Hide("dr_settings_back")]
                action [Hide("dr_menu"), SetField(persistent, "dr_widget", False)]
        else:
            textbutton("•Виджет ОП - OFF"):
                xpos 880
                ypos 397
                background None
                text_style "dr_keys_white"
                style "dr_keys_white"
                unhovered [ShowTransient("dr_settings_back", transition = Dissolve(0.1)), Hide("dr_widget_desc")]
                hovered [ShowTransient("dr_widget_desc", transition = Dissolve(0.1)), Hide("dr_settings_back")]
                action [Hide("dr_menu"), SetField(persistent, "dr_widget", True)]


        showif persistent.dr_chapter_skip:
           textbutton("•Пропуск названий глав - ON"):
                xpos 880
                ypos 412
                background None
                text_style "dr_keys_white"
                style "dr_keys_white"
                unhovered [ShowTransient("dr_settings_back", transition = Dissolve(0.1)), Hide("dr_chskip_desc")]
                hovered [ShowTransient("dr_chskip_desc", transition = Dissolve(0.1)), Hide("dr_settings_back")]
                action [Hide("dr_menu"), SetField(persistent, "dr_chapter_skip", False)]
        else:
           textbutton("•Пропуск названий глав - OFF"):
                xpos 880
                ypos 412
                background None
                text_style "dr_keys_white"
                style "dr_keys_white"
                unhovered [ShowTransient("dr_settings_back", transition = Dissolve(0.1)), Hide("dr_chskip_desc")]
                hovered [ShowTransient("dr_chskip_desc", transition = Dissolve(0.1)), Hide("dr_settings_back")]
                action [Hide("dr_menu"), SetField(persistent, "dr_chapter_skip", True)]


        textbutton("•Перейти в настройки игры"):
            xpos 880
            ypos 432
            background None
            text_style "dr_keys_white"
            style "dr_keys_white"
            unhovered[ShowTransient("dr_settings_back", transition=Dissolve(0.1)), Hide("dr_es_settings_desc")]
            hovered[ShowTransient("dr_es_settings_desc"), Hide("dr_settings_back")]
            action [ShowMenu("preferences")]

screen dr_settings_back:
    textbutton("/Назад/"):
        xpos 500
        ypos 500
        text_style "dr_keys_white"
        style "dr_keys_white"
        action [Show("dr_menu", transition = Dissolve(0.55)), Hide("dr_settings", transition = Dissolve(0.25)), Hide("dr_settings_back", transition = Dissolve(0.25)), SetVariable("dr_inmenu", True)]

label dr_achievements_menu:
    "Undone."
    return

screen dr_exit_promt:
    tag menu
    modal True

    key "game_menu":
        action NullAction()

    key "screenshot":
        action NullAction()

    key "K_F1":
        action NullAction()

    add "#ffffff"

    if (u"Заслуженная Реальность" in save_name and persistent.prologue_done == 1):
        $ dr_quittext = "Вы уверены, что хотите\nвернуться в свою реальность?"

    else:
        $ dr_quittext  = "Вы действительно\nхотите выйти из мода?"

    text dr_quittext:
        style "dr_keys"
        size 60
        text_align 0.5
        xalign 0.5
        yalign 0.33
        color "#800000"
        antialias True
        kerning 2

    textbutton "Да":
        text_size 80
        style "dr_keys"
        text_style "dr_keys"
        xalign 0.35
        yalign 0.55
        text_color "#000000"
        text_hover_color "#800000"
        action [Hide("dr_exit_promt", transition=dissolve), Return("dr_exit_final")]

    textbutton "Нет":
        text_size 80
        style "dr_keys"
        text_style "dr_keys"
        xalign 0.66
        yalign 0.55
        text_color "#000000"
        text_hover_color "#006400"
        action [Hide("dr_exit_promt", transition=Dissolve(0.5)), Show("dr_menu", transition=Dissolve(0.5))]
    #action [Hide("dr_menu"), Jump("original_mm")]

screen dr_placeholder_desc:
    textbutton "Данная опция позволяет включить заглушки,\nкоторые препятствуют переходу\nна незаконченный рут.":
        style "dr_desc"
        text_style "dr_keys_white"
        text_size 44
        pos (250, 500)
        unhovered[Hide("dr_placeholder_desc", transition=Dissolve(0.1))]

screen dr_difficulty_desc:
    textbutton "Данная опция позволяет сменить сложность\nпри выборе по умолчанию.\nНормальная сложность - рекомендуется.\nHard - меньше ОП, сложнее выйти на рут.":
        style "dr_desc"
        text_style "dr_keys_white"
        text_size 44
        pos (250, 480)
        unhovered[Hide("dr_difficulty_desc", transition=Dissolve(0.1))]

screen dr_widget_desc:
    textbutton "Данная опция позволяет включить виджет,\nкоторый показывает очки, получаемые во \nвремя прохождения мода.":
        style "dr_desc"
        text_style "dr_keys_white"
        text_size 44
        pos (250, 500)
        unhovered[Hide("dr_widget_desc", transition=Dissolve(0.1))]

screen dr_es_settings_desc:
    textbutton "По нажатию этой кнопки\nВы можете перейти в настройки игры,\nЧтобы изменить различные настройки.":
        style "dr_desc"
        text_style "dr_keys_white"
        text_size 44
        pos (250, 500)
        unhovered[Hide("dr_es_settings_desc", transition=Dissolve(0.1))]

screen dr_chskip_desc:
    textbutton "Данная опция позволяет пропускать\nназвания глав и дней.":
        style "dr_desc"
        text_style "dr_keys_white"
        text_size 44
        pos (250, 500)
        unhovered [Hide("dr_chskip_desc", transition=Dissolve(0.1))]


screen intro_noir_screen:
    add "intro_noir_screen" xalign 0.0 yalign 0.0

screen intro_limb_screen:
    add "intro_limb_screen" xalign 0.0 yalign 0.0

screen prologue_dream:
    add "prologue_dream" xalign 0.0 yalign 0.0

screen dr_white2:
    add "dr_white2" xalign 0.0 yalign 0.0

screen dr_role_choose:
    tag menu
    modal False
    imagemap:
        ground "bg black"
        hotspot ((0, 0, 960, 1080)):
            hovered [Show("intro_noir_screen", transition=Dissolve(0.5))]
            unhovered [Hide("intro_noir_screen", transition=Dissolve(1.0))]
            action [Hide("intro_noir_screen", transition=Dissolve(0.5)), Jump("dr_day0_cr")]
        hotspot ((960, 0, 960, 1080)):
            hovered [Show("intro_limb_screen", transition=Dissolve(0.5))]
            unhovered [Hide("intro_limb_screen", transition=Dissolve(1.0))]
            action [Hide("intro_limb_screen", transition=Dissolve(0.5)), Jump("dr_day1_cr")]