label sch_router:
    scene anim prolog2 with fade
    stop music fadeout 1
    stop ambience fadeout 1
    jump sch_dv_router

label sch_dv_router:
    if pt_dv >= 11 and sch_sabotage == 6:
        "Вот это выдался день - спасибо Алисе. Надеюсь, завтра будет ещё лучше."
        call sch_dv_vars
        $ routetag_sch = "dv_sab"
        return
    elif pt_dv >= 11 and sch_sabotage == -6:
        "Слишком много на меня за день, и всё из-за Алисы. Надеюсь, завтра будет лучше."
        call sch_dv_vars
        $ routetag_sch = "dv_peace"
        return
    elif pt_dv >= 11 and sch_sabotage < 6 and sch_sabotage > -6:
        call sch_dv_vars
        $ routetag_sch = "dv"
        jump sch_day4_dv_cr
        "Слишком много на Алису за этот день. Надеюсь, завтра будет лучше."
        return
    else:
        jump sch_sl_router

label sch_sl_router:
    if pt_sl >=11:
        "Мне снилась одна златовласка, которая сделала моё появление в лагере самым мягким и приятным."
        $ routetag_sch = "sl"
        call sch_sl_vars
        return
    else:
        jump sch_mi_router

label sch_mi_router:
    if pt_mi >=11:
        "Мне снился концертный зал и поющая голограмма, невидимая для меня в свету прожекторов."
        $ routetag_sch = "mi"
        call sch_mi_vars
        return
    else:
        jump sch_un_router

label sch_un_router:
    if pt_un >=11:
        "Мне снилось, как какая-то художница что-то рисовала на холсте фиолетовыми красками. Это был... я?"
        $ routetag_sch = "un"
        call sch_un_vars
        return
    else:
        jump sch_us_router

label sch_us_router:
    if pt_us >=8 and sch_sabotage == 5:
        "Я почти час не мог уснуть из-за зашкаливающего уровня адреналина в крови, а после лишь видел яркие красные искры."
        $ routetag_sch = "us"
        call sch_us_vars
        return
    else:
        jump sch_loner_router

label sch_loner_router:
    if noir_flag == 3:
        $ routetag_sch = "nr"
        call sch_nr_vars
        return
    else:
        $ routetag_Sch = "ln"
        call sch_ln_vars
        return









label sch_final_router:
    if routetag_sch == "dv_sab":
        jump sch_day4_dv_sabotage_cr
    elif routetag_sch == "dv_peace":
        jump sch_day4_dv_negotiator_cr
    elif routetag_sch == "dv":
        jump sch_day_dv_cr
    elif routetag_sch == "sl":
        jump sch_day4_sl_cr
    elif routetag_sch == "mi":
        jump sch_day4_mi_cr
    elif routetag_sch == "un":
        jump sch_day4_un_cr
    elif routetag_sch == "us":
        jump sch_day4_us_cr
    elif routetag_sch == "nr":
        jump sch_day4_nr_cr
    elif routetag_sch == "ln":
        jump sch_day4_ln_cr
    else:
        jump sch_router
