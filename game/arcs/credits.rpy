label end_credits:
    $ _game_menu_screen = None
    show text ("{size=80}Credits\n\n{size=40}Writing\n{size=60}Ayanna Palmer\n\n{size=40}Art\n{size=60}Han Thi\n\n{size=40}Music\n{size=60}Matteo Staciarine\n\n{size=40}Programming\n{size=60}Luke Zeches\n\n{size=60}{size=40}Made using Ren'Py 7.4.10.2178\nfor the 2021 KSU Fall Game Jam\n\n\n{size=60}A MAHL.GG production") at Move((0.5, 2.5), (0.5, 0.0), 20, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(20)
    show text ("{size=80}Thank you for playing!") with dissolve
    with Pause(3.5)
    $ _game_menu_screen = "save"
    scene bg black with fade

    return
