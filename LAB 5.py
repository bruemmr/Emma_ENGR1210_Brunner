CODEBOOK = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
]
    # The lines above create a list of tuples, of letters and their associated pattern by using [] and ().

# =============================================================================
# SECTION 1 — ANCHOR
# =============================================================================
print("=" * 52)
print("SECTION 1: ANCHOR — The Encode Map")
print("=" * 52)
    # These lines print a header for Section 1, which is about the Encode Map.

ENCODE_MAP = {letter: pattern for (letter, pattern) in CODEBOOK}
    # The line above creates a variable with a comprehension that builds a dictionary from the list of tuples (CODEBOOK). 
    # The for (letter,pattern) in CODEBOOK reads over each tuple and unpacks it so that letter and pattern are available to used in this comprehension.
    # This unpacked tuple can then be used to create a dictionary with the letter: pattern key-value pair.

print(f"\nENCODE_MAP has {len(ENCODE_MAP)} entries.")
print(f"Looking up 'S': {ENCODE_MAP['S']}     (one step — no scanning!)")
print(f"Looking up 'O': {ENCODE_MAP['O']}")
    # The lines above are f-strings that print a newline, "ENCODE_MAP has (length of encode_map) entries." 
    # and then look up the letter 'S' and 'O' in the ENCODE_MAP dictionary and print their associated patterns.

            # -- Safe lookup with .get() -----------------------------------------------
            # ENCODE_MAP['@'] would CRASH with a KeyError. .get() returns a default
            # instead, which is perfect for "unknown character -> '?'".

print(f"Looking up '@': {ENCODE_MAP.get('@', '?')}   (.get returns '?' for unknowns)")
    # This line prints the f-string "Looking up '@': (the result of ENCODE_MAP.get('@', '?')) (.get returns '?' for unknowns)".

# -- ANCHOR QUESTIONS ------------------------------------------------------
# Q1. Last week a lookup for 'Z' scanned 26 entries. How many entries does ENCODE_MAP['Z'] check? Why doesn't dictionary size slow it down?
    # In the dictionary it uses the key directly to find the value, so it only checks one entry. It does not slow it down because it uses a hash table to 
    # store the key-value pairs.

# Q2. What is the difference between ENCODE_MAP['@'] and ENCODE_MAP.get('@', '?') ? When would each be the right choice?
    # Encode_MAP['@'] will raise a KeyError because '@' is not a key in the dictionary, while ENCODE_MAP.get('@', '?') will return '?' as a default value for unknown 
    # characters. Use ENCODE_MAP['@'] when the key exists and want to catch errors if it doesn't, and use ENCODE_MAP.get('@', '?') to handle unknown keys without 
    # raising an error.

# Q3. Why can a dictionary NEVER have the parallel-list bug from Week 2, where a letter and its pattern drift out of alignment?
    # A dictionary uses key-value pairs, so the letter is directly associated with the pattern. This prevents the parallel-list bug because of the association between 
    # the letters and patterns is maintained through the dictionary structure. So they cannot drift out of alignment.

# =============================================================================
# SECTION 2 — GUIDED
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 2: GUIDED — The Decode Map and a Round Trip")
print("=" * 52)
    # The lines above print a header for Section 2, which is about the Decode Map and a Round Trip.

DECODE_MAP = {pattern: letter for letter, pattern in ENCODE_MAP.items()}   
#ENCODE_MAP = {letter: pattern for (letter, pattern) in CODEBOOK}
    # The line above 

print(f"\nDECODE_MAP has {len(DECODE_MAP)} entries.")
    # This line prints the f-string "DECODE_MAP has (length of DECODE_MAP) entries."

# -- Encode a message using the dictionary ---------------------------------
message  = "SOS"

encoded  = []
for character in message.upper():
    if character == ' ':
        encoded.append(' ')
    else:
        encoded.append(ENCODE_MAP.get(character, '?'))
print(f"\nEncoded '{message}' -> {encoded}")

decoded_chars = []
for pattern in encoded:
    if pattern == ' ':
        decoded_chars.append(' ')
    else:
        decoded_chars.append(DECODE_MAP.get(pattern, '?'))

decoded = "".join(decoded_chars)
print(f"Decoded back  -> '{decoded}'")


# =============================================================================
# SECTION 3 — EXTENSION
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION — Round-Trip Check on a Phrase")
print("=" * 52)
    # These lines above print a header for Section 3, which is about Round-Trip Check on a Phrase.

phrase = "HI MOM"

encoded_phrase = []
for character in phrase.upper():
    if character == ' ':
        encoded_phrase.append(' ')
    else:
        encoded_phrase.append(ENCODE_MAP.get(character, '?'))
print(f"\nEncoded '{phrase}' -> {encoded_phrase}")

decoded_phrase_chars = []
for pattern in encoded_phrase:
    if pattern == ' ':
        decoded_phrase_chars.append(' ')
    else:
        decoded_phrase_chars.append(DECODE_MAP.get(pattern, '?'))
print(f"Decoded back  -> '{''.join(decoded_phrase_chars)}'")

# -- YOUR EXTENSION --------------------------------------------------------
# Decode 'encoded_phrase' back into text (remember: ' ' -> ' '). Then print whether the round trip matched the original uppercased phrase.
    # The round trip did match the all caps phrase. Even if the phrase came in with mixed case, the round trip would still match the original phrase 
    # because the encode function converts all characters to uppercase before encoding.

# =============================================================================
# SECTION 4 — STRETCH
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 4: STRETCH — Add the Digits, and Audit the Maps")
print("=" * 52)
    # This section prints a header for Section 4, which is about adding the digits and auditing the maps.

DIGITS_CODEBOOK = [
    ('0', '-----'), ('1', '.----'), ('2', '..---'), ('3', '...--'), ('4', '....-'),
    ('5', '.....'), ('6', '-....'), ('7', '--...'), ('8', '---..'), ('9', '----.'),
]
    # The lines above create a list of tuples, of digits and their associated pattern by using [] and ().

ENCODE_DIGITS_MAP = {letter: pattern for (letter, pattern) in DIGITS_CODEBOOK}
DECODE_DIGITS_MAP = {pattern: letter for letter, pattern in DIGITS_CODEBOOK}
    # The lines above turn the list of tuples into two dictionaries, one for encoding and one for decoding the digits.

print(f"\nENCODE_DIGITS_MAP has {len(ENCODE_DIGITS_MAP)} entries.")
print(f"\nDECODE_DIGITS_MAP has {len(DECODE_DIGITS_MAP)} entries.")


phrase = "SOS 911"

encoded_phrase = []
for character in phrase.upper():
    if character == ' ':
        encoded_phrase.append(' ')
    elif character in ENCODE_DIGITS_MAP:
        encoded_phrase.append(ENCODE_DIGITS_MAP[character])
    else:
        encoded_phrase.append(ENCODE_MAP.get(character, '?'))
print(f"\nEncoded '{phrase}' -> {encoded_phrase}")

decoded_phrase_chars = []
for pattern in encoded_phrase:
    if pattern == ' ':
        decoded_phrase_chars.append(' ')
    elif pattern in DECODE_DIGITS_MAP:
        decoded_phrase_chars.append(DECODE_DIGITS_MAP[pattern])
    else:
        decoded_phrase_chars.append(DECODE_MAP.get(pattern, '?'))
print(f"Decoded back  -> '{''.join(decoded_phrase_chars)}'")  


