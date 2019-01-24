label sichium:
    $ sch_save_version = sch_version  # создаём имя сохранению при запуске новой игры

    $ init_map_zones_sch() # По заветам 7ДЛ инициализируем карту единожны, чтобы сохранкам не приходил армаггедец

    if not "Deserved Reality" in config.version: # закидываем себя в трейс на случай армаггедеца игре
        $ config.version = config.version + "Deserved Reality %s, %s %s codename %s" % (sch_state, sch_version, sch_hotfix, sch_codename)

    # Переименовываем игрушку во имя всех богов
    $ config.developer = True #TODO В релиз попасть не должно
    $ config.window_title = u"Заслуженная | Реальность"

    jump sichium_start


label sichium_start: # Меню

    $ sch_forgeteveryone()

    $ persistent.sprite_time = "night"
    $ prolog_time()
    $ name_sch()

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
        ease 1.0 zoom 1.0
        linear 0.75 xzoom 0.12
        easein 0.75 yzoom 3.62
        linear 0.75 xanchor 111
    pause(5.25)
    show white2:
        xpos 861
    show sch_begin behind white2:
        pos(861, 382)
        linear 0.75 xanchor 498
    show sch_continue behind white2:
        pos(861, 462)
        linear 0.75 xanchor 498
    show sch_settings behind white2:
        pos(861, 542)
        linear 0.75 xanchor 498
    show sch_achievements behind white2:
        pos(861, 622)
        linear 0.75 xanchor 498
    show exit_idle:
        pos (-72, 1008)
        linear 0.75 pos(0, 1008)
    pause(0.75)

    call screen sch_menu

label sch_settings_in: # Переход в настройки
    $ renpy.block_rollback()


    scene white
    show blacksquare:
        xalign 0.5 yalign 0.5
        xanchor 111 xzoom 0.12 yzoom 3.62
    show sch_begin:
        pos(363, 382)
    show sch_continue:
        pos(363, 462)
    show sch_settings_pressed:
        pos(363, 542)
    show sch_achievements:
        pos(363, 622)
    show exit_idle:
        pos(0, 1008)



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
            pos(903, 382)
    else:
        show sch_placeholder_off:
            pos(903, 382)

    if persistent.sch_widget:
        show sch_widget_on:
            pos(903, 442)
    else:
        show sch_widget_off:
            pos(903, 442)

    if persistent.sch_difficulty == True:
        show sch_difficulty_Hard:
            pos(903, 436)
    elif persistent.sch_difficulty == False:
        show sch_difficulty_normal:
            pos(903, 436)
    elif persistent.sch_difficulty == None:
        show sch_difficulty_undefined:
            pos(903, 436)

    show sch_es_settings:
        pos(903, 644)

    with Dissolve(0.25)

    show screen sch_settings_menu

    show screen sch_settings_back




label sch_settings_out:
    $ renpy.block_rollback()

    scene gray

    show whitesquare:
       xalign 0.5 yalign 0.5
       xanchor 111 xzoom 0.12 yzoom 3.62

    pause(0.25)

    scene white
    show blacksquare:
        xalign 0.5 yalign 0.5 xzoom 0.12 yzoom 3.62 xanchor 111

    show sch_begin:
        pos(363, 382)
    show sch_continue:
        pos(363, 462)
    show sch_settings:
        pos(363, 542)
    show sch_achievements:
        pos(363, 622)

    with Dissolve(0.25)
    pause(0.25)

    show exit_idle:
        pos (-72, 1008)
        linear 0.25 pos(0, 1008)

    pause(0.25)


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

    pause(0.75)


    show blacksquare:
        xalign 0.5 yalign 0.5 xanchor 111 xzoom 0.12 yzoom 3.62
        easein 0.75 yzoom 1.0
        linear 0.75 xzoom 1.0
        xalign 0.5 yalign 0.5
        easein 1.0 zoom 20.0


    pause(2.75)

    jump sch_game_start

    return

label sch_game_start:

    stop music fadeout 1

    #call sch_day0_cr

    #pause(1)

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
