label dr_day1_cr:

    $ day_time()
    $ persistent.sprite_time = 'day'
    $ name_sch(u'Ваня')
    $ dr_forgeteveryone()

    # Старт!

    call dr_day1_intro

    pause(1)

    # Встреча с лагерем

    $ day_time()
    $ persistent.sprite_time = 'day'
    call dr_day1_meeting
    pause(1)

    $ day_time()
    $ persistent.sprite_time = 'day'
    call dr_day1_od
    pause(1)

    $ day_time()
    $ persistent.sprite_time = 'day'
    call dr_day1_afterod
    pause(1)

    $ sunset_time()
    $ persistent.sprite_time = 'sunset'
    call dr_day1_supper
    pause(1)

    $ sunset_time()
    $ persistent.sprite_time = 'sunset'
    call dr_day1_evening_map
    pause(1)

    jump dr_day2_cr