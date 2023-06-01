radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        servos.P0.setAngle(30)
    } else if (receivedNumber == 0) {
        servos.P0.setAngle(90)
    }
})
input.onGesture(Gesture.ScreenUp, function () {
    radio.sendNumber(0)
    basic.clearScreen()
})
input.onGesture(Gesture.TiltLeft, function () {
    radio.sendNumber(1)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
})
radio.setGroup(1)
servos.P0.setAngle(90)
