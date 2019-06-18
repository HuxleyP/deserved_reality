label dr_day3_cr:
    $ day_time()
    $ persistent.sprite_time = 'day'
    call dr_day3_morning
    pause(1)

    $ day_time()
    $ persistent.sprite_time = 'day'
    call dr_day3_breakfast
    pause(1)

    $ day_time()
    $ persistent.sprite_time = 'day'
    call dr_day3_clubs # Посещение клубов или заманчивое предложение Шурика
    pause(1)

    if not dr_day3_sh_combs_accepted:
    
        $ day_time()
        $ persistent.sprite_time = 'day'
        call dr_day3_scene_prep # Подготовка к минорному концерту
        pause(1)

        $ day_time()
        $ persistent.sprite_time = 'day'
        call dr_day3_dinner
        pause(1)

        $ day_time()
        $ persistent.sprite_time = 'day'
        call dr_day3_clutter # Ворох, шорох и массовая занятость всего первого отряда. События отличаются по рутам
        pause(1)

        $ sunset_time()
        $ persistent.sprite_time = 'sunset'
        call dr_day3_supper
        pause(1)

    else:

        $ day_time()
        $ persistent.sprite_time = 'day'
        call dr_day3_sh_combs
        pause(1)

        $ sunset_time()
        $ persistent.sprite_time = 'sunset'
        call dr_day3_sh_supper
        pause(1)



    $ sunset_time()
    $ persistent.sprite_time = 'sunset'
    call dr_day3_disco_clutter # Перетащить аппаратуру со сцены на площадь, повесить огоньки, подкрасить траву
    pause(1)

    if (dr_sabotage == 5) or (dr_sabotage == -6):
        $ night_time()
        $ persistent.sprite_time = 'night'
        call dr_day3_sabotage


    $ night_time()
    $ persistent.sprite_time = 'night'
    call dr_day3_disco_1 # Танцульки или сычевание/разгребание последствий
    pause(1)

    $ day_time()
    $ persistent.sprite_time = 'night'
    call dr_day3_rainchaos # Дождь, ад и сОтона
    pause(1)

    jump dr_day3_router