# ВЗЯТО ИЗ 7ДЛ
# Ко всем идентификаторам добавляем суффикс "_dr" ; этот же суффикс используем в описаниях дней

# отключение чибиков
init -1001 python:
    def disable_all_chibi_dr():
        global global_zones_dr
        for name,data in global_zones_dr.iteritems():
            data["map_chibi_dr"] = None


# Определяем источник изображений для картоосновы:
#    bgpic = "подложка"; avaliable = "доступно для выбора"; selected = "наведен курсор"

init -997 python:
    store.map_pics_dr = {
        "bgpic_dr": dr_gui("maps/map_bg.png"),
        "avaliable_dr": dr_gui("maps/map_avaliable.png"),
        "selected_dr": dr_gui("maps/map_selected.png")
    }


    
    store.map_chibi_dr = {
        "?" : dr_maps("chibi/map_icon_n00.png"),
        "me": dr_maps("chibi/map_icon_n01.png"),
        "mi": dr_maps("chibi/map_icon_n02.png"),
        "sh": dr_maps("chibi/map_icon_n03.png"),
        "el": dr_maps("chibi/map_icon_n04.png"),
        "mz": dr_maps("chibi/map_icon_n05.png"),
        "mt": dr_maps("chibi/map_icon_n06.png"),
        "uv": dr_maps("chibi/map_icon_n07.png"),
        "un": dr_maps("chibi/map_icon_n08.png"),
        "us": dr_maps("chibi/map_icon_n09.png"),
        "dv": dr_maps("chibi/map_icon_n10.png"),
        "sl": dr_maps("chibi/map_icon_n11.png"),
        "cs": dr_maps("chibi/map_icon_n12.png"),
    }

    #store.map_decale_dr = {
    #    "catacombs1": im.Scale(dr_maps("overlays/catacombs-1.png"), 1920, 1080)
    #    "catacombs2": im.Scale(dr_maps("overlays/catacombs-2.png"), 1920, 1080)
    #    "catacombs12": im.Scale(dr_maps("overlays/catacombs-12.png"), 1920, 1080)
    #    "catacombs13": im.Scale(dr_maps("overlays/catacombs-13.png"), 1920, 1080)
    #    "catacombs124": im.Scale(dr_maps("overlays/catacombs-124.png"), 1920, 1080)
    #    "noir-cat1": im.Scale(dr_maps("overlays/noir-cat1.png"), 1920, 1080)
    #    "noir-cat2": im.Scale(dr_maps("overlays/noir-cat2.png"), 1920, 1080)
    #    "noir-cat3": im.Scale(dr_maps("overlays/noir-cat3.png"), 1920, 1080)
    #    "map_default": im.Scale(dr_maps("overlays/map_default.png"), 1920, 1080)
    #    "note-FFR": im.Scale(dr_maps("overlays/map_frontForestRoute.png"), 1920, 1080)
    #    "note-FFRN-in": im.Scale(dr_maps("overlays/maps_frontForestRouteNoteIn.png"), 1920, 1080)
    #    "note-FFRN-out": im.Scale(dr_maps("overlays/maps_frontForestRouteNoteOut.png"), 1920, 1080)
    #    "noir-note-clubs": im.Scale(dr_maps("overlays/noir_note-clubs.png"), 1920, 1080)
    #    "noir-note-forest": im.Scale(dr_maps("overlays/noir_note-forest.png"), 1920, 1080)
    #    "noir-note-infroad": im.Scale(dr_maps("overlays/noir_note-infiniteRoad.png"), 1920, 1080)
    #    "noir-note-infroute": im.Scale(dr_maps("overlays/noir_note-infiniteRoute.png"), 1920, 1080)
    #    "noir-note-island": im.Scale(dr_maps("overlays/noir_note-island.png"), 1920, 1080)
    #}

# Определяем ключи и координаты локаций данной карты:
#     ключи и координаты взяты из файла классики media.rpy
#     дополнительно добавлены из файла мода alt_script.rpy

init -996 python:
    store.map_zones_dr = {
# зоны, определенные в классике
            "me_mt_house_dr":   {"position":[960,178,992,227],"default_bg":bg_tmp_image(u"Мой домик")},
            "estrade_dr":       {"position":[1062,54,1154,135],"default_bg":bg_tmp_image(u"Эстрада")},
            "music_club_dr":    {"position":[627,255,692,337],"default_bg":bg_tmp_image(u"Музклуб")},
            "square_dr":        {"position":[887,360,998,545],"default_bg":bg_tmp_image(u"Площадь")},
            "dining_hall_dr":   {"position":[1010,458,1140,581],"default_bg":bg_tmp_image(u"Столовая")},
            "sport_area_dr":    {"position":[1220,481,1574,658],"default_bg":bg_tmp_image(u"Спорткомплекс")},
            "beach_dr":         {"position":[1198,674,1488,831],"default_bg":bg_tmp_image(u"Пляж")},
            "boat_station_dr":  {"position":[832,801,957,855],"default_bg":bg_tmp_image(u"Лодочный причал")},
            "clubs_dr":         {"position":[437,437,647,597],"default_bg":bg_tmp_image(u"Клубы")},
            "library_dr":       {"position":[1158,271,1285,357],"default_bg":bg_tmp_image(u"Библиотека")},
            "medic_house_dr":   {"position":[1042,357,1138,444],"default_bg":bg_tmp_image(u"Медпункт")},
            "camp_entrance_dr": {"position":[284,440,412,554],"default_bg":bg_tmp_image(u"Ворота в лагерь")},
            "forest_dr":        {"position":[562,50,690,188],"default_bg":bg_tmp_image(u"о. Лес")},
# зоны, определенные в моде
            "un_mi_house_dr":  {"position":[811,154,848,195],"default_bg":bg_tmp_image(u"Лена и Мику")},
            "sl_mz_house_dr":  {"position":[1027,257,1058,300],"default_bg":bg_tmp_image(u"Славя и Женя")},
            "el_sh_house_dr":  {"position":[854,292,884,331],"default_bg":bg_tmp_image(u"Эл и Шурик")},
            "dv_us_house_dr":  {"position":[717,624,758,670],"default_bg":bg_tmp_image(u"Алиса и Ульяна")},
            "shed_dr":         {"position":[1144,488,1211,584],"default_bg":bg_tmp_image(u"Склад")},
            "admin_house_dr":  {"position":[775,350,875,447],"default_bg":bg_tmp_image(u"Администрация")},
            "old_house_dr":    {"position":[238,1005,340,1071],"default_bg":bg_tmp_image(u"Старый корпус")}

    }

# Определяем новый класс нашей карты (сборка кода из mapclass.rpy и pyclasses.rpy оригинала)

init -51 python:
    global_map_result_dr="error"

    def init_map_zones_realization_dr(zones_dr,default):
        global global_zones_dr
        global_zones_dr=zones_dr
        for i,data in global_zones_dr.iteritems():
            data["chibi"] = None
            data["label"] = default
            data["avaliable"] = True
            data["been_here"] = 0

    class Map_dr(renpy.Displayable): 
        def __init__(self,pics,chibi,default):
            renpy.Displayable.__init__(self)
            self.pics=pics
            self.chibi=chibi
            self.default=default
            config.overlay_functions.append(self.overlay)

        def disable_all_zones(self):
            global global_zones_dr
            for name,data in global_zones_dr.iteritems():
                data["label"] = self.default
                data["avaliable"] = False
                data["been_here"] = 0
        def enable_all_zones(self):
            global global_zones_dr
            for name,data in global_zones_dr.iteritems():
                data["label"] = self.default
                data["avaliable"] = True
                data["been_here"] = 0
        def set_zone(self,name,label):
            global global_zones_dr
            global_zones_dr[name]["label"] = label
            global_zones_dr[name]["avaliable"] = True
        def reset_zone(self,name):
            global global_zones_dr
            global_zones_dr[name]["label"] = self.default
            global_zones_dr[name]["avaliable"] = False
            global_zones_dr[name]["been_here"] = 0
        def enable_empty_zone(self,name):
            global global_zones_dr
            self.set_zone(name,self.default)
            global_zones_dr[name]["avaliable"] = True
        def reset_current_zone(self):
            self.enable_empty_zone(global_map_result_dr)
        def disable_current_zone(self):
            global global_zones_dr
            global_zones_dr[global_map_result_dr]["avaliable"] = False
        def been_there(self):
            global global_zones_dr
            return global_zones_dr[global_map_result_dr]["been_here"]
        def set_chibi(self,name,ch):
            global global_zones_dr
            if  ch in self.chibi:
                global_zones_dr[name]["chibi"] = self.chibi[ch]
            else:
                global_zones_dr[name]["chibi"] = None
        def reset_chibi(self,name):
            self.set_chibi(name,"")
        def event(self, ev, x, y, st):
            return
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)
        def zoneclick(self,name):
            global global_zones_dr
            global global_map_result_dr
            store.map_enabled_dr=False
            renpy.scene('mapoverlay')
            global_zones_dr[name]["been_here"] += 1
            global_map_result_dr = name
            renpy.scene()
            ui.jumps(global_zones_dr[name]["label"])()
        def overlay(self):
            if  store.map_enabled_dr:
                global global_zones_dr
                renpy.scene('mapoverlay')
                ui.layer('mapoverlay')
                for name,data in global_zones_dr.iteritems():
                    if data["avaliable"]:
                        pos = data["position"]
                        ui.imagebutton(
                            im.Crop(self.pics["avaliable_dr"],pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]),
                            im.Crop(self.pics["selected_dr"], pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]), # добавляем сюда суффикс, и в альт_сторе тоже
                            clicked = renpy.curry(self.zoneclick)(name),
                            xpos = pos[0],
                            ypos = pos[1]
                        )
                        if  data["chibi"] != None:
                            ui.imagebutton(
                                anim.Blink(data["chibi"]),
                                anim.Blink(data["chibi"]),
                                clicked = renpy.curry(self.zoneclick)(name),
                                xpos = pos[0],
                                ypos = pos[1]
                            )
                ui.close()

# … и создаем новый объект класса
    store.map_dr = Map_dr(store.map_pics_dr, store.map_chibi_dr, default) 

# Ниже кусок из pyclasses.rpy; возможно, есть и лишние строки - но без этого карта работать отказывалась
    import pygame
    import os
    import os.path
    from renpy.store import *
    from renpy.display.im import ImageBase, image, cache, Composite

    store.map_enabled_dr = False
    store.map_enabled_dr_tmp = False
    def disable_stuff():
        store.map_enabled_dr_tmp = store.map_enabled_dr_tmp or store.map_enabled_dr
        store.map_enabled_dr = False
    def enable_stuff():
        store.map_enabled_dr = store.map_enabled_dr_tmp
        store.map_enabled_dr_tmp = False

# инициализируем функции по методам вновь созданного класса

init 5 python:
    import renpy.store as store 
    if  not config_session:

        def disable_all_zones_dr():
            store.map_dr.disable_all_zones()
        def enable_all_zones_dr():
            store.map_dr.enable_all_zones()
        def set_zone_dr(name,label):
            store.map_dr.set_zone(name,label)
        def reset_zone_dr(name):
            store.map_dr.reset_zone(name)
        def enable_empty_zone_dr(name):
            store.map_dr.enable_empty_zone(name)
        def reset_current_zone_dr():
            store.map_dr.reset_current_zone()
        def disable_current_zone_dr():
            store.map_dr.disable_current_zone()
        def been_there_dr():
            return store.map_dr.been_there()
        def set_chibi_dr(name,ch):
            store.map_dr.set_chibi(name,ch)
        def reset_chibi_dr(name):
            store.map_dr.reset_chibi(name)
        def show_map_dr():
            ui.jumps("_show_map_dr")()
        def init_map_zones_dr():
            init_map_zones_realization_dr(store.map_zones_dr,"nothing_here")

# определяем подосновы нашей карты (widget и bg) - собственно, подоснова карты:

init 5:
    if not config_session:
        image widget map_dr = dr_gui("maps/map_bg.png")
        image bg map_dr = dr_gui("maps/map_bg.png")

init 52 python:
    def disable_all_chibi_dr():
        global global_zones_dr
        for name,data in global_zones_dr.iteritems():
            data["chibi"] = None

# инициализация зон карты должна проводиться один раз, при старте

# ну и собственно - выводим нашу карту на экран, любуемся ею и ждем-с нажатия мыша.

label _show_map_dr:
    scene widget map_dr
    $ store.map_enabled_dr = True #
    $ ui.interact()
    jump _show_map_dr
