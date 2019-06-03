label dr_day2_call:
    $ sunset_time()
    $ persistent.sprite_time = 'sunset'
    call dr_day2_morning
    pause(1)

    $ day_time()
    $ persistent.sprite_time = 'day'
    call dr_day2_breakfast
    pause(1)

    $ day_time()
    $ persistent.sprite_time = 'day'
    call dr_day2_round_map
    pause(1)

    $ day_time()
    $ persistent.sprite_time = 'day'
    call dr_day2_dinner
    pause(1)

    $ day_time()
    $ persistent.sprite_time = 'day'
    call dr_day2_NR_events
    pause(1)

    $ sunset_time()
    $ persistent.sprite_time = 'sunset'
    call dr_day2_supper
    pause(1)

    $ sunset_time()
    $ persistent.sprite_time = 'sunset'
    call dr_day2_evening
    pause(1)

    jump dr_day3_cr