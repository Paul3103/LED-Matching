import machine
import utime
import random


def play_tone(frequency):
    # TODO: Implement the function to play a tone on the buzzer
    pass


def be_quiet():
    # TODO: Implement the function to turn off the buzzer
    pass


def initialize_leds(pin_numbers):
    # TODO: Implement the function to initialize LED pins
    pass


def choose_random_led(led_list):
    # TODO: Implement the function to choose a random LED from the list
    pass


def turn_on_led(led):
    # TODO: Implement the function to turn on the specified LED
    pass


def turn_off_led(led):
    # TODO: Implement the function to turn off the specified LED
    pass


def generate_random_delay():
    # TODO: Implement the function to generate a random delay
    pass


def light_up_leds(led_list):
    # TODO: Implement the function to light up all LEDs
    pass



# Define the GPIO pins connected to the LEDs
led_pins = []  # Replace pin1, pin2, pin3 with the actual GPIO pin numbers
for i in range(0, 28):
    if i != 18:
        led_pins.append(i)

# Set up the GPIO pins as output
leds = initialize_leds(led_pins)
buzzer = machine.PWM(machine.Pin(18))


while True:
    led1 = choose_random_led(leds)
    led2 = choose_random_led(leds)

    #TODO: turn both LEDs on, wait and see if they are the same LED

    if led1 == led2:
        #TODO: if they are the same, light up all the leds and play a buzzer sound