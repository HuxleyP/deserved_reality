label sch_day1_cr:

    $ day_time()
    $ persistent.sprite_time = 'day'

    # Старт!

    call sch_day1_sl

    pause(1)

    if pt_ka == -10:
        call sch_day1_un

    if not 'sl' in list_sch_day1_together or not 'un' in list_sch_day1_together or not 'un' in list_sch_ch_known:
        call sch_day1_mi

    if ('un' in list_sch_ch_known and not 'un' in list_sch_day1_together) or not 'mi' in list_sch_day1_together:
        call sch_day1_dv


    # Вожатая

    call sch_day1_od

    if 'sl' in list_sch_day1_help:
        call sch_day1_sq_sl

    if 'un' in list_sch_day1_help:
        call sch_day1_med_un

    # Ужин!


    $ sunset_time()
    $ persistent.sprite_time = 'sunset'

    call sch_day1_supper

    # Вечерние события

    call sch_day1_aftersupper # Ветка Алисы и Слави

    if 'mi' in list_sch_day1_help:
        call sch_day1_mi_boat # Ветка Мику

    # Домик

    call sch_day1_home # Уже в домике

    jump sch_day2_cr
