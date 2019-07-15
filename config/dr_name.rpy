init python:
    dr_std_set_for_preview = {}
    dr_std_set = {}
    store.dr_colors = {}
    store.dr_names = {}
    store.dr_names_list = []
    time_of_day = "night"

    _show_two_window = True

    store.dr_names_list.append("narrator")

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

    def name_dr(dr_name):
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
        global store
        global time_of_day
        gl = globals()
        v = "_voice"
        if  x == 'narrator':
            if  is_nvl:
                gl['narrator'] = Character(None, kind=nvl, what_style="narrator_%s"%time_of_day, ctc="ctc_animation_nvl", ctc_position="fixed")
            else:
                gl['narrator'] = Character(None, what_style="narrator_%s"%time_of_day, ctc="ctc_animation", ctc_position="fixed")
            return
        if  x == 'dr_th':
            if  is_nvl:
                gl['dr_th'] = Character(None, kind=nvl, what_style="thoughts_%s"%time_of_day,what_italic = True, ctc="ctc_animation_nvl", ctc_position="fixed")
            else:
                gl['dr_th'] = Character(None, what_style="thoughts_%s"%time_of_day,what_italic = True, ctc="ctc_animation", ctc_position="fixed")
            return
        if  is_nvl:
            gl[x] = DynamicCharacter("%s_dr_name"%x, color=store.dr_colors[x][time_of_day], kind=nvl, what_style="normal_%s"%time_of_day,who_suffix=":", ctc="ctc_animation_nvl", ctc_position="fixed")
            gl["%s_dr_name"%x] = store.dr_names[x]
        else:
            gl[x] = DynamicCharacter("%s_dr_name"%x, color=store.dr_colors[x][time_of_day], show_two_window=_show_two_window,  what_style="normal_%s"%time_of_day, ctc="ctc_animation", ctc_position="fixed")
            gl["%s_dr_name"%x] = store.dr_names[x]

    def dr_mode_adv():
        nvl_clear()
        
        global menu
        menu = renpy.display_menu
        
        global store
        for x in store.dr_names_list:
            dr_char_define(x)

    def dr_mode_nvl(clear=True):
        if clear:
            nvl_clear()
        
        global menu
        menu = nvl_menu
        
        global narrator
        global dr_th
        narrator_nvl = narrator
        th_nvl = dr_th
        
        global store
        for x in store.dr_names_list:
            dr_char_define(x,True)

    def dr_reload_names():
        global store
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
        dr_reload_names()
        if menu == nvl_menu:
            dr_mode_nvl(False)
        else:
            dr_mode_adv()

    def dr_save_names_known():
        gl = globals()
        global store
        for x in store.dr_names_list:
            if not (x == 'narrator' or x == 'th'):
                store.dr_names[x] = gl["%s_name"%x]


    def dr_forgeteveryone():
        global store
        dr_meet('dr_voice', u"Голос")
        dr_meet('dr_myself', u"Некто")
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
    name_dr(u"Я")
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

