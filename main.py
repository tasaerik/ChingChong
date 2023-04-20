Temperatur = 0

def on_button_pressed_a():
    global Temperatur
    Temperatur = input.temperature()
    basic.show_number(Temperatur)
    if Temperatur > 15:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.UMBRELLA)
input.on_button_pressed(Button.A, on_button_pressed_a)
