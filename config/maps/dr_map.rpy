# Карта слизана с 7ДЛ чуть более, чем полностью, но я всё равно умудрился накосячить

# отключение чибиков - непонятно, зачем в этом месте - слишком рано.
init -1001 python:
    def disable_all_chibi_dr():
        global global_zones_dr
        for name,data in global_zones_dr.iteritems():
            data["map_chibi"] = None


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
#     дополнительно добавлены РАЗДЕЛЬНЫЕ локации спорткомплекса и клубов.
#     (можно разделить еще спортзал и футбол, но надо перекрасить душевые на _avaliable и _selected картинках)

init -996 python:
    store.map_zones_dr = {
            "un_mi_house_dr":   {"position":[659,312,692,352],"default_bg":bg_tmp_image(u"Лена и Мику")},
            "me_mt_house_dr":   {"position":[785,334,819,374],"default_bg":bg_tmp_image(u"Мой домик")},
            "sl_mz_house_dr":   {"position":[837,396,870,438],"default_bg":bg_tmp_image(u"Славя и Женя")},
            "estrade_dr":       {"position":[870,234,939,306],"default_bg":bg_tmp_image(u"Эстрада")},
            "el_sh_house_dr":   {"position":[693,425,721,465],"default_bg":bg_tmp_image(u"Эл и Шурик")},
            "music_club_dr":    {"position":[509,400,568,468],"default_bg":bg_tmp_image(u"Музклуб")},
            "admin_house_dr":   {"position":[632,479,715,560],"default_bg":bg_tmp_image(u"Админкорпус")},
            "wash_house_dr":    {"position":[1061,292,1118,324],"default_bg":bg_tmp_image(u"Баня")},
            "square_dr":        {"position":[723,490,818,646],"default_bg":bg_tmp_image(u"Площадь")},
            "dining_hall_dr":   {"position":[825,565,934,671],"default_bg":bg_tmp_image(u"Столовая")},
            "dv_us_house_dr":   {"position":[582,698,622,740],"default_bg":bg_tmp_image(u"Алиса и Ульяна")},
            "store_house_dr":   {"position":[939,591,992,671],"default_bg":bg_tmp_image(u"Склад")},
            "cape_dr":          {"position":[1211,948,1328,1070],"default_bg":bg_tmp_image(u"Мыс")},
            "sport_area_dr":    {"position":[1000,508,1293,732],"default_bg":bg_tmp_image(u"Спорткомплекс")},
            "beach_dr":         {"position":[976,746,1222,871],"default_bg":bg_tmp_image(u"Пляж")},
            "boat_station_dr":  {"position":[679,849,781,892],"default_bg":bg_tmp_image(u"Лодочный причал")},
            "old_house_dr":     {"position":[8,1019,88,1071],"default_bg":bg_tmp_image(u"Старый корпус")},
            "clubs_dr":         {"position":[354,554,531,688],"default_bg":bg_tmp_image(u"Клубы")},
            "library_dr":       {"position":[953,416,1052,485],"default_bg":bg_tmp_image(u"Библиотека")},
            "sandpit_dr":       {"position":[1728,463,1918,721],"default_bg":bg_tmp_image(u"Карьер")},
            "medic_house_dr":   {"position":[853,486,931,557],"default_bg":bg_tmp_image(u"Медпункт")},
            "camp_entrance_dr": {"position":[229,554,333,645],"default_bg":bg_tmp_image(u"Остановка автобуса")},
            "forest_dr":        {"position":[454,275,538,324],"default_bg":bg_tmp_image(u"Умывальники")},
            "islaone_dr":       {"position":[453,960,706,1076],"default_bg":bg_tmp_image(u"о. Ближний")},
            "islatwo_dr":       {"position":[711,992,1084,1077],"default_bg":bg_tmp_image(u"о. Длинный")},
            "lake_dr":          {"position":[74,27,223,148],"default_bg":bg_tmp_image(u"Озеро")},
            "meadow_dr":        {"position":[297,991,405,1079],"default_bg":bg_tmp_image(u"Луг")},
            "campfire_dr":      {"position":[1501,970,1673,1072],"default_bg":bg_tmp_image(u"Костровая поляна")},
# раздельные локации спорткомплекса и клубов
            "sports_hall_dr":   {"position":[1082,584,1290,732],"default_bg":bg_tmp_image(u"Спортзал и футбольное поле")},
            "volleyball_dr":    {"position":[999,593,1079,685],"default_bg":bg_tmp_image(u"Воллейбольная площадка")},
            "court_dr":         {"position":[1107,509,1176,576],"default_bg":bg_tmp_image(u"Теннисный корт")},
            "kyber_club_dr":    {"position":[354,608,461,687],"default_bg":bg_tmp_image(u"Клуб кибернетиков")},

    }

# Определяем новый класс нашей карты (сборка кода из mapclass.rpy и pyclasses.rpy оригинала )

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
        # Своя фигня TODO
        #def set_decale(self,name,decale):
        #    if  decale in self.decale:
        #        global_zones_dr[name]["decale"] = self.decale[decale]
        #    else:
        #        global_zones_dr[name]["decale"] = None
        #def reset_decale(self,name):
        #    self.set_decale(name, "")
        #конец
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
            if renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
                if not not_in_rollback_or_fast_forward():
                    renpy.log("renpy.roll_forward_info()")
                    renpy.config.skipping = False
                    renpy.game.after_rollback = False
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
                            im.Crop(self.pics["selected_dr"], pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]), # добавляем сюда суффикс, и в dr_store тоже
                            clicked = renpy.curry(self.zoneclick)(name),
                            xpos = pos[0],
                            ypos = pos[1]
                        )
                        if  data["chibi"] != None:
                            chibi_scale = im.Scale(data["chibi"],40,40) # масштабируем картинку чибика до нужного размера (напр. 40х40 пикс)
                            ui.imagebutton(
                                anim.Blink(chibi_scale), #показываем с измененным размером
                                anim.Blink(chibi_scale),
                                clicked = renpy.curry(self.zoneclick)(name),
                                xpos = pos[0],
                                ypos = pos[1]
                            )
                        #if data["decale"] != None: # тоже своё TODO
                        #    decale_final = data["chibi"]
                        #    ui.imagebutton(
                        #        clicked = renpy.curry(self,zoneclick)(name),
                        #        xpos = pos[0]
                        #        ypos = pos[1]
                        #    )
                ui.close()

# … и создаем новый объект класса
    store.map_dr = Map_dr(store.map_pics_dr, store.map_chibi, default)

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
    if not config_session:
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
        # Мои бесполезные попытки
        #def set_decale_dr(name,decale):
        #    store.map_dr.set_decale(name,decale)
        #def reset_decale_dr(name):
        #    store.map.dr.reset_decale(name)

# определяем подосновы нашей карты (widget и bg) - собственно, подоснова карты:

init 5:
    if not config_session:
        image widget map_dr = dr_gui("maps/dr_bg.png")
        image bg map_dr = dr_gui("maps/dr_bg.png")

# еще раз отключаем чибиков

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
