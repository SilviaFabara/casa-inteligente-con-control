def on_received_number(receivedNumber):
    global estadox, estadoy
    if receivedNumber == 1:
        servos.P0.set_angle(30)
        estadox = 1
    elif receivedNumber == 0:
        servos.P0.set_angle(90)
        estadoy = 0
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global logging
    logging = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.set_group(1)
    if input.is_gesture(Gesture.SCREEN_UP):
        radio.send_number(0)
    elif input.is_gesture(Gesture.LOGO_DOWN):
        radio.send_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

estadoy = 0
estadox = 0
logging = False
radio.set_group(1)
servos.P0.set_angle(90)
logging = False
datalogger.set_column_titles("X", "Y")

def on_every_interval():
    if logging:
        datalogger.log(datalogger.create_cv("X", estadox),
            datalogger.create_cv("Y", estadoy))
loops.every_interval(1000, on_every_interval)
