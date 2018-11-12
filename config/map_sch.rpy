

# отключение чибиков - непонятно, зачем в этом месте - слишком рано.
init -1001 python:
    def disable_all_chibi_sch():
        global global_zones_sch
        for name,data in global_zones_sch.iteritems():
            data["map_chibi"] = None


# Определяем источник изображений для картоосновы:
#    bgpic = "подложка"; avaliable = "доступно для выбора"; selected = "наведен курсор"

init -997 python:
    store.map_pics_sch = {
        "bgpic_sch": gui_sch("maps/map_bg.png"),
        "avaliable_sch": gui_sch("mps/map_avaliable.png"),
        "selected_sch": gui_sch("maps/map_selected.png")
    }

# Определяем ключи и координаты локаций данной карты:
#     дополнительно добавлены РАЗДЕЛЬНЫЕ локации спорткомплекса и клубов.
#     (можно разделить еще спортзал и футбол, но надо перекрасить душевые на _avaliable и _selected картинках)

init -996 python:
    store.map_zones_sch = {
            "un_mi_house_sch":   {"position":[659,312,692,352],"default_bg":bg_tmp_image(u"Лена и Мику")},
            "me_mt_house_sch":   {"position":[785,334,819,374],"default_bg":bg_tmp_image(u"Мой домик")},
            "sl_mz_house_sch":   {"position":[837,396,870,438],"default_bg":bg_tmp_image(u"Славя и Женя")},
            "estrade_sch":       {"position":[870,234,939,306],"default_bg":bg_tmp_image(u"Эстрада")},
            "el_sh_house_sch":   {"position":[693,425,721,465],"default_bg":bg_tmp_image(u"Эл и Шурик")},
            "music_club_sch":    {"position":[509,400,568,468],"default_bg":bg_tmp_image(u"Музклуб")},
            "admin_house_sch":   {"position":[632,479,715,560],"default_bg":bg_tmp_image(u"Админкорпус")},
            "wash_house_sch":    {"position":[1061,292,1118,324],"default_bg":bg_tmp_image(u"Баня")},
            "square_sch":        {"position":[723,490,818,646],"default_bg":bg_tmp_image(u"Площадь")},
            "dining_hall_sch":   {"position":[825,565,934,671],"default_bg":bg_tmp_image(u"Столовая")},
            "dv_us_house_sch":   {"position":[582,698,622,740],"default_bg":bg_tmp_image(u"Алиса и Ульяна")},
            "store_house_sch":   {"position":[939,591,992,671],"default_bg":bg_tmp_image(u"Склад")},
            "cape_sch":          {"position":[1211,948,1328,1070],"default_bg":bg_tmp_image(u"Мыс")},
            "sport_area_sch":    {"position":[1000,508,1293,732],"default_bg":bg_tmp_image(u"Спорткомплекс")},
            "beach_sch":         {"position":[976,746,1222,871],"default_bg":bg_tmp_image(u"Пляж")},
            "boat_station_sch":  {"position":[679,849,781,892],"default_bg":bg_tmp_image(u"Лодочный причал")},
            "old_house_sch":     {"position":[8,1019,88,1071],"default_bg":bg_tmp_image(u"Старый корпус")},
            "clubs_sch":         {"position":[354,554,531,688],"default_bg":bg_tmp_image(u"Клубы")},
            "library_sch":       {"position":[953,416,1052,485],"default_bg":bg_tmp_image(u"Библиотека")},
            "sandpit_sch":       {"position":[1728,463,1918,721],"default_bg":bg_tmp_image(u"Карьер")},
            "medic_house_sch":   {"position":[853,486,931,557],"default_bg":bg_tmp_image(u"Медпункт")},
            "camp_entrance_sch": {"position":[229,554,333,645],"default_bg":bg_tmp_image(u"Остановка автобуса")},
            "forest_sch":        {"position":[454,275,538,324],"default_bg":bg_tmp_image(u"Умывальники")},
            "islaone_sch":       {"position":[453,960,706,1076],"default_bg":bg_tmp_image(u"о. Ближний")},
            "islatwo_sch":       {"position":[711,992,1084,1077],"default_bg":bg_tmp_image(u"о. Длинный")},
            "lake_sch":          {"position":[74,27,223,148],"default_bg":bg_tmp_image(u"Озеро")},
            "meadow_sch":        {"position":[297,991,405,1079],"default_bg":bg_tmp_image(u"Луг")},
            "campfire_sch":      {"position":[1501,970,1673,1072],"default_bg":bg_tmp_image(u"Костровая поляна")},
# раздельные локации спорткомплекса и клубов
            "sports_hall_sch":   {"position":[1082,584,1290,732],"default_bg":bg_tmp_image(u"Спортзал и футбольное поле")},
            "volleyball_sch":    {"position":[999,593,1079,685],"default_bg":bg_tmp_image(u"Воллейбольная площадка")},
            "court_sch":         {"position":[1107,509,1176,576],"default_bg":bg_tmp_image(u"Теннисный корт")},
            "kyber_club_sch":    {"position":[354,608,461,687],"default_bg":bg_tmp_image(u"Клуб кибернетиков")},

    }

# Определяем новый класс нашей карты (сборка кода из mapclass.rpy и pyclasses.rpy оригинала )

init -51 python:
    global_map_result_sch="error"

    def init_map_zones_realization_sch(zones_sch,default):
        global global_zones_sch
        global_zones_sch=zones_sch
        for i,data in global_zones_sch.iteritems():
            data["chibi"] = None
            data["label"] = default
            data["avaliable"] = True
            data["been_here"] = 0

    class Map_sch(renpy.Displayable):
        def __init__(self,pics,chibi,default):
            renpy.Displayable.__init__(self)
            self.pics=pics
            self.chibi=chibi
            self.default=default
            config.overlay_functions.append(self.overlay)

        def disable_all_zones(self):
            global global_zones_sch
            for name,data in global_zones_sch.iteritems():
                data["label"] = self.default
                data["avaliable"] = False
                data["been_here"] = 0
        def enable_all_zones(self):
            global global_zones_sch
            for name,data in global_zones_sch.iteritems():
                data["label"] = self.default
                data["avaliable"] = True
                data["been_here"] = 0
        def set_zone(self,name,label):
            global global_zones_sch
            global_zones_sch[name]["label"] = label
            global_zones_sch[name]["avaliable"] = True
        def reset_zone(self,name):
            global global_zones_sch
            global_zones_sch[name]["label"] = self.default
            global_zones_sch[name]["avaliable"] = False
            global_zones_sch[name]["been_here"] = 0
        def enable_empty_zone(self,name):
            global global_zones_sch
            self.set_zone(name,self.default)
            global_zones_sch[name]["avaliable"] = True
        def reset_current_zone(self):
            self.enable_empty_zone(global_map_result_sch)
        def disable_current_zone(self):
            global global_zones_sch
            global_zones_sch[global_map_result_sch]["avaliable"] = False
        def been_there(self):
            global global_zones_sch
            return global_zones_sch[global_map_result_sch]["been_here"]
        def set_chibi(self,name,ch):
            global global_zones_sch
            if  ch in self.chibi:
                global_zones_sch[name]["chibi"] = self.chibi[ch]
            else:
                global_zones_sch[name]["chibi"] = None
        def reset_chibi(self,name):
            self.set_chibi(name,"")
        def event(self, ev, x, y, st):
            return
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)
        def zoneclick(self,name):
            global global_zones_sch
            global global_map_result_sch
            store.map_enabled_sch=False
            renpy.scene('mapoverlay')
            global_zones_sch[name]["been_here"] += 1
            global_map_result_sch = name
            renpy.scene()
            if renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
                if not not_in_rollback_or_fast_forward():
                    renpy.log("renpy.roll_forward_info()")
                    renpy.config.skipping = False
                    renpy.game.after_rollback = False
            ui.jumps(global_zones_sch[name]["label"])()
        def overlay(self):
            if  store.map_enabled_sch:
                global global_zones_sch
                renpy.scene('mapoverlay')
                ui.layer('mapoverlay')
                for name,data in global_zones_sch.iteritems():
                    if data["avaliable"]:
                        pos = data["position"]
                        ui.imagebutton(
                            im.Crop(self.pics["avaliable_sch"],pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]),
                            im.Crop(self.pics["selected_sch"], pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]), # добавляем сюда суффикс, и в sch_store тоже
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
                ui.close()

# … и создаем новый объект класса
    store.map_sch = Map_sch(store.map_pics_sch, store.map_chibi, default)

# Ниже кусок из pyclasses.rpy; возможно, есть и лишние строки - но без этого карта работать отказывалась
    import pygame
    import os
    import os.path
    from renpy.store import *
    from renpy.display.im import ImageBase, image, cache, Composite

    store.map_enabled_sch = False
    store.map_enabled_sch_tmp = False
    def disable_stuff():
        store.map_enabled_sch_tmp = store.map_enabled_sch_tmp or store.map_enabled_sch
        store.map_enabled_sch = False
    def enable_stuff():
        store.map_enabled_sch = store.map_enabled_sch_tmp
        store.map_enabled_sch_tmp = False

# инициализируем функции по методам вновь созданного класса

init 5 python:
    import renpy.store as store
    if not config_session:
        def disable_all_zones_sch():
            store.map_sch.disable_all_zones()
        def enable_all_zones_sch():
            store.map_sch.enable_all_zones()
        def set_zone_sch(name,label):
            store.map_sch.set_zone(name,label)
        def reset_zone_sch(name):
            store.map_sch.reset_zone(name)
        def enable_empty_zone_sch(name):
            store.map_sch.enable_empty_zone(name)
        def reset_current_zone_sch():
            store.map_sch.reset_current_zone()
        def disable_current_zone_sch():
            store.map_sch.disable_current_zone()
        def been_there_sch():
            return store.map_sch.been_there()
        def set_chibi_sch(name,ch):
            store.map_sch.set_chibi(name,ch)
        def reset_chibi_sch(name):
            store.map_sch.reset_chibi(name)
        def show_map_sch():
            ui.jumps("_show_map_sch")()
        def init_map_zones_sch():
            init_map_zones_realization_sch(store.map_zones_sch,"nothing_here")

# определяем подосновы нашей карты (widget и bg) - собственно, подоснова карты:

init 5:
    if not config_session:
        image widget map_sch = gui_sch("maps/sch_bg.png")
        image bg map_sch = gui_sch("maps/sch_bg.png")

# еще раз отключаем чибиков

init 52 python:
    def disable_all_chibi_sch():
        global global_zones_sch
        for name,data in global_zones_sch.iteritems():
            data["chibi"] = None

# инициализация зон карты должна проводиться один раз, при старте

# ну и собственно - выводим нашу карту на экран, любуемся ею и ждем-с нажатия мыша.

label _show_map_sch:
    scene widget map_sch
    $ store.map_enabled_sch = True #
    $ ui.interact()
    jump _show_map_sch

#    ЗАМЕЧАНИЯ ПО РЕАЛИЗАЦИИ
#-------------------------------
#    Чукча не писатель, чукча читатель.
#    Чукча не погромист (точнее, таки да, но совсем в другой области и на других языках).
#    Чукча две недели назад не умел ни в Питон, ни в Ренпай, от слова "совсем", да и сейчас не умеет.
#
#    Но вышенаписанное вроде бы как работает.
#    Скорее всего - в этом коде можно выкинуть что-то без потери функционала.
