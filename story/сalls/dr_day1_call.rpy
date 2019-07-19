label dr_day1_cr:

    $ day_time()
    $ persistent.sprite_time = 'day'
    $ name_dr(u'Ваня')
    $ dr_forgeteveryone()

    # Старт!

    call dr_day1_intro

    pause(1)

    # Встреча с лагерем

    $ day_time()
    $ persistent.sprite_time = 'day'
    call dr_day1_meeting # Встречи
    pause(1)

    $ day_time()
    $ persistent.sprite_time = 'day'
    call dr_day1_od # Вожатая
    pause(1)

    $ day_time()
    $ persistent.sprite_time = 'day'
    call dr_day1_afterod # Склад
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