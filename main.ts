radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        servos.P0.setAngle(30)
        estadox = 1
    } else if (receivedNumber == 0) {
        servos.P0.setAngle(90)
        estadoy = 0
    }
})
input.onButtonPressed(Button.A, function () {
    logging = true
})
let estadoy = 0
let estadox = 0
let logging = false
radio.setGroup(1)
servos.P0.setAngle(90)
logging = false
datalogger.setColumnTitles(
"X",
"Y"
)
loops.everyInterval(1000, function () {
    if (logging) {
        datalogger.log(
        datalogger.createCV("X", estadox),
        datalogger.createCV("Y", estadoy)
        )
    }
})
