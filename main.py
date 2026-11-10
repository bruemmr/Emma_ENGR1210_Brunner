try:
    import hal_pico as hw
except ImportError:
    import hal_pc as hw

import morse_code

from morse_code import WORD_GAP_MS, DOT_MS, DASH_MS, SYMBOL_GAP_MS, LETTER_GAP_MS, encode_message

# The lines above import hal_pico.py if running on a real Pico, or hal_pc.py if running on a PC. 
# The rest of the program uses the same function names in either case, so it works without changing a line.

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
# The def blink_pattern() is a function that flashes a Morse code pattern. Within it, it has a for loop that iterates through each symbol in the pattern. 
# Depending on whether the symbol is a dot, dash, or space, it sets the duration for which the LED should be on and off. 
# The time duration for a dot is DOT_MS, for a dash is DASH_MS, and for a space is WORD_GAP_MS.
# It is also to be noted that the hw.set_led_timed(False, word_gap_ms) is used to turn off the LED for the duration of a word gap when a space is encountered in the pattern.
# Where as the hw.set_led_timed(True, on_ms) is used to turn on the LED for the duration of a dot or dash, and hw.set_led_timed(False, SYMBOL_GAP_MS) is used to turn off the LED for the duration of a symbol gap after each dot or dash.

def send_message(message):

    morse_patterns = encode_message(message)

    print("Morse code:", morse_patterns)

    for pattern in morse_patterns:
        blink_pattern(pattern)
        hw.set_led_timed(False, LETTER_GAP_MS)

# The def send message() is a function that takes a message string as input, encodes it into Morse code patterns using the encode_message() function, 
# and then sends each pattern by calling the blink_pattern() function.

def receive():
# def receive() is a function that reads the light signal from the photoresistor and decodes it back into a message string.

    decoded_message = ""
    current_pattern = ""
    # These two lines create variables decoded_message and current_pattern that have the value of empty strings.

    on_count = 0
    off_count = 0
    # These two lines create variables on_count and off_count with a value of zero. They will be used to count the number of consecutive samples where the light is on or off, respectively.
    # Samples are taken at a regular interval defined by morse_code.SAMPLE_MS, which is 5 milliseconds.

    previous_light = False
    # This line creates a variable previous_light with a value of False. It will be used to keep track of whether the light was on or off in the previous sample.

    
    dot_reads = int(morse_code.DOT_MS / morse_code.SAMPLE_MS)
    # The line dot_reads = int(morse_code.DOT_MS / morse_code.SAMPLE_MS) outputs the number of samples that correspond to the duration of a dot in Morse code.
    
    letter_gap_reads = dot_reads * 2
    word_gap_reads = dot_reads * 5
    # The two lines above calculate the number of samples that correspond to the duration of a letter gap and a word gap in Morse code, respectively.
    
    end_reads = dot_reads * 14
    # This line calculates the number of samples that correspond to a long period of darkness, which is used to determine when to stop receiving the message.

    while True:
        # The while True: loop continuously reads the light signal from the photoresistor until a long period of darkness is detected, indicating the end of the message.
        
        value = hw.read_u16()
        
        
        light_on = value > 500
        # This line determines whether the light is on or off based on the value read from the photoresistor. If the value is greater than 500, 
        # it is considered that the light is on; otherwise, it is off.

        if light_on:
            if not previous_light:
                if off_count > 0:
                    if off_count >= word_gap_reads:
                        if current_pattern != "":
                        # != means "not equal to". This line checks if the current_pattern variable is not an empty string.

                            decoded_message = decoded_message + morse_code.decode_pattern(current_pattern)
                            current_pattern = ""

                        if decoded_message != "" and decoded_message[-1] != " ":
                        # != means "not equal to". and decoded_message[-1] != " " checks if the last character of the decoded_message is not a space.

                            decoded_message = decoded_message + " "

                    elif off_count >= letter_gap_reads:
                    # This line checks if the off_count is greater than or equal to the number of samples that correspond to a letter gap in Morse code.

                        if current_pattern != "":
                            decoded_message = decoded_message + morse_code.decode_pattern(current_pattern)
                            current_pattern = ""
                off_count = 0
            on_count = on_count + 1

        else:
            if previous_light:
                # Determine whether the signal was a dot or dash

                if on_count < dot_reads * 2:
                    current_pattern = current_pattern + "."
                else:
                    current_pattern = current_pattern + "-"
                on_count = 0

            off_count = off_count + 1

            if off_count >= end_reads:
                break

        previous_light = light_on
        # ALL lines from 86 to 125 are used to read the light signal from the photoresistor and decode it into Morse code patterns. 
        # The logic checks for transitions between light on and off states, counts the duration of each state, and determines whether the signal 
        # corresponds to a dot, dash, letter gap, or word gap. The decoded message is built up as the signal is processed.
        
        hw.sleep_ms(morse_code.SAMPLE_MS)
        # This line pauses the execution of the loop for a duration defined by morse_code.SAMPLE_MS (5 milliseconds) before taking the next sample from the photoresistor.
    
    if current_pattern != "":
        decoded_message = decoded_message + morse_code.decode_pattern(current_pattern)
    # The above two lines check if there is any remaining Morse code pattern in current_pattern after the loop ends. 
    # If there is, it decodes that pattern and appends the corresponding character to decoded_message.

    return decoded_message
    # The return statement returns the fully decoded message string to the caller of the receive() function.

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
# Frome line 145 to 177 is the main loop of the program that allows the user to choose between sending or receiving a Morse code message.