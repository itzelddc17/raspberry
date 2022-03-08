import RPi.GPIO as GPIO
BUTTON_GPIO = 16
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    """while True:
        GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING)
        print("You've pressed the Button!")"""

    while True:
        GPIO.wait_for_edge(BUTTON_GPIO, GPIO.BOTH)
        if not GPIO.input(BUTTON_GPIO):
            print("You've pressed the Button!")
        else:
            print("You've released the Button!")
