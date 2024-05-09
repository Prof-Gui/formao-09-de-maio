def on_forever():
    basic.show_string("AOBA, EU SOU O GUI")
    basic.show_leds("""
        . # # # .
        # . # . #
        # # # # #
        . # . # .
        . # # # .
        """)
    basic.pause(100)
    basic.clear_screen()
basic.forever(on_forever)
