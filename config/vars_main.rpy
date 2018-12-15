# инит от 14.12

init -9999 python:
    sch_path = 'deserved_reality/'
    source_sch = sch_path+'source/'
    #def sources_sch(file):
    #    return sch_path+"source/%s" % (file)
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


init -1:
#Объявляю ВСЕ переменные в нулевом дне и проверяю что надо
    $ mods['sichium'] = u"{font=[dr_font]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color}{/font}"
    $ repeated = 0
    $ deathflag = False
    $ inside_volume = 0.6
    $ outside_volume = 1
    $ pt_iv = 0
    $ pt_sl = 0
    $ pt_un = 0
    $ pt_us = 0
    $ pt_dv = 0
    $ pt_mi = 0
    $ pt_pi = 0 # Поинты пионера, вычисляются в десятках и сотнях, прибавляются за каждый правильный поступок со стороны регламента лагеря (я серьёзно не знаю, как назвать устав), за правильные поступки даются послабления в дальнейшем, а так же ГГ больше доверяют. Поведение проверяет сам вездесущий Генда и его ручная кошкодевочка, которая для генсека will be fine too
    $ pt_wi = 0 # Поинты воли
    $ pt_ka = 0 #c поинты кармы
    $ pt_nr = 0 # Очки Нуара
    $ sch_bound = False # при всех гудах
    $ sch_true = False # При получении ВЫХОДА к  ТруЪ концовке
    $ sch_hard = False
    $ sch_launch = 0
    $ sch_dayNo = 0
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
    if (persistent.mi_good_sch or persistent.mi_bad_sch or persistent.mi_reject_sch or persistent.mi_neutral_sch or persistent.mi_true_sch or persistent.mi_transit_good_sch or persistent.mi_transit_bad_sch or persistent.dv_good_sch or persistent.dv_bad_sch or persistent.dv_reject_sch or persistent.dv_neutral_sch or persistent.dv_true_sch or persistent.dv_transit_good_sch or persistent.dv_transit_bad_sch or persistent.sl_good_sch or persistent.sl_bad_sch or persistent.sl_reject_sch or persistent.sl_neutral_sch or persistent.sl_true_sch or persistent.sl_transit_good_sch or persistent.sl_transit_bad_sch or persistent.un_good_sch or persistent.un_bad_sch or persistent.un_reject_sch or persistent.un_neutral_sch or persistent.un_true_sch or persistent.un_transit_good_sch or persistent.un_transit_bad_sch or persistent.us_good_sch or persistent.us_bad_sch or persistent.us_neutral_sch or persistent.us_true_sch or persistent.iv_good_sch or persistent.iv_bad_sch or persistent.iv_transit_good_sch or persistent.iv_transit_bad_sch or persistent.nr_good_sch or persistent.nr_bad_sch or persistent.nr_rf_true_sch or persistent.nr_ussr_true_sch): #Как же долго я искал ошибку...
        $ cycled = True

init 99999999:
    $ config.developer = True
    $ config.window_title = u"Заслуженная | Реальность"
    $ config.name = u"Заслуженная | Реальность"


# Нулевой день
label sch_vars_day0:

    $ true_prologue = False
    $ deathflag = False

    return

#Первый день
label sch_vars_day1:

    $ sch_day1_sl_runaway = False #сбежал от Слави
    $ day1_info_check = False # Проверка связи

    $ list_sch_ch_known = [] # Знакомые персонажи
    $ list_sch_day1_together = [] # С кем пошёл к ОД

    $ list_sch_day1_map_visited = [] # Посещённые места на карте
    $ sch_day1_med_asked_alone = False
    $ sch_day1_aidpost = False
    $ sch_day1_un_walk = 0
    $ sch_day1_sl_cleanuphelp = False
    $ sch_sabotage = 0 # 0 -не знает, -1 - отказ, 1, 2... - этапы, -2 - отказ в середине, -3 - отказ перед самым концом




    return

#Второй день
label sch_vars_day2:

    #

    return


#Третий день
label sch_vars_day3:

    $ list_rootflag_sch = [] #Список рутфлагов, чтобы не писать по 7 переменных

    return


#Characters
    $ iv = Character(color="#E2C778", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ god = Character(u'Харон', color="#00fa9a", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ chat = Character(u'Друг', color="#6e3961", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ mother = Character(u'Мама', color="#f9106b", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    # $ glitch = Character(u'Глюк', color="#556b2f", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000") Рест ин пис, бесполезная заглушка.

init -1000:
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


    #CG
    image uvao_d0 = image_sch("cg/uvao_d0.png")
    image cg uvao_d0 = image_sch("cg/d1_uv.jpg")
    image cg uvao_d0_2 = image_sch("cg/d1_uv_2.jpg")

    #gui
    image day_chapter = gui_sch("day_chapter.png")
    image sunset_chapter = gui_sch("sunset_chapter.png")
    image night_chapter = gui_sch("night_chapter.png")
    image prolog_chapter = gui_sch("prolog_chapter.png")

    image day1 = gui_sch('day1.png')
    image day2 = gui_sch('day2.png')
    image day3 = gui_sch('day3.png')
    image day4 = gui_sch('day4.png')
    image day5 = gui_sch('day5.png')
    image day6 = gui_sch('day6.png')
    image day7 = gui_sch('day7.png')



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
    $ heartbeat = sfx_sch("heartbeat.ogg")
    $ whiteflash = sfx_sch("flash.ogg")
    $ wind = sfx_sch("wind.ogg")
    $ watersplash = sfx_sch("watersplash.ogg")
    $ whisper = sfx_sch('whisper.ogg')

    #Шрифт
    $ dr_font = image_sch("LemonTuesday.otf")
    $ csn = image_sch("csn.ttf") # computer says no.



    # Заставки
    $ preroll = video_sch("preroll.webm")



#init:
#    transform rclose:
#         yalign 1.0
#         linear 1.5 yalign 0.0
#         repeat
#
#    transform rnormal:
#         yalign 1.0 xalign 0.0
#         linear 2.5 yalign 0.0
#         repeat
#
#    transform rfar:
#         yalign 1.0 xalign 0.0
#         linear 3.5 yalign 0.0
#         repeat


# Там, где меня нет.
#init python:
    #def name_sch(sch_name):
    #    globals()["name_sch"] = sch_name
        # 920202 - тёмно-красный
        # 295f48 - тёмно-зелёный
        # 5B5BE5 - синий
        #if sch_name == u"Иван":
    #        globals()["sch_colorname"] = "#295f48" # green
    #    elif sch_name == u"Ваня":
    #        globals()["sch_colorname"] = "#5B5BE5" # blue
    #    else:
    #        globals()["sch_colorname"] = "#920202" # red
#
    #    globals()["ivan"] = Character(u"[name_sch]", color = sch_colorname, what_color = "#E2C778", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

init python:
    def name_sch(sch_name='Я'):
        # 920202 - тёмно-красный
        # 295f48 - тёмно-зелёный
        # 5B5BE5 - синий
        if sch_name == "Иван":
            globals()["ivan"] = Character("Иван", color = "#295f48", what_color = "#E2C778", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
        elif sch_name == "Ваня":
            globals()["ivan"] = Character("Ваня", color = "#5B5BE5", what_color = "#E2C778", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
        else:
            globals()["ivan"] = DynamicCharacter(sch_name, color = "#920202", what_color = "#E2C778", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")



#Поинты
python early: # переписать
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




init 999 python:
    def meet(who, name):
        global store
        gl = globals()
        gl[who + "_name"] = name
        store.names[who] = name

    def save_name_known():
        gl = globals()
        global store
        for x in store.names_list:
            if not (x == 'narrator' or x == 'th' or x == 'iv'):
                store.names[x] = gl["%s_name"%x]


    def sch_meeteveryone():
        global store
        meet('mi', u"Азиатка")
        meet('sl', u"Блондинка")
        meet('dv', u"Рыжая")
        meet('us', u"Девочка-СССР")
        meet('un', u"Стесняшка")
        meet('mt', u"Вожатая")
        meet('cs', u"Медсестра")
        meet('dreamgirl', u"Харон")
        meet('el', u"Блондин")
        meet('pi', u"Пионер")
        meet('sh', u"Очкарик")
        meet('uv', u"Нэко")
        meet('god' u'Харон')
        meet('chat', u'Ребёнок')
        meet('mother', u"Мама")

    def sch_forgeteveryone():
        global store
        meet('mi', u"Мику")
        meet('sl', u"Славя")
        meet('dv', u"Алиса")
        meet('us', u"Ульяна")
        meet('un', u"Лена")
        meet('mt', u"Ольга Дмитриевна")
        meet('cs', u"Виола")
        meet('dreamgirl', u"...")
        meet('el', u"Электроник")
        meet('pi', u"Пионер")
        meet('sh', u"Шурик")
        meet('uv', u"Юля")
        meet('god', u'Харон')
        meet('chat', u'Друг')
        meet('mother', u"Мама")

    sch_forgeteveryone()
    set_mode_adv()
    reload_names()

#QTE


# screen sch_day1_qte:
    # image qte:
        # xalign 0.5 yalign 0.5
    # key "q" action [Hide ("sch_day1_walker"), SetVariable ('sch_day1_walker_suc', '1')]
    # key "Q" action [Hide ("sch_day1_walker"), SetVariable ('sch_day1_walker_suc', '1')]
    # key "й" action [Hide ("sch_day1_walker"), SetVariable ('sch_day1_walker_suc', '1')]
    # key "Й" action [Hide ("sch_day1_walker"), SetVariable ('sch_day1_walker_suc', '1')]
    # timer 1 action [Hide ("sch_day1_qte"),]

# QTE Порт эдишн
#call screen sch_qte_day3 # для вызова
#    screen sch_qte_day3:
#        imagebutton xalign 0.5 yalign 0.5: #координаты
#        idle (image_sch("gui/qte_idle.png")) #свободное изображение
#        hover (image_sch("qte_hover.png") #при наведение
#        action [] #действие при нажатие , пиши через запятую
#timer 1 action [Hide("gas_action")] #что произойдет, через указанное время, пиши через запятую


init -1:
    python:
        # цветная вспышка
        # with flash("#822")
        def flash(color="#fff"):
            return Fade(.25, 0, .75, color=color)

        def inside(lights):
            global time_of_day
            global inside_voliume

            volume (inside_volume, 'ambience')
            if day_of_time == "night":
                if lights:
                    persistent.sprite_time = "sunset"

        def outside(lights):
            global time_of_day
            global outside_volume

            volume (outside_volume, 'ambience')

            if day_of_time == "night" and persistent.sprite_time != "night":
                persistent.sprite_time = "night"
        def stop_skip(): # остановка перемотки
            renpy.config.skipping = None


init -10 python: # главы
    def sch_chapter(sch_dayNo, sch_ch_name, new_day=False):
        global save_name # название сейва
        global routetag_sch # руттэг
        renpy.block_rollback()


        renpy.scene()
        renpy.music.play('whisper', channel=sound, fadein=0.5, fadeout = 0.25)
        renpy.show(gui_sch('[persistent.timeofday]_chapter.png'))
        renpy.pause(1)
        renpy.transition(fade)
        dayname = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color}{/font}") # так надо, иначе ошибка
        if new_day:
            if sch_dayNo != 0:
                dayname = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color} - {color=#afafaf}День{/font} {font=[dr_font]}%d{/font}{/color}{/size}") % (sch_dayNo)
            elif sch_dayNo >= 8:
                dayname = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color} - {color=#afafaf}Эпилог. День{/font} {font=[dr_font]}%d{/font}{/color}{/size}") % (sch_dayNo)
            else:
                dayname = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color}{/font}")

        savename = (u'Заслуженная | Реальность')

        renpy.show('day_num', what=Text(dayname, xcenter=0.5,ycenter=0.25))
        renpy.pause(3)
        renpy.scene()
        renpy.show('bg black')
        renpy.transition(fade)
        dayname = (u"{size=70}{font=[csn]}{color=#afafaf}%s{/color}{/font}{/size}") % (sch_ch_name)
        renpy.show('day_num', what=Text(dayname, xcenter=0.5,ycenter=0.45))

        renpy.pause(3)
        renpy.scene()
        renpy.show('bg black')
        renpy.transition(fade)
        renpy.pause(1.5)
        set_mode_adv()

    def sch_newday(sch_dayNo):
        renpy.block_rollback()
        global pt_dv #Алиса
        global pt_un #Лена
        global pt_us #Ульяна
        global pt_sl #Славя
        global pt_iv #ГГ
        global pt_mi #Мику
        global pt_nr #Нуар
        renpy.scene()
        if sch_dayNo != 0:
            if (pt_dv or pt_un or pt_us or pt_sl or pt_iv or pt_mi or pt_nr) == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr):
                renpy.show("Color(hsv=(0, 1.0, [0.1 + pt_iv*0.06]))") # для 15 поинтов у Сыча
            elif pt_us == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr): #Уля
                renpy.show("Color(hsv=(0, 1.0, [pt_us*0.04]))")
            elif pt_dv == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr): # Алиса
                renpy.show("Color(hsv=(.06666, 1.0, [pt_dv*0.04]))")
            elif pt_sl == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr): # Славя
                renpy.show("Color(hsv=(.12222, 1.0, [pt_sl*0.04]))")
            elif pt_mt == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr): # ОД - DLC not included in pack, sry(
                renpy.show("Color(hsv=(.33333, 1.0, [pt_mt*0.04]))")
            elif pt_mi == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr): # Мику
                renpy.show("Color(hsv=(.5, 1.0, [pt_mi*0.04]))")
            elif pt_nr == max(pt_dv, pt_un, pt_us, pt_sl, pt_iv, pt_mi, pt_nr): # Нуар
                renpy.show("Color(hsv=(.75833333, 1.0, [pt_nr*0.04]))")
            else:
                renpy.show("#a6a6a6")
        if not sch_dayNo == 0:
            renpy.show('day[sch_dayNo]')
        renpy.transition(fade)
        renpy.pause(3)
        renpy.scene()
        renpy.show('bg black')
        renpy.transition(fade)
        set_mode_adv()

        #Бекдроп со вкусом костылей (наверное)
        #US - 0
        #DV -  24
        #SL - 44
        #MT - 120
        #MI - 180
        #UN - 273
        #IV - 0-0-x
        #LN - 215


init:
    transform sch_running:
        anchor (0.1, 0.1)
        zoom 1.2
        ease 0.2 pos (0, 0)
        ease 0.2 pos(50,50)
        ease 0.2 pos (0, 0)
        ease 0.2 pos(-50,50)
        repeat



init python:
    import os

init python:
    sch_overriding_on = None
    def overriding_overlay():
        if not overriding_on:
            return
        ui.keymap(mousedown_1=ui.returns(None))
        ui.keymap(mouseup_1=ui.returns(None))
        ui.keymap(I=ui.returns('False'))



# КОММЕНТАРИИ К КОДУ
# ------------------
#   Аффтар-с не паграмист-с, и изволил учиться CPP/JS в школе, что даже не близко
#   Паграмист-с не кодер-с, и изволил учиться на C#, что даже не близко
# ------------------
#   Половина кода написана методом мажорных костылей по типу метода точки в бекдроп-скрине в конце дня
#   Вторая половина кода была либо элементарной в исполнении, либо заезженной, либо сворованной с более мажорных модов
#   В Змейку из нас никто не долбится, потому решаем проблемы по общей логике всех языков паграмиравания
