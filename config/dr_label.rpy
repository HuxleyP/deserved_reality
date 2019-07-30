label dr_prestart:
    $ dr_save_version = dr_version  # создаём имя сохранению при запуске новой игры

    #$ init_map_zones_dr() # По заветам 7ДЛ инициализируем карту единожны, чтобы сохранкам не приходил армаггедец

    if not "Deserved Reality" in config.version: # закидываем себя в трейс на случай армаггедеца игре
        $ config.version = config.version + ": Deserved Reality \n%s ver %s; \"%s\"" % (dr_state, dr_version, dr_codename)

    # Переименовываем игрушку во имя всех богов, да так, чтобы потом оно тоже оставалось, бугага
    $ config.window_title = u"Заслуженная | Реальность"
    $ config.developer = True #TODO В релиз попасть не должно
    $ config.debug_text_overflow = True #это тоже
    $ config.conditionswitch_predict_all = True # и это

    # а это важно
    $ config.after_load_callbacks.append(name_dr)

    jump sichium_start

# ------------------------------------------------------
# Переменные

label dr_commonvars:
    # получаемые в прологе
    #------------------------------
    # получаемые в первом
    $ list_dr_noir_flag = [] # флаги Нуара, показывают успех рута
    $ dr_noir_flag = 0 # флаги Нуара численно, показывают выход на рут
    $ list_dr_ch_known = [] # Знакомые персонажи
    $ dr_sl_keys = False
    #---------------------------------------------
    # получаемые во втором
    $ dr_sabotage = 0 # 0 -не знает, 1, 2... - этапы, -1 - отказ в начале -2 - отказ при подтверждении, -3 - отказ в середине, -4 - отказ в конце, -6 - переманил Алису на мирную сторону,


# Пролог

label dr_day0_vars:
    $ deathflag = False # Смерть, невыход в игру
    $ dr_day0_keychain = False # Брелок
    $ true_prologue = False

    return

# День 1

label dr_day1_vars:

    $ dr_day1_sl_together = False # С кем пошёл к ОД TODO сделать не списком, а string
    $ dr_day1_ev_mi = False # позвала ли Мику на пристань
    $ dr_ginger_lie = 0
    $ dr_known_list = []
    $ dr_tmp_d1_sl_insta_warehouse = False
    $ dr_tmp_d1_sl_after = False
    $ dr_day1_salty_supper = False
    $ dr_day1_mi_musclub_promise = False
    $ dr_day1_mi_musclub_leave = False

    return

# День 2

label dr_day2_vars:

    $ list_dr_day2_walk = []
    #блокировка
    $ dr_day2_od_photo = False
    $ dr_day2_od_failed = False
    $ dr_day2_forest = False
    $ dr_day2_sl_keys_given = True
    $ dr_day2_dv_rightanswers = 0

    return
# День 3

label dr_day3_vars:

    $ list_rootflag_dr = [] #Список рутфлагов, чтобы не писать по 7 переменных

    return

label dr_allvars:
    call dr_forgotten_lists_init
    call dr_commonvars # общие
    call dr_day0_vars # онли пролог
    call dr_day1_vars # онли первый день
    call dr_day2_vars # онли второй день
    call dr_day3_vars # онли третий день

    return

label sichium_start: # Меню
    # анимации

    $ dr_forgeteveryone()

    $ persistent.sprite_time = "night"
    $ prolog_time()
    $ name_dr("Я")
    #$ volume('sound', 0.5)

    scene bg black
    $ renpy.movie_cutscene(preroll)

    play sound dr_sfx["whiteflash"]

    $ save_name = "Заслуженная Реальность. Меню."
    
    scene dr_white

    show dr_blacksquare:
        xalign 0.5 yalign 0.5
        zoom 20.0
        pause 0.5
        ease 0.5 zoom 1.0
        ease 0.35 xzoom 0.12
        easein 0.35 yzoom 3.62
        ease 0.35 xanchor 111

    pause(2.05) # дефакто 2.3

    show dr_white2:
        xpos 861

    play music dr_music["honor"] fadein 1

    play sound dr_sfx["whiteflash"]

    show dr_begin behind dr_white2:
        pos(861, 357)
        ease 0.25 xanchor 498

    #pause(0.25)

    show dr_continue behind dr_white2:
        pos(861, 431)
        ease 0.25 xanchor 498

    #pause(0.25)

    show dr_settings behind dr_white2:
        pos(861, 505)
        ease 0.25 xanchor 498
        
    #pause(0.25)

    show dr_achievements behind dr_white2:
        pos(861, 579)
        ease 0.25 xanchor 498

    #pause(0.25)
    
    show dr_titles_text behind dr_white2:
        pos(861, 653)
        ease 0.25 xanchor 498


    #pause(0.25)


    pause(0.25)

    show dr_exit_idle:
        pos (-72, 1008)
        linear 0.25 pos(0, 1008)

    pause(0.25)
    # де факто 2.05+0.05+1.25=3.35
    ##$ volume('sound', 1.0)
    call screen dr_menu_pre

    jump dr_menu_callout

label dr_menu_callout:
    $ renpy.block_rollback()
    $ dr_result = _return
    #hide screen dr_settings_back
    #hide screen dr_menu
    if dr_result == "dr_newgame":
        pass
    elif dr_result == "dr_debug":
        jump dr_debug_sandbox
    else:
        stop music fadeout 2.5
        scene bg black with Dissolve(2.5)
        return
    

    scene dr_white


    show dr_begin:
        pos(363, 357)

    show dr_continue:
        pos(363, 431)

    show dr_settings:
        pos(363, 505)

    show dr_achievements:
        pos(363, 579)

    show dr_titles_text:
        pos(353, 653)

    show dr_exit_idle:
        pos(0, 1008)

    show dr_blacksquare:
        xalign 0.5 yalign 0.5
        xanchor 111 xzoom 0.12 yzoom 3.62

    show dr_logo:
        xpos 1131
        yalign 0.5
        easeout 0.5 xpos 2131 yalign 0.5


    with Dissolve(0.5)

    show dr_white2 behind dr_blacksquare:
        xpos 861
    show dr_begin behind dr_white2:
        pos(363, 357)
        linear 0.75 xanchor -498

    show dr_continue behind dr_white2:
        pos(363, 431)
        linear 0.75 xanchor -498

    show dr_settings behind dr_white2:
        pos(363, 505)
        linear 0.75 xanchor -498

    show dr_achievements behind dr_white2:
        pos(363, 579)
        linear 0.75 xanchor -498
    
    show dr_titles_text behind dr_white2:
        pos(363, 653)
        linear 0.75 xanchor -498

    show dr_exit_idle:
        pos(0, 1008)
        linear 0.75 xpos -72

    pause(1.5)

    show dr_blacksquare:
        pause .1
        xalign 0.5 yalign 0.5
        xanchor 111 xzoom 0.12 yzoom 3.62 
        # дефолт состояние
        ease 0.25 xanchor 0
        ease 0.1 xalign 0.5 yalign 0.5
        easein 0.5 yzoom 1.0
        linear 0.5 xzoom 1.0
        pause .5
        easein 1.0 zoom 20.0

    $ renpy.pause(5, hard=True)

    jump dr_game_start

    return

label dr_final_exit:
    stop music fadeout 3.5
    scene bg black with Dissolve(3.5)
    $ MainMenu()

label dr_game_start:

    $ renpy.block_rollback()
    scene black
    #call screen dr_role_choose

    stop music fadeout 1

    call dr_day0_cr

    pause(1)

    call dr_day1_cr

    pause(1)

    call dr_day2_cr

    pause(1)

    call dr_tbc

    pause(1)

    return

# Распределитель, пока бесполезен

label dr_router:
    scene anim prolog2 with fade
    stop music fadeout 1
    stop ambience fadeout 1
    jump dr_dv_router

label dr_dv_router:
    if dr_dv >= 11 and dr_sabotage == 6:
        "Вот это выдался день - спасибо Алисе. Надеюсь, завтра будет ещё лучше."
        call dr_dv_vars
        $ routetag_dr = "dv_sab"
        return
    elif dr_dv >= 11 and dr_sabotage == -6:
        "Слишком много на меня за день, и всё из-за Алисы. Надеюсь, завтра будет лучше."
        call dr_dv_vars
        $ routetag_dr = "dv_peace"
        return
    elif dr_dv >= 11 and dr_sabotage < 6 and dr_sabotage > -6:
        call dr_dv_vars
        $ routetag_dr = "dv"
        jump dr_day4_dv_cr
        "Слишком много на Алису за этот день. Надеюсь, завтра будет лучше."
        return
    else:
        jump dr_sl_router

label dr_sl_router:
    if dr_sl >=11:
        "Мне снилась одна златовласка, которая сделала моё появление в лагере самым мягким и приятным."
        $ routetag_dr = "sl"
        call dr_sl_vars
        return
    else:
        jump dr_mi_router

label dr_mi_router:
    if dr_mi >=11:
        "Мне снился концертный зал и поющая голограмма, невидимая для меня в свету прожекторов."
        $ routetag_dr = "mi"
        call dr_mi_vars
        return
    else:
        jump dr_un_router

label dr_un_router:
    if dr_un >=11:
        "Мне снилось, как какая-то художница что-то рисовала на холсте фиолетовыми красками. Это был... я?"
        $ routetag_dr = "un"
        call dr_un_vars
        return
    else:
        jump dr_us_router

label dr_us_router:
    if dr_us >=8 and dr_sabotage == 5:
        "Я почти час не мог уснуть из-за зашкаливающего уровня адреналина в крови, а после лишь видел яркие красные искры."
        $ routetag_dr = "us"
        call dr_us_vars
        return
    else:
        jump dr_loner_router

label dr_loner_router:
    if noir_flag == 3:
        $ routetag_dr = "nr"
        call dr_nr_vars
        return
    else:
        $ routetag_Sch = "ln"
        call dr_ln_vars
        return

label dr_final_router:
    if routetag_dr == "dv_sab":
        jump dr_day4_dv_sabotage_cr

    elif routetag_dr == "dv_peace":
        jump dr_day4_dv_negotiator_cr

    elif routetag_dr == "dv":
        jump dr_day_dv_cr

    elif routetag_dr == "sl":
        jump dr_day4_sl_cr

    elif routetag_dr == "mi":
        jump dr_day4_mi_cr

    elif routetag_dr == "un":
        jump dr_day4_un_cr

    elif routetag_dr == "us":
        jump dr_day4_us_cr

    elif routetag_dr == "nr":
        jump dr_day4_nr_cr
        
    elif routetag_dr == "ln":
        jump dr_day4_ln_cr
        
    else:
        jump dr_router
