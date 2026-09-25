# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 4 Lab: if Statements
# Chapter 5 — Python Crash Course, 3rd Edition
#
# Standalone script. Still no functions, still no imports.
# New tool this week: if / elif / else. This is what lets us make
# DECISIONS — handle spaces, lowercase input, unknown characters, and
# decide what the "LED" should do for each symbol.
#
# (The LED is still just a printed line this week. Real hardware and a
#  swappable hardware module arrive in Week 7.)
# =============================================================================

# --- Carried forward from earlier weeks --------------------------------------
DOT_MS        = 100
DASH_MS       = DOT_MS * 3
SYMBOL_GAP_MS = DOT_MS * 1
LETTER_GAP_MS = DOT_MS * 3
WORD_GAP_MS   = DOT_MS * 7
    # The lines above create variables with the associated time increments for the morse code symbols.
CODEBOOK = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
]
    # The lines above create the list of tuples.
letters  = [pair[0] for pair in CODEBOOK]
patterns = [pair[1] for pair in CODEBOOK]
    # The lines above are variables with comprehensions that label the first position in a tuple as letters and the second position as patterns.

# =============================================================================
# SECTION 1 — ANCHOR
# =============================================================================
print("=" * 52)
print("SECTION 1: ANCHOR — Classifying a Symbol with if/elif/else")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 1: ANCHOR — Classifying a Symbol with if/elif/else", and another seperaton using equal signs.

test_symbols = ['.', '-', ' ', '*']
    # This line creates the variable test_symbols with a list.
print("\nClassifying symbols:")
    # This line prints a newline and the str, "Classifying symbols:".
for symbol in test_symbols:
    if symbol == '.':
        kind = 'dot'
    elif symbol == '-':
        kind = 'dash'
    elif symbol == ' ':
        kind = 'word_gap'
    else:
        kind = 'unknown'
    print(f"  '{symbol}' -> {kind}")
    # The lines above are a if/elif/else statement that sorts through the list, test_symbols, and associates the kind it falls under. It then prints the symbol and its kind on seperate lines.

# -- ANCHOR QUESTIONS ------------------------------------------------------
# Q1. The chain checks '.', then '-', then ' ', then else. What happens if
#     a symbol matches the FIRST branch — do the others still get checked?
    # The others do not get checked, because it matched based on the statements requirements.
# Q2. Why do we need the final 'else' (unknown)? What real input might land
#     there, and why is silently ignoring it safer than crashing?
    # The final else is needed because it gives value to the input that was asked to be read. Otherwise if it doesnt match with anything the interpreter might not know where to "put it." It is safer to ignore it because then you still have a place for it and it then doesnt harm anything.
# Q3. Could you rewrite this with three separate 'if' statements instead of
#     elif? Would the result be the same? Which is clearer?
    # You definetly could. The result may be the same depending one how it is written. By making multiple if statements however it lengthen the code ( Ex. more print statements, more else statements and so on).

# =============================================================================
# SECTION 2 — GUIDED
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 2: GUIDED — Encode a Message (with the messy cases)")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 2: GUIDED — Encode a Message (with the messy cases)", and another seperaton using equal signs.

message = "Hi Mom"     
message = message.upper()    

encoded = []
for character in message:
    if character == ' ':
        encoded.append(' ')
    elif character in letters:
        pattern = patterns[letters.index(character)]
        encoded.append(pattern)
    else:
        encoded.append('?')

print(f"\nEncoding '{message}':")
print(f"  result -> {encoded}")

# Expected once complete: ['....', '..', ' ', '--', '---', '--']

# =============================================================================
# SECTION 3 — EXTENSION
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION — Decide What the LED Does")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 3: EXTENSION — Decide What the LED Does", and another seperaton using equal signs.

print("\nTransmitting 'A' ( .- ):")
for symbol in '.-':
    if symbol == '.':
        print(f"  [LED] ON {DOT_MS}ms (dot), then OFF {SYMBOL_GAP_MS}ms")
    elif symbol == '-':
        print(f"  [LED] ON {DASH_MS}ms (dash), then OFF {SYMBOL_GAP_MS}ms")
print(f"  [LED] OFF {LETTER_GAP_MS}ms (letter gap)")

print("\nTransmitting 'S' ( ... ):")
for symbol in '...':
    if symbol == '.':
        print(f"  [LED] ON {DOT_MS}ms (dot), then OFF {SYMBOL_GAP_MS}ms")
    elif symbol == '-':
        print(f"  [LED] ON {DASH_MS}ms (dash), then OFF {SYMBOL_GAP_MS}ms")
print(f"  [LED] OFF {LETTER_GAP_MS}ms (letter gap)")

# =============================================================================
# SECTION 4 — STRETCH
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 4: STRETCH — A Grade-Style Boundary Check")
print("=" * 52)
measurements = [60, 110, 200, 260, 95, 305]

decoded = []

for measured in measurements:
    if measured <= 200:
        decoded.append('dot')
    elif measured <= 400:
        decoded.append('dash')
    else:
        print('noisy')

print(decoded)

    # The 200ms, I believs should go with dot, because in real applications it may be very difficult to get just before the 200ms mark. Adding the 200ms means if they just hit that mark it will still be qualified as a dot and not a dash.
    # I also wanted to not that I made the bounds for dash up to 400 because if dot is in the 200ms range then I believe the dash should have the same amount (a 200ms range).



# =============================================================================
# CHECKLIST
#   [ ] ANCHOR:    ran the classifier; answered Q1-Q3
#   [ ] GUIDED:    'Hi Mom' -> ['....', '..', ' ', '--', '---', '--']
#   [ ] EXTENSION: 'S' transmits as three dots + a letter gap
#   [ ] STRETCH:   (optional) dot/dash boundary decisions
#   [ ] I can explain why the first matching branch wins
#
# LOOKING AHEAD — Week 5
#   Next week: DICTIONARIES. Every letters.index() lookup you've written
#   gets replaced by an instant dictionary lookup, and you'll build a
#   reverse dictionary that decodes patterns straight back to letters.
# =============================================================================
