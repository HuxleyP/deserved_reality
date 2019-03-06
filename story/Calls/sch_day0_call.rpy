label sch_day0_cr:
    $ sch_savename_init()
    call sch_day0_prehistory_part_1

    pause(1)

    if true_prologue:
        call sch_day0_prehistory_true

    pause(1)

    if deathflag:
        if persistent.sch_died:
            $ persistent.sch_died +=1
        else:
            $ persistent.sch_died = 1
        call sch_day0_cr

    jump sch_day1_cr
