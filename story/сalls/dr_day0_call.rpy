label dr_day0_cr:
    $ prolog_time()
    $ persistent.sprite_time = "night"
    $ name_dr(u"Я")
    call dr_day0_prehistory_part_1

    pause(1)

    if deathflag:
        jump dr_day0_cr

    if true_prologue:
        call dr_day0_prehistory_part_2
    else:
        pass

    return