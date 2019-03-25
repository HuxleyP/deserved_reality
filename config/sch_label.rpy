label sichium:
    $ sch_save_version = sch_version  # создаём имя сохранению при запуске новой игры

    $ init_map_zones_sch() # По заветам 7ДЛ инициализируем карту единожны, чтобы сохранкам не приходил армаггедец

    if not "Deserved Reality" in config.version: # закидываем себя в трейс на случай армаггедеца игре
        $ config.version = config.version + " + Deserved Reality \n%s ver %s; \"%s\"" % (sch_state, sch_version, sch_codename)

    # Переименовываем игрушку во имя всех богов
    $ config.developer = True #TODO В релиз попасть не должно
    $ config.debug_text_overflow = True #это тоже
    $ config.conditionswitch_predict_all = True # и это
    $ config.after_load_callbacks = True
    $ config.window_title = u"Заслуженная | Реальность"

    jump sichium_start

# ------------------------------------------------------
# Переменные


label sch_commonvars:
    # получаемые в прологе
    $ sch_violent = False # злой
    $ sch_escapist = False # добрый
    # получаемые в первом
    $ list_sch_noir_flag = [] # флаги Нуара, показывают успех рута
    $ sch_noir_flag = 0 # флаги Нуара численно, показывают выход на рут
    $ list_sch_ch_known = [] # Знакомые персонажи
    $ sch_sl_keys = False
    # получаемые во втором
    $ sch_sabotage = 0 # 0 -не знает, 1, 2... - этапы, -1 - отказ в начале -2 - отказ при подтверждении, -3 - отказ в середине, -4 - отказ в конце, -6 - переманил Алису на мирную сторону,


# Пролог

label sch_day0_vars:
    $ deathflag = False # Смерть, невыход в игру
    $ true_prologue = False

    return

# День 1

label sch_day1_vars:

    $ list_sch_day1_together = [] # С кем пошёл к ОД TODO сделать не списком, а string
    $ sch_day1_help = '' # помогал в послевожатье
    $ list_sch_day1_supper = 'us' # с кем сел, по дефолту Уля
    $ sch_day1_el_fingal = False # остановлена ли Алиса около столовой
    $ sch_day1_clothes = False # получил ли форму
    $ sch_day1_helper = True # вызвался ли помочь, false - заставили
    $ sch_day1_hungry = False # налажал ли
    $ sch_day1_ev_mi = False # позвала ли Мику на пристань
    $ sch_ginger_lie = 0


    return

# День 2

label sch_day2_vars:

    $ list_sch_day2_walk = []
    #блокировка
    $ sch_day2_od_photo = False
    $ sch_day2_od_failed = False
    $ sch_day2_forest = False
    $ sch_day2_sl_keys_given = True
    $ sch_day2_dv_rightanswers = 0

    return
# День 3

label sch_day3_vars:

    $ list_rootflag_sch = [] #Список рутфлагов, чтобы не писать по 7 переменных

    return

label sch_allvars:
    call sch_commonvars # общие
    call sch_day0_vars # онли пролог
    call sch_day1_vars # онли первый день
    call sch_day2_vars # онли второй день
    call sch_day3_vars # онли третий день
    return



label sichium_start: # Меню
    # анимации

    $ sch_forgeteveryone()

    $ persistent.sprite_time = "night"
    $ prolog_time()
    $ name_sch("Я")

    scene white
    $ renpy.movie_cutscene(preroll)

    play sound whiteflash
    play music honor fadein 1

    $ save_name = "Заслуженная Реальность. Меню."

    scene bg white
    show blacksquare:
        xalign 0.5 yalign 0.5
        zoom 20.0
        pause 2.0
        ease 0.75 zoom 1.0
        linear 0.5 xzoom 0.12
        easein 0.5 yzoom 3.62
        linear 0.5 xanchor 111
    pause(2)
    pause(2.35)
    show white2:
        xpos 861
    show sch_begin behind white2:
        pos(861, 382)
        linear 0.5 xanchor 498
    show sch_continue behind white2:
        pos(861, 462)
        linear 0.5 xanchor 498
    show sch_settings behind white2:
        pos(861, 542)
        linear 0.5 xanchor 498
    show sch_achievements behind white2:
        pos(861, 622)
        linear 0.5 xanchor 498
    show exit_idle:
        pos (-72, 1008)
        linear 0.5 pos(0, 1008)
    play sound whiteflash
    pause(0.5)

    call screen sch_menu


label sch_newgame:
    $ renpy.block_rollback()
    hide screen sch_settings_back
    hide screen sch_menu
    scene white
    show blacksquare:
        xalign 0.5 yalign 0.5
        xanchor 111 xzoom 0.12 yzoom 3.62
    show white2 behind blacksquare:
        xpos 861
    show sch_begin behind white2:
        pos(363, 382)
        linear 0.75 xanchor -498
    show sch_continue behind white2:
        pos(363, 462)
        linear 0.75 xanchor -498
    show sch_achievements behind white2:
        pos(363, 622)
        linear 0.75 xanchor -498
    show sch_settings behind white2:
        pos(363, 542)
        linear 0.75 xanchor -498
    show exit_idle:
        pos(0, 1008)
        linear 0.75 xpos -72

    pause(1.5)

    show blacksquare:
        pause .1
        xalign 0.5 yalign 0.5 xzoom 0.12 yzoom 3.62
        easein 0.75 yzoom 1.0
        linear 0.75 xzoom 1.0
        xalign 0.5 yalign 0.5
        pause .5
        easein 1.0 zoom 20.0

    with flash



    $ renpy.pause(5, hard=True)

    jump sch_game_start

    return

label sch_game_start:

    stop music fadeout 1

    call sch_day0_cr

    pause(1)

    call sch_day1_cr

    pause(1)

    call sch_day2_cr

    pause(1)

    call sch_tbc

    pause(1)

    return

# Распределитель, пока бесполезен

label sch_router:
    scene anim prolog2 with fade
    stop music fadeout 1
    stop ambience fadeout 1
    jump sch_dv_router

label sch_dv_router:
    if pt_dv >= 11 and sch_sabotage == 6:
        "Вот это выдался день - спасибо Алисе. Надеюсь, завтра будет ещё лучше."
        call sch_dv_vars
        $ routetag_sch = "dv_sab"
        return
    elif pt_dv >= 11 and sch_sabotage == -6:
        "Слишком много на меня за день, и всё из-за Алисы. Надеюсь, завтра будет лучше."
        call sch_dv_vars
        $ routetag_sch = "dv_peace"
        return
    elif pt_dv >= 11 and sch_sabotage < 6 and sch_sabotage > -6:
        call sch_dv_vars
        $ routetag_sch = "dv"
        jump sch_day4_dv_cr
        "Слишком много на Алису за этот день. Надеюсь, завтра будет лучше."
        return
    else:
        jump sch_sl_router

label sch_sl_router:
    if pt_sl >=11:
        "Мне снилась одна златовласка, которая сделала моё появление в лагере самым мягким и приятным."
        $ routetag_sch = "sl"
        call sch_sl_vars
        return
    else:
        jump sch_mi_router

label sch_mi_router:
    if pt_mi >=11:
        "Мне снился концертный зал и поющая голограмма, невидимая для меня в свету прожекторов."
        $ routetag_sch = "mi"
        call sch_mi_vars
        return
    else:
        jump sch_un_router

label sch_un_router:
    if pt_un >=11:
        "Мне снилось, как какая-то художница что-то рисовала на холсте фиолетовыми красками. Это был... я?"
        $ routetag_sch = "un"
        call sch_un_vars
        return
    else:
        jump sch_us_router

label sch_us_router:
    if pt_us >=8 and sch_sabotage == 5:
        "Я почти час не мог уснуть из-за зашкаливающего уровня адреналина в крови, а после лишь видел яркие красные искры."
        $ routetag_sch = "us"
        call sch_us_vars
        return
    else:
        jump sch_loner_router

label sch_loner_router:
    if noir_flag == 3:
        $ routetag_sch = "nr"
        call sch_nr_vars
        return
    else:
        $ routetag_Sch = "ln"
        call sch_ln_vars
        return









label sch_final_router:
    if routetag_sch == "dv_sab":
        jump sch_day4_dv_sabotage_cr
    elif routetag_sch == "dv_peace":
        jump sch_day4_dv_negotiator_cr
    elif routetag_sch == "dv":
        jump sch_day_dv_cr
    elif routetag_sch == "sl":
        jump sch_day4_sl_cr
    elif routetag_sch == "mi":
        jump sch_day4_mi_cr
    elif routetag_sch == "un":
        jump sch_day4_un_cr
    elif routetag_sch == "us":
        jump sch_day4_us_cr
    elif routetag_sch == "nr":
        jump sch_day4_nr_cr
    elif routetag_sch == "ln":
        jump sch_day4_ln_cr
    else:
        jump sch_router
