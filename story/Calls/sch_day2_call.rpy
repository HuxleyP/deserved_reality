label sch_day2_cr:

    $ sunset_time()
    $ persistent.sprite_time = 'sunset'

    call sch_day2_start

    pause(1)

    # немного кода сюда
    if len(list_sch_day2_walk) == 1:
        $ sch_day2_walk_accepted = True
    elif len(list_sch_day2_walk) >1: # от фига подальше
        $ sch_day2_walk_accepted = False
        $ list_sch_day2_walk.append('ln')
    else:
        $ sch_day2_walk_accepted = False

    #-------------------------------

    if not 'forest_un' in list_sch_noir_flag:
        call sch_day2_sq_morning

        pause(1)

    $ day_time()
    $ persistent.sprite_time = 'day'

    call sch_day2_breakfast
