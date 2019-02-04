label sch_day2_cr:

    $ sunset_time()
    $ persistent.sprite_time = 'sunset'

    call sch_day2_start

    pause(1)

    if not 'forest_un' in list_sch_noir_flag:
        call sch_day2_sq_morning

        pause(1)

    call sch_day2_breakfast
