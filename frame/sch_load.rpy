init:

    $ mods["sch_pre_load"]=u"{font=sch/res/fonts/elixia.ttf}{size=55}Иллюзион{/font}{/size}"
    $ filter_tags["sch_pre_load"] = ["gameplay:vn", "translation:russian"]

    if persistent.sch_current_version:
        $ persistent.sch_current_version = "nothing"

screen sch_download_resources:
    tag menu
    modal False
    key "game_menu":
        action NullAction()
    key "screenshot":
        action NullAction()
    add "bg black"
    text (u"Внимание! Ресурсы мода не загружены!\nДля игры загрузите дополнительные файлы."):
        size 85
        kerning 2.2
        xalign 0.5
        yalign 0.2
    textbutton "Загрузить ресурсы":
        anchor(0,0.5)
        text_align 0.0
        yalign 0.65
        xalign 0.30
        style "log_button"
        action (Hide("sch_download_resources",transition=dissolve), Jump("sch_dwnl"))
    textbutton "Выход":
        anchor(0,0.5)
        text_align 0.0
        yalign 0.65
        xalign 0.70
        style "log_button"
        action (Hide("sch_download_resources",transition=dissolve), Return())

label sch_dwnl:
    $ nfo_text = 'Загружаются ресурсы для мода.'
    $ m_nfo_text = 'Пожалуйста, подождите...'
    $ renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
    $ renpy.pause (3, hard=True)
    $ m_nfo_text = 'Идёт закачка жидкого Графониума-236...'
    $ renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
    $ renpy.pause (1.5, hard=True)
    $ sch_download_rpa()
    $ m_nfo_text = 'Идёт тренировка обезьян-конфигураторов...'
    $ renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
    $ renpy.pause (1.5, hard=True)
    $ sch_download_config_rpyc()
    $ m_nfo_text = 'Идёт оцифрование мозга сценаритиста...'
    $ renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
    $ renpy.pause (1.5, hard=True)
    $ sch_download_scenario_rpyc()
    $ nfo_text = 'Загрузка была завершена.'
    $ m_nfo_text = 'Будет произведена перезагрузка.'
    $ renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
    $ renpy.pause (3, hard=True)
    $ persistent.sch_current_version = persistent.sch_new_version
    $ renpy.utter_restart()

label sch_update_mod:
    $ nfo_text = 'Идёт обновление модификации.'
    $ m_nfo_text = 'Пожалуйста, подождите...'
    $ renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
    $ renpy.pause (3, hard=True)
    $ sch_update_files()
    $ m_nfo_text = 'Обновление было завершено. Будет совершена перезагрузка.'
    $ renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
    $ renpy.pause (3, hard=True)
    $ renpy.utter_restart()


label sch_pre_load:
    scene bg black
    with dissolve
    pause 1

    if persistent.sch_current_version == "nothing":
        call screen sch_download_resources with fade
    elif persistent.sch_current_version != persistent.sch_new_version:
        jump sch_update_mod
    else:
        pass

    play music sch_mus_a_l fadein 2

#    $ soznanie("bg ext_library_night")
    show sch_logo:
        xalign 0.5 yalign 0.3
    show text "{font=dr_font}{size=150}System{/font}{/size}":
        xalign 0.5 yalign 0.6
    with Dissolve(3.0)
    $ renpy.pause(5, hard=True)
    hide sch_logo
    hide text
    with dissolve

    scene bg black with dissolve

    call screen sch_main_menu_pre

    $ renpy.pause (1, hard=True)
    stop music fadeout 3
    scene bg black with fade3
    pause 1

    jump sch_main_menu_call

label sch_main_menu_call:
    $ renpy.block_rollback()
    $ result = _return
    if result == "sch_prologue":
        $ renpy.pause(0.7, hard=True)
        jump sch_prologue
    elif result == "exit":
        stop music fadeout 3.5
        scene bg black with Dissolve(3.5)
        return

init python:

    from urllib2 import urlopen
    import os, shutil

    def sch_download_rpa(): #Загрузка rpa файла, со всей музыкой, звуками, артами и прочим визуалом
        sch_file_url = "https://github.com/HuxleyP/deserved_reality/source"
        sch_destination = renpy.config.basedir + "/game/deserved_reality/"
        sch_file_name = "source"
        try:
            response = urlopen(sch_file_url)
            CHUNK = 16 * 1024
            with open(sch_file_name, 'wb') as f:
                while True:
                    chunk = response.read(CHUNK)
                    if not chunk:
                        break
                    f.write(chunk)
            os.rename(sch_file_name, sch_destination + sch_file_name)
        except IOError as e:
            nfo_text = 'Ошибка!'
            m_nfo_text = 'Мы сломались! Возможно, ошибка на сервере.\nМожет быть, у вас проблемы с интернет-соединением либо атрибутами папок...'
            renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
            renpy.pause (5, hard=True)
            renpy.show("git_es_rst")
            renpy.utter_restart()



    def sch_download_config_rpyc(): #Загрузка rpy файлов конфигов
	

        sch_github_config = [
            ("sch_guideline.rpy, "https://https://github.com/HuxleyP/deserved_reality/tree/master/config/sch_guideline.rpy")
			("sch_scripts.rpy, "https://github.com/HuxleyP/deserved_reality/tree/master/config/sch_scripts.rpy")
        ]
		
		for i in range(1, 3):
			if i.startswitch("https://https://github.com/HuxleyP/deserved_reality/tree/master/config/") and i.endswitch(".rpy"):
				sch_github_config.append(

        try:
            sch_destination = renpy.config.basedir + "/game/sch/config/"
            os.mkdir(sch_destination)
        except IOError as e:
            nfo_text = 'Ошибка!'
            m_nfo_text = 'Мы не знаем, как это произошло... Возможно ошибка на сервере.\nМожет быть, у вас проблемы с интернет-соединением либо атрибутами папок...'
            renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
            renpy.pause (5, hard=True)
            renpy.show("git_es_rst")
            renpy.utter_restart()

        for sch_file_name, sch_file_url in sch_github_config:
            try:
                response = urlopen(sch_file_url)
                CHUNK = 16 * 1024
                with open(sch_file_name, 'wb') as f:
                    while True:
                        chunk = response.read(CHUNK)
                        if not chunk:
                            break
                        f.write(chunk)
                os.rename(sch_file_name, sch_destination + sch_file_name)
            except IOError as e:
                nfo_text = 'Ошибка!'
                m_nfo_text = 'Мы сломались! Возможно, ошибка на сервере.\nМожет быть, у вас проблемы с интернет-соединением либо атрибутами папок...'
                renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
                renpy.pause (5, hard=True)
                renpy.show("git_es_rst")
                renpy.utter_restart()


    def sch_download_scenario_rpyc(): #Загрузка rpyc файлов сценария

        sch_github_scenario = [
            ("sch_prologue.rpyc", "https://github.com/Cesoneemz/sch/raw/master/scenario/sch_prologue.rpyc"),
        ]

        try:
            sch_destination_s = renpy.config.basedir + "/game/sch/scenario/"
            os.mkdir(sch_destination_s)
        except IOError as e:
            nfo_text = 'Ошибка!'
            m_nfo_text = 'Мы не знаем, как это произошло... Возможно ошибка на сервере.\nМожет быть, у вас проблемы с интернет-соединением либо атрибутами папок...'
            renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
            renpy.pause (5, hard=True)
            renpy.show("git_es_rst")
            renpy.utter_restart()

        for sch_file_name, sch_file_url in sch_github_scenario:
            try:
                response = urlopen(sch_file_url)
                CHUNK = 16 * 1024
                with open(sch_file_name, 'wb') as f:
                    while True:
                        chunk = response.read(CHUNK)
                        if not chunk:
                            break
                        f.write(chunk)
                os.rename(sch_file_name, sch_destination_s + sch_file_name)
            except IOError as e:
                nfo_text = 'Ошибка!'
                m_nfo_text = 'Мы не знаем, как это произошло... Возможно ошибка на сервере.\nМожет быть, у вас проблемы с интернет-соединением либо атрибутами папок...'
                renpy.show_screen('knz_info_screen', nfo_text, m_nfo_text)
                renpy.pause (5, hard=True)
                renpy.show("git_es_rst")
                renpy.utter_restart()
