label sch_day1_aftersupper:
    $ set_zone_sch('square_sch', 'sch_day1_square_map_2')
    if 'mi' in list_sch_day1_supper:
        $ set_chibi_sch('boat_station_sch', 'mi')
    if 'un' in list_sch_day1_supper:
        $ set_chibi_sch('square_sch', 'un')

    $ persistent.sprite_time = "sunset"
    $ sunset_time()
