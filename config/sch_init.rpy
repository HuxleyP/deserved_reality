init -1: # Version data
    $ sch_version = "5.4.1"
    $ sch_state = "alpha"
    $ sch_hotfix = "hf0"
    $ sch_codename = "arctic apricot"

init: # Объявляем мод
    $ mods["sichium"] = u"{color=#FFFFFF}Заслуженная {color=#999999}|{/color}{color=#999999}Реальность{/color}{/size}"


init 2:

# Общие

    $ repeated = 0
    $ persistent.nonsteam_sch = False
    $ save_name = "Заслуженная | Реальность."
    $ sch_dayNo = 0

    $ hide_back = False # Меню - Убрать кнопку Назад при True

    $ sch_name = "me"

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


    $ sch_karma_shown = False

    $ sch_WidgetVisible = False

    if sch_launch == 0 and persistent.sch_launcher == None:
        $ persistent.sch_widget = False # Виджет ОП, надо поработать над ним
        $ persistent.sch_difficulty = False # False для Noraml
        $ persistent.undone_jumper = False # Прыгалка на незаконченные руты, при False герой заведомо не будет выходить
        $ persistent.sch_launched = True # Проверка на запуск, при нём применяются настройки выше и больше не трогаются
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

    if sch_true:
        $ sch_karma_shown = True

# Пролог

    $ deathflag = False # Смерть, невыход в игру
    $ true_prologue = False

# День 1

    $ list_sch_noir_flag = [] # флаги Нуара
    $ list_sch_ch_known = [] # Знакомые персонажи
    $ list_sch_day1_together = [] # С кем пошёл к ОД
    $ list_sch_day1_help = []
    $ list_sch_day1_supper = []

    $ list_sch_day1_map_visited = [] # Посещённые места на карте
    $ sch_day1_med_asked_alone = False
    $ sch_day1_aidpost = False
    $ sch_day1_un_walk = 0
    $ sch_day1_sl_cleanuphelp = False
    $ sch_sabotage = 0 # 0 -не знает, 1, 2... - этапы, -1 - отказ в начале -2 - отказ при подтверждении, -3 - отказ в середине, -4 - отказ в конце, -6 - переманил Алису на мирную сторону,
    $ sch_day1_hungry = False

# День 2

    $ list_sch_day2_walk = []

    $ sch_day2_od_photo = False
    $ sch_day2_od_failed = False
    $ sch_day2_forest = False



# День 3

    $ list_rootflag_sch = [] #Список рутфлагов, чтобы не писать по 7 переменных


# Визуал, аудио, т.д.

init -998:
    #BG
    image bg bus_stop_summer = image_sch("bg/bus_stop_summer.jpg")
    image bg ext_entrance_night_clear_sch = image_sch("bg/ext_entrance_night_clear_sch.png")
    image bg ext_entrance_night_clear_closed_sch = image_sch("bg/ext_entrance_night_clear_closed_sch.png")
    image bg earth = im.Grayscale(im.Scale(image_sch("bg/earth.png"), 1920, 1080))
    image bg ext_entrance_night_water_sch = image_sch("bg/ext_enterance_night_water.png")
    image bg underwater = image_sch("bg/underwater.jpg")
    image bg semen_room_night = image_sch("bg/semen_room_night.png")
    image bg semen_room_day = image_sch("bg/semen_room_day.png")
    image bg semen_room_sunset = image_sch("bg/semen_room_sunset.png")
    image bg sky = im.Scale(image_sch("bg/sky.jpg"), 1920, 1080)
    image bg ext_warehouse_day_sch = image_sch("bg/ext_warehouse_day_sch.jpg")
    image bg ext_warehouse_rain_sch = image_sch("bg/ext_warehouse_rain_sch.jpg")
    image bg ext_warehouse_sunset_sch = image_sch("bg/ext_warehouse_sunset_sch.jpg")
    image bg ext_warehouse_night_sch = image_sch("bg/ext_warehouse_night_sch.jpg")
    image bg int_home_lift_sch = image_sch("bg/int_home_lift_sch.png")
    image bg ext_winterpark = image_sch("bg/ext_winterpark.jpg")
    image bg speaker_room = image_sch('bg/speaker_room.jpg')


    #CG
    image uvao_d0 = image_sch("cg/uvao_d0.png")
    image cg uvao_d0 = image_sch("cg/d1_uv.jpg")
    image cg uvao_d0_2 = image_sch("cg/d1_uv_2.jpg")

    #gui

    image map_av =  maps_sch('maps/map_avaliable.jpg')
    image map_def =  maps_sch('overlays/map_default.png')

    image dr_pattern = gui_sch('pattern.png')

    image fuchsia_case = gui_sch('widget_case.png')

    image day1 = gui_sch('day1.png')
    image day2 = gui_sch('day2.png')
    image day3 = gui_sch('day3.png')
    image day4 = gui_sch('day4.png')
    image day5 = gui_sch('day5.png')
    image day6 = gui_sch('day6.png')
    image day7 = gui_sch('day7.png')

    # Объявляем основные ассеты

    image bg white = "#fff"
    image white2 = "#ffffff"
    image blacksquare = 'deserved_reality/source/images/gui/menu/square.png'
    image whitesquare = im.MatrixColor("deserved_reality/source/images/gui/menu/square.png", im.matrix.colorize("#fff", "#fff"))
    image gray = "#171717"
    image beige = "#fbf0b3"

    # Объявляем текст для анимаций

    # Меню

    image sch_begin = Text("•Продолжить_Игру", style="sch_keys")
    image sch_continue = Text("•Новая_Игра", style="sch_keys")
    image sch_settings = Text("•Настройки", style="sch_keys")
    image sch_achievements = Text("•Достижения", style="sch_keys")


    image sch_settings_reversed = Text("•Настройки", style="sch_keys_reversed")

    # Настройки

    image sch_back_white = Text("/Назад/", style="sch_keys_white", size = 100)

    image sch_placeholder_off = Text("•Заглушки - OFF", style="sch_keys_white")
    image sch_placeholder_on = Text("•Заглушки - ON", style="sch_keys_white")

    image sch_widget_off = Text("•Виджет ОП - OFF", style="sch_keys_white")
    image sch_widget_on = Text("•Виджет ОП - ON", style="sch_keys_white")

    image sch_difficulty_Hard = Text("•Сложность по умолчанию - Hard", style="sch_keys_white")
    image sch_difficulty_Normal = Text("•Сложность по умолчанию - Обычная", style="sch_keys_white")
    image sch_difficulty_undefined = Text("•Сложность по умолчанию - не установлена", style="sch_keys_white")

    image sch_es_settings = Text("•Перейти в настройки игры", style="sch_keys_white")



    # А тут Мику-диджей крутит музыку :3
    #Music


    $ aire = music_sch("aire.ogg")
    $ cassiopeia = music_sch("cassiopeia.ogg")
    $ connor = music_sch("connor.ogg")
    $ distant = music_sch("distant.ogg")
    $ drowninrain = music_sch("drowninrain.ogg")
    $ dust = music_sch("dust.ogg")
    $ faunts = music_sch("faunts.ogg")
    $ finale = music_sch("finale.ogg")
    $ hallways = music_sch("hallways.ogg")
    $ honor = music_sch("honor.ogg")
    $ lastdawn = music_sch("lastdawn.ogg")
    $ markus = music_sch("markus.ogg")
    $ nullspace = music_sch("nullspace.ogg")
    $ prologue = music_sch("prologue.ogg")
    $ static = music_sch("static.ogg")
    $ sunpatterns = music_sch("sunpatterns.ogg")

    #Ambience
    $ dream = ambience_sch("ambience_safe.ogg")
    $ ambience_elevator = ambience_sch("ambience_elevator")

    #SFX
    $ bang = sfx_sch('bang.ogg')
    $ heartbeat = sfx_sch("heartbeat.ogg")
    $ whiteflash = sfx_sch("flash.ogg")
    $ wind = sfx_sch("wind.ogg")
    $ watersplash = sfx_sch("watersplash.ogg")
    $ whisper = sfx_sch('whisper.ogg')
    $ click = sfx_sch('click.ogg')

    #Шрифт
    $ dr_font = fonts_sch("LemonTuesday.otf")
    $ csn = fonts_sch("csn.ttf") # computer says no.
    $ roboto = fonts_sch("Roboto-Thin.ttf")



    # Заставки
    $ preroll = video_sch("preroll.webm")



# Плюшки

init:
    transform sch_running:
        anchor (0.1, 0.1)
        zoom 1.2
        ease 0.2 pos (0, 0)
        ease 0.2 pos(50,50)
        ease 0.2 pos (0, 0)
        ease 0.2 pos(-50,50)
        repeat

    transform transpa:
        alpha 0.5

    transform right_lower_zoom:
        xalign 0.75 #TODO подкорректировать приближение
        yalign 0.1
        zoom 1.5

    transform lil_zoom:
        zoom 1.0
        xalign 0.5
        yalign 0.5
        linear 0.25 zoom 0.8

    # transform sch_easeinleft







init -10 python: # главы
    def sch_savename_init(sch_char_name):
        global save_name
        if sch_char_name != None:
            save_name = (u" Заслуженная | Реальность\n%s ver.%s/%s; codename \"%s\:\nПролог %s.") % (sch_state, sch_version, sch_hotfix, sch_codename, sch_char_name)
        else:
            save_name = (u" Заслуженная | Реальность\n%s ver.%s/%s; codename \"%s\:\nПролог.") % (sch_state, sch_version, sch_hotfix, sch_codename)


    def sch_chapter(sch_dayNo=0, sch_ch_name=" ", new_day=False, sch_part=0): #dayNo - номер дня (>=8 - пролог), ch_name - название главы,ы, new_day - новый день
        global save_name # название сейва
        global routetag_sch # руттэг
        global pt_dv #Алиса
        global pt_un #Лена
        global pt_us #Ульяна
        global pt_sl #Славя
        global pt_iv #ГГ
        global pt_mi #Мику
        global pt_nr #Нуар
        renpy.block_rollback()

        save_name = (u"Заслуженная | Реальность.") # так надо, иначе ошибка
        if sch_dayNo != 0:
            save_name = (u"Заслуженная | Реальность - День %d.") % (sch_dayNo)
        elif sch_dayNo >= 8:
            save_name = (u"Заслуженная | Реальность. \nЭпилог.")
        elif sch_dayNo == 0 and sch_part !=0:
            save_name = (u"Заслуженная | Реальность.\nЧасть %d.") % (sch_part)
        else:
            save_name = (u"Заслуженная | Реальность.\n%d.") % (sch_part)


        chapter_name = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color}{/font}") # так надо, иначе ошибка
        if sch_dayNo >= 1 or sch_dayNo <= 7:
            chapter_name = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color} - {color=#afafaf}День{/font} {font=[dr_font]}%d{/font}{/color}{/size}") % (sch_dayNo)
        elif sch_dayNo >=8 and sch_part !=0:
            chapter_name = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color} - {color=#afafaf}Часть %d{/font}{/color}{/size}") % (sch_part)
        elif sch_dayNo == 8:
                chapter_name = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color} - {color=#afafaf} Эпилог.{/font}{/color}{/size}")
        else:
            chapter_name = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность.{/font}{/color}{/size}") % (sch_part)

        if new_day:
            renpy.scene()
            if sch_dayNo >=1 and sch_dayNo <=7:
                renpy.show('day[sch_dayNo]')
            renpy.scene()
            if sch_dayNo > 1:
                if max(pt_dv, pt_un, pt_us, pt_sl, pt_mi) >=8 and max(pt_dv, pt_un, pt_us, pt_sl, pt_mi) != 0 and sch_dayNo <=3:
                    if (pt_dv or pt_un or pt_us or pt_sl or pt_iv or pt_mi or pt_nr) == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr):
                        pt_overall = max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr)
                        renpy.show("Color(hsv=(0.9722222, [pt_overall*0.03], 1.0))") # Если очков столько
                    else:
                        renpy.show("#a6a6a6")
                elif pt_us == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr): #Уля
                    renpy.show("Color(hsv=(0, 1.0, [0.5+pt_us*0.04]))")
                elif pt_dv == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr): # Алиса
                    renpy.show("Color(hsv=(.06666, 1.0, [pt_dv*0.04]))")
                elif pt_sl == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr): # Славя
                    renpy.show("Color(hsv=(.12222, 1.0, [pt_sl*0.04]))")
                elif pt_mt == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr): # ОД
                    renpy.show("Color(hsv=(.33333, 1.0, [pt_mt*0.04]))")
                elif pt_mi == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr): # Мику
                    renpy.show("Color(hsv=(.5, 1.0, [pt_mi*0.04]))")
                elif pt_nr == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr): # Нуар
                    renpy.show("Color(hsv=(.75833333, 1.0, [pt_nr*0.04]))")
                else:
                    renpy.show("#a6a6a6")
            elif sch_dayNo >=1 and sch_dayNo <=7:
                renpy.show('day[sch_dayNo]')
            else:
                renpy.show('a6a6a6')
            renpy.show('dr_pattern')

                #Бекдроп со вкусом костылей (наверное)
                #US - 0
                #DV -  24
                #SL - 44
                #MT - 120
                #MI - 180
                #UN - 273
                #IV - 0-0-x
                #LN - 215
                #Совпадение очков - 0,97222

        else:
            renpy.scene()
            renpy.music.play('deserved_reality/source/Sound/sfx/whisper.ogg', channel='sound', fadein=1.5, fadeout = 0.25)
            renpy.show('black')
            renpy.pause(1)
            renpy.transition(fade)
            if sch_ch_name != " ":
                renpy.show('day_num', what=Text(chapter_name, xcenter=0.5,ycenter=0.25))
            renpy.pause(2)
            renpy.scene()
            renpy.show('bg black')
            renpy.transition(fade)
            dayname = (u"{size=70}{font=[csn]}{color=#afafaf}%s{/color}{/font}{/size}") % (sch_ch_name)
            renpy.show('day_num', what=Text(chapter_name, xcenter=0.5,ycenter=0.45))

        renpy.pause(3)
        renpy.scene()
        renpy.show('bg black')
        renpy.transition(fade)
        renpy.pause(1.5)
        set_mode_adv()



#Поинты

python:
    def sch_widget_OP():
        sch_known = len(list_sch_ch_known) # Надо для скрина
        if u"Заслуженная Реальность" or "Заслуженная | Реальность" in save_name and persistent.sch_widget:
            renpy.show_screen('sch_widget_pile')
        else:
            renpy.hide_screen('sch_widget_pile')
        config.overlay_functions.append(bac_widgetFunc) #добавление виджета

# Покоится на японской горе К Ху Ям
python early: #TODO переписать
    def CycleCounter():
        def editoverlay():
            ui.button(clicked=None, xpos=0.1, xanchor=0.0, ypos=2, xpadding=6, xminimum=120)
            if pt_wi >= 90:
                if pt_wi < 150:
                    ui.text("%s: %d" % ("Воля", pt_wi), style="button_text", size=14, color="#007f00")
                else:
                    ui.text("%s: %d" % ("Воля", pt_wi), style="button_text", size=15, color="#009900")
            else:
                ui.text("%s: %d" % ("Воля", pt_wi), style="button_text", size=13)

            ui.button(clicked=None, xpos=0.005, xanchor=0.0, ypos=2, xpadding=6, xminimum=120)
            if pt_pi >= 70:
                if pt_pi < 150:
                    ui.text("%s: %d" % ("Очки Пионера", pt_wi), style="button_text", size=14, color="#007f00")
                else:
                    ui.text("%s: %d" % ("Очки Пионера", pt_wi), style="button_text", size=15, color="#009900")
            else:
                ui.text("%s: %d" % ("Очки Пионера", pt_wi), style="button_text", size=13)

            ui.button(clicked=None, xpos=1.0, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
            if pt_us >= 7:
                if pt_us< 16:
                    ui.text("%s: %d" % ("Ульяна", pt_mi), style="button_text", size=14, color="#e50000")
                else:
                    ui.text("%s: %d" % ("Ульяна", pt_mi), style="button_text", size=15, color="#990000")
            else:
                ui.text("%s: %d" % ("Ульяна", pt_mi), style="button_text", size=13)

            ui.button(clicked=None, xpos=0.93, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
            if pt_mi >= 9:
                if pt_mi < 20:
                    ui.text("%s: %d" % ("Мику", pt_mi), style="button_text", size=14, color="#00bbbb")
                else:
                    ui.text("%s: %d" % ("Мику", pt_mi), style="button_text", size=15, color="#00ffff")
            else:
                ui.text("%s: %d" % ("Мику", pt_mi), style="button_text", size=13)

            ui.button(clicked=None, xpos=0.86, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
            if pt_dv >=11:
                if pt_dv < 18:
                    ui.text("%s: %d" % ("Алиса", pt_dv), style="button_text", size=14, color="#bb8800")
                else:
                    ui.text("%s: %d" % ("Алиса", pt_dv), style="button_text", size=15, color="#ffaa00")
            else:
                ui.text("%s: %d" % ("Алиса", pt_dv), style="button_text", size=13)

            ui.button(clicked=None, xpos=0.79, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
            if pt_sl >= 14:
                if pt_sl < 20:
                    ui.text("%s: %d" % ("Славя", pt_sl), style="button_text", size=14, color="#bbb200")
                else:
                    ui.text("%s: %d" % ("Славя", pt_sl), style="button_text", size=15, color="#ffaa00")
            else:
                ui.text("%s: %d" % ("Славя", pt_sl), style="button_text", size=13)

            ui.button(clicked=None, xpos=0.72, xanchor=1.0, ypos=2, xpadding=6, xminimum=120) #Я выпиливаюсь
            if pt_un >= 12:
                if pt_un < 20:
                    ui.text("%s: %d" % ("Лена", pt_un), style="button_text", size=14, color="#9a6eb8")
                else:
                    ui.text("%s: %d" % ("Лена", pt_un), style="button_text", size=15, color="#a849e9")
            else:
                    ui.text("%s: %d" % ("Лена", pt_un), style="button_text", size=13)

        config.overlay_functions.append(editoverlay)


init python:
    def name_sch(sch_name="me"): #args - me - Я, pr - Протагонист, iv - Иван, van - Ваня
        global colors
        global names
        #if sch_name == "me":
        #    globals()["ivan"] = Character("Иван", color = "#295f48", what_color = "#E2C778", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
        #elif sch_name == "van":
        #    globals()["ivan"] = Character("Ваня", color = "#5B5BE5", what_color = "#E2C778", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
        #elif sch_name == "pr":
        #    globals()["ivan"] = Character("Протагонист", color = "#5b5b5b", what_color = "#E2C778", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
        #else:
        #    globals()["ivan"] = Character("Я", color = "#920202", what_color = "#E2C778", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

        if 'ivan' in store.names_list:
            store.names_list.remove('ivan')
        if sch_name == "ivan":
            colors['ivan'] = {'night': (24, 64, 48, 255), 'sunset': (39, 79, 72, 255), 'day': (41, 96, 72, 255), 'prolog': (34, 69, 72, 255)}
            names['ivan'] = u"Иван"
            store.names_list.append('ivan')
        elif sch_name == "van":
            colors['ivan'] = {'night': (53, 61, 154, 255), 'sunset': (86, 75, 230, 255), 'day': (91, 91, 230, 255), 'prolog': (76, 66, 230, 255)}
            names['ivan'] = u"Ваня"
            store.names_list.append('ivan')
        elif sch_name == "pr":
            colors['ivan'] = {'night': (53, 61, 61, 255), 'sunset': (86, 75, 91, 255), 'day': (91, 91, 91, 255), 'prolog': (76, 66, 91, 255)}
            names['ivan'] = u"Протагонист"
            store.names_list.append('ivan')
        else:
            colors['ivan'] = {'night': (85, 1, 1, 255), 'sunset': (138, 2, 2, 255), 'day': (147, 2, 2, 255), 'prolog': (123, 1, 2, 255)}
            names['ivan'] = u"Я"
            store.names_list.append('ivan')



init 2:
    $ iv = Character( what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000", what_italic = True)
    #$ chat = Character(u'Собеседник', color="#6e3961", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    #$ mother = Character(u'Мама', color="#f9106b", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    #$ ami = Character(u'Амина', color="#cd6c2e", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    #Day - базис
    #Sunset - 94%, 82%, 100%
    #Night - 58%, 67%, 67%
    #Prologue - 84%, 72%, 100%
    #RGBA

    $ colors['ai'] = {'night': (42, 165, 1, 255), 'sunset': (68, 202, 2, 255), 'day': (72, 246, 2, 255), 'prolog': (60, 177, 2, 255)} #rgb(72, 246, 2)
    $ store.names_list.append('ai')#Собеседник, ИИ

    $ colors['chat'] = {'night': (64, 38, 65, 255), 'sunset': (103, 47, 97, 255), 'day': (110, 57, 97, 255), 'prolog': (92, 41, 97, 255)} #rgb(110, 57, 97)
    $ store.names_list.append('chat')#Собеседник

    $ colors['mother'] = {'night': (144, 11, 72, 255), 'sunset': (234, 13, 107, 255), 'day': (249, 16, 107, 255), 'prolog': (209, 12, 107, 255)}
    $ store.names_list.append('mother')#Мама

    $ colors['ami'] = {'night': (119, 72, 31, 255), 'sunset': (193, 89, 46, 255), 'day': (205, 108, 46, 255), 'prolog': (172, 78, 46, 255)}
    $ store.names_list.append('ami')#Амина


    $ names['chat'] = u'Собеседник'
    $ names['ai'] = u'ИИ'
    $ names['mother'] = u"Мама"
    $ names['ami'] = u"Амина"


init 3 python:
    def meet_sch(who, name):
        global store
        gl = globals()
        gl[who + "_name"] = name
        store.names[who] = name


    def save_known_names():
        gl = globals()
        global store
        for x in store.names_list:
            if not (x == 'narrator' or x == 'th' or x == 'iv'):
                store.names[x] = gl["%s_name"%x]


    def sch_forgeteveryone():
        global store
        meet_sch('mi', u"Азиатка")
        meet_sch('sl', u"Блондинка")
        meet_sch('dv', u"Рыжая")
        meet_sch('us', u"Девочка-СССР")
        meet_sch('un', u"Стесняшка")
        meet_sch('mt', u"Вожатая")
        meet_sch('cs', u"Медсестра")
        meet_sch('dreamgirl', u"Харон")
        meet_sch('el', u"Блондин")
        meet_sch('pi', u"Пионер")
        meet_sch('sh', u"Очкарик")
        meet_sch('uv', u"Нэко")
        meet_sch('chat', u'Ребёнок')
        meet_sch('mother', u"Мама")
        meet_sch('ami', u"Амина")
        meet_sch('ai', u"Механический голос")

    def sch_meeteveryone():
        global store
        meet_sch('mi', u"Мику")
        meet_sch('sl', u"Славя")
        meet_sch('dv', u"Алиса")
        meet_sch('us', u"Ульяна")
        meet_sch('un', u"Лена")
        meet_sch('mt', u"Ольга Дмитриевна")
        meet_sch('cs', u"Виола")
        meet_sch('dreamgirl', u"...")
        meet_sch('el', u"Электроник")
        meet_sch('pi', u"Пионер")
        meet_sch('sh', u"Шурик")
        meet_sch('uv', u"Харон")
        meet_sch('chat', u'Друг')
        meet_sch('mother', u"Мама")
        meet_sch('ami', u"Девушка")
        meet_sch('ai', u'ИИ')

    sch_forgeteveryone()
    set_mode_adv()
    reload_names()

init 52 python:
    def disable_all_chibi():
        global global_zones
        for name,data in global_zones.iteritems():
            data["chibi"] = None

init -1001 python:
    def disable_all_chibi():
        global global_zones
        for name,data in global_zones.iteritems():
            data["map_chibi"] = None


init -1000 python: # Пути
    #def sources_sch(file):
    #    return sch_path+"source/%s" % (file)
    config_session = False
    if renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
        sch_path = 'deserved_reality/'
    elif (renpy.version(tuple=False) == "Ren'Py 6.18.3.761") or (persistent.nonsteam_sch == True):
        sch_path = 'mods/deserved_reality/'
    else:
        if renpy.mobile:
            sch_path = 'deserved_reality/'
        else:
            sch_path = '../deserved_reality/' # изменить на выходе
    source_sch = sch_path+'source/'
    def image_sch(file):
        return source_sch+"images/%s" % (file)
    def music_sch(file):
        return source_sch+"Sound/music/%s" % (file)
    def ambience_sch(file):
        return source_sch+"Sound/ambience/%s" % (file)
    def sfx_sch(file):
        return source_sch+"Sound/sfx/%s" % (file)
    def video_sch(file):
        return source_sch+"images/video/%s" % (file)
    def menu_sch(file):
        return source_sch+"images/gui/menu/%s" % (file)
    def gui_sch(file):
        return source_sch+"images/gui/%s" % (file)
    def fonts_sch(file):
        return source_sch+"images/fonts/%s" % (file)
    def maps_sch(file):
        return source_sch+"images/maps/%s" % (file)


# Стили

init -998:
    $ style.sch_keys = Style(style.default)
    $ style.sch_keys.color = "#000000"
    $ style.sch_keys.hover_color = "#800000"
    $ style.sch_keys.size = 83
    $ style.sch_keys.font = csn

    $ style.sch_keys_reversed = Style(style.default)
    $ style.sch_keys_reversed.color = "#800000"
    $ style.sch_keys_reversed.hover_color = "#000000"
    $ style.sch_keys_reversed.size = 83
    $ style.sch_keys_reversed.font = dr_font

    $ style.sch_keys_white = Style(style.default) # Объявление
    $ style.sch_keys_white.color = "#ffffff" # Цвет текста
    $ style.sch_keys_white.hover_color = "#800000" # Цвет при наведении
    $ style.sch_keys_white.size = 83 # Размер
    $ style.sch_keys_white.font = csn

    $ style.sch_desc = Style(style.default)
    $ style.sch_desc.color = "#ffffff"
    $ style.sch_desc.hover_color = "#800000"
    $ style.sch_desc.size = 60
    $ style.sch_desc.font = csn

    $ style.sch_fuchsia = Style(style.default)
    $ style.sch_fuchsia.font = roboto
    $ style.sch_fuchsia.size = 36
