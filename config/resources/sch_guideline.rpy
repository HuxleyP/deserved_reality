label sichium_start: # Меню

    $ sch_forgeteveryone()
    
    if sch_launch == 0:
        call sch_defaultsettings
        $ persistent.sch_launched = True

    $ persistent.sprite_time = "night"
    $ prolog_time()
    $ name_sch()

    scene white
    $ renpy.movie_cutscene(preroll)

    play sound whiteflash
    play music honor fadein 1

    jump sch_menu_anim_intro

label sch_game_start:

    stop music fadeout 1

    call sch_day0_vars

    call sch_day0_cr

    if deathflag:
        return

    pause(1)

    if persistent.sch_widget:
        $ CycleCounter() # Виджет ЛП

    call sch_day1_cr

    pause(1)

    call sch_day2_cr

    return
