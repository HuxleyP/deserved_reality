#call dr_day1_remember_me
screen dr_show_name(forgotten): # эта хрень делает эти хрень туда-сюда как DVD
    tag menu
    modal False
    text bac_curse_name(forgotten) at dr_name_move(random.uniform(0.1,.5),random.random(),random.random()): 
        size 100 
        color '#FFF'


label dr_forgotten_lists_init:
    $ dr_placeholder_list = ['Мама', "\"Восход\"", "Линзы", "Искин", "Лагерь", "Совёнок", "Икарус", "Экспедиция", "395678geo", "Линзы", "Странные сны", "Институт", "Я", "?", "Неон", "Лас-Вегас", "Лунапарк", "Охранник", "Москва-Сити", "Небоскрёб"]
    $ dr_forgotten_dict = {
        "dr_remember_myname": {"Иван": 0},
        "dr_remember_amethyst": {"Аметист": 0},
        "dr_remember_city": {"Москва": 0},
        "dr_remember_amina": {"Амина": 0},
        "dr_remember_hospital": {"Больница": 0},
        "dr_remember_zipcode": {"Индекс": 0},
        "dr_remember_street": {"Улица": 0},
        "dr_remember_password": {"Пароль от соцсети": 0},
        "dr_remember_os": {"Олег Степанович": 0}
        #dr_remember_pumpkinpie: {"Тыквенный пирог": 0} # только если Амина = 1
        #dr_remember_keychain: {"Брелок": 0} # только если игрок его нашёл
    }
    $ dr_forgotten_dict_upd
    return

init python:
    def dr_forgotten_dict_upd():
        global dr_placeholder_list
        global dr_forgotten_dict
        try:
            if dr_day0_keychain:
                dr_forgotten_dict.update({"dr_remember_pumpkinpie":{"Брелок": 0}})
            if dr_forgotten_dict.get("Амина"):
                dr_forgotten_dict.update({"dr_remember_keychain":{"Тыквенный пирог": 0}})

        except:
            pass

init:









    image dr_remember_style = ParameterizedText(style = "settings_link", size = 100, color="fff")


    transform dr_scale(z,a,b): #трансформ текста из 2 списка
        zoom z
        align(a,b)
        parallel:
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            repeat
        parallel:
            ease renpy.random.randint(1,10) zoom random.uniform(0.1,0.5)
            ease renpy.random.randint(1,10) zoom random.uniform(0.1,0.5)
            repeat
        parallel:
            ease renpy.random.randint(1,10) alpha random.uniform(0.4,1)
            ease renpy.random.randint(1,10) alpha random.uniform(0.4,1)
            repeat 


    transform dr_scale_pre: #трансформ текста из 2 списка
        zoom random.random()
        align(random.random(),random.uniform(0.1,0.5))
        parallel:
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,10) align(renpy.random.random(),renpy.random.random())
            repeat
        parallel:
            ease renpy.random.randint(1,10) zoom random.uniform(0.1,0.5)
            ease renpy.random.randint(1,10) zoom random.uniform(0.1,0.5)
            repeat
        parallel:
            ease renpy.random.randint(1,10) alpha random.uniform(0.4,1)
            ease renpy.random.randint(1,10) alpha random.uniform(0.4,1)
            repeat 



    $ dr_names_time = 5

    transform dr_names_move(z,a,b): # трансформ отвлекающих текстов
            zoom z
            align(a,b)
            alpha .4
            parallel:
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                ease renpy.random.randint(1,dr_names_time) align(renpy.random.uniform(-0.2,1.2),renpy.random.uniform(-0.2,1.2))
                repeat
            parallel:
                linear renpy.random.uniform(0,0.75) alpha .4
                linear renpy.random.uniform(0,0.75) alpha 0
                repeat

    transform dr_name_move(z,a,b): #трансформ для основной песни
        zoom z
        align(a,b)
        alpha 1
        parallel:
            ease renpy.random.randint(1,6) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,6) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,6) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,6) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,6) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,6) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,6) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,6) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,6) align(renpy.random.random(),renpy.random.random())
            ease renpy.random.randint(1,6) align(renpy.random.random(),renpy.random.random())
            repeat
        parallel:
            linear renpy.random.uniform(0,0.75) alpha .42
            linear renpy.random.uniform(0,0.75) alpha .05
            repeat        


init python:


    def dr_curse_name(s): #"ломание" текста
        import random
        for i in range(int(len(s) / 2)):
            ch = random.randint(0,len(s)-2)
            if (ord(s[ch]) < 192 or ord(s[ch]) > 1039) and s[ch] != ' ' and s[ch] != '-':
                a = random.choice([(33,47),(58,64),(94,96)])
                s = (s[:ch] + chr(random.randint(a[0],a[1])) + s[ch+1:])
        return s

    def dr_rand_name(): #генерация левых текстов для белого шума и отвлекаловки - они постоянные
            import random
            s = ''
            if random.randint(0,2):
                for i in range(random.randint(10,30)):
                    c = 91
                    while c in (91,93,123,125):
                        c = random.randint(32,126)
                    s += chr(c)
            else:
                s = random.choice(dr_placeholder_list)
                
            return s


    def get_key(dict, value): # получаем ключ из словаря
        for i, k in dict.items():
            if k == value:
                return i

    def get_key_two(dict, value): # получаем ключ из словаря в словаре
        for i, k in dict1.items():
            if get_key(dict2, 0) == value: # Проверка на наличие значения во втором словаре, где dict2 = k
                pass #TODO THEN RAKI WILL ZIMOVAT'

label dr_day1_remember_me:
    # А эт вообще не нужно же!
    # Но я использую это как глюки в глазах 
    #image amnefor_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.08))
    
    # Суть этих текстбаттонов в том, что бы по нажатию они чинили сломанный текст и вызывали кусочек текста
    #vbox:
        #$ dr_tmp = ""
        #for i in dr_forgotten_dict: # если не сработает, то len(dr_forgotten_dict)
        #    if dr_forgotten_dict.get(i) == 0:
        #        tmp = dr_curse_name(get_key(dr_forgotten_dict, 0))
        #        dr_forgotten_dict[i] = 1
        #        call dr_forgotten_dict_upd
        #    textbutton("tmp") at dr_scale_pre:
        #        text_style "settings_link"
        #        style "settings_link"
        #        size 100
        #        color = "#fff"
        #        #action СДЕЛАТЬ НОРМАЛЬНО

    $ amnetext_w = random.random()
    $ amnetext_h = random.random()
    $ amnetext_s = random.uniform(0.1,0.5)

    $ volume(random.uniform(0.1,.45), 'sound_loop2')
    $ volume(random.uniform(0.1,.45), 'sound_loop3')
    
    play sound_loop2 bac_whispers fadein 40
    play sound_loop3 bac_whispers2 fadein 40
    
    scene anim prolog_1
    show anim prolog_2 as anim2:
        alpha 0.0
        parallel:
            linear 3 alpha 1
            linear 3 alpha 0
            repeat
    with Fade(0.4,1,0.5, color = '#000')

    
    label dr_placeholderstuff:
        $ drk = 0
        #for drk in dr_placeholder_list:
        #    show dr_remember_style dr_rand_name() at dr_names_move(random.uniform(0.1,0.5),random.random(),random.random()) as text[drk]
        #    $ drk +=1
        $ drk = 0
        with Fade(0.4,1,0.5, color = '#000')

    show black onlayer master:
        alpha 0.0
        parallel:
            linear 0.75 alpha 0.75
            linear 0.75 alpha 0
            repeat
