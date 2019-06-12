init python:
        class dr_FunctionCallback(Action):
            def __init__(self,function,*arguments):
                self.function=function
                self.arguments=arguments
            def __call__(self):
                return self.function(self.arguments)
    
        def dr_on_load_callback(slot):
            try:
                if persistent.dr_on_save_timeofday[slot]:
                    persistent.timeofday = persistent.dr_on_save_timeofday[slot][0]
                    persistent.sprite_time = persistent.dr_on_save_timeofday[slot][1]
                    persistent.font_size = persistent.dr_on_save_timeofday[slot][2]
                    persistent.hentai = persistent.dr_on_save_timeofday[slot][3]
                    _preferences.volumes['music'] = persistent.dr_on_save_timeofday[slot][4]
                    _preferences.volumes['sfx'] = persistent.dr_on_save_timeofday[slot][5]
                    _preferences.volumes['voice'] = persistent.dr_on_save_timeofday[slot][6]
        
            except:
                pass
    
        def dr_on_save_callback(slot):
            if not persistent.dr_on_save_timeofday:
                persistent.dr_on_save_timeofday={}
            persistent.dr_on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, persistent.hentai, _preferences.volumes['music'], _preferences.volumes['sfx'], _preferences.volumes['voice'])
        
        def dr_screen_save():
            renpy.display.screen.screens[("dr_old_main_menu", None)] = renpy.display.screen.screens[("main_menu", None)]
            renpy.display.screen.screens[("dr_old_quit", None)] = renpy.display.screen.screens[("quit", None)]
            renpy.display.screen.screens[("dr_old_say", None)] = renpy.display.screen.screens[("say", None)]
            renpy.display.screen.screens[("dr_old_nvl", None)] = renpy.display.screen.screens[("nvl", None)]
            renpy.display.screen.screens[("dr_old_game_menu_selector", None)] = renpy.display.screen.screens[("game_menu_selector", None)]
            renpy.display.screen.screens[("dr_old_yesno_prompt", None)] = renpy.display.screen.screens[("yesno_prompt", None)] 
            renpy.display.screen.screens[("dr_old_choice", None)] = renpy.display.screen.screens[("choice", None)]
            renpy.display.screen.screens[("dr_old_help", None)] = renpy.display.screen.screens[("help", None)]
        
        def dr_screen_act():
            config.window_title = u"Заслуженная | Реальность"
            config.name = "dr"
            config.version = "7.3 A"
            renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("dr_main_menu", None)]
            renpy.display.screen.screens[("quit", None)] = renpy.display.screen.screens[("dr_quit", None)]
            renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("dr_say", None)]
            renpy.display.screen.screens[("nvl", None)] = renpy.display.screen.screens[("dr_nvl", None)]
            renpy.display.screen.screens[("game_menu_selector", None)] = renpy.display.screen.screens[("dr_game_menu_selector", None)]
            renpy.display.screen.screens[("yesno_prompt", None)] = renpy.display.screen.screens[("dr_yesno_prompt", None)] 
            renpy.display.screen.screens[("choice", None)] = renpy.display.screen.screens[("dr_choice", None)]
            renpy.display.screen.screens[("help", None)] = renpy.display.screen.screens[("dr_help", None)]
            layout.LOADING = "Вы можете потерять несохраненые данные. Продолжить?"
            
            config.mouse = {'default' : [("dr/images/gui/cursor.png", 0, 0)]} 
            #config.main_menu_music = "mods/dr/sounds/music/tl_mega_drive_narc.mp3"
            config.linear_saves_page_size = None
            persistent._file_page = "dr_FilePage_1"  

        def dr_screens_diact():
            config.window_title = u"Бесконечное лето"
            config.name = "Everlasting_Summer"
            config.version = "1.2"
            renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("dr_old_main_menu", None)]
            renpy.display.screen.screens[("quit", None)] = renpy.display.screen.screens[("dr_old_quit", None)]
            renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("dr_old_say", None)]
            renpy.display.screen.screens[("nvl", None)] = renpy.display.screen.screens[("dr_old_nvl", None)]
            renpy.display.screen.screens[("game_menu_selector", None)] = renpy.display.screen.screens[("dr_old_game_menu_selector", None)]
            renpy.display.screen.screens[("yesno_prompt", None)] = renpy.display.screen.screens[("dr_old_yesno_prompt", None)]
            renpy.display.screen.screens[("choice", None)] = renpy.display.screen.screens[("dr_old_choice", None)]
            renpy.display.screen.screens[("help", None)] = renpy.display.screen.screens[("dr_old_help", None)]
            layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
            
            config.mouse = {'default' : [("images/misc/mouse/1.png",  0, 0)]}
            config.main_menu_music = "sound/music/blow_with_the_fires.ogg"

            persistent._file_page = 1
            renpy.music.stop("ambience")
            renpy.music.stop("music")
            renpy.music.stop("sound")
            renpy.play(music_list["blow_with_the_fires"], channel = "music")

        def dr_screens_save_act():
            dr_screen_save()
            dr_screen_act()