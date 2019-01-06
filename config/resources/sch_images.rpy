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
    $ click = sfx_sch('click.ogg')

    #Шрифт
    $ dr_font = fonts_sch("LemonTuesday.otf")
    $ csn = fonts_sch("csn.ttf") # computer says no.



    # Заставки
    $ preroll = video_sch("preroll.webm")
