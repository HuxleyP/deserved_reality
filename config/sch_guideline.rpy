label sichium: # Меню

    $ sch_forgeteveryone()

    if sch_launch == 0:
        call sch_defaultsettings
        $ persistent.sch_launched = True

    $ persistent.sprite_time = "night"
    $ prolog_time()
    $ name_sch()

    if not sch_ingame:
        scene bg white
        $ renpy.movie_cutscene(preroll)
        scene bg white with fade

    play sound whiteflash
    play music honor fadein 1

    $ renpy.movie_cutscene(sch_menu_cs)
    call screen sch_menu

    stop music fadeout 1

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
