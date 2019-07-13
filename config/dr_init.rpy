init 999999999:
    $ config.developer = True #TODO В релиз попасть не должно
    $ config.debug_text_overflow = True #это тоже
    $ config.conditionswitch_predict_all = True # и это

init -1: # Version data
    $ dr_version = "7.4.1"
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


    # #effects
    # image raineffect = dr_image("effects/raineffect.png")
    # image vignette = dr_image("effects/vignette.png")
    # image cricket = dr_image("effects/cricket.jpg")

    # #CG
    # image cg uvao_d0 = dr_image("cg/uvao_d0.png")
    # image cg uvao_d0 = dr_image("cg/d1_uv.jpg")
    # image cg uvao_d0_2 = dr_image("cg/d1_uv_2.jpg")

    #image dr_sky_day = dr_image("temp/sky_day.png")
    #image dr_sky_sunset = dr_image("temp/sky_sunset.png")
    #image dr_sky_night = dr_image("temp/sky_night2.jpg")

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

    image dr_white = "#fff"
    image dr_white2 = "#ffffff"
    image dr_blacksquare = dr_menu("blacksquare.png")
    image dr_whitesquare = im.MatrixColor(dr_menu("blacksquare.png"), im.matrix.colorize("#fff", "#fff"))
    image dr_gray = "#171717"
    image dr_beige = "#fbf0b3"
    image dr_yellowish = "#7d5f34"
    image dr_exit_idle = dr_menu("ButtonExit_idle.png")


    image intro_noir_screen = dr_gui("noir_chosen1.png")
    image intro_limb_screen = dr_gui("limb_chosen1.png")

    # Объявляем текст для анимаций

    # Меню

    image dr_begin = Text("•Продолжить_Игру", style = "dr_keys")
    image dr_continue = Text("•Новая_Игра", style = "dr_keys")
    image dr_settings = Text("•Настройки", style = "dr_keys")
    image dr_achievements = Text("•Достижения", style = "dr_keys")
    image dr_logo = Text("{size=150}Заслуженная{/size}\n  {size=120}Реальность{/color}", style="dr_keys")


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
        def hpause(t=None):
            if t !=None:
                renpy.pause(t, hard=True)
            else:
                renpy.pause(hard=True) #А что будет если?...

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



    transform dr_ease_left_away:
        ease 1.0 xalign -0.5

    transform dr_ease_right_away:
        ease 1.0 xalign 1.5

    transform dr_ease_down_away:
        ease 1.0 yalign -1.0

    image dr_main_menu_atl:
        "dr_white2" with Dissolve(0.5)
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
        global save_name
        save_name = "Заслуженная Реальность. День [dr_dayNo]"
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
            dr_path = "deserved_reality/" # изменить на выходе

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


init python:
    dr_ambience = {}
    dr_music = {}
    dr_sfx = {}

    for i in renpy.list_files():
        if i.startswith(("deserved_reality/source/images/bg/", "deserved_reality/source/images/cg/")) and i.endswith((".png", ".jpg")):
            renpy.image((str(i)[34:-4]), i)

        if i.startswith(("deserved_reality/source/sounds/ambience/")) and i.endswith((".ogg")):
            dr_ambience[i[40:-4]] = i

        if i.startswith(("deserved_reality/source/sounds/music/")) and i.endswith((".ogg")):
            dr_music[i[37:-4]] = i

        if i.startswith(("deserved_reality/source/sounds/sfx/")) and i.endswith((".ogg")):
            dr_sfx[i[35:-4]] = i

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


# ДЕБАААААААААААААААААААААААААААААААААААГИНГ ЛЮБИМЫЙ РОДНОЙ ПИЗДЕЦ КАКОЙ

python early: # переписать
    def CycleCounter():
        def editoverlay():
            ui.button(clicked=None, xalign=0.5, yalign = 0.98, xpadding=6)
            ui.text(save_name, style="button_text", size=13, color="ff32000")

        config.overlay_functions.append(editoverlay)