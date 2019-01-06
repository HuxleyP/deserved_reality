init -1:
    python:
        # цветная вспышка
        # with flash("#822")
        def flash(color="#fff"):
            return Fade(.25, 0, .75, color=color)




init -10 python: # главы
    def sch_chaper_init(sch_char_name):
        global save_name
        if sch_char_name != None:
            save_name = (u"{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color}%s ver.%s/%s; codename \"%s\: пролог %s.{/font}") % (sch_state, sch_version, sch_hotfix, sch_codename, sch_char_name)
        else:
            save_name = (u"{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color}%s ver.%s/%s; codename \"%s\: пролог.{/font}") % (sch_state, sch_version, sch_hotfix, sch_codename)


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

        if new_day:
            renpy.scene()
            if sch_dayNo >=1 and sch_dayNo <=7:
                renpy.show('day[sch_dayNo]')
            renpy.scene()
            if sch_dayNo > 1:
                if max(pt_dv, pt_un, pt_us, pt_sl, pt_mi) >=8 and max(pt_dv, pt_un, pt_us, pt_sl, pt_mi) != 0 and sch_dayNo <=3
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
            elif sch_dayNo == 1:
                renpy.show('day1')
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
            renpy.music.play('whisper', channel='sound', fadein=0.5, fadeout = 0.25)
            renpy.show('black')
            renpy.pause(1)
            renpy.transition(fade)
            save_name = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color}{/font}") # так надо, иначе ошибка
            if new_day:
                if sch_dayNo != 0:
                    save_name = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color} - {color=#afafaf}День{/font} {font=[dr_font]}%d{/font}{/color}{/size}") % (sch_dayNo)
                elif sch_dayNo >= 8:
                    if sch_dayNo >=9:
                        sch_part = sch_dayNo - 7
                        save_name = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color} - {color=#afafaf} Эпилог. Часть %d{/font}{/color}{/size}") % (sch_part)
                    else:
                        save_name = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color} - {color=#afafaf}Эпилог.{/font}{/color}{/size}")
                elif sch_dayNo == 0 and sch_part !=0:
                    save_name = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность{/color} - {color=#afafaf}Часть %d{/font}{/color}{/size}") % (sch_part)
                else:
                    save_name = (u"{size=80}{font=[csn]}{color=#FFFFFF}Заслуженная | {/color}{color=#999999}Реальность.{/font}{/color}{/size}") % (sch_part)

            if sch_ch_name != " ":
                renpy.show('day_num', what=Text(save_name, xcenter=0.5,ycenter=0.25))
            renpy.pause(2)
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


python



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
    if renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
        sch_path = 'deserved_reality/'
    elif (renpy.version(tuple=False) == "Ren'Py 6.18.3.761") or (persistent.nonsteam_7dl == True):
        sch_path = 'mods/deserved_reality/'
    else:
        if renpy.mobile:
            sch_path = 'deserved_reality/'
        else:
            #sch_path = '../ТУТ БУДУТ ЦИФРЫ/deserved_reality/'
    config_session = False
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
    def fonts_sch(file):
        return source_sch+"images/fonts/%s" % (file)
    def maps_sch(file):
        return source_sch+"images/maps/%s" % (file)


init -1000 python:
    if renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
        sch_path = 'deserved_reality/'
    elif (renpy.version(tuple=False) == "Ren'Py 6.18.3.761") or (persistent.nonsteam_7dl == True):
        sch_path = 'mods/deserved_reality/'
    else:
        if renpy.mobile:
            sch_path = 'deserved_reality/'
        else:
            sch_path = '../441054187/deserved_reality/'
