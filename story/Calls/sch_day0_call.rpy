label sch_day0_cr:
    call sch_day0_prehistory_part_1

    pause(1)

    if true_prologue:
        call sch_day0_prehistory_true

    else:
        pass

    pause(1)

    if deathflag:
        return

    jump sch_day1_cr
