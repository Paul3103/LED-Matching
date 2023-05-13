import machine
import utime
import random


def play_tone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)


def be_quiet():
    buzzer.duty_u16(0)


def initialize_leds(pin_numbers):
    return [machine.Pin(pin, machine.Pin.OUT) for pin in pin_numbers]


def choose_random_led(led_list):
    return random.choice(led_list)


def turn_on_led(led):
    led.value(1)


def turn_off_led(led):
    led.value(0)


def generate_random_delay():
    return random.uniform(0.1, 1)


def light_up_leds(led_list):
    for led in led_list:
        led.value(1)


def turn_off_all_leds(led_list):
    for led in led_list:
        led.value(0)


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

    turn_on_led(led1)
    delay = generate_random_delay()
    utime.sleep(delay)

    turn_on_led(led2)
    delay = generate_random_delay()
    utime.sleep(delay)

    turn_off_led(led2)
    turn_off_led(led1)

    if led1 == led2:
        play_tone(988)
        light_up_leds(leds)
        delay = generate_random_delay()
        utime.sleep(delay)
        be_quiet()
        turn_off_all_leds(leds)
    utime.sleep(1)