label sichium: # Меню
    $ sch_forgeteveryone()
    if sch_launch == 0:
        call sch_defaultsettings
        $ persistent.sch_launched = True
    $ persistent.sprite_time = "night"
    $ prolog_time()
    $ name_sch()
    if not sch_ingame:
        scene bg white
        $ renpy.movie_cutscene(preroll)
        scene bg white with fade
    play sound whiteflash
    play music honor fadein 1
    $ renpy.movie_cutscene(sch_menu_cs)
    call screen sch_menu
    stop music fadeout 1

label day1_cr:
    $ prolog_time()
    $ persistent.sprite_time = "night"
    scene bg white with dissolve
    stop music fadeout 1
    stop ambience fadeout 1
    stop sound fadeout 1
    # Название
    if sch_true:
        $ sch_chapter(0, u"Последний путь.", new_day=True)
    elif sch_bound:
        $ sch_chapter(0, u"Правильный выбор.", new_day=True)
    else:
        $ sch_chapter(0, u"Сквозь время и пространство.", new_day=True)
    call sch_prologue_prehistory # предыстория
    pause(1)
    if (persistent.mi_good_sch) or (persistent.dv_good_sch) or (persistent.sl_good_sch) or (persistent.us_good_sch) or (persistent.un_good_sch) or (persistent.iv_good_sch) or (persistent.ln_good_sch):
        call sch_keys_check_prologue
    call sch_prologue_start # Пролог
    pause(1)
    if not (sch_bound or sch_true): # "смерть"
        call prologue_normal_end
    else:
        call prologue_true_end
    if deathflag:
        call sichium_death
    else:
        call day1_campcr

label day1_campcr:
    pause(1)
    # Начало первого дня
    $ sch_newday(1)
    $ sch_chapter(1, u"Реинкарнация в новом мире!", new_day=True)
    if persistent.sch_widget:
        $ CycleCounter() # Виджет ЛП
    call sch_day1_default_morning # Утро
    pause(1)
    if day1_info_check: # Не зашёл в лагерь // Waiter-ветка
        $ list_sch_ch_known.append['sl']
        call sch_day1_waiting # Встреча со Славей
        pause(1)
        if sch_day1_sl_together: # ЕСЛИ пошёл со Славей вместе
            call sch_day1_camp_enter_sl # Славя в клубы
            pause(1)
            if sch_day1_sl_escape: # Сбежал от Слави
                call sch_d1cr_dv # Алиса-ветка
                pause(1)
            else:
                call sch_day1_sl # Славя-ветка
                pause(1)
        else: # Отказался идти
            call sch_d1cr_dv #Алиса-ветка
            pause(1)
    else:
        $ sch_chapter(1, u"Тет-а-тет с лагерем.")
        call sch_day1_walker # Walker-ветка
        pause(1)
        if not ('un' in list_sch_ch_known): #Если прошёл мимо Лены
            call sch_day1_mi_meet # Встреча с Мику
            pause(1)
            if sch_day1_mi_help:
                call sch_day1_mi # Мику-ветка
                pause(1)
                if sch_day1_endhelp: # Помог Мику до конца
                    $ sch_day1_late = True
                    $ sch_day1_mi_help = True
                else: #Решил пойти к вожатой
                    $ sch_day1_mi_together = True
            else:
                call sch_d1cr_dv #Алиса-ветка
    #Вожатая
    if not sch_day1_late:
        $ sch_chapter(1, u"Встреча с вожатой.")
        call sch_day1_a_hat_meeting
        $ sch_chapter(1, u"Послевожатье.")
        pause(1)
    call sch_day1_afterod
    pause(1)
    $ sch_chapter(1, u"Прогулка.")
    call sch_day1_map_preparation # После тихого часа
    pause(1)
    call sch_day1_supper #Ужин
    pause(1)




# сокращения call-ов
label sch_d1cr_dv:
    $ sch_chapter(1, u"Наедине с собой.")
    $ list_sch_ch_known.append['dv']
    call sch_day1_dv # Алиса-ветка
    if sch_day1_dv_chase: # Если побежал за Алисой
        $ sch_day1_late = True
    elif not (persistent.dv_good_sch or persistent.dv_reject_sch or persistent.dv_neutral_sch or persistent.dv_true_sch or persistent.dv_transit_good_sch or persistent.dv_transit_bad_sch) or persistent.dv_bad_sch:
        call sch_day1_dv_sl_meet #Облит
        call sch_day1_sl # Прыжок на Славя-ветку
    else:
        pass # Не облит, прямиком к вожатой
    return
