label dr_day1_cr:

    $ day_time()
    $ persistent.sprite_time = 'day'
    $ name_sch(u'Я')
    $ sch_forgeteveryone()

    # Старт!

    call dr_day1_intro

    pause(1)

    # Встреча с лагерем

    call sch_day1_camp

    pause(1)

    # Вожатая

    call sch_day1_od

    pause(1)

    call sch_day1_helper

    pause(1)

    # Ужин!
    $ sunset_time()
    $ persistent.sprite_time = 'sunset'

    call sch_day1_pre_supper

    call sch_day1_supper

    # Вечерние события

    call sch_day1_aftersupper # Ветка Алисы и Слави

    if sch_day1_ev_mi:
        call sch_day1_mi_boat # Ветка Мику

    # Домик

    call sch_day1_home # Уже в домике



    jump sch_day2_cr
