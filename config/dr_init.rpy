init python:
    dr_ambience = {}
    dr_music = {}
    dr_sfx = {}

    for i in renpy.list_files():
        if i.startswith(("[dr_path]source/images/bg/", "[dr_path]source/images/cg/")) and i.endswith((".png", ".jpg")):
            renpy.image((str(i)[39:-4]), i)

        if i.startswith(("[dr_path]source/sounds/ambience/")) and i.endswith((".ogg")):
            dr_ambience[i[45:-4]] = i

        if i.startswith(("[dr_path]source/sounds/music/")) and i.endswith((".ogg")):
            dr_music[i[42:-4]] = i

        if i.startswith(("[dr_path]source/sounds/sfx/")) and i.endswith((".ogg")):
            dr_sfx[i[40:-4]] = i

init 999999999:
    $ config.developer = True #TODO В релиз попасть не должно
    $ config.debug_text_overflow = True #это тоже
    $ config.conditionswitch_predict_all = True # и это

init -1: # Version data
    $ dr_version = "7.3"
    $ dr_state = "Alpha rework"
    $ dr_codename = "Bubble Bean"

init: # Объявляем мод
    $ mods["dr_prestart"] = u"Заслуженная {color=#808080}{font=[dr_source]images/fonts/LemonTuesday.otf}|{/font}Реальность{/color}"


init 2:

# Общие

    $ repeated = 0
    $ save_name = "Заслуженная | Реальность."
    $ dr_dayNo = 0

    $ hide_back = False # Меню - Убрать кнопку Назад при True

    $ dr_iv = 0
    $ dr_sl = 0
    $ dr_un = 0
    $ dr_us = 0
    $ dr_dv = 0
    $ dr_mi = 0
    $ dr_pi = 0 # Поинты пионера, вычисляются в десятках и сотнях, прибавляются за каждый правильный поступок со стороны регламента лагеря (я серьёзно не знаю, как назвать устав), за правильные поступки даются послабления в дальнейшем, а так же ГГ больше доверяют. Поведение проверяет сам вездесущий Генда и его ручная кошкодевочка, которая для генсека will be fine too
    $ dr_wi = 0 # Поинты воли
    $ dr_ka = 0 # Поинты кармы
    $ dr_nr = 0 # Очки Нуара
    $ dr_overall = max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr) # для удобства

    $ girls_pt = [dr_sl, dr_un, dr_us, dr_dv, dr_mi]

    $ dr_bound = False # при всех гудах
    $ dr_true = False # При получении ВЫХОДА к  ТруЪ концовке

    $ dr_hard = False

    if persistent.dr_launched == None:
        $ dr_launch = False

    else:
        $ dr_launch = True


    $ dr_karma_shown = False

    $ dr_WidgetVisible = False

    $ dr_ingame = False # был ли в игре, пока что надобность в переменной только ради плейсхолдера

    $ dr_inmenu = False

    $ limb = False # Лимб, имя "дефолта", чтобы не путать с Иваном и не писать ГГ, ибо каждый из них ГГ (Тоха уже сказал, что отсылка на один мод, но чёрта с два!)
    $ prophet = False # Пророк, он же трушник, но при этом он выносится как отдельный игрок, ибо Пророк не может выйти на обычные руты, а только на нуара с небольшими изменениями и дополненным тру и на саму тру-ветку

    $ cycled = False

    if persistent.dr_difficulty:
        $ dr_hard = True

    if ((persistent.mi_good_dr) and (persistent.dv_good_dr) and (persistent.sl_good_dr) and (persistent.us_good_dr) and (persistent.un_good_dr) and (persistent.iv_good_dr) and (persistent.nr_good_dr)):
        $ dr_bound = True

    if ((persistent.mi_true_dr) and (persistent.dv_true_dr) and (persistent.sl_true_dr) and (persistent.us_true_dr) and (persistent.un_true_dr) and (persistent.iv_true_dr) and (persistent.nr_ussr_true_dr) and (persistent.nr_rf_true_dr)):
        $ dr_true = True

    if (persistent.mi_good_dr or persistent.mi_bad_dr or persistent.mi_reject_dr or persistent.mi_neutral_dr or persistent.mi_true_dr or persistent.mi_transit_good_dr or persistent.mi_transit_bad_dr or persistent.dv_good_dr or persistent.dv_bad_dr or persistent.dv_reject_dr or persistent.dv_neutral_dr or persistent.dv_true_dr or persistent.dv_transit_good_dr or persistent.dv_transit_bad_dr or persistent.sl_good_dr or persistent.sl_bad_dr or persistent.sl_reject_dr or persistent.sl_neutral_dr or persistent.sl_true_dr or persistent.sl_transit_good_dr or persistent.sl_transit_bad_dr or persistent.un_good_dr or persistent.un_bad_dr or persistent.un_reject_dr or persistent.un_neutral_dr or persistent.un_true_dr or persistent.un_transit_good_dr or persistent.un_transit_bad_dr or persistent.us_good_dr or persistent.us_bad_dr or persistent.us_neutral_dr or persistent.us_true_dr or persistent.iv_good_dr or persistent.iv_bad_dr or persistent.iv_transit_good_dr or persistent.iv_transit_bad_dr or persistent.nr_good_dr or persistent.nr_bad_dr or persistent.nr_rf_true_dr or persistent.nr_ussr_true_dr): # Как же долго я искал ошибку...
        $ persistent.cycled = True # а эта куча строк показывает мои огромные амбиции

    if dr_true:
        $ persistent.dr_karma_shown = True

init 3:
    if dr_launch != True:
        $ persistent.dr_widget = False # Виджет ОП, надо поработать над ним
        $ persistent.dr_music = True # Виджет музыки
        $ persistent.dr_difficulty = False # False для Normal
        $ persistent.undone_jumper = False # Прыгалка на незаконченные руты, при False герой заведомо не будет выходить
        $ persistent.dr_chapter_skip = False # Пропуск глав
        $ persistent.dr_butterfly = False # Режим Бабочки

        # тут типа failsafe, но он какой-то тупой
        $ dr_launch = True
        $ persistent.dr_launched = True # Проверка на запуск, при нём применяются настройки выше и больше не трогаются

    call dr_allvars


# Визуал, аудио, т.д.

init -998:
    # image bg_null = Null(1920,1080)
    # #BG
    # image bg boss_office_dr = dr_image("bg/boss_office_dr.jpg")
    # #image bg bus_stop_summer_dr = dr_image("bg/bus_stop_summer.jpg")
    # image bg dr_city = im.Scale(dr_image("bg/city.jpg"), 1920, 1080)
    # image bg raincity_dr = dr_image("bg/rainycity.jpg")
    # image bg int_hospital_storage = dr_image("bg/hospital_storage.png")
    # image bg int_bar_dr = im.Scale(dr_image("bg/int_bar.jpg"), 1920, 1080)
    # image bg ext_bar_dr = dr_image("bg/ext_bar.jpg")
    # image bg ext_cityroad_night_dr = dr_image("bg/ext_cityroad_night_dr.png")
    # image bg ext_entrance_night_clear_dr = dr_image("bg/ext_entrance_night_clear_dr.png")
    # image bg ext_entrance_night_clear_closed_dr = dr_image("bg/ext_entrance_night_clear_closed_dr.png")
    # #image bg earth = im.Grayscale(im.Scale(dr_image("bg/earth.png"), 1920, 1080))
    # image bg ext_entrance_night_water_dr = dr_image("bg/ext_enterance_night_water.png")
    # image bg underwater = dr_image("bg/underwater.jpg")
    # image bg semen_room_night = dr_image("bg/semen_room_night.jpg")
    # image bg semen_room_day = dr_image("bg/semen_room_day.png")
    # image bg semen_room_sunset = dr_image("bg/semen_room_sunset.png")
    # image bg sky_dr = im.Scale(dr_image("bg/sky.jpg"), 1920, 1080)
    # image bg night_sky = im.Scale(dr_image("bg/night_sky.jpg"), 1920, 1080)
    # image bg int_warehouse_day_dr = dr_image("bg/int_warehouse_day_dr.png")
    # image bg ext_warehouse_day_dr = dr_image("bg/ext_warehouse_day_dr.png")
    # image bg ext_warehouse_rain_dr = dr_image("bg/ext_warehouse_rain_dr.png")
    # image bg ext_warehouse_sunset_dr = dr_image("bg/ext_warehouse_sunset_dr.png")
    # image bg ext_warehouse_night_dr = dr_image("bg/ext_warehouse_night_dr.png")
    # image bg int_home_lift_dr = dr_image("bg/int_home_lift_dr.png")
    # #image bg ext_winterpark = dr_image("bg/ext_winterpark.jpg")
    # image bg speaker_room = dr_image("bg/speaker_room.jpg")
    # image bg ext_square_rain_day_dr = dr_image("bg/ext_square_rain_day_dr.jpg")
    # image bg int_hospital_hall_dr = dr_image("bg/int_hospital_hall_dr.jpg")
    # image bg int_hospital_corridor_dr = dr_image("bg/int_hospital_corridor_dr.png")
    # image bg ward_dr = dr_image("bg/ward.png")

    # image bg citybird = dr_image("bg/citybird.jpg")
    # image bg operation_room_dr = dr_image("bg/operation.jpg")
    # image bg int_institute_dr = dr_image("bg/int_institute_dr.jpg")
    # image bg int_institute_corridor_dr = dr_image("bg/corridor_night.png")
    # image bg plain_dr = dr_image("bg/plain.jpg")
    # image bg int_coupe_day_dr = dr_image("bg/int_coupe_day.png")
    # image bg int_coupe_night_dr = dr_image("bg/int_coupe_night.png")
    # image bg doctor_cabinet_dr = Placeholder("bg")

    # image dr_sky_day = dr_image("temp/sky_day.png")
    # image dr_sky_sunset = dr_image("temp/sky_sunset.png")
    # image dr_sky_night = dr_image("temp/sky_night2.jpg")

    # #effects
    # image raineffect = dr_image("effects/raineffect.png")
    # image vignette = dr_image("effects/vignette.png")
    # image cricket = dr_image("effects/cricket.jpg")

    # #CG
    # image cg uvao_d0 = dr_image("cg/uvao_d0.png")
    # image cg uvao_d0 = dr_image("cg/d1_uv.jpg")
    # image cg uvao_d0_2 = dr_image("cg/d1_uv_2.jpg")

    #gui

    image map_av =  dr_maps("maps/map_avaliable.jpg")
    image map_def =  dr_maps("overlays/map_default_fullhd.png")

    image dr_pattern = dr_gui("pattern.png")

    image fuchsia_case = dr_gui("widget_case.png")

    image day1 = im.Scale(dr_gui("/days/day1.png"), 1920, 1080)
    image day2 = im.Scale(dr_gui("/days/day2.png"), 1920, 1080)
    image day3 = im.Scale(dr_gui("/days/day3.png"), 1920, 1080)
    image day4 = im.Scale(dr_gui("/days/day4.png"), 1920, 1080)
    image day5 = im.Scale(dr_gui("/days/day5.png"), 1920, 1080)
    image day6 = im.Scale(dr_gui("/days/day6.png"), 1920, 1080)
    image day7 = im.Scale(dr_gui("/days/day7.png"), 1920, 1080)

    # Объявляем основные ассеты

    image bg dr_white = "#fff"
    image dr_white2 = "#ffffff"
    image dr_blacksquare = "[dr_path]source/images/gui/menu/square.png"
    image dr_whitesquare = im.MatrixColor("[dr_path]source/images/gui/menu/square.png", im.matrix.colorize("#fff", "#fff"))
    image dr_gray = "#171717"
    image dr_beige = "#fbf0b3"
    image dr_yellowish = "#7d5f34"
    image dr_exit_idle = "[dr_source]images/gui/menu/ButtonExit_idle.png"

    # Объявляем текст для анимаций

    # Меню

    image dr_begin = Text("•Продолжить_Игру", style = "dr_keys")
    image dr_continue = Text("•Новая_Игра", style = "dr_keys")
    image dr_settings = Text("•Настройки", style = "dr_keys")
    image dr_achievements = Text("•Достижения", style = "dr_keys")


    #image dr_settings_reversed = Text("•Настройки", style="dr_keys_reversed")

    # Настройки, неактуально из-за нового меню

    #image dr_back_white = Text("/Назад/", style="dr_keys_white", size = 100)

    #image dr_placeholder_off = Text("•Заглушки - OFF", style="dr_keys_white")
    #image dr_placeholder_on = Text("•Заглушки - ON", style="dr_keys_white")

    #image dr_widget_off = Text("•Виджет ОП - OFF", style="dr_keys_white")
    #image dr_widget_on = Text("•Виджет ОП - ON", style="dr_keys_white")

    #image dr_difficulty_hard = Text("•Сложность по умолчанию - Hard", style="dr_keys_white")
    #image dr_difficulty_normal = Text("•Сложность по умолчанию - Обычная", style="dr_keys_white")
    #image dr_difficulty_undefined = Text("•Сложность по умолчанию - не установлена", style="dr_keys_white")

    #image dr_es_settings = Text("•Перейти в настройки игры", style="dr_keys_white")



    # А тут Мику-диджей крутит музыку :3
    # Красочные описания присутствуют
    #Music


    # $ aire = dr_music("aire.ogg")
    # $ angelalive = dr_music("angelalive.ogg") # Тема Слави

    # $ cassiopeia = dr_music("cassiopeia.ogg") # Сон
    # $ connor = dr_music("connor.ogg") # технологичная напряжёнка

    # $ distant = dr_music("distant.ogg") # пессимистичная
    # $ drowninrain = dr_music("drowninrain.ogg") # Дождь
    # #$ dust = dr_music("dust.ogg")

    # $ faunts = dr_music("faunts.ogg") # стелс
    # $ finale = dr_music("finale.ogg") # финалка
    # $ followme = dr_music("followme.ogg") # ты пойдёшь со мной?

    # $ goodday = dr_music("goodday.ogg") # ежедневка 1

    # $ hallways = dr_music("hallways.ogg") # напряжённая
    # $ honor = dr_music("honor.ogg") # main menu, ТЫ проиграл
    # $ hope = dr_music("hope.ogg") # из меланхолии в надежду

    # $ lastdawn = dr_music("lastdawn.ogg") # грустняк
    # $ lasvegas = dr_music("lasvegas.ogg") # грустняк 2

    # $ markus = dr_music("markus.ogg") # всё скатилось, но есть надежда

    # $ nightshow = dr_music("nightshow.ogg") # техно
    # $ nullspace = dr_music("nullspace.ogg") # где-то по ту сторону, герой умер?

    # $ premonition = dr_music("premonition.ogg") # напряжённая
    # $ prologue = dr_music("prologue.ogg") # мажорная мелодия, оптимистичная

    # $ regenerate = dr_music("killedthelord.ogg") # надежда

    # $ spring = dr_music("spring.ogg") # надежда, которая как бы всё, но ещё не совсем
    # $ static = dr_music("static.ogg") # непростая ситуация


    # #Ambience
    # $ dream = dr_ambience("ambience_safe.ogg")
    # $ ambience_elevator = dr_ambience("ambience_elevator")
    # $ citynoise = dr_ambience("ambience_citynoise.ogg")

    # #SFX
    # $ bang = dr_sfx("bang.ogg")
    # $ heartbeat = dr_sfx("heartbeat.ogg")
    # $ whiteflash = dr_sfx("flash.ogg")
    # $ wind = dr_sfx("wind.ogg")
    # $ watersplash = dr_sfx("watersplash.ogg")
    # $ whisper = dr_sfx("whisper.ogg")
    # $ click = dr_sfx("click.ogg")
    # $ get_shot = dr_sfx("getshot.ogg")
    # $ car_stop = dr_sfx("car_stop.ogg")
    # $ surprise = dr_sfx("surprise.ogg")
    # $ sneeze = dr_sfx("sneeze.ogg")

    #Шрифт
    $ dr_font = dr_fonts("LemonTuesday.otf")
    $ dr_csn = dr_fonts("csn.ttf") # computer says no.
    $ dr_roboto = dr_fonts("Roboto.ttf")



    # Заставки
    $ preroll = dr_video("preroll.webm")



# Плюшки


init:
    # поиграем в красоту
    python:
        def dr_window_hide(pause=True):
            renpy.show_layer_at(dr_screenhide, layer="screens")
            if pause:
                renpy.pause(delay=0.5, hard=True)

        def dr_window_show(pause=True):
            renpy.show_layer_at(dr_screenshow, layer="screens")
            if pause:
                renpy.pause(delay=0.5, hard=True)

    transform dr_screenhide:
        xpos 0.0 ypos 0.0 alpha 1.0
        ease 0.5 xpos 0.0 ypos 0.1 alpha 0.0

    transform dr_screenshow:
        ypos 0.1 alpha 0.0
        ease 0.5 ypos 0.0 alpha 1.0

    #а дальше история умалчивает

    transform dr_transpa:
        alpha 0.5

    transform dr_right_lower_zoom:
        xalign 0.75 #TODO подкорректировать приближение
        yalign 0.1
        zoom 1.5

    transform dr_lil_zoom:
        zoom 1.0
        xalign 0.5
        yalign 0.5
        linear 0.25 zoom 0.8

    image dr_main_menu_atl:
        "white2" with Dissolve(0.5)
        pause 0.5
        block:
            "dr_sky_day" with Dissolve(4)
            pause 6.0
            "dr_sky_sunset" with Dissolve(4)
            pause 6.0
            "dr_sky_night" with Dissolve(4)
            pause 6.0
            repeat

    image dr_main_menu_atl_short:
        "dr_sky_day" with Dissolve(4)
        pause 6.0
        "dr_sky_sunset" with Dissolve(4)
        pause 6.0
        "dr_sky_night" with Dissolve(4)
        pause 6.0
        repeat

# старый на всякий
#    transform dr_running:
#        anchor (0.1, 0.1)
#        zoom 1.2
#        ease 0.2 pos (0, 0)
#        ease 0.2 pos(50,50)
#        ease 0.2 pos (0, 0)
#        ease 0.2 pos(-50,50)
#        repeat


    transform dr_running:
        parallel:
            # приближаем, унижаем, для красоты
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            ease 0.2 zoom 1.04 xpos 0.5 ypos 0.49
        parallel:
            # дергаем экранчик на ничего - 0.1-0.2 (хотя иногда ренпай от таких маленьких изменений заставляет изменяемую вещь в космос улететь)
            ease 0.2 xpos 0.5 ypos 0.49
            ease 0.2 xpos 0.48 ypos 0.51
            ease 0.2 xpos 0.5 ypos 0.49
            ease 0.2 xpos 0.52 ypos 0.51
            repeat

    transform dr_running_stop:
        ease 0.2 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 # тупа возвращаем всё обратно

    transform dr_menu_ease:
        xpos 2131
        yalign 0.5
        linear 0.5 xpos 1131 yalign 0.5

init python:
    def dr_noir(id, brightness = -0.4, tint_r = 0.2126, tint_g = 0.7152, tint_b = 0.0722, saturation = 0.5):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) * im.matrix.tint(tint_r, tint_g, tint_b) * im.matrix.saturation(saturation))

    # изменяемый ЧБ
    #def BlackWhite(id, power, brightness = 1.0, saturation = 1.0):
    #    r = power*0.255
    #    g = r
    #    b = r
    #    return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) * im.matrix.tint(r, g, b) * im.matrix.saturation(saturation))

    def dr_BlackWhite(id, saturation):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(saturation))

    def dr_Sepia(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.15) * im.matrix.tint(1.0, .94, .76))

    def dr_NeonSepia(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.15) * im.matrix.tint(.7, .3, .1))



# TODO!!!!!!!!!!!!!!!!!!!! Требует полного рерайта
init 10 python: # главы #TODO к херам
    def dr_savename_init(dr_char_name=" "):
        global save_name
        if dr_char_name != " ":
            save_name = (u" Заслуженная | Реальность \n%s ver.%s/; \"%s\":\nПролог %s.") % (dr_state, dr_version, dr_codename, dr_char_name)
        else:
            save_name = (u" Заслуженная | Реальность \n%s ver.%s/; \"%s\":\nПролог.") % (dr_state, dr_version, dr_codename)

    def dr_newday(dr_dayNo):
        #TODO TODO ЦВЕТА С НУЛЯ, НЕ РАБОТАЕТ
        global dr_dv #Алиса
        global dr_un #Лена
        global dr_us #Ульяна
        global dr_sl #Славя
        global dr_iv #ГГ
        global dr_mi #Мику
        global dr_nr #Нуар
        renpy.scene()

        if dr_dayNo >=1 and dr_dayNo <=7:
            renpy.show("day1")
            renpy.transition(fade)
            renpy.pause(3, hard=True)
            renpy.scene()
            renpy.show("black")
            renpy.transition(fade)
        renpy.scene()

        if (dr_dayNo > 1) and (not dr_hard):

            if dr_noir_flag == 1: # сделать проверку на тян
                renpy.show("Color(hsv = (0, 0, 0.4875))")

            elif dr_noir_flag == 2:
                renpy.show("Color(hsv = (0, 0, 0.325))")

            elif dr_noir_flag == 3:
                renpy.show("Color(hsv = (0, 0, 0.1625))")

            elif (max(dr_dv, dr_un, dr_us, dr_sl, dr_mi)  >= 0) and (dr_dayNo <=3): # до 4 дня, очков тян больше нуля,

                if (dr_dv or dr_un or dr_us or dr_sl or dr_iv or dr_mi or dr_nr) == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): #если равно
                    dr_overall = max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr)
                    renpy.show("Color(hsv = (0.9722222, [dr_overall*0.03], 1.0))") #розовый

                elif (max(dr_dv, dr_un, dr_us, dr_sl, dr_mi) >=8): #  больше восьми, saturation = 100, изменяется brightness
                    if dr_us == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): #Уля
                        renpy.show("Color(hsv = (0, [0.5+dr_us*0.04], 1.0))")

                    elif dr_dv == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # Алиса
                        renpy.show("Color(hsv = (.06666, [dr_dv*0.04], 1.0))")

                    elif dr_sl == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # Славя
                        renpy.show("Color(hsv = (.12222, [dr_sl*0.04], 1.0))")

                    elif dr_mt == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # ОД
                        renpy.show("Color(hsv = (.33333, [dr_mt*0.04], 1.0))")

                    elif dr_mi == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # Мику
                        renpy.show("Color(hsv = (.5, [dr_mi*0.04], 1.0))")

                else: # от одного до восьми, brightness = color*0.32, изменяется saturation

                    if dr_us == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): #Уля
                        renpy.show("Color(hsv = (0, 1.0, [0.5+dr_us*0.04]))")

                    elif dr_dv == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # Алиса
                        renpy.show("Color(hsv = (.06666, 1.0, [dr_dv*0.04]))")

                    elif dr_sl == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # Славя
                        renpy.show("Color(hsv = (.12222, 1.0, [dr_sl*0.04]))")

                    elif dr_mt == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # ОД
                        renpy.show("Color(hsv = (.33333, 1.0, [dr_mt*0.04]))")

                    elif dr_mi == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # Мику
                        renpy.show("Color(hsv = (.5, 1.0, [dr_mi*0.04]))")
                        
            elif dr_dayNo >=4:
                pass
                #TODO по руттегам, без лого ЗР
            else:
                renpy.show("#a6a6a6") # НЕ РАБОТАЕТ!
            renpy.show("dr_pattern")
            renpy.transition(fade)
            renpy.pause(3, hard=True)
            renpy.scene()
        renpy.show("black")
        renpy.transition(fade)
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


    def dr_chapter(dr_dayNo, dr_ch_name): #dayNo - номер дня (>=8 - пролог), ch_name - название главы,ы, new_day - новый день
        global dr_inmenu
        global save_name # название сейва
        global routetag_dr # руттэг
        global dr_chapter_skip
        renpy.fix_rollback()

        dr_inmenu = False # при возвращении в главное меню анимация начинается с белого экрана

        save_name = (u"Заслуженная | Реальность") # так надо, иначе ошибка
        if dr_dayNo != 0:
            save_name = (u"Заслуженная | Реальность - День %d.") % (dr_dayNo)
            if dr_ch_name != "":
                save_name = (u"Заслуженная | Реальность - День %d.\n%s.") % (dr_dayNo, dr_ch_name)

        elif dr_dayNo >= 8:
            save_name = (u"Заслуженная | Реальность. \nЭпилог.")


        chapter_name = (u"{size=80}{font=[dr_csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color}{/font}") # так надо, иначе ошибка

        if not persistent.dr_chapter_skip:
            #renpy.music.play("deserved_reality/source/sounds/sfx/whisper.ogg", channel="sound", fadein=1.5, fadeout=0.5)
            renpy.scene()
            renpy.show("black")
            renpy.transition(fade)
            renpy.show("day_num", what=Text(chapter_name, xcenter=0.5, ycenter=0.25))
            renpy.transition(fade)
            renpy.pause(1.5)
            renpy.scene()
            renpy.show("bg black")
            renpy.transition(fade)
            dayname = (u"{size=70}{font=[dr_csn]}{color=#afafaf}%s{/color}{/font}{/size}") % (dr_ch_name)
            renpy.show("day_num", what=Text(dayname, xcenter=0.5,ycenter=0.45))
            renpy.pause(1.5)
            renpy.scene()
            renpy.show("bg black")
            renpy.transition(fade)
            renpy.pause(1.25, hard=True)

#TODO END


#Поинты

init python:
    def dr_widget_OP():
        if (u"Заслуженная Реальность" or "Заслуженная | Реальность" in save_name) and persistent.dr_widget:
            renpy.show_screen("dr_fuchsia_widget")
        else:
            renpy.hide_screen("dr_fuchsia_widget")
        config.overlay_functions.append(dr_widget_OP) #добавление виджета

init python:
    dr_std_set_for_preview = {}
    dr_std_set = {}
    store.dr_colors = {}
    store.dr_names = {}
    store.dr_names_list = []
    dr_time_of_day = "night"

    _show_two_window = True

    store.dr_names_list.append("dr_narrator")

    store.dr_names_list.append("dr_th")


    dr_colors["dr_voice"] = {"night": (225, 221, 125, 255), "sunset": (225, 221, 125, 255), "day": (225, 221, 125, 255), "prolog": (225, 221, 125, 255)}
    dr_names["dr_voice"] = "Голос"
    store.dr_names_list.append("dr_voice")

    dr_colors["dr_myself"] = {"night": (225, 221, 125, 255), "sunset": (225, 221, 125, 255), "day": (225, 221, 125, 255), "prolog": (225, 221, 125, 255)}
    dr_names["dr_myself"] = "Я"
    store.dr_names_list.append("dr_myself")

    dr_colors["dr_el"] = {"night": (205, 205, 0, 255), "sunset": (255, 255, 0, 255), "day": (255, 255, 0, 255), "prolog": (255, 255, 0, 255)}
    dr_names["dr_el"] = "Электроник"
    store.dr_names_list.append("dr_el")

    dr_colors["dr_un"] = {"night": (170, 100, 217, 255), "sunset": (185, 86, 255, 255), "day": (185, 86, 255, 255), "prolog": (185, 86, 255, 255)}
    dr_names["dr_un"] = "Лена"
    store.dr_names_list.append("dr_un")

    dr_colors["dr_dv"] = {"night": (210, 139, 16, 255), "sunset": (255, 170, 0, 255), "day": (255, 170, 0, 255), "prolog": (255, 170, 0, 255)}
    dr_names["dr_dv"] = "Алиса"
    store.dr_names_list.append("dr_dv")

    dr_colors["dr_sl"] = {"night": (214, 176, 0, 255), "sunset": (255, 210, 0, 255), "day": (255, 210, 0, 255), "prolog": (255, 210, 0, 255)}
    dr_names["dr_sl"] = "Славя"
    store.dr_names_list.append("dr_sl")

    dr_colors["dr_us"] = {"night": (234, 55, 0, 255), "sunset": (255, 50, 0, 255), "day": (255, 50, 0, 255), "prolog": (255, 50, 0, 255)}
    dr_names["dr_us"] = "Ульяна"
    store.dr_names_list.append("dr_us")

    dr_colors["dr_mt"] = {"night": (0, 182, 39, 255), "sunset": (0, 234, 50, 255), "day": (0, 234, 50, 255), "prolog": (0, 234, 50, 255)}
    dr_names["dr_mt"] = "Ольга Дмитриевна"
    store.dr_names_list.append("dr_mt")

    dr_colors["dr_cs"] = {"night": (134, 134, 230, 255), "sunset": (165, 165, 255, 255), "day": (165, 165, 255, 255), "prolog": (165, 165, 255, 255)}
    dr_names["dr_cs"] = "Виола"
    store.dr_names_list.append("dr_cs")

    dr_colors["dr_mz"] = {"night": (84, 129, 219, 255), "sunset": (114, 160, 255, 255), "day": (74, 134, 255, 255), "prolog": (74, 134, 255, 255)}
    dr_names["dr_mz"] = "Женя"
    store.dr_names_list.append("dr_mz")

    dr_colors["dr_mi"] = {"night": (0, 180, 207, 255), "sunset": (0, 252, 255, 255), "day": (0, 222, 255, 255), "prolog": (0, 222, 255, 255)}
    dr_names["dr_mi"] = "Мику"
    store.dr_names_list.append("dr_mi")

    dr_colors["dr_uv"] = {"night": (64, 208, 0, 255), "sunset": (78, 255, 0, 255), "day": (78, 255, 0, 255), "prolog": (78, 255, 0, 255)}
    dr_names["dr_uv"] = "Харон"
    store.dr_names_list.append("dr_uv")

    dr_colors["dr_sh"] = {"night": (205, 194, 18, 255), "sunset": (255, 242, 38, 255), "day": (255, 242, 38, 255), "prolog": (255, 242, 38, 255)}
    dr_names["dr_sh"] = "Шурик"
    store.dr_names_list.append("dr_sh")

    dr_colors["dr_pi"] = {"night": (230, 0, 0, 255), "sunset": (230, 0, 0, 255), "day": (230, 1, 1, 255), "prolog": (230, 0, 0, 255)}
    dr_names["dr_pi"] = "Пионер"
    store.dr_names_list.append("dr_pi")

    dr_colors["dr_bush"] = {"night": (192, 192, 192, 255), "sunset": (192, 192, 192, 255), "day": (192, 192, 192, 255), "prolog": (192, 192, 192, 255)}
    dr_names["dr_bush"] = "Голос"
    store.dr_names_list.append("dr_bush")

    dr_colors['dr_ai'] = {'night': (42, 165, 1, 255), 'sunset': (68, 202, 2, 255), 'day': (72, 246, 2, 255), 'prolog': (60, 177, 2, 255)} #rgb(72, 246, 2)
    dr_names['dr_ai'] = 'ИИ'
    store.dr_names_list.append('dr_ai')#Собеседник, ИИ

    dr_colors['dr_chat'] = {'night': (64, 38, 65, 255), 'sunset': (103, 47, 97, 255), 'day': (110, 57, 97, 255), 'prolog': (92, 41, 97, 255)} #rgb(110, 57, 97)
    dr_names['dr_chat'] = 'Собеседник'
    store.dr_names_list.append('dr_chat')#Собеседник

    dr_colors['dr_mother'] = {'night': (144, 11, 72, 255), 'sunset': (234, 13, 107, 255), 'day': (249, 16, 107, 255), 'prolog': (209, 12, 107, 255)}
    dr_names['dr_mother'] = "Мама"
    store.dr_names_list.append('dr_mother')#Мама

    dr_colors['dr_ami'] = {'night': (119, 72, 31, 255), 'sunset': (193, 89, 46, 255), 'day': (205, 108, 46, 255), 'prolog': (172, 78, 46, 255)}
    dr_names['dr_ami'] = "Амина"
    store.dr_names_list.append('dr_ami')#Амина

    dr_colors['dr_os'] = {'night': (26, 215, 14, 255), 'sunset': (26, 215, 14, 255), 'day': (26, 215, 14, 255), 'prolog': (26, 215, 14, 255)}
    dr_names['dr_os'] = "Олег Степанович"
    store.dr_names_list.append('dr_os')#Олег Степанович

    dr_colors['dr_med'] = {'night': (210, 182, 72, 255), 'sunset': (210, 182, 72, 255), 'day': (210, 182, 72, 255), 'prolog': (210, 182, 72, 255)}
    dr_names['dr_med'] = "Доктор"
    store.dr_names_list.append('dr_med')#Доктор

    dr_colors['dr_guard'] = {'night': (2, 73, 138, 255), 'sunset': (2, 73, 138, 255), 'day': (2, 73, 138, 255), 'prolog': (2, 73, 138, 255)}
    dr_names['dr_guard'] = "Охранник"
    store.dr_names_list.append('dr_guard')#охранник

    #th_prefix = "~ "
    #th_suffix = " ~"

    def name_sch(dr_name):
        global dr_colors
        global dr_names
        global dr_store
        gl = globals()

        if 'ivan' in dr_colors:
            del dr_colors['ivan']

        if 'ivan' in store.dr_names_list:
            store.dr_names_list.remove('ivan')

        gl['ivan' + "_name"] = dr_name

        if dr_name == u"Иван":
            dr_colors['ivan'] = {'night': (24, 64, 48, 255), 'sunset': (39, 79, 72, 255), 'day': (41, 96, 72, 255), 'prolog': (34, 69, 72, 255)}
            store.dr_names['ivan'] = u"Иван"
            #names['ivan'] = u"Иван"
            store.dr_names_list.append('ivan')

        elif dr_name == u"Ваня":
            dr_colors['ivan'] = {'night': (53, 61, 154, 255), 'sunset': (86, 75, 230, 255), 'day': (91, 91, 230, 255), 'prolog': (76, 66, 230, 255)}
            store.dr_names['ivan'] = u"Ваня"
            #names['ivan'] = u"Ваня"
            store.dr_names_list.append('ivan')

        elif dr_name == u"Протагонист" or dr_name == u"Пророк":
            dr_colors['ivan'] = {'night': (53, 61, 61, 255), 'sunset': (86, 75, 91, 255), 'day': (91, 91, 91, 255), 'prolog': (76, 66, 91, 255)}
            store.dr_names['ivan'] = dr_name
            #names['ivan'] = u"Протагонист"
            store.dr_names_list.append('ivan')

        else:
            dr_colors['ivan'] = {'night': (85, 1, 1, 255), 'sunset': (138, 2, 2, 255), 'day': (147, 2, 2, 255), 'prolog': (123, 1, 2, 255)}
            store.dr_names['ivan'] = dr_name
            #names['ivan'] = dr_name
            store.dr_names_list.append('ivan')

        dr_reload_names()

    def dr_char_define(x,is_nvl=False):
        global DynamicCharacter
        global _show_two_window
        global nvl
        global dr_store
        global dr_time_of_day
        gl = globals()
        v = "_voice"
        if  x == 'dr_narrator':
            if  is_nvl:
                gl['dr_narrator'] = Character(None, kind=nvl, what_style="narrator_%s"%dr_time_of_day, ctc="ctc_animation_nvl", ctc_position="fixed")
            else:
                gl['dr_narrator'] = Character(None, what_style="narrator_%s"%dr_time_of_day, ctc="ctc_animation", ctc_position="fixed")
            return
        if  x == 'dr_th':
            if  is_nvl:
                gl['dr_th'] = Character(None, kind=nvl, what_style="thoughts_%s"%dr_time_of_day,what_italic = True, ctc="ctc_animation_nvl", ctc_position="fixed")
            else:
                gl['dr_th'] = Character(None, what_style="thoughts_%s"%dr_time_of_day,what_italic = True, ctc="ctc_animation", ctc_position="fixed")
            return
        if  is_nvl:
            gl[x] = DynamicCharacter("%s_dr_name"%x, color=store.dr_colors[x][dr_time_of_day], kind=nvl, what_style="normal_%s"%dr_time_of_day,who_suffix=":", ctc="ctc_animation_nvl", ctc_position="fixed")
            gl["%s_dr_name"%x] = store.dr_names[x]
        else:
            gl[x] = DynamicCharacter("%s_dr_name"%x, color=store.dr_colors[x][dr_time_of_day], show_two_window=_show_two_window,  what_style="normal_%s"%dr_time_of_day, ctc="ctc_animation", ctc_position="fixed")
            gl["%s_dr_name"%x] = store.dr_names[x]

    def dr_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global dr_store
        for x in store.dr_names_list:
            dr_char_define(x)

    def dr_mode_nvl():
        nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global narrator
        global th
        narrator_nvl = narrator
        th_nvl = th
        
        global dr_store
        for x in store.dr_names_list:
            dr_char_define(x,True)

    def dr_reload_names():
        global dr_store
        for x in store.dr_names_list:
            dr_char_define(x)

    dr_mode_adv()
    dr_reload_names()


init 3 python:
    def dr_meet(who, name):
        global store
        gl = globals()
        gl[who + "_name"] = name
        store.dr_names[who] = name

    def dr_save_names_known():
        gl = globals()
        global store
        for x in store.dr_names_list:
            if not (x == 'narrator' or x == 'th'):
                store.dr_names[x] = gl["%s_name"%x]


    def dr_forgeteveryone():
        global store
        dr_meet('dr_voice', u"Голос")
        dr_meet('dr_myself', u"Я")
        dr_meet('dr_mi', u"Азиатка")
        dr_meet('dr_sl', u"Блондинка")
        dr_meet('dr_dv', u"Рыжая")
        dr_meet('dr_us', u"Девочка-СССР")
        dr_meet('dr_un', u"Стесняшка")
        dr_meet('dr_mt', u"Вожатая")
        dr_meet('dr_cs', u"Медсестра")
        dr_meet('dr_dreamgirl', u"...")
        dr_meet('dr_el', u"Блондин")
        dr_meet('dr_pi', u"Пионер")
        dr_meet('dr_sh', u"Очкарик")
        dr_meet('dr_uv', u"Девушка")
        dr_meet('dr_chat', u'Ребёнок')
        dr_meet('dr_mother', u"Мама")
        dr_meet('dr_ami', u"Амина")
        dr_meet('dr_ai', u"Искин")
        dr_meet('dr_os', u'Олег Степанович')
        dr_meet('dr_med', u'Доктор')
        dr_meet('dr_guard', u'Охранник')

    def dr_meeteveryone():
        global store
        dr_meet('dr_voice', u"Голос")
        dr_meet('dr_myself', u"Я")
        dr_meet('dr_mi', u"Мику")
        dr_meet('dr_sl', u"Славя")
        dr_meet('dr_dv', u"Алиса")
        dr_meet('dr_us', u"Ульяна")
        dr_meet('dr_un', u"Лена")
        dr_meet('dr_mt', u"Ольга Дмитриевна")
        dr_meet('dr_cs', u"Виола")
        dr_meet('dr_dreamgirl', u"Харон")
        dr_meet('dr_el', u"Электроник")
        dr_meet('dr_pi', u"Пионер")
        dr_meet('dr_sh', u"Шурик")
        dr_meet('dr_uv', u"Харон")
        dr_meet('dr_chat', u'Друг')
        dr_meet('dr_mother', u"Мама")
        dr_meet('dr_ami', u"Девушка")
        dr_meet('dr_ai', u'Искин')
        dr_meet('dr_os', u'Олег Степанович')
        dr_meet('dr_med', u'Доктор')
        dr_meet('dr_guard', u'Охранник')


    dr_forgeteveryone()
    name_sch(u"Я")
    dr_mode_adv()
    dr_reload_names()

# init 2:
#     $ iv = Character(what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000", what_italic = True) #TODO перевести в nvl и упорядочить звёздочку /// + добавить префикс и суффикс
#     #$ chat = Character(u"Собеседник", color="#6e3961", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
#     #$ mother = Character(u"Мама", color="#f9106b", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
#     #$ ami = Character(u"Амина", color="#cd6c2e", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

#     #Day - базис
#     #Sunset - 94%, 82%, 100%
#     #Night - 58%, 67%, 67%
#     #Prologue - 84%, 72%, 100%
#     #RGBA



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
    #def sources_dr(file):
    #    return dr_path+"source/%s" % (file)
    config_session = False


    # Я ХЗ, какой извращенец будет ставить мой мод на 6.16 или 6.18. Оно не заработает! (95%)
    if renpy.version (tuple = False) == "Ren'Py 6.16.3.502":
        dr_path = "deserved_reality/"

    elif (renpy.version (tuple = False) == "Ren'Py 6.18.3.761") or (persistent.nonsteam_dr == True):
        dr_path = "deserved_reality/"

    else: # Так что это фактически единственная нормальная часть этого кода
        if renpy.mobile:
            dr_path = "deserved_reality/"
        else:
            dr_path = "mods/deserved_reality/" # изменить на выходе

    dr_source = dr_path + "source/"

    # def dr_image(file):
    #     return dr_source + "images/%s" % (file)

    # def dr_music(file):
    #     return dr_source + "sounds/music/%s" % (file)

    # def dr_ambience(file):
    #     return dr_source + "sounds/ambience/%s" % (file)

    # def dr_sfx(file):
    #     return dr_source + "sounds/sfx/%s" % (file)

    def dr_video(file):
        return dr_source + "images/video/%s" % (file)

    def dr_menu(file):
        return dr_source + "images/gui/menu/%s" % (file)

    def dr_gui(file):
        return dr_source + "images/gui/%s" % (file)

    def dr_fonts(file):
        return dr_source + "images/fonts/%s" % (file)

    def dr_maps(file):
        return dr_source + "images/maps/%s" % (file)


# Стили

init -998 python:

    style.dr_keys_undefined = Style(style.default)
    style.dr_keys_undefined.font = dr_csn

    # дефолт
    style.dr_keys = Style(style.dr_keys_undefined)
    style.dr_keys.color = "#000000"
    style.dr_keys.hover_color = "#800000"
    style.dr_keys.size = 83

    # Реверсивные, другой шрифт
    style.dr_keys_reversed = Style(style.dr_keys)
    style.dr_keys_reversed.color = "#800000"
    style.dr_keys_reversed.hover_color = "#000000"
    style.dr_keys_reversed.font = dr_font

    # белые
    style.dr_keys_white = Style(style.dr_keys) # Объявление
    style.dr_keys_white.color = "#ffffff" # Цвет текста
    style.dr_keys_white.hover_color = "#800000"

    # белые с определённым размером
    style.dr_desc = Style(style.dr_keys_white)
    style.dr_desc.size = 80

    style.dr_fuchsia = Style(style.default)
    style.dr_fuchsia.font = dr_roboto
    style.dr_fuchsia.size = 36

    style.dr_keys_gray = Style(style.dr_keys_undefined)
    style.dr_keys_gray.color = "#a6a6a6"
    style.dr_keys_gray.hover_color = "#a6a6a6"
    style.dr_keys_gray.size = 83


    #style.base_font = Style(style.default)
    #style.base_font.font  = main_font
    #style.base_font.size = 28
    #style.base_font.line_spacing = 2

    #style.settings_link = Style(style.base_font)
    #style.settings_link.font  = link_font
    #style.settings_link.size = 60
    #style.settings_link.kerning = 3
    #style.settings_link.color = "#909ca3"
    #style.settings_link.hover_color = "#ffffff"
    #style.settings_link.selected_color = "#909ca3"
    #style.settings_link.selected_idle_color = "#909ca3"
    #style.settings_link.selected_hover_color = "#ffffff"
    #style.settings_link.insensitive_color = "#909ca3"

init python: # скомунизженно прямиком с сайта доки Ренпая
        import math

        class Shaker(object):

            anchors = {
                "top" : 0.0,
                "center" : 0.5,
                "bottom" : 1.0,
                "left" : 0.0,
                "right" : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to integers
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)