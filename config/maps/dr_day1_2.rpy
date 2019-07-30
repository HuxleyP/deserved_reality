label dr_day1_2_map_preparation:
    if 'mi' or 'dv' in list_dr_day1_together:
        $ dr_day1_mp = 1
    else:
        $ dr_day1_mp = 0
    $ disable_all_zones_dr()
    $ disable_all_chibi_dr()
    $ set_zone_dr('square_dr', 'dr_day1_square_map')
    $ set_zone_dr('music_club_dr', 'dr_day1_music_club_map')
    if dr_day1_mi_inclub:
        $ set_chibi_dr('music_club_dr', 'mi')
    $ set_zone_dr('boat_station_dr', 'dr_day1_boat_station_map')
    $ set_zone_dr('estrade_dr', 'dr_day1_estrade_map')
    $ set_zone_dr('library_dr', 'dr_day1_library_map')
    $ set_zone_dr('clubs_dr', 'dr_day1_clubs_map')
    $ set_zone_dr('beach_dr', 'dr_day1_beach_map')


    $ persistent.sprite_time = "sunset"
    $ sunset_time()

label dr_day1_map_1:

    if dr_day1_mp == 1:
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ set_zone_dr('dining_hall_dr', 'dr_day1_dining_hall_map')

    else:
        $ persistent.sprite_time = "day"
        $ day_time()

    play music music_list["my_daily_life"]

    if dr_day1_mp <2:
        $ show_map_dr()

    else:
        return

        

label dr_day1_square_map:
    # площадь

    if not ('sq' in list_dr_day1_map_1_visited):
        call dr_day1_event_square
        $ list_dr_day1_map_1_visited.append['sq']
        $ dr_day1_mp +=1

        pause(1)

    else:
        call dr_day1_event_square_visited
        pause(1)

        $ disable_current_zone_dr()

    jump dr_day1_map_1

label dr_day1_music_club_map:
    # музклуб

    if not ('mc' in list_dr_day1_map_1_visited) or dr_day1_mi_inclub:
        call dr_day1_event_music_club
        $ dr_day1_mp +=1

        $ list_dr_day1_map_1_visited.append['mc']
        pause(1)

    else:
        call dr_day1_event_music_club_visited
        pause(1)

        $ disable_current_zone_dr()

    jump dr_day1_map_1

label dr_day1_boat_station_map:
    # причал

    if not ('bs' in list_dr_day1_map_1_visited):
        call dr_day1_event_boat_station
        $ list_dr_day1_map_1_visited.append['bs']
        $ dr_day1_mp +=1

        pause(1)

    else:
        call dr_day1_event_boat_station_visited
        pause(1)

        $ disable_current_zone_dr()

    jump dr_day1_map_1

label dr_day1_estrade_map:
    # сцена

    if not ('es' in list_dr_day1_map_1_visited):
        call dr_day1_event_estrade
        $ list_dr_day1_map_1_visited.append['es']
        $ dr_day1_mp +=1

        pause(1)

    else:
        call dr_day1_event_estrade_visited

        pause(1)

        $ disable_current_zone_dr()
    jump dr_day1_map_1

label dr_day1_library_map:
    # библиотека
    if not ('lib' in list_dr_day1_map_1_visited):
        call dr_day1_event_library
        $ list_dr_day1_map_1_visited.append['lib']
        $ dr_day1_mp +=1

        pause(1)

    else:
        call dr_day1_event_library_visited

        pause(1)

        $ disable_current_zone_dr()
    jump dr_day1_map_1

label dr_day1_clubs_map:
    if not ('cl' in list_dr_day1_map_1_visited):
        call dr_day1_event_clubs
        $ list_dr_day1_map_1_visited.append['cl']
        $ dr_day1_mp +=1

        pause(1)

    else:
        call dr_day1_event_clubs_visited
        pause(1)

        $ disable_current_zone_dr()
    jump dr_day1_map_1

label dr_day1_beach_map:
    if not ('bh' in list_dr_day1_map_1_visited):
        call dr_day1_event_beach
        $ list_dr_day1_map_1_visited.append['bh']
        $ dr_day1_mp +=1

        pause(1)
    else:
        call dr_day1_event_clubs_visited
        pause(1)

        $ disable_current_zone_dr()
    jump dr_day1_map_1

label dr_day1_dining_hall_map:
    call dr_day1_event_dining_hall
    $ list_dr_day1_map_1_visited.append['bh']
    $ dr_day1_mp +=1
    $ disable_current_zone_dr()

    pause(1)
    jump dr_day1_map_1
