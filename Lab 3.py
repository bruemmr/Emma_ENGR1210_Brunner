# SECTION 1: ANCHOR — Tuples and Looping the Codebook

#DESCRIPTION: Title Section:
print("=" * 52)
print("SECTION 1: ANCHOR — Tuples and Looping the Codebook")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 1: ANCHOR — Tuples and Looping the Codebook", and another seperaton using equal signs.

#DESCRIPTION: Codebook list.
CODEBOOK = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..')]
    # The lines above are creating the list CODEBOOK that containes tuples.

#DESCRIPTION: First eight of Codebook.
print("\nThe full codebook (first 8 rows):")
print(f"  {'Letter':<8}{'Pattern'}")
    # The lines above print a newline, string, and then the f-string.
print("  " + "-" * 18)
    #This prints space, dash pattern 18 long.
for letter, pattern in CODEBOOK[:8]:        # slice: just the first 8
    print(f"  {letter:<8}{pattern}")
    # Loop that recalls the first 8 letters and associated patterns and prints it as a list.
print(f"\nThe codebook has {len(CODEBOOK)} entries.")
    # Prints a f-string and includes the length of the Codebook.

# -- ANCHOR QUESTIONS ------------------------------------------------------
# Q1. Why is a tuple ('A', '.-') safer here than a list ['A', '.-']? (Hint: what should NEVER change about a codebook entry?)
    # A tuple is safer because it cannot be changed, where as in a list can be changed or edited, causing more errors to occur.
# Q2. "for letter, pattern in CODEBOOK" unpacks each tuple into two names. How is that different from "for entry in CODEBOOK"?
    # If you weren't to specify letter, pattern and just did entry you would output the whole tuple and not the individual values.
# Q3. CODEBOOK[:8] is a slice. What would CODEBOOK[-3:] give you?
    # Using CODEBOOK[-3] would output the last three tuples.

# SECTION 2: GUIDED — Encode a Whole Word with a Loop

#DESCRIPTION: Title Section.
print("\n" + "=" * 52)
print("SECTION 2: GUIDED — Encode a Whole Word with a Loop")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 2: GUIDED — Encode a Whole Word with a Loop", and another seperaton using equal signs.

#DESCRIPTION: Defining tuple.
letters  = [pair[0] for pair in CODEBOOK]
patterns = [pair[1] for pair in CODEBOOK]  
    # The lines above dont output anything but they define the first item in the tuple to be letters and the second term in the tuple to be patterns.

#DESCRIPTION: Decoding "Hello" 
word = "HELLO"          
    # Defines the variable word as "Hello"
encoded = []
    # Makes an empty tuple.
for character in word:
    position = letters.index(character)
    encoded.append(patterns[position])
    # Loop that reads a character gets its index position in letters then with that value it is then used as a index value in patterns to retreive the pattern at that position. This is then appended to encoded to create a list.
print(f"\nEncoding '{word}':")
print(f"  result -> {encoded}")
    # Lines above print a newline, "Encoding" and then the word associated to the variable word, and then "result ->" with the encoded output fron the loop.

# SECTION 3: EXTENSION — Comprehensions and Why Lookup Is Slow

#DESCRIPTION: Title Section.
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION — Comprehensions and Why Lookup Is Slow")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 3: EXTENSION — Comprehensions and Why Lookup Is Slow", and another seperaton using equal signs.

#DESCRIPTION: Decoding "AEIOU".
vowel_patterns = [pattern for (letter, pattern) in CODEBOOK if letter in 'AEIOU']
    # This line is a varible with the associated value that is a comprehensions. 
print(f"\nVowel patterns (A,E,I,O,U): {vowel_patterns}")
    # This line prints the f-string that contains a str and value associated with vowel_pattern.

#DESCRIPTION: Counting tuples.
counter = 0
for pair in CODEBOOK:
    counter += 1
    if pair[0] =='Z':
        break
    # The lines above create a loop with a if statement. It reads the pair/tuple in Codebook and then adds 1 to counter and it does that until the if statement is met.
print(f"\nCounted Python checks: {counter}")
    # This line prints the f-string that conatins a str and the value associated with counter.

# SECTION 4: STRETCH — Codebook Statistics

#DESCRIPTION: Title Section.
print("\n" + "=" * 52)
print("SECTION 4: STRETCH — Codebook Statistics")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 4: STRETCH — Codebook Statistics", and another seperaton using equal signs.

#DESCRIPTION: Statistics.
lengths = [len(pattern) for letter, pattern in CODEBOOK]
    # This line is a comprehension and it makes a list of the lengths of the patterns in codebook. 
srt_pattern = min(lengths)
lng_pattern = max(lengths)
    # The lines above create variables that have min and max len count for patterns.
srt_letter = [letter for letter, pattern in CODEBOOK if len(pattern) == srt_pattern]
lng_letter = [letter for letter, pattern in CODEBOOK if len(pattern) == lng_pattern]
    # The lines above are new variables that have comprehensions that determine what letters match the min and max len counts for patterns.
print(f"Shortest pattern lenth: {srt_pattern}\nLetters associated with lenth: {srt_letter}")
print(f"\nShortest pattern length: {lng_pattern}\n Letters associated with length: {lng_letter}")
    # These lines are f-strings that print descriptions and values for patterns and letters associated with them.
avg_pattern_length = sum(lengths)/len(CODEBOOK)
print(f"\nAverage pattern length: {avg_pattern_length}")
    # These define what avg_pattern_len is and prints a description and that value.
print(f"\nCodebook")
for i in range(len(CODEBOOK)):
    letter, pattern = CODEBOOK[i]
    print(f"{i+1}. {letter} {pattern}") 
    # These print the Codebook tuples into a counted list.
