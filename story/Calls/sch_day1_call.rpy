label sch_day1_cr:

    $ day_time()
    $ persistent.sprite_time = 'day'
    $ name_sch('Я')
    $ sch_forgeteveryone()

    # Старт!

    call sch_day1_sl

    if sch_waited == 5:
        return

    pause(1)

    if not ('sl' in list_sch_day1_together):
        call sch_day1_un


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
