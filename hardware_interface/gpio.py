import RPi.GPIO as GPIO


def setup_gpio():
    # Set up GPIO pins using RPi.GPIO or gpiozero

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.cleanup()


def set_gpio_mode(pin, mode):
    # Set the mode of a GPIO pin

    GPIO.setup(pin, mode)


def set_gpio_value(pin, value):
    # Set the value of a GPIO pin

    GPIO.output(pin, value)


def get_gpio_value(pin):
    # Get the value of a GPIO pin

    return GPIO.input(pin)
