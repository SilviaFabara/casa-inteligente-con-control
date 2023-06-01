def on_received_number(receivedNumber):
    if receivedNumber == 1:
        servos.P0.set_angle(30)
    elif receivedNumber == 0:
        servos.P0.set_angle(90)
radio.on_received_number(on_received_number)

def on_gesture_screen_up():
    radio.send_number(0)
    basic.clear_screen()
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_tilt_left():
    radio.send_number(1)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

radio.set_group(1)
servos.P0.set_angle(90)