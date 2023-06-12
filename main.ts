radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        servos.P0.setAngle(30)
    } else if (receivedNumber == 0) {
        servos.P0.setAngle(90)
    }
})
radio.setGroup(1)
servos.P0.setAngle(90)
