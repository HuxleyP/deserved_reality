# Сделано на логической основе 7ДЛ
# ----------------------------------------------
# Про местную иерархию:
# Всё, что начинается с sch_ - переменные или объявленные функции
# Всё, что заканчивается на _sch - использование функций
# Префикс _save означает информацию о сохранении
#
#
#
#
#
#
#
#
#
# ----------------------------------------------




init -1: # Version data
    $ sch_version = "0.0"
    $ sch_state = "alpha"
    $ sch_hotfix = ""
    $ sch_codename = "arctic apricot"

init 2:
    $ mods["sichium"] = u"{size=60}{font=[csn]}{color=#FFFFFF}Заслуженная {/font}{font=[dr_font]}{color=#999999}|{/color}{/font} {font=[csn]}{/color}{color=#999999}Реальность{/color}{/font}{/size}"


label sichium:
    $ sch_save_version = sch_version  # создаём имя сохранению при запуске новой игры

    $ init_map_zones_sch() # По заветам 7ДЛ инициализируем карту единожны, чтобы сохранкам не приходил армаггедец

    if not "Deserved Reality" in config.version: # закидываем себя в трейс на случай армаггедеца игре
        $ config.version = config.version + "Deserved Reality %s, %s %s codename %s" % (sch_state, sch_version, sch_hotfix, sch_codename)

    # Переименовываем игрушку во имя всех богов
    $ config.developer = True #TODO В релиз попасть не должно
    $ config.window_title = u"Заслуженная | Реальность"

    jump sichium_start

init 3:
    call sch_vars # от вылетов подальше

    call sch_day0_vars

label sch_vars: # Основные переменные, без которых жизнь не легка и приводит к трейсам и моему запутыванию
    $ repeated = 0
    $ sch_dayNo = 0

    $ pt_iv = 0
    $ pt_sl = 0
    $ pt_un = 0
    $ pt_us = 0
    $ pt_dv = 0
    $ pt_mi = 0
    $ pt_pi = 0 # Поинты пионера, вычисляются в десятках и сотнях, прибавляются за каждый правильный поступок со стороны регламента лагеря (я серьёзно не знаю, как назвать устав), за правильные поступки даются послабления в дальнейшем, а так же ГГ больше доверяют. Поведение проверяет сам вездесущий Генда и его ручная кошкодевочка, которая для генсека will be fine too
    $ pt_wi = 0 # Поинты воли
    $ pt_ka = 0 # Поинты кармы
    $ pt_nr = 0 # Очки Нуара

    $ girls_pt = [pt_sl, pt_un, pt_us, pt_dv, pt_mi]

    $ sch_bound = False # при всех гудах
    $ sch_true = False # При получении ВЫХОДА к  ТруЪ концовке

    $ sch_hard = False

    $ sch_launch = 0
    if persistent.sch_launched:
        $ sch_launch = 1
    $ sch_ingame = False # был ли в игре, пока что надобность в переменной только ради плейсхолдера

    $ limb = False # Лимб, имя "дефолта", чтобы не путать с Иваном и не писать ГГ, ибо каждый из них ГГ (Тоха уже сказал, что отсылка на один мод, но чёрта с два!)
    $ prophet = False # Пророк, он же трушник, но при этом он выносится как отдельный игрок, ибо Пророк не может выйти на обычные руты, а только на нуара с небольшими изменениями и дополненным тру и на саму тру-ветку

    $ cycled = False
    if persistent.sch_difficulty:
        $ sch_hard = True
    if ((persistent.mi_good_sch) and (persistent.dv_good_sch) and (persistent.sl_good_sch) and (persistent.us_good_sch) and (persistent.un_good_sch) and (persistent.iv_good_sch) and (persistent.nr_good_sch)):
        $ sch_bound = True
    if ((persistent.mi_true_sch) and (persistent.dv_true_sch) and (persistent.sl_true_sch) and (persistent.us_true_sch) and (persistent.un_true_sch) and (persistent.iv_true_sch) and (persistent.nr_ussr_true_sch) and (persistent.nr_rf_true_sch)):
        $ sch_true = True
    if (persistent.mi_good_sch or persistent.mi_bad_sch or persistent.mi_reject_sch or persistent.mi_neutral_sch or persistent.mi_true_sch or persistent.mi_transit_good_sch or persistent.mi_transit_bad_sch or persistent.dv_good_sch or persistent.dv_bad_sch or persistent.dv_reject_sch or persistent.dv_neutral_sch or persistent.dv_true_sch or persistent.dv_transit_good_sch or persistent.dv_transit_bad_sch or persistent.sl_good_sch or persistent.sl_bad_sch or persistent.sl_reject_sch or persistent.sl_neutral_sch or persistent.sl_true_sch or persistent.sl_transit_good_sch or persistent.sl_transit_bad_sch or persistent.un_good_sch or persistent.un_bad_sch or persistent.un_reject_sch or persistent.un_neutral_sch or persistent.un_true_sch or persistent.un_transit_good_sch or persistent.un_transit_bad_sch or persistent.us_good_sch or persistent.us_bad_sch or persistent.us_neutral_sch or persistent.us_true_sch or persistent.iv_good_sch or persistent.iv_bad_sch or persistent.iv_transit_good_sch or persistent.iv_transit_bad_sch or persistent.nr_good_sch or persistent.nr_bad_sch or persistent.nr_rf_true_sch or persistent.nr_ussr_true_sch): # Как же долго я искал ошибку...
        $ cycled = True

    return


label sch_day0_vars:

    $ deathflag = False # Смерть, невыход в игру
    $ true_prologue = False

    return

#Первый день
label sch_day1_vars:

    $ sch_day1_sl_runaway = False #сбежал от Слави
    $ day1_info_check = False # Проверка связи

    $ list_sch_ch_known = [] # Знакомые персонажи
    $ list_sch_day1_together = [] # С кем пошёл к ОД
    $ list_sch_day1_supper = []

    $ list_sch_day1_map_visited = [] # Посещённые места на карте
    $ sch_day1_med_asked_alone = False
    $ sch_day1_aidpost = False
    $ sch_day1_un_walk = 0
    $ sch_day1_sl_cleanuphelp = False
    $ sch_sabotage = 0 # 0 -не знает, 1, 2... - этапы, -1 - отказ в начале -2 - отказ при подтверждении, -3 - отказ в середине, -4 - отказ в конце, -6 - переманил Алису на мирную сторону,
    $ sch_day1_hungry = False

    return

label sch_day2_vars:


    $ sch_day2_od_photo = False
    $ sch_day2_od_failed = False
    $ sch_day2_forest = False

    return

label sch_day3_vars:

    $ list_rootflag_sch = [] #Список рутфлагов, чтобы не писать по 7 переменных

    return

label sch_sl_vars:

    return

label sch_dv_vars:

    return

label sch_un_vars:

    return

label sch_us_vars:

    return

label sch_mi_vars:

    return

label sch_ln_vars:

    return

label sch_nr_vars:

    return

label sch_bound_vars:

    return

label sch_true_vars:

    return
