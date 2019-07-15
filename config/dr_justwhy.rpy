#call dr_day1_remember_me



screen dr_show_name(forgotten): # эта хрень делает эти хрень туда-сюда как DVD
    tag menu
    modal False
    text bac_curse_name(forgotten) at dr_name_move(random.uniform(0.1,.5),random.random(),random.random()): 
        size 100 
        color '#FFF'


init:
    dr_placeholder_list = ['Мама', "\"Восход\"", "Линзы", "Искин", "Лагерь", "Совёнок", "Икарус", "Экспедиция", "395678geo", "Линзы", "Странные сны", "Институт", "Я", "?", "Неон", "Лас-Вегас", "Лунапарк", "Охранник", "Москва-Сити", "Небоскрёб"])
    dr_forgotten_dict = {
        "Иван": 0
        "Аметист": 0
        "Москва": 0
        "Амина": 0
        #"Тыквенный пирог": 0 # только если Амина = 1
        "Больница": 0
        "Брелок": 0 
        "Индекс": 0
        "Улица": 0
        "Пароль от соцсети": 0
        "Олег Степанович": 0
        # "Брелок": 0 # только если игрок его нашёл
    }
    if dr_day0_keychain:
        dr_forgotten_dict.update({"Брелок": 0})
    if dr_forgotten_dict.get("Амина"):
        dr_forgotten_dict.update({"Тыквенный пирог": 0})












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

    def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k

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


label dr_day1_remember_me:
    # А эт вообще не нужно же! 
    #image amnetext1_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.08))
    #image amnetext11_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.09))
    #image amnetext2_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.08))
    #image amnetext22_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.09))
    #image amnetext3_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.08))
    #image amnetext33_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.09))
    #image amnetext4_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.08))
    #image amnetext44_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.09))
    #image amnetext5_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.08))
    #image amnetext55_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.09))
    #image amnetext6_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.08))
    #image amnetext66_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.09))
    #image amnetext7_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.08))
    #image amnetext77_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.09))
    #image amnetext8_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.08))
    #image amnetext88_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.09))
    #image amnetext9_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.08))
    #image amnetext99_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.09))
    #image amnetext10_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.08))
    #image amnetext1010_dr = im.MatrixColor(dr_source + 'images/effects/fog_ball.png', im.matrix.tint(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))*im.matrix.brightness(.09))
    vbox:
        dr_tmp = ""
        for i in dr_forgotten_dict: # если не сработает, то len(dr_forgotten_dict)
            if dr_forgotten_dict.get == 0:
                tmp = get_key(dr_forgotten_dict, 0)
            textbutton("tmp") at scale(amnetext_s[i], amnetext_w[i], amnetext_h[i])

    $ amnetext_w1 = random.random()
    $ amnetext_h1 = random.random()
    $ amnetext_s1 = random.uniform(0.1,0.5)
    $ amnetext_w2 = random.random()
    $ amnetext_h2 = random.random()
    $ amnetext_s2 = random.uniform(0.1,0.5)
    $ amnetext_w3 = random.random()
    $ amnetext_h3 = random.random()
    $ amnetext_s3 = random.uniform(0.1,0.5)
    $ amnetext_w5 = random.random()
    $ amnetext_h5 = random.random()
    $ amnetext_s5 = random.uniform(0.1,0.5)
    $ amnetext_w4 = random.random()
    $ amnetext_h4 = random.random()
    $ amnetext_s4 = random.uniform(0.1,0.5)
    $ amnetext_w6 = random.random()
    $ amnetext_h6 = random.random()
    $ amnetext_s6 = random.uniform(0.1,0.5)
    $ amnetext_w7 = random.random()
    $ amnetext_h7 = random.random()
    $ amnetext_s7 = random.uniform(0.1,0.5)
    $ amnetext_w10 = random.random()
    $ amnetext_h10 = random.random()
    $ amnetext_s10 = random.uniform(0.1,0.5)
    $ amnetext_w9 = random.random()
    $ amnetext_h9 = random.random()
    $ amnetext_s9 = random.uniform(0.1,0.5)
    $ amnetext_w8 = random.random()
    $ amnetext_h8 = random.random()
    $ amnetext_s11 = random.uniform(0.1,0.5)
    $ amnetext_w11 = random.random()
    $ amnetext_h11 = random.random()
    $ amnetext_s12 = random.uniform(0.1,0.5)
    $ amnetext_w12 = random.random()
    $ amnetext_h12 = random.random()
    $ amnetext_s13 = random.uniform(0.1,0.5)
    $ amnetext_w13 = random.random()
    $ amnetext_h14 = random.random()
    $ amnetext_s15 = random.uniform(0.1,0.5)
    $ amnetext_w16 = random.random()
    $ amnetext_h16 = random.random()
    $ amnetext_s17 = random.uniform(0.1,0.5)

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
        for drk in dr_placeholder_list:
            show dr_remember_style dr_rand_name() at dr_names_move(random.uniform(0.1,0.5),random.random(),random.random()) as text[drk]
            $ drk +=1
        $ drk = 0
        with Fade(0.4,1,0.5, color = '#000')

    show black onlayer master:
        alpha 0.0
        parallel:
            linear 0.75 alpha 0.75
            linear 0.75 alpha 0
            repeat
