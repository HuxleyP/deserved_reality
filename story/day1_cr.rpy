label sch_day1_cr:
    $ day_time()
    $ persisent.sprite_time = 'day'

    call sch_day1_arrival
    pause(1)

    if sch_day1_info_check:

        $ list_sch_ch_known.append['sl']

        call sch_day1_slavya
		
		pause(1)
        
        if sch_day1_sl_route:
		
			call sch_day1_camp_slavya
			
