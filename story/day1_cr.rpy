label sch_day1_cr:

    call sch_vars_day1

    $ day_time()
    $ persisent.sprite_time = 'day'

    call sch_day1_arrival
    pause(1)

    if sch_day1_info_check: # Walker
        $ list_sch_ch_known.append['sl']

        call sch_day1_p1_sl_1 # Встреча со Славей

        pause(1)

        if not 'sl' in list_sch_day1_together: # Если попрощался
            call sch_day1_p1_dv  # Алиса штрафует, КОНЕЦ Алиса-ветки

        else:
            call sch_day1_p1_sl_2

            pause(1)

            if sch_day1_sl_runaway: #Если Сбежал от Слави
                call sch_day1_p1_mi_1 # Встреча с Мику

                pause(1)

                if not 'mi' in list_sch_day1_together: # Если не помог Мику
                    call sch_day1_p1_dv # Алиса штрафует, КОНЕЦ Алиса-ветки

                else:
                    call sch_day1_pi_mi_2 # Если помог, КОНЕЦ Мику-ветки

            else:
                call sch_day1_p1_sl_3 # Если остался со Славей до конца, КОНЕЦ Славя-ветки

    else: #Waiter

        call sch_day1_p1_un_1 #Встреча с Леной, кусок "поздороваться" относится к этому лейблу

        pause(1)

        if not 'un' in list_sch_ch_known: #проверка, здоровался ли с Леной
            call sch_day1_p1_mi_1 # Встреча с Мику

            pause(1)

            if not 'mi' in list_sch_day1_together: # Если не помог Мику
                call sch_day1_p1_dv # Алиса штрафует, КОНЕЦ Алиса-ветки

            else:
                call sch_day1_pi_mi_2 # Если помог, КОНЕЦ Мику-ветки

        else:
            if 'un' in list_sch_day1_together: # Продолжил говорить с Леной
                call sch_day1_p1_un_2

            else:
                call sch_day1_med

    pause(1)

    if not sch_day1_aidpost:
        call sch_day1_od

        pause(1)

        call sch_day1_map_1

        pause(1)
    else:
        pass

    call sch_day1_dinner

    pause(1)

    call sch_day1
