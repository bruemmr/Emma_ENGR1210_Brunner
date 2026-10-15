# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 6 Lab: User Input and while Loops
# Chapter 7 — Python Crash Course, 3rd Edition
#
# Standalone script — the LAST week before "The Great Refactor."
# Still no functions and no imports. New tools: input() and while loops.
# This week your translator becomes INTERACTIVE, and you start turning
# measured signal durations back into dots, dashes, and gaps.
#
# NOTE: this file asks for keyboard input, so RUN it (F5) and type at the
# prompts. Type 'quit' to leave the loop.
# =============================================================================
CODEBOOK = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
]
ENCODE_MAP = {letter: pattern for (letter, pattern) in CODEBOOK}
DECODE_MAP = {pattern: letter for (letter, pattern) in CODEBOOK}

DOT_MS = 100


# =============================================================================
# SECTION 1 — ANCHOR
# =============================================================================
print("=" * 52)
print("SECTION 1: ANCHOR — An Interactive Encoder")
print("=" * 52)
print("Type a message to encode. Type 'quit' to stop.\n")
    # The lines above print the section header "SECTION 1: ANCHOR — An Interactive Encoder."

while True:
    text = input("Message> ")
    if text.lower() == 'quit':
        print("Goodbye!")
        break                    

    encoded = []
    for character in text.upper():
        if character == ' ':
            encoded.append(' ')
        else:
            encoded.append(ENCODE_MAP.get(character, '?'))
    print(f"  Morse: {' '.join(encoded)}\n")

# -- ANCHOR QUESTIONS ------------------------------------------------------
# Q1. What is the 'sentinel' value here, and what would happen if we forgot
#     the break? (Careful — that's an infinite loop. Use Ctrl+C to escape.)
    # The value is "quit". If we forgot the break, the loop would continue indefinitely.
# Q2. Why do we check text.lower() == 'quit' instead of text == 'quit'?
    # We use text.lower() to make the comparison case-insensitive.
# Q3. input() always returns a string. Why does that matter the moment you ask the user for a NUMBER (see the GUIDED section)?
    # It matters because input() will return a string, so if we expect a number, we need to convert it to an integer.

# =============================================================================
# SECTION 2 — GUIDED
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 2: GUIDED — Classify Received Signal Durations")
print("=" * 52)
    # The lines above print the section header "SECTION 2: GUIDED — Classify Received Signal Durations."

# The RECEIVER measures how long the light was ON or OFF, in milliseconds,
# and must decide what each measurement means. The boundaries are multiples
# of DOT_MS:
#     ON  pulse:   shorter than DOT_MS*2 (200ms) = dot,  otherwise dash
#     OFF gap:     shorter than DOT_MS*2 = symbol gap (within a letter)
#                  shorter than DOT_MS*5 (500ms) = letter gap
#                  DOT_MS*5 or longer = word gap


pulse_durations = [55, 105, 180, 240, 300]   # measured ON times (ms)
gap_durations   = [90, 150, 320, 480, 700]   # measured OFF times (ms)

print("\nPulse (LED ON) classification:")
for duration in pulse_durations:
    if duration < DOT_MS * 2:
        kind = "dot"
    else:
        kind = "dash"
    print(f"  {duration:4}ms -> {kind}")

print("\nGap (LED OFF) classification:")
for duration in gap_durations:
    if kind == "dot" or kind == "dash":
        kind = "symbol_gap"
    elif duration < DOT_MS * 5:
        kind = "letter_gap"
    else:
        kind = "word_gap"
    print(f"  {duration:4}ms -> {kind}")


# =============================================================================
# SECTION 3 — EXTENSION
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION — An Encode / Decode Menu")
print("=" * 52)
    # The lines above print the section header "SECTION 3: EXTENSION — An Encode / Decode Menu."

while True:
    print("\nMenu:")
    print("1) Encode text -> Morse")
    print("2) Decode Morse -> text")
    print("3) Quit")
    choice = input("Choose 1-3> ")
    # Above is the menu the user sees. 

    if choice == '1':
        encoded = []
        text = input("Text to encode> " ).upper()
        for character in text:
            if character == ' ':
                encoded.append('/')
            else:
                encoded.append(ENCODE_MAP.get(character, '?'))
        print(f"  Morse: {' '.join(encoded)}\n")

    elif choice == '2':
        decoded = []
        morse = input("Morse to decode> ")
        for token in morse.split():
            if token == '/':
                decoded.append(' ')
            else:
                decoded.append(DECODE_MAP.get(token, '?'))
        print(f"  Text: {''.join(decoded)}\n")
        
    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")




# =============================================================================
# SECTION 4 — STRETCH
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 4: STRETCH — Robust Numeric Input")
print("=" * 52)
    # The lines above print the section header "SECTION 4: STRETCH — Robust Numeric Input."

while True:
    user_input = input("How many times should I repeat the message? ")
    encoded = "HELLO" # Example encoded message for demonstration

    try:
        count = int(user_input)
        if count > 0:
            print(f"Repeating the message {count} times: {' '.join([encoded] * count)}")
            break
        else:
            print("Please enter a whole number greater than 0.")
    except ValueError:
        print("Please enter a valid whole number.")




