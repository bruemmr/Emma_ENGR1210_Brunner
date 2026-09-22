#SECTION 1: ANCHOR - Storing the Cookbook in Lists

(function) config: user.email "bruemmr@dunwoody.edu"

#DESCRPTION: Title section.
print("=" * 52)
print("SECTION 1: ANCHOR — Storing the Codebook in Lists")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 1: ANCHOR - storing the Codebook in Lists", and another seperaton using equal signs.

#DESCRIPTION: Defining the codebook (no visible attributes in the output).
letters  = ['A',  'B',    'C',    'D',   'E']
patterns = ['.-', '-...', '-.-.', '-..', '.']
    # The two lines above are creating variables that have lists as its value.

#DESCRIPTION: 
print(f"\nThe codebook currently has {len(letters)} letters.")
    # This line is printing on a newline, f-string "The codebook currently has 'length of the list letters' letters.".
print(f"First letter:  {letters[0]}  ->  {patterns[0]}")
    # This line is printing f-string "First letter: {pulling the letter associated with the position 0 in letters & the morse code pattern associated with the position 0}".
print(f"Last letter:   {letters[-1]}  ->  {patterns[-1]}")   # -1 = last item
    # Printing f-string "Last letter: {pulls the letter associated with the position -1 in letters & the morse code pattern associated with the position -1}".

#DESCRIPTION:
        # .index() finds WHERE a value sits in a list. 
c_position = letters.index('C')
    # This line is creating the variable, c-position and its value is the associated index value to the letter C in the list letters.
c_pattern  = patterns[c_position]
    # This line is creating the varible, c_pattern and its value is the pattern for C which is called forward from c_position.

print(f"\nLooking up 'C': it is at position {c_position}, pattern is '{c_pattern}'")
    # This line is printing on a newline, f-string "Looking up 'C': it is position {pulls the pattern for C}, pattern is '{pulls position number of the letter C}".

#DESCRIPTION: Growing the codebook with append().
letters.append('F')
patterns.append('..-.')
print(f"After adding F: {len(letters)} letters, last is {letters[-1]} -> {patterns[-1]}")
    # The lines above... Add F to the end of letters, adds f's pattern to the end of patterns, and prints the f-string.

# -- ANCHOR QUESTIONS ------------------------------------------------------
# Q1. Why must 'letters' and 'patterns' stay in exactly the same order?
    # The two list need to stay in the exact order because each postion in a list is defined by a number. They are basically invisible numbers that start with 0 and can go infinitly. So when having two list, like letters and patterns, if you want a value in one to associate with another in the other list you would want them to be in the same postion. EXAMPLE letters[0]= position 0 and that value could be MANGOS then 0 in patterns should be the associated value lets say FRUIT, Zero then equals MANGOS AND FRUIT, just in diferent lists.
# What breaks if you append to one list but forget the other? 
    # What ends up breaking for this code is the association to a item on a list will just not exist. So, for example deleting the patterns.append for f, the line 32 will still print the f-string, howoever the last value in the list of patterns that is actually associated for E will print for F.
# Q2. letters[-1] always gives the last item. Why is that handier than writing letters[4] when the list keeps growing?
    # It ends up being handier because there is no chance in error and it is just simply faster. Say you dont know the length of a list or dont know any contents of the list, instead of having to dive into finding information its a quick method that guarentees you are getting the last on the list, without using other methods or operations.
# Q3. .index('C') returns a number. What do you think happens if you call letters.index('Z') when 'Z' is not in the list? (Try it, read the error.)
    # Calling letter.index('Z') causes ValueError: list.index(x): x not in list.

#SECTION 2: GUIDED - Encode a Word by Hand

#DESCRIPTION: Title section.
print("\n" + "=" * 52)
print("SECTION 2: GUIDED — Encode a Word by Hand")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 2: GUIDED - Encode a Word by Hand", and another seperaton using equal signs.


#DESCRIPTION: Defining full codebook (no visible attributes in the output).
letters  = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
patterns = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---',
            '-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-',
            '..-','...-','.--','-..-','-.--','--..']
    # The lines above recreate the two variables to have large lists.

#DESCRIPTION: Letter count.
print(f"\nFull codebook loaded: {len(letters)} letters.")
    # This line prints a newline and says "Full codebook loaded: {prints the length of letters} letters."

#DESCRIPTION: Encoding the word "SOS" using three index lookups
s_pattern = patterns[letters.index('S')]
o_pattern = patterns[letters.index('O')]  
s2_pattern = patterns[letters.index('S')] 
    # The three lines above are creating three new variables and their values are the pattern outputted from the inner operation which is determining the number associated with the letter.

#DESCRIPTION: Printing the encoded 'SOS' one at a time.
print("\nEncoding 'SOS' by hand:")
print(f"  S -> {s_pattern}")
print(f"  O -> {o_pattern}")
print(f"  S -> {s2_pattern}")
    # These lines start with printing a newline and says "Encoding 'SOS' by hand:", next comes the print of each f-string that has its, letter and its variable with its value that is the pattern of the letter.

#DESCRIPTION: Printing encode 'SOS' at once.
sos_encoded = [s_pattern, o_pattern, s2_pattern]
    # This line defines a new variable that creates a list of the variables that associate with patterns.
print(f"\n  'SOS' encoded -> {sos_encoded}")
    # This line prints a new line and says the f-string "'SOS' encoded -> {calls for the varible created above}".

#SECTION 3: EXTENSION - Decode One Pattern Yourself

#DESCRIPTION: Title section.
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION — Decode One Pattern by Hand")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 3: EXTENSION - Decode One Pattern Yourself", and another seperaton using equal signs.
    
#DESCRIPTION: Decoding patterns to output letter associated. 
        # Encoding goes letter -> pattern. DECODING goes the other way:pattern -> letter. With parallel lists we just search the OTHER list.
decoded_position = patterns.index('-.-.')  
decoded_letter   = letters[decoded_position]
print(f"\nPattern '-.-.' is at position {decoded_position} -> letter '{decoded_letter}'")
    # These lines define two variables, decoded_position and decoded_letter, and prints out a f-sting that contain said variables values.
decoded_position = patterns.index('...')
decoded_letter = letters[decoded_position]
print(f"\nPattern '...' is at position {decoded_position} -> letter '{decoded_letter}'")
    # These lines define two variables, decoded_position and decoded_letter, and prints out a f-sting that contain said variables values.

# SECTION 4: STRETCH - List Slicing and Sorting

#DESCRIPTION: Title Section. 
print("\n" + "=" * 52)
print("SECTION 4: STRETCH — List Slicing and Sorting")
print("=" * 52)
    # These lines print a seperation using equal signs, a str that says "SECTION 4: STRETCH - List Slicing and Sorting", and another seperaton using equal signs. 

#DESCRIPTIONS: Slicing and sorting two lists.
print(f"\n{letters[:5]} \n{patterns[23:]}")
    # This line prints a newline, gives a list of the first five letters, prints another newline and then gives a list of the last 3 patterns.
letters.sort()
    # This method for lists, sorts the list.
print(letters)
    # They do match up. Prints the sorted list letters.
print(f"\n{"=" * 52}")

# The dangers that come with parallel lists is, two or more list solely depend on eachothers items locations. So if you modify one then that possibly changes the position but not the other. For example if you sorted letters and not patterns then the possible pattern and letter association may not exist anymore. Random letters would be matching up with random patterns.



