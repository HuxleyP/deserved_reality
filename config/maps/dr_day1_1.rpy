label dr_day1_1_map_preparation:
    $ disable_all_zones_dr()
    $ disable_all_chibi_dr()
    $ set_zone_dr('square_dr', 'dr_day1_1_square_map')
    $ set_zone_dr('music_club_dr', 'dr_day1_1_music_club_map')
    $ set_zone_dr('clubs_dr', 'dr_day1_1_clubs_map')

    $ persistent.sprite_time = 'day'
    $ day_time()

label hueybel:
    pass