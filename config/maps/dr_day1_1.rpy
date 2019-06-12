label sch_day1_map_preparation:
    if 'mi' or 'dv' in list_sch_day1_together:
        $ sch_day1_mp = 1
    else:
        $ sch_day1_mp = 0
    $ disable_all_zones_sch()
    $ disable_all_chibi_sch()
    $ set_zone_sch('square_sch', 'sch_day1_square_map')
    $ set_zone_sch('music_club_sch', 'sch_day1_music_club_map')
    if sch_day1_mi_inclub:
        $ set_chibi_sch('music_club_sch', 'mi')
    $ set_zone_sch('boat_station_sch', 'sch_day1_boat_station_map')
    $ set_zone_sch('estrade_sch', 'sch_day1_estrade_map')
    $ set_zone_sch('library_sch', 'sch_day1_library_map')
    $ set_zone_sch('clubs_sch', 'sch_day1_clubs_map')
    $ set_zone_sch('beach_sch', 'sch_day1_beach_map')


    $ persistent.sprite_time = "day"
    $ day_time()

label sch_day1_map_1:

    if sch_day1_mp == 1:
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ set_zone_sch('dining_hall_sch', 'sch_day1_dining_hall_map')

    else:
        $ persistent.sprite_time = "day"
        $ day_time()

    play music music_list["my_daily_life"]

    if sch_day1_mp <2:
        $ show_map_sch()

    else:
        return

        

label sch_day1_square_map:
    # площадь

    if not ('sq' in list_sch_day1_map_1_visited):
        call sch_day1_event_square
        $ list_sch_day1_map_1_visited.append['sq']
        $ sch_day1_mp +=1

        pause(1)

    else:
        call sch_day1_event_square_visited
        pause(1)

        $ disable_current_zone_sch()

    jump sch_day1_map_1

label sch_day1_music_club_map:
    # музклуб

    if not ('mc' in list_sch_day1_map_1_visited) or sch_day1_mi_inclub:
        call sch_day1_event_music_club
        $ sch_day1_mp +=1

        $ list_sch_day1_map_1_visited.append['mc']
        pause(1)

    else:
        call sch_day1_event_music_club_visited
        pause(1)

        $ disable_current_zone_sch()

    jump sch_day1_map_1

label sch_day1_boat_station_map:
    # причал

    if not ('bs' in list_sch_day1_map_1_visited):
        call sch_day1_event_boat_station
        $ list_sch_day1_map_1_visited.append['bs']
        $ sch_day1_mp +=1

        pause(1)

    else:
        call sch_day1_event_boat_station_visited
        pause(1)

        $ disable_current_zone_sch()

    jump sch_day1_map_1

label sch_day1_estrade_map:
    # сцена

    if not ('es' in list_sch_day1_map_1_visited):
        call sch_day1_event_estrade
        $ list_sch_day1_map_1_visited.append['es']
        $ sch_day1_mp +=1

        pause(1)

    else:
        call sch_day1_event_estrade_visited

        pause(1)

        $ disable_current_zone_sch()
    jump sch_day1_map_1

label sch_day1_library_map:
    # библиотека
    if not ('lib' in list_sch_day1_map_1_visited):
        call sch_day1_event_library
        $ list_sch_day1_map_1_visited.append['lib']
        $ sch_day1_mp +=1

        pause(1)

    else:
        call sch_day1_event_library_visited

        pause(1)

        $ disable_current_zone_sch()
    jump sch_day1_map_1

label sch_day1_clubs_map:
    if not ('cl' in list_sch_day1_map_1_visited):
        call sch_day1_event_clubs
        $ list_sch_day1_map_1_visited.append['cl']
        $ sch_day1_mp +=1

        pause(1)

    else:
        call sch_day1_event_clubs_visited
        pause(1)

        $ disable_current_zone_sch()
    jump sch_day1_map_1

label sch_day1_beach_map:
    if not ('bh' in list_sch_day1_map_1_visited):
        call sch_day1_event_beach
        $ list_sch_day1_map_1_visited.append['bh']
        $ sch_day1_mp +=1

        pause(1)
    else:
        call sch_day1_event_clubs_visited
        pause(1)

        $ disable_current_zone_sch()
    jump sch_day1_map_1

label sch_day1_dining_hall_map:
    call sch_day1_event_dining_hall
    $ list_sch_day1_map_1_visited.append['bh']
    $ sch_day1_mp +=1
    $ disable_current_zone_sch()

    pause(1)
    jump sch_day1_map_1
