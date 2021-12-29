import time
from morsecodelibrary.morsecode import code_to_text
from TSL2591 import tsl2951

standard_time_unit = 0.2

tsl = tsl2951.Tsl2591


def average_sensor_normal_value():
    total_time = 10
    avg_value = 0
    while total_time:
        full = tsl.get_full_luminosity()
        avg_value += full
        time.sleep(1)
        total_time -= 1
    return avg_value / 10


def signal_to_binary():
    normal_value = average_sensor_normal_value()
    binary = []
    low_count = 0

    stop_cond = False
    while not stop_cond:
        full = tsl.get_full_luminosity()
        if full > normal_value + 300:
            binary.append('1')
            low_count = 0
        else:
            binary.append('0')
            low_count += 1
        if low_count >= 10:
            stop_cond = True
        time.sleep(standard_time_unit)
    return ''.join(binary)


def binary_to_code(binary):
    prev_signal = binary[0]
    current_count = 0

    code = []

    for binary_signal in binary:
        if binary_signal == prev_signal:
            current_count += 1
        else:
            if prev_signal == '0':
                if current_count == 3:
                    code.append('_')
                elif current_count == 7:
                    code.append('|')
                current_count = 1
            elif prev_signal == '1':
                if current_count == 3:
                    code.append('-')
                elif current_count == 1:
                    code.append('.')
                current_count = 1
            prev_signal = binary_signal
    return ''.join(code)


def receiver_main():
    binary = signal_to_binary()
    code = binary_to_code(binary)
    text = code_to_text(code)
    print("TEXT: " + text)