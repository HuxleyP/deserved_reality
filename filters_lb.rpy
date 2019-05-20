init:
    $ filters["menu__cheats_7dl"] = u"(Меню)Очевидное Лето"
    $ filters["menu__lucky_7dl"] = u"(Меню)Мне повезёт!"
    $ filters["text__nya_kawaii_7dl"] = u"(Текст)Кавайное Лето"
    $ filters["text__no_r_7dl"] = u"(Текст)Картавый Семён"
#    $ filters["text__blah"] = u"(Текст)Грязные Мысли"
    $ filters["widget__filename_7dl"] = u"(GUI)Текущая строка"

python early:
    def lb__dis(code):
        import dis, sys, StringIO
        tmp_stdout,sys.stdout = sys.stdout,StringIO.StringIO()
        dis.disassemble(code)
        tmp_stdout,sys.stdout = sys.stdout,tmp_stdout
        return tmp_stdout.getvalue()

    # see https://raw.github.com/lolbot-iichan/decompile.rpy/master/decompile.rpy for more serious renpy&python decompilation
    def lb__decompile_py_light(code):
        from dis import opmap, opname, HAVE_ARGUMENT
        stack, res = [], []
        itercode = iter([ord(x) for x in code.co_code][:-4])
        for o in itercode:
            if  o >= HAVE_ARGUMENT:
                id = next(itercode) + next(itercode)*256
            opsplit = opname[o].split("_")
            if  opname[o] in ["STORE_ATTR"] or opsplit[0] in ["BINARY","INPLACE"]:
                tmp = stack.pop()
            if   o == opmap["POP_TOP"]:       res   += [stack.pop()]
            elif o == opmap["STORE_NAME"]:    res   += ["%s = %s"%(code.co_names[id],stack.pop())]
            elif o == opmap["STORE_ATTR"]:    res   += ["%s.%s = %s"%(tmp,code.co_names[id],stack.pop())]
            elif o == opmap["LOAD_NAME"]:     stack += [code.co_names[id]]
            elif o == opmap["LOAD_CONST"]:    stack += [`code.co_consts[id]`]
            elif o == opmap["LOAD_ATTR"]:     stack += ["%s.%s"%(stack.pop(),code.co_names[id])]
            elif opsplit[0] in ["BINARY","INPLACE"] and opsplit[-1] in ["ADD","SUBTRACT"]:
                if   opname[o].endswith("_ADD"):      stack += ["%s+%s"%(stack.pop(),tmp)]
                elif opname[o].endswith("_SUBTRACT"): stack += ["%s-%s"%(stack.pop(),tmp)]
            elif o == opmap["CALL_FUNCTION"] and id/256 == 0:
                args = ", ".join([stack.pop() for i in range(id%256)])
                stack += ["%s(%s)"%(stack.pop(),args)]
            else:
                # renpy.error((lb__dis(code),opname[o]))
                return "python: #TODO\n"+lb__dis(code)
        return "$ "+res[0] if len(res) == 1 else "\n    ".join(["python:"]+res)

    def lb__decompile_rpy_light(i):
        return "jump "+i.target if isinstance(i,renpy.ast.Jump) else lb__decompile_py_light(i.code.bytecode) if isinstance(i,renpy.ast.Python) else ""

    def menu__cheats_7dl():
        renpy.display.screen.screens[("choice",None)] = renpy.display.screen.screens[("choice_cheat",None)]
        for item in (item for item in renpy.game.script.namemap.values() if isinstance(item, renpy.ast.Menu)):
            for (id,(text,condition,block)) in enumerate(item.items):
                if  block is not None:
                    text = "{color=#66cc00}{size=-10}-({/size}{/color}".join([text]+["{color=#66cc00}{size=-10}{i}%s){/size}{/i}{/color}"%s for s in [lb__decompile_rpy_light(i) for i in block] if (s!="") and (s.find('TODO')==-1) and ((s.find('jump')!=-1) or (s.find('Jump')!=-1) or (s.find('=')!=-1) or (s.find('set_zone')!=-1) or (s.find('call')!=-1) or (s.find('Call')!=-1))])
                    item.items[id] = (text,condition,block)
            
    def menu__lucky_7dl():
        import random
        def display_menu_lucky(items,
                 window_style='menu_window',
                 interact=True,
                 with_none=None,
                 caption_style='menu_caption',
                 choice_style='menu_choice',
                 choice_chosen_style='menu_choice_chosen',
                 choice_button_style='menu_choice_button',
                 choice_chosen_button_style='menu_choice_chosen_button',
                 scope={ },
                 widget_properties=None,
                 screen="choice",
                 type="menu", #@ReservedAssignment
                 predict_only=False,
                 **kwargs):
            """
            Altered RenPy display_menu.
            The replacement of options in the menu takes place just before passing them to ui constructor.
            Thus, any randomly picked option is valid, and RenPy thinks we are choosing options from the ordinary menu.
            NB: "Очевидное Лето" filter still won't predict the outcome of the timed autochoice.
            This solution is implemented by yakui-lover, based on the original RenPy display_menu.
            """

            if interact:
                renpy.exports.mode(type)
                renpy.exports.choice_for_skipping()

            choices = [ val for label, val in items ]
            while None in choices:
                choices.remove(None)

            roll_forward = renpy.exports.roll_forward_info()

            if roll_forward not in choices:
                roll_forward = None

            if renpy.config.auto_choice_delay:

                renpy.ui.pausebehavior(renpy.config.auto_choice_delay,
                                       random.choice(choices))

            location=renpy.game.context().current

            if renpy.exports.in_fixed_rollback() and renpy.config.fix_rollback_without_choice:
                renpy.ui.saybehavior()
            
            # Altered code
            lucky_label, lucky_val = random.choice([item for item in items])
            # Newline splitting for the needs of "Очевидное Лето" filter
            if lucky_label.count('\n'):
                lucky_label = u"Мне повезёт!" + lucky_label[lucky_label.find('\n'):]
            else:
                lucky_label = u"Мне повезёт!"
            
            if renpy.display.screen.has_screen(screen):

                item_actions = [ ]

                if widget_properties is None:
                    props = { }
                else:
                    props = widget_properties

                action = renpy.ui.ChoiceReturn(lucky_label, lucky_val , location)

                if renpy.config.choice_screen_chosen:
                    item_actions.append((lucky_label, action, action.get_chosen()))
                else:
                    item_actions.append((lucky_label, action))

                renpy.display.screen.show_screen(screen, items=item_actions, _widget_properties=props, _transient=True, **scope)

            else:
                renpy.ui.window(style=window_style, focus="menu")
                renpy.ui.menu([(lucky_label, lucky_val)],
                              location=renpy.game.context().current,
                              focus="choices",
                              default=True,
                              caption_style=caption_style,
                              choice_style=choice_style,
                              choice_chosen_style=choice_chosen_style,
                              choice_button_style=choice_button_style,
                              choice_chosen_button_style=choice_chosen_button_style,
                              **kwargs)
                              
            # End of altered code
            renpy.exports.shown_window()

            for label, val in items:
                if val is not None:
                    renpy.exports.log("Choice: " + label)
                else:
                    renpy.exports.log(label)

            renpy.exports.log("")

            if interact:

                rv = renpy.ui.interact(mouse='menu', type=type, roll_forward=roll_forward)

                for label, val in items:
                    if rv == val:
                        renpy.exports.log("User chose: " + label)
                        break
                else:
                    renpy.exports.log("No choice chosen.")

                renpy.exports.log("")

                renpy.exports.checkpoint(rv)

                if with_none is None:
                    with_none = renpy.config.implicit_with_none

                if with_none:
                    renpy.game.interface.do_with(None, None)

                return rv

            return None
            
        renpy.display_menu = display_menu_lucky


    def lb__txt(f,lst):
        import re, random
        for item in (item for item in renpy.game.script.namemap.values() if isinstance(item, renpy.ast.Say)):
            for i in lst:
                if  len(i)>2 and item.who not in i[2]:
                    continue
                item.what = f(item.what,i[0],i[1])
    lb__regexp_replace = lambda what,before,after: re.sub(before,after,what,flags=re.UNICODE)
    lb__random_replace = lambda what,before,afters: "".join(sum(([random.choice(afters),s] for s in what.split(before)),[])[1:])

    text__nya_kawaii_7dl = lambda: lb__txt(lb__regexp_replace,[(ur'([\w])\.\.\.', u'\\1, унью…'), (ur'([\w])\.', u'\\1, ня.'), (ur'([\w])!', u'\\1, нипа!'), (ur'([\w])\?', u'\\1, нёро~н?')])
    text__no_r_7dl       = lambda: lb__txt(lb__regexp_replace,[(ur'р',u'г',['me']), (ur'Р',u'Г',['me'])])
    #text__blah       = lambda: lb__txt(lb__random_replace,[(',',[u', как его там,',u', мать его,',u', мля,',u', это самое,']+[u',']*5,['th','narrator','me'])])



    def widget__filename_7dl():
        import os
        def editoverlay():
            fullfn, line = renpy.get_filename_line()
            ui.button(clicked=None, xpos=config.screen_width, xanchor=1.0, ypos=2, xpadding=6, xminimum=200)
            ui.text("%s:%d" % (os.path.basename(fullfn), line), style="button_text", size=14)
        config.overlay_functions.append(editoverlay)

screen choice_cheat:

    modal True

    python:
        choice_colors_hover={                        
        'day': "#9dcd55",
        'night': "#3ccfa2",
        'sunset': "#dcd168",
        'prologue': "#98d8da"
                            }

        choice_colors={
        'day': "#466123",
        'night': "#145644",
        'sunset': "#69652f",
        'prologue': "#496463"
                            }

        choice_colors_selected={                        
            'day': "#2a3b15",
            'night': "#0b3027",
            'sunset': "#42401e",
            'prologue': "#2d3d3d",
                        }

    window background Frame(get_image("gui/choice/"+persistent.timeofday+"/choice_box.png"),50,50) xfill True yalign 0.5 left_padding 50 right_padding 50 bottom_padding 50 top_padding 50:

        has vbox xalign 0.5

        for caption, action, chosen in items:
            if action and caption:

                button background None:
                    action action
                    if caption in persistent.choices and caption != "Налево" and caption != "Направо" and caption != "Go left" and caption != "Go right":
                        text caption font "fonts/corbel.ttf" size 38 hover_size 38 color choice_colors_selected[persistent.timeofday] hover_color choice_colors_hover[persistent.timeofday] xcenter 0.5
                    else:
                        text caption font "fonts/corbel.ttf" size 38 hover_size 38 color choice_colors[persistent.timeofday] hover_color choice_colors_hover[persistent.timeofday] xcenter 0.5
            else:
                text caption font "fonts/corbel.ttf" size 38 color choice_colors[persistent.timeofday]


init:
    $ filters["widget__filename_7dl"] = u"(GUI)Текущая строка кода"
    $ filters["widget__music_7dl"] = u"(GUI)Текущая музыка"
    $ filters["widget__images_7dl"] = u"(GUI)Текущие изображения"

translate english strings:
    old "(GUI)Текущая строка кода"
    new "(GUI)Current source line"
    old "(GUI)Текущая музыка"
    new "(GUI)Current music"
    old "(GUI)Текущие изображения"
    new "(GUI)Current images"

init python:
    widget_overlay_set = []
    widget__filename_7dl = lambda: widget_overlay_set.append(("src",widget__filename_inner))
    widget__music_7dl    = lambda: widget_overlay_set.append(("♪♫♬",widget__music_inner))
    widget__images_7dl   = lambda: widget_overlay_set.append(("img",widget__images_inner))

    def widget__filename_inner():
        import os
        fullfn, line = renpy.get_filename_line()
        return [ "%s:%d" % (os.path.basename(fullfn), line) ]

    def widget__music_inner():
        m = renpy.music.get_channel("music").get_playing()
        if  m:
            return [ m.split("/")[-1].replace(".ogg","").replace(".mp3","") ]
        return []

    def widget__images_inner():
        return [" ".join(x.name) for x in renpy.display.core.scene_lists().layers["master"]]

init 9999 python:
    if  widget_overlay_set:
        def editoverlay():
            ui.vbox(xpos=config.screen_width, xanchor=1.0, ypos=2)
            for  k,f in widget_overlay_set:
                for v in f():
                    ui.hbox()
                    ui.button(clicked=None, xpadding=6, xminimum=50)
                    ui.text(k, style="button_text", size=14)
                    ui.button(clicked=None, xpadding=6, xminimum=300)
                    ui.text(v, style="button_text", size=14)
                    ui.close()
            ui.close()
        config.overlay_functions.append(editoverlay)