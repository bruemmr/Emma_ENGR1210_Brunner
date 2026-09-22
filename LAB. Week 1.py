#SECTION 1: ANCHOR - Timing Constants

#DESCRIPTION: Title section.
print("=" * 52)
    # This line is printing... 52 equal signs to create a visual seperatioon between its next line and previous line.
print("SECTION 1: ANCHOR - Timing Constants")
    # This line is printing the string "SECTION 1: ANCHOR - Timing Constants".
print("=" * 52)
    #This line is printing the equal sign 52 times to create a visual seperatioon between its next line and previous line.
        # What is morse code timing? Timing Ratios
        # The (.) dot/dit is the base unit.
        # Standard timing ratios are as follows:
         # 1 unit = dot/dit
            # 3 units = dash/daah
            # 1 Unit = pause between dots/dashes in a character
            # 3 Units = pause between letters
            # 7 units = pause between words
        # Base unit in milliseconds (ms)
#DESCRIPTION: definition of base unit & table column names.
DOT_MS = 100 #base unit: one dot = 50ms
DASH_MS = DOT_MS * 3 # one dash = 150ms
SYMBOL_GAP_MS = DOT_MS * 1 #gap within a character = 50ms
LETTER_GAP_MS = DOT_MS * 3 #gap between letters = 150ms
WORD_GAP_MS = DOT_MS * 7 #gap between words = 350ms
    # These are all variables given a value to be used in the code.

#DESCRIPTION: timing table information.
print(f"\nBase unit (DOT_MS): {DOT_MS} ms")
    # This line is printing \n which creates a new line, the f-string "Base unit (DOT_MS): containing the variable in the the brackets, DOT_MS, and finishing the string with ms.
print(f"{'Symbol':<15} {'Duration':>10} ms {'Ratio':>8}")
    # This line is printing... The f-string that includes variables and shifting components. 
print("=" * 36)
    # This line is printing 36 equal signs to create a visual seperatioon between its next line and previous line.
print(f"{'dot':<15} {DOT_MS:>10}  {'1x':>8}")
    # This ine is printing... The f-string that includes variables and shifting components.
print(f"{'dash':<15} {DASH_MS:>10}  {'3x':>8}")
    # This line is printing... The f-string that includes variables and shifting components.
print(f"{'symbol gap':<15} {SYMBOL_GAP_MS:>10}  {'1x':>8}")
    # This line is printing... The f-string that includes variables and shifting components.
print(f"{'letter gap':<15} {LETTER_GAP_MS:>10}  {'3x':>8}")
    # This line is printing... the f-string that includes variables and shifting components.
print(f"{'word gap':<15} {WORD_GAP_MS:>10}  {'7x':>8}")
    # This line is printing... the f-string that includes variables and shifting components.

#DESCRIPTION: NOT FINISHED< THIS IS FOR WEEK 7
print("\n[LED] ON")
print("[LED] OFF")

# -- ANCHOR QUESTIONS (discuss with your partner before continuing) --------
# Q1. Change DOT_MS to 50. What happens to DASH_MS and WORD_GAP_MS?
    # Changing DOT_MS to 50ms changes all the other vairables tht are calculated from DOT_MS. DASH_MS becomes 150ms and WORD_GAP_MS becomes 350ms.
# Why does this work without changing any other lines? 
    # DOT_MS is the base unit and only itself and other variables containing it will chaning. All others stand on there because the variable is not being called.
# Q2. What does the :<15 in the f-string format specifier do?
    # The :<15 shifts the text to the left and, including the text, makes the total length of the str 15 characters long. So if the text for example is three charaacters long then the three characters + 12 spaces equals that 15. If the text is longer than the specified amount then it will still print the full text.
# Try changing 15 to 8 and observe what happens to the output.
    # The output showed that the text would not be shifted to the same amount evrything else was.
# Q3. Every other timing variable is calculated from DOT_MS instead of being typed in as a fixed number. Why is that safer than writing DASH_MS = 300 directly?
    # It is a safer and more efficent way to write those variables because, by having every variable connected to one variable, DOT_MS, means changing the one (base unit) you adjust the rest. This also means no math will have to be done by the programmer if they decide to change the base unit, so there is less of a chance of making a mistake.

#SECTION 2: GUIDED — Project Banner and Metadata

#DESCRIPTION: Title section.
print("\n" + "=" * 52)
print("SECTION 2: GUIDED — Project Banner and Metadata")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 2: GUIDED - Project Banner and Metadata", and another seperaton using equal signs.

#DESCRIPTION: Variable naming, to be used in project banner.
PROJECT_NAME = "Morse Code Translator" 
FIRST_NAME = "emma" 
LAST_NAME = "brunner" 
VERSION = "0.1.0"
TARGET_BOARD = "Pi Pico" 
ON_PC = True
ALPHABET_SIZE = 26 
    # These lines are variables which are each given a value.

#DESCRIPTION: Project banner. 
print("=" * 52)
print(f"{PROJECT_NAME} v{VERSION}")
print(f"{FIRST_NAME.title()} {LAST_NAME.title()}") 
print(f"Board: {TARGET_BOARD}")
    # These lines print the first part of the prject banner.
mode_str = "PC (VS Code)"
    # The variable mode_str is created and given the value "PC (VS Code)"
print(f"Mode: {mode_str}")
print(f"Alphabet: {ALPHABET_SIZE} letters") 
print("=" * 52)
    # These lines print the rest of the project banner.

#SECTION 3 — EXTENSION

#DESCRIPTION: 
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION — Transmission Time of One Letter")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 3: EXTENSION - Transmission Time of One Letter", and another seperaton using equal signs.
a_dot_part = DOT_MS
a_gap_part = SYMBOL_GAP_MS
a_dash_part = DASH_MS
a_total_ms = a_dot_part + a_gap_part + a_dash_part
    # The first three lines are variables which are each given a value. And the last line uses the addition symbol to add up the a_total_ms.
print(f"\nLetter A ( .- ):")
print(f" dot {a_dot_part}ms + gap {a_gap_part}ms + dash {a_dash_part}ms")
print(f" total = {a_total_ms}ms")
    # These lines print the letter choosen (a), the breakdown of the total ms and the value for total ms.
u_dot_part = DOT_MS
u_gap_part = SYMBOL_GAP_MS
u_dash_part = DASH_MS
u_total_ms = u_dot_part + u_gap_part + u_dot_part + u_gap_part + u_dash_part
    # The first three lines are variables which are each given a value. And the last line uses the addition symbol to add up the u_total_ms.
print(f"\nLetter U ( ..- ):")
print(f"dot {u_dot_part}ms + gap {u_gap_part}ms + dot {u_dot_part}ms + gap {u_gap_part}ms + dash {u_dash_part}ms")
print(f"total ={u_total_ms}ms")
    # These lines print the letter choosen (u), the breakdown of the total ms and the value for total ms.

# (Week 7: you will replace this hand-counting with a function that
# takes ANY pattern string and loops over it. For now, do it by hand —
# it makes the function you write later much easier to understand.)

# SECTION 4 — STRETCH

print("\n" + "=" * 52)
print("SECTION 4: STRETCH — Words-Per-Minute Speed")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 4: STRETCH — Words-Per-Minute Speed", and another seperaton using equal signs.
# 1.
# WPM = 1200 / DOT_MS (when DOT_MS is in milliseconds). WPM is words per minute

current_wpm = 1200 / DOT_MS
print(f"With DOT_MS at {u_dot_part}ms, WPM is at {current_wpm}")

# 2.
wanted_wpm = 5
calculated_dot_ms = 1200 / wanted_wpm
print(f"What DOT_MS would need to be to get {wanted_wpm} WPM, {calculated_dot_ms}ms")

# 3.
print("\n" + "-" * 52)
print("SPEED CARD: For Fixed Values")
print(f"\nFixed WPM           Needed DOT_MS")
print("=" * 52)

fixed_5 = 5
fixed_12 = 12
fixed_20 = 20
calculated_dot_ms_5 = 1200/fixed_5
calculated_dot_ms_12 = 1200/fixed_12
calculated_dot_ms_20 = 1200/fixed_20

print(f"{'5':>4} {calculated_dot_ms_5:>22} \n{'12':>5} {calculated_dot_ms_12:>21} \n{'20':>5} {calculated_dot_ms_20:> 21}")
print("=" * 52)

# Bonus: change DOT_MS at the top of the file from 100 to 50 and re-run.
# Confirm your WPM line updates automatically. Why does it? 
    # It updates because it is directly connected the the variable DOT_MS.
