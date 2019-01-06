label sch_day0_cr:

    call sch_vars_day0

    $ prolog_time()
    $ persistent.sprite_time = "night"

    scene bg white with dissolve
    stop music fadeout 1
    stop ambience fadeout 1
    stop sound fadeout 1


    if sch_true:
        $ sch_chapter(0, u"Последний путь.", new_day=True)

    elif sch_bound:
        $ sch_chapter(0, u"Правильный выбор.", new_day=True)

    else:
        $ sch_chapter(0, u"Сквозь время и пространство.", new_day=True)

    call sch_prologue_chose
    pause(1)


    if not true_prologue:
        call sch_day0_prehistory
        pause(1)

    if (persistent.mi_good_sch) or (persistent.dv_good_sch) or (persistent.sl_good_sch) or (persistent.us_good_sch) or (persistent.un_good_sch) or (persistent.iv_good_sch) or (persistent.ln_good_sch):
        call sch_day0_keys
        pause(1)


    if prophet:
        call sch_prologue_true
        pause(1)
        call sch_prologue_true_end

    else:
        call sch_prologue_normal
        pause(1)
        call sch_prologue_normal_end


    if deathflag:
        call sch_prologue_death
        pause(1)

        return

    return
