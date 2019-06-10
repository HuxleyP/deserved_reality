init 999999999:
    $ config.developer = True #TODO В релиз попасть не должно
    $ config.debug_text_overflow = True #это тоже
    $ config.conditionswitch_predict_all = True # и это

init -1: # Version data
    $ sch_version = "7.3"
    $ sch_state = "Alpha rework"
    $ sch_codename = "Arctic Apricot"

init: # Объявляем мод
    $ mods["aaasichium"] = u"Заслуженная {color=#808080}{font=[source_sch]images/fonts/LemonTuesday.otf}|{/font}Реальность{/color}"


init 2:

# Общие

    $ repeated = 0
    $ save_name = "Заслуженная | Реальность."
    $ sch_dayNo = 0

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

    $ sch_bound = False # при всех гудах
    $ sch_true = False # При получении ВЫХОДА к  ТруЪ концовке

    $ sch_hard = False

    if persistent.sch_launched == None:
        $ sch_launch = False
    else:
        $ sch_launch = True


    $ sch_karma_shown = False

    $ sch_WidgetVisible = False

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
        $ persistent.cycled = True # а эта куча строк показывает мои огромные амбиции

    if sch_true:
        $ persistent.sch_karma_shown = True

init 3:
    if sch_launch != True:
        $ persistent.sch_widget = False # Виджет ОП, надо поработать над ним
        $ persistent.sch_music = True # Виджет музыки
        $ persistent.sch_difficulty = False # False для Normal
        $ persistent.undone_jumper = False # Прыгалка на незаконченные руты, при False герой заведомо не будет выходить
        $ persistent.sch_chapter_skip = False # Пропуск глав
        $ persistent.sch_butterfly = False # Режим Бабочки

        # тут типа failsafe, но он какой-то тупой
        $ sch_launch = True
        $ persistent.sch_launched = True # Проверка на запуск, при нём применяются настройки выше и больше не трогаются
    call sch_allvars


# Визуал, аудио, т.д.

init -998:
    image bg_null = Null(1920,1080)
    #BG
    image bg boss_office_sch = image_sch('bg/boss_office_sch.jpg')
    #image bg bus_stop_summer_sch = image_sch("bg/bus_stop_summer.jpg")
    image bg sch_city = im.Scale(image_sch('bg/city.jpg'), 1920, 1080)
    image bg raincity_sch = image_sch('bg/rainycity.jpg')
    image bg int_hospital_storage = image_sch('bg/hospital_storage.png')
    image bg int_bar_sch = im.Scale(image_sch('bg/int_bar.jpg'), 1920, 1080)
    image bg ext_bar_sch = image_sch('bg/ext_bar.jpg')
    image bg ext_cityroad_night_sch = image_sch('bg/ext_cityroad_night_sch.png')
    image bg ext_entrance_night_clear_sch = image_sch("bg/ext_entrance_night_clear_sch.png")
    image bg ext_entrance_night_clear_closed_sch = image_sch("bg/ext_entrance_night_clear_closed_sch.png")
    #image bg earth = im.Grayscale(im.Scale(image_sch("bg/earth.png"), 1920, 1080))
    image bg ext_entrance_night_water_sch = image_sch("bg/ext_enterance_night_water.png")
    image bg underwater = image_sch("bg/underwater.jpg")
    image bg semen_room_night = image_sch("bg/semen_room_night.jpg")
    image bg semen_room_day = image_sch("bg/semen_room_day.png")
    image bg semen_room_sunset = image_sch("bg/semen_room_sunset.png")
    image bg sky_sch = im.Scale(image_sch("bg/sky.jpg"), 1920, 1080)
    image bg night_sky = im.Scale(image_sch('bg/night_sky.jpg'), 1920, 1080)
    image bg int_warehouse_day_sch = image_sch('bg/int_warehouse_day_sch.png')
    image bg ext_warehouse_day_sch = image_sch("bg/ext_warehouse_day_sch.png")
    image bg ext_warehouse_rain_sch = image_sch("bg/ext_warehouse_rain_sch.png")
    image bg ext_warehouse_sunset_sch = image_sch("bg/ext_warehouse_sunset_sch.png")
    image bg ext_warehouse_night_sch = image_sch("bg/ext_warehouse_night_sch.png")
    image bg int_home_lift_sch = image_sch("bg/int_home_lift_sch.png")
    #image bg ext_winterpark = image_sch("bg/ext_winterpark.jpg")
    image bg speaker_room = image_sch('bg/speaker_room.jpg')
    image bg ext_square_rain_day_sch = image_sch('bg/ext_square_rain_day_sch.jpg')
    image bg int_hospital_hall_sch = image_sch('bg/int_hospital_hall_sch.jpg')
    image bg int_hospital_corridor_sch = image_sch('bg/int_hospital_corridor_sch.png')
    image bg ward_sch = image_sch("bg/ward.png")

    image bg citybird = image_sch("bg/citybird.jpg")
    image bg operation_room_sch = image_sch("bg/operation.jpg")
    image bg int_institute_sch = image_sch("bg/int_institute_sch.jpg")
    image bg int_institute_corridor_sch = image_sch("bg/corridor_night.png")
    image bg plain_sch = image_sch("bg/plain.jpg")
    image bg int_coupe_day_sch = image_sch("bg/int_coupe_day.png")
    image bg int_coupe_night_sch = image_sch("bg/int_coupe_night.png")
    image bg doctor_cabinet_sch = Placeholder("bg")

    image dr_sky_day = image_sch('temp/sky_day.png')
    image dr_sky_sunset = image_sch('temp/sky_sunset.png')
    image dr_sky_night = image_sch('temp/sky_night2.jpg')

    #effects
    image raineffect = image_sch("effects/raineffect.png")
    image vignette = image_sch("effects/vignette.png")
    image cricket = image_sch("effects/cricket.jpg")

    #CG
    image cg uvao_d0 = image_sch("cg/uvao_d0.png")
    image cg uvao_d0 = image_sch("cg/d1_uv.jpg")
    image cg uvao_d0_2 = image_sch("cg/d1_uv_2.jpg")

    #gui

    image map_av =  maps_sch('maps/map_avaliable.jpg')
    image map_def =  maps_sch('overlays/map_default_fullhd.png')

    image dr_pattern = gui_sch('pattern.png')

    image fuchsia_case = gui_sch('widget_case.png')

    image day1 = im.Scale(gui_sch('/days/day1.png'), 1920, 1080)
    image day2 = im.Scale(gui_sch('/days/day2.png'), 1920, 1080)
    image day3 = im.Scale(gui_sch('/days/day3.png'), 1920, 1080)
    image day4 = im.Scale(gui_sch('/days/day4.png'), 1920, 1080)
    image day5 = im.Scale(gui_sch('/days/day5.png'), 1920, 1080)
    image day6 = im.Scale(gui_sch('/days/day6.png'), 1920, 1080)
    image day7 = im.Scale(gui_sch('/days/day7.png'), 1920, 1080)

    # Объявляем основные ассеты

    image bg white = "#fff"
    image white2 = "#ffffff"
    image blacksquare = "mods/deserved_reality/source/images/gui/menu/square.png"
    image whitesquare = im.MatrixColor("mods/deserved_reality/source/images/gui/menu/square.png", im.matrix.colorize("#fff", "#fff"))
    image gray = "#171717"
    image beige = "#fbf0b3"
    image yellowish = "#7d5f34"

    # Объявляем текст для анимаций

    # Меню

    image sch_begin = Text("•Продолжить_Игру", style = "sch_keys")
    image sch_continue = Text("•Новая_Игра", style = "sch_keys")
    image sch_settings = Text("•Настройки", style = "sch_keys")
    image sch_achievements = Text("•Достижения", style = "sch_keys")


    #image sch_settings_reversed = Text("•Настройки", style="sch_keys_reversed")

    # Настройки, неактуально из-за нового меню

    #image sch_back_white = Text("/Назад/", style="sch_keys_white", size = 100)

    #image sch_placeholder_off = Text("•Заглушки - OFF", style="sch_keys_white")
    #image sch_placeholder_on = Text("•Заглушки - ON", style="sch_keys_white")

    #image sch_widget_off = Text("•Виджет ОП - OFF", style="sch_keys_white")
    #image sch_widget_on = Text("•Виджет ОП - ON", style="sch_keys_white")

    #image sch_difficulty_hard = Text("•Сложность по умолчанию - Hard", style="sch_keys_white")
    #image sch_difficulty_normal = Text("•Сложность по умолчанию - Обычная", style="sch_keys_white")
    #image sch_difficulty_undefined = Text("•Сложность по умолчанию - не установлена", style="sch_keys_white")

    #image sch_es_settings = Text("•Перейти в настройки игры", style="sch_keys_white")



    # А тут Мику-диджей крутит музыку :3
    # Красочные описания присутствуют
    #Music


    $ aire = music_sch("aire.ogg")
    $ angelalive = music_sch("angelalive.ogg") # Тема Слави

    $ cassiopeia = music_sch("cassiopeia.ogg") # Сон
    $ connor = music_sch("connor.ogg") # технологичная напряжёнка

    $ distant = music_sch("distant.ogg") # пессимистичная
    $ drowninrain = music_sch("drowninrain.ogg") # Дождь
    #$ dust = music_sch("dust.ogg")

    $ faunts = music_sch("faunts.ogg") # стелс
    $ finale = music_sch("finale.ogg") # финалка
    $ followme = music_sch("followme.ogg") # ты пойдёшь со мной?

    $ goodday = music_sch("goodday.ogg") # ежедневка 1

    $ hallways = music_sch("hallways.ogg") # напряжённая
    $ honor = music_sch("honor.ogg") # main menu, ТЫ проиграл
    $ hope = music_sch("hope.ogg") # из меланхолии в надежду

    $ lastdawn = music_sch("lastdawn.ogg") # грустняк
    $ lasvegas = music_sch("lasvegas.ogg") # грустняк 2

    $ markus = music_sch("markus.ogg") # всё скатилось, но есть надежда

    $ nightshow = music_sch("nightshow.ogg") # техно
    $ nullspace = music_sch("nullspace.ogg") # где-то по ту сторону, герой умер?

    $ premonition = music_sch("premonition.ogg") # напряжённая
    $ prologue = music_sch("prologue.ogg") # мажорная мелодия, оптимистичная

    $ regenerate = music_sch("killedthelord.ogg") # надежда

    $ spring = music_sch("spring.ogg") # надежда, которая как бы всё, но ещё не совсем
    $ static = music_sch("static.ogg") # непростая ситуация


    #Ambience
    $ dream = ambience_sch("ambience_safe.ogg")
    $ ambience_elevator = ambience_sch("ambience_elevator")
    $ citynoise = ambience_sch("ambience_citynoise.ogg")

    #SFX
    $ bang = sfx_sch('bang.ogg')
    $ heartbeat = sfx_sch("heartbeat.ogg")
    $ whiteflash = sfx_sch("flash.ogg")
    $ wind = sfx_sch("wind.ogg")
    $ watersplash = sfx_sch("watersplash.ogg")
    $ whisper = sfx_sch('whisper.ogg')
    $ click = sfx_sch('click.ogg')
    $ get_shot = sfx_sch("getshot.ogg")
    $ car_stop = sfx_sch("car_stop.ogg")
    $ surprise = sfx_sch("surprise.ogg")

    #Шрифт
    $ dr_font = fonts_sch("LemonTuesday.otf")
    $ csn = fonts_sch("csn.ttf") # computer says no.
    $ roboto = fonts_sch("Roboto.ttf")



    # Заставки
    $ preroll = video_sch("preroll.webm")



# Плюшки


init:
    # поиграем в красоту
    python:
        def sch_window_hide(pause=True):
            renpy.show_layer_at(sch_screenhide, layer='screens')
            if pause:
                renpy.pause(delay=0.5, hard=True)

        def sch_window_show(pause=True):
            renpy.show_layer_at(sch_screenshow, layer='screens')
            if pause:
                renpy.pause(delay=0.5, hard=True)

    transform sch_screenhide:
        xpos 0.0 ypos 0.0 alpha 1.0
        ease 0.5 xpos 0.0 ypos 0.1 alpha 0.0

    transform sch_screenshow:
        ypos 0.1 alpha 0.0
        ease 0.5 ypos 0.0 alpha 1.0

    #а дальше история умалчивает

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




# старый на всякий
#    transform sch_running:
#        anchor (0.1, 0.1)
#        zoom 1.2
#        ease 0.2 pos (0, 0)
#        ease 0.2 pos(50,50)
#        ease 0.2 pos (0, 0)
#        ease 0.2 pos(-50,50)
#        repeat


    transform sch_running:
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

    transform sch_running_stop:
        ease 0.2 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 # тупа возвращаем всё обратно

    transform sch_menu_ease:
        xpos 2131
        yalign 0.5
        linear 0.5 xpos 1131 yalign 0.5

init python:
    def Noir(id, brightness = -0.4, tint_r = 0.2126, tint_g = 0.7152, tint_b = 0.0722, saturation = 0.5):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) * im.matrix.tint(tint_r, tint_g, tint_b) * im.matrix.saturation(saturation))

    # изменяемый ЧБ
    #def BlackWhite(id, power, brightness = 1.0, saturation = 1.0):
    #    r = power*0.255
    #    g = r
    #    b = r
    #    return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) * im.matrix.tint(r, g, b) * im.matrix.saturation(saturation))

    def BlackWhite(id, saturation):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(saturation))

    def Sepia(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.15) * im.matrix.tint(1.0, .94, .76))

    def NeonSepia(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.15) * im.matrix.tint(.7, .3, .1))

init 10 python: # главы #TODO к херам
    def sch_savename_init(sch_char_name=" "):
        global save_name
        if sch_char_name != " ":
            save_name = (u" Заслуженная | Реальность \n%s ver.%s/; \"%s\":\nПролог %s.") % (sch_state, sch_version, sch_codename, sch_char_name)
        else:
            save_name = (u" Заслуженная | Реальность \n%s ver.%s/; \"%s\":\nПролог.") % (sch_state, sch_version, sch_codename)

    def sch_newday(sch_dayNo):
        #TODO TODO ЦВЕТА С НУЛЯ, НЕ РАБОТАЕТ
        global dr_dv #Алиса
        global dr_un #Лена
        global dr_us #Ульяна
        global dr_sl #Славя
        global dr_iv #ГГ
        global dr_mi #Мику
        global dr_nr #Нуар
        renpy.scene()

        if sch_dayNo >=1 and sch_dayNo <=7:
            renpy.show('day1')
            renpy.transition(fade)
            renpy.pause(3, hard=True)
            renpy.scene()
            renpy.show('black')
            renpy.transition(fade)
        renpy.scene()

        if (sch_dayNo > 1) and (not sch_hard):

            if sch_noir_flag == 1: # сделать проверку на тян
                renpy.show("Color(hsv=(0, 0, 0.4875))")

            elif sch_noir_flag == 2:
                renpy.show("Color(hsv=(0, 0, 0.325))")

            elif sch_noir_flag == 3:
                renpy.show('Color(hsv=(0, 0, 0.1625))')

            elif (max(dr_dv, dr_un, dr_us, dr_sl, dr_mi)  >= 0) and (sch_dayNo <=3): # до 4 дня, очков тян больше нуля,

                if (dr_dv or dr_un or dr_us or dr_sl or dr_iv or dr_mi or dr_nr) == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): #если равно
                    dr_overall = max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr)
                    renpy.show("Color(hsv=(0.9722222, [dr_overall*0.03], 1.0))") #розовый

                elif (max(dr_dv, dr_un, dr_us, dr_sl, dr_mi) >=8): #  больше восьми, saturation = 100, изменяется brightness
                    if dr_us == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): #Уля
                        renpy.show("Color(hsv=(0, [0.5+dr_us*0.04], 1.0))")

                    elif dr_dv == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # Алиса
                        renpy.show("Color(hsv=(.06666, [dr_dv*0.04], 1.0))")

                    elif dr_sl == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # Славя
                        renpy.show("Color(hsv=(.12222, [dr_sl*0.04], 1.0))")

                    elif dr_mt == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # ОД
                        renpy.show("Color(hsv=(.33333, [dr_mt*0.04], 1.0))")

                    elif dr_mi == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # Мику
                        renpy.show("Color(hsv=(.5, [dr_mi*0.04], 1.0))")

                else: # от одного до восьми, brightness = color*0.32, изменяется saturation

                    if dr_us == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): #Уля
                        renpy.show("Color(hsv=(0, 1.0, [0.5+dr_us*0.04]))")

                    elif dr_dv == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # Алиса
                        renpy.show("Color(hsv=(.06666, 1.0, [dr_dv*0.04]))")

                    elif dr_sl == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # Славя
                        renpy.show("Color(hsv=(.12222, 1.0, [dr_sl*0.04]))")

                    elif dr_mt == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # ОД
                        renpy.show("Color(hsv=(.33333, 1.0, [dr_mt*0.04]))")

                    elif dr_mi == max(dr_dv, dr_un, dr_us, dr_sl, dr_iv, dr_mi, dr_nr): # Мику
                        renpy.show("Color(hsv=(.5, 1.0, [dr_mi*0.04]))")
                        
            elif sch_dayNo >=4:
                pass
                #TODO по руттегам, без лого ЗР
            else:
                renpy.show("#a6a6a6") # НЕ РАБОТАЕТ!
            renpy.show('dr_pattern')
            renpy.transition(fade)
            renpy.pause(3, hard=True)
            renpy.scene()
        renpy.show('black')
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


    def sch_chapter(sch_dayNo, sch_ch_name): #dayNo - номер дня (>=8 - пролог), ch_name - название главы,ы, new_day - новый день
        global save_name # название сейва
        global routetag_sch # руттэг
        global sch_chapter_skip
        renpy.fix_rollback()

        save_name = (u"Заслуженная | Реальность") # так надо, иначе ошибка
        if sch_dayNo != 0:
            save_name = (u"Заслуженная | Реальность - День %d.") % (sch_dayNo)
            if sch_ch_name != "":
                save_name = (u"Заслуженная | Реальность - День %d.\n%s.") % (sch_dayNo, sch_ch_name)
        elif sch_dayNo >= 8:
            save_name = (u"Заслуженная | Реальность. \nЭпилог.")


        chapter_name = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color}{/font}") # так надо, иначе ошибка

        if not persistent.sch_chapter_skip:
            #renpy.music.play('deserved_reality/source/sounds/sfx/whisper.ogg', channel='sound', fadein=1.5, fadeout=0.5)
            renpy.scene()
            renpy.show('black')
            renpy.transition(fade)
            renpy.show('day_num', what=Text(chapter_name, xcenter=0.5, ycenter=0.25))
            renpy.transition(fade)
            renpy.pause(1.5)
            renpy.scene()
            renpy.show('bg black')
            renpy.transition(fade)
            dayname = (u"{size=70}{font=[csn]}{color=#afafaf}%s{/color}{/font}{/size}") % (sch_ch_name)
            renpy.show('day_num', what=Text(dayname, xcenter=0.5,ycenter=0.45))
            renpy.pause(1.5)
            renpy.scene()
            renpy.show('bg black')
            renpy.transition(fade)
            renpy.pause(1.25, hard=True)

#Поинты

init python:
    def sch_widget_OP():
        if (u"Заслуженная Реальность" or "Заслуженная | Реальность" in save_name) and persistent.sch_widget:
            renpy.show_screen('sch_fuchsia_widget')
        else:
            renpy.hide_screen('sch_fuchsia_widget')
        config.overlay_functions.append(sch_widget_OP) #добавление виджета

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
    store.dr_names_list.append('ai')#Собеседник, ИИ
    dr_names['dr_ai'] = 'ИИ'

    dr_colors['dr_chat'] = {'night': (64, 38, 65, 255), 'sunset': (103, 47, 97, 255), 'day': (110, 57, 97, 255), 'prolog': (92, 41, 97, 255)} #rgb(110, 57, 97)
    store.dr_names_list.append('chat')#Собеседник
    dr_names['dr_chat'] = 'Собеседник'

    dr_colors['dr_mother'] = {'night': (144, 11, 72, 255), 'sunset': (234, 13, 107, 255), 'day': (249, 16, 107, 255), 'prolog': (209, 12, 107, 255)}
    store.dr_names_list.append('mother')#Мама
    dr_names['dr_mother'] = "Мама"

    dr_colors['dr_ami'] = {'night': (119, 72, 31, 255), 'sunset': (193, 89, 46, 255), 'day': (205, 108, 46, 255), 'prolog': (172, 78, 46, 255)}
    store.dr_names_list.append('ami')#Амина
    dr_names['dr_ami'] = "Амина"

    dr_colors['dr_os'] = {'night': (26, 215, 14, 255), 'sunset': (26, 215, 14, 255), 'day': (26, 215, 14, 255), 'prolog': (26, 215, 14, 255)}
    store.dr_names_list.append('os')#Олег Степанович
    dr_names['dr_os'] = "Олег Степанович"

    dr_colors['dr_med'] = {'night': (210, 182, 72, 255), 'sunset': (210, 182, 72, 255), 'day': (210, 182, 72, 255), 'prolog': (210, 182, 72, 255)}
    store.dr_names_list.append('med')#Доктор
    dr_names['dr_med'] = "Доктор"

    dr_colors['dr_guard'] = {'night': (2, 73, 138, 255), 'sunset': (2, 73, 138, 255), 'day': (2, 73, 138, 255), 'prolog': (2, 73, 138, 255)}
    store.dr_names_list.append('guard')#охранник
    dr_names['dr_guard'] = "Охранник"

    def name_sch(dr_name): #args - me - Я, pr - Протагонист, iv - Иван, van - Ваня
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

        reload_names()

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
    set_mode_adv()
    reload_names()



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



# init 2:
#     $ iv = Character(what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000", what_italic = True) #TODO перевести в nvl и упорядочить звёздочку /// + добавить префикс и суффикс
#     #$ chat = Character(u'Собеседник', color="#6e3961", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
#     #$ mother = Character(u'Мама', color="#f9106b", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
#     #$ ami = Character(u'Амина', color="#cd6c2e", what_color="#E2C778", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

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
    #def sources_sch(file):
    #    return sch_path+"source/%s" % (file)
    config_session = False

    if renpy.version (tuple = False) == "Ren'Py 6.16.3.502":
        sch_path = 'mods/deserved_reality/'

    elif (renpy.version (tuple = False) == "Ren'Py 6.18.3.761") or (persistent.nonsteam_sch == True):
        sch_path = 'mods/deserved_reality/'

    else:
        if renpy.mobile:
            sch_path = "mods/deserved_reality/"
        else:
            sch_path = "mods/deserved_reality/" # изменить на выходе

    source_sch = sch_path + "source/"

    def image_sch(file):
        return source_sch + "images/%s" % (file)

    def music_sch(file):
        return source_sch + "sounds/music/%s" % (file)

    def ambience_sch(file):
        return source_sch + "sounds/ambience/%s" % (file)

    def sfx_sch(file):
        return source_sch + "sounds/sfx/%s" % (file)

    def video_sch(file):
        return source_sch + "images/video/%s" % (file)

    def menu_sch(file):
        return source_sch + "images/gui/menu/%s" % (file)

    def gui_sch(file):
        return source_sch + "images/gui/%s" % (file)

    def fonts_sch(file):
        return source_sch + "images/fonts/%s" % (file)

    def maps_sch(file):
        return source_sch + "images/maps/%s" % (file)


# Стили

init -998 python:

    style.sch_keys_undefined = Style(style.default)
    style.sch_keys_undefined.font = csn

    # дефолт
    style.sch_keys = Style(style.sch_keys_undefined)
    style.sch_keys.color = "#000000"
    style.sch_keys.hover_color = "#800000"
    style.sch_keys.size = 83

    # Реверсивные, другой шрифт
    style.sch_keys_reversed = Style(style.sch_keys)
    style.sch_keys_reversed.color = "#800000"
    style.sch_keys_reversed.hover_color = "#000000"
    style.sch_keys_reversed.font = dr_font

    # белые
    style.sch_keys_white = Style(style.sch_keys) # Объявление
    style.sch_keys_white.color = "#ffffff" # Цвет текста

    # белые с определённым размером
    style.sch_desc = Style(style.sch_keys_white)
    style.sch_desc.size = 80

    style.sch_fuchsia = Style(style.default)
    style.sch_fuchsia.font = roboto
    style.sch_fuchsia.size = 36

    style.sch_keys_gray = Style(style.sch_keys_undefined)
    style.sch_keys_gray.color = "#a6a6a6"
    style.sch_keys_gray.hover_color = "#a6a6a6"
    style.sch_keys_gray.size = 83


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
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
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

