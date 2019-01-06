
init:
    transform sch_running:
        anchor (0.1, 0.1)
        zoom 1.2
        ease 0.2 pos (0, 0)
        ease 0.2 pos(50,50)
        ease 0.2 pos (0, 0)
        ease 0.2 pos(-50,50)
        repeat

    transform transpa:
        alpha 0.5

    transform right_lower_zoom:
        xalign 0.75 #TODO подкорректировать приближение
        yalign 0.1
        zoom 1.5




init python:

    def double_vision_on(picture):


        renpy.scene()

        renpy.show(picture)



        renpy.show(picture, at_list=[transpa,randmotion], tag="blur_image")


        renpy.with_statement(dissolve)


    def double_vision_off():

        # renpy.hide() is like "hide"

        renpy.hide("blur_image")

        renpy.with_statement(dissolve)
