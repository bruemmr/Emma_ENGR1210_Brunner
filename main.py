try:
    import hal_pico as hw
except ImportError:
    import hal_pc as hw

import morse_code

from morse_code import WORD_GAP_MS, DOT_MS, DASH_MS, SYMBOL_GAP_MS, LETTER_GAP_MS, encode_message


def blink_pattern(pattern):

    # pattern is one letter, like '...'
    for symbol in pattern:
        if symbol == '.':
            on_ms = DOT_MS
        elif symbol == '-':
            on_ms = DASH_MS
        elif symbol == ' ':
            hw.set_led_timed(False, WORD_GAP_MS)
            continue
        else:
            continue

        hw.set_led_timed(True, on_ms)
        hw.set_led_timed(False, SYMBOL_GAP_MS)

    print("...done")


def send_message(message):

    # Convert the entire message into Morse code
    morse_patterns = encode_message(message)

    print("Morse code:", morse_patterns)

    # Flash each letter of the message
    for pattern in morse_patterns:
        blink_pattern(pattern)
        hw.set_led_timed(False, LETTER_GAP_MS)


def receive():

    decoded_message = ""
    current_pattern = ""

    on_count = 0
    off_count = 0

    previous_light = False

    # Calculate the number of samples in one timing unit
    dot_reads = morse_code.DOT_MS // morse_code.SAMPLE_MS

    # Set thresholds between the different gap lengths
    letter_gap_reads = dot_reads * 2
    word_gap_reads = dot_reads * 5

    # Allow extra darkness to detect the end of the message
    end_reads = dot_reads * 14

    while True:

        # Read the photoresistor
        value = hw.read_u16()

        # Determine whether the light is ON or OFF
        light_on = value > 500

        if light_on:

            # Detect when the light changes from OFF to ON
            if not previous_light:

                if off_count > 0:

                    # Check for a word gap
                    if off_count >= word_gap_reads:

                        if current_pattern != "":
                            decoded_message = decoded_message + morse_code.decode_pattern(current_pattern)
                            current_pattern = ""

                        # Add a space between words
                        if decoded_message != "" and decoded_message[-1] != " ":
                            decoded_message = decoded_message + " "

                    # Check for a letter gap
                    elif off_count >= letter_gap_reads:

                        if current_pattern != "":
                            decoded_message = decoded_message + morse_code.decode_pattern(current_pattern)
                            current_pattern = ""

                    # Short gaps are between Morse symbols

                off_count = 0

            on_count = on_count + 1

        else:

            # Detect when the light changes from ON to OFF
            if previous_light:

                # Determine whether the signal was a dot or dash
                if on_count < dot_reads * 2:
                    current_pattern = current_pattern + "."
                else:
                    current_pattern = current_pattern + "-"

                on_count = 0

            off_count = off_count + 1

            # Stop after a long period of darkness
            if off_count >= end_reads:
                break

        previous_light = light_on

        # Maintain a steady sampling rate
        hw.sleep_ms(morse_code.SAMPLE_MS)

    # Decode the final letter
    if current_pattern != "":
        decoded_message = decoded_message + morse_code.decode_pattern(current_pattern)

    return decoded_message


# =============================================================================
# THE MORSE CODE STATION
# =============================================================================

print("Board:", hw.board_info())
print("Morse station. Choose a mode each round.")

while True:

    mode = input("\n[s]end or [r]eceive? (blank to quit) ")
    mode = mode.strip().lower()

    if mode == "":
        break

    if mode == "s" or mode == "send":

        message = input("  message to SEND: ")
        message = message.strip().upper()

        if message != "":
            send_message(message)

    elif mode == "r" or mode == "receive":

        message = input("  message being sent to you: ")
        message = message.strip().upper()

        if message != "":
            hw.play(message)
            decoded = receive()
            print("  you received:", decoded)

    else:
        print("  please type s or r")

print("done.")
