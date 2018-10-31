import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)  # set 26 as output for LED1
GPIO.setup(19, GPIO.OUT)  # set 19 as output for LED2
led1 = GPIO.PWM(26, 100)  # create object led for PWM on  port 25 at 100 hertz
led2 = GPIO.PWM(19, 100)
led1.start(0)             # start LED at 0 percent duty cycle (off)
led2.start(0)
pause_time = 0.02         # you can change this to speed/slow
# glowing eyes
GPIO.setup(20, GPIO.OUT)
GPIO.output(20, GPIO.HIGH)
# led hood
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.HIGH)

try:
        while True:
                for i in range(0, 101):  # 101 b/c it stops when it hits 100
                        led1.ChangeDutyCycle(i)
                        led2.ChangeDutyCycle(100-i)
                        sleep(pause_time)
                for i in range(100, -1, -1):  # from 100 to zero in steps of -1
                        led1.ChangeDutyCycle(i)
                        led2.ChangeDutyCycle(100-i)
                        sleep(pause_time)
except KeyboardInterrupt:
        led1.stop()     # stop the led PWM output
        led2.stop()
        GPIO.output(21, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        # noinspection PyArgumentList
        GPIO.cleanup()  # clean up the GPIO on exit
