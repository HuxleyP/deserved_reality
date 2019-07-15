label dr_debug_sandbox:
    $ dr_forgeteveryone()
    $ name_dr("Иван")
    $ day_time()
    $ dr_mode_adv()
    scene bg ext_road_day
    dr_uv "Я незнакомка."
    $ dr_meet("dr_uv", "Юля")
    dr_uv "Я Юля."
    $ dr_meet("dr_uv", "Харон")
    dr_uv "Я Харон."
    $ dr_meet("dr_uv", "Юля")
    $ dr_mode_nvl()
    dr_uv "Я Юля в новелле."
    $ dr_meet("dr_uv", "Харон")
    dr_uv "Я Харон в новелле."
    dr_th "Я мысли героя."
    "А я рассказчик."
    "Всё хорошо?"
    menu:
        "Да":
            $ dr_mode_adv()
            dr_uv "Ну и хорошо. Дай поспать-то!"
            $ dr_meet("dr_uv", "Кошка драная")
            ivan "А ну вернись, Кошка драная!"
            dr_uv "Ой, а кто это? Неужели Иван?"
            ivan "Откуда ты... Нет, Я - это Я!"
            $ name_dr("Я")
            dr_uv "Да ну? Прям \"Я?\""
            $ name_dr("Ваня")
            ivan "Ну... Да."
            dr_uv "Понятно всё с тобой. Иди отдыхать, Ваня."

        "Нет":
            dr_uv "Нет?! Так переделывай!"
    $ dr_mode_adv()
    "Рассказчик стреляется."
    return