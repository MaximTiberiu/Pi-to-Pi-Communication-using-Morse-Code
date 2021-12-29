import RPi.GPIO as GPIO
import time
from morsecodelibrary.morsecode import text_to_code

led_pin = 6
standard_time_unit = 0.2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)


def led_off(pin_number):
    GPIO.output(pin_number, GPIO.LOW)


def led_on(pin_number):
    GPIO.output(pin_number, GPIO.HIGH)


def wait(custom_time):
    time.sleep(custom_time)


def text_to_signal(text):
    code = text_to_code(text)
    led_off(led_pin)

    for signal in code:
        if signal == '.':
            led_on(led_pin)
            wait(standard_time_unit)
            led_off(led_pin)
            wait(standard_time_unit)
        elif signal == '-':
            led_on(led_pin)
            wait(standard_time_unit * 3)
            led_off(led_pin)
            wait(standard_time_unit)
        elif signal == '_':
            led_off(led_pin)
            wait(standard_time_unit * 2)
        elif signal == '|':
            led_off(led_pin)
            wait(standard_time_unit * 6)


def transmitter_main():
    led_off(led_pin)
    wait(10)

    text = input("Text: ")
    text_to_signal(text)
