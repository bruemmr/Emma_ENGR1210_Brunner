# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 7 Lab: Functions  —  "THE GREAT REFACTOR"
# Chapter 8 — Python Crash Course, 3rd Edition
# =============================================================================

# Timing constants (these can stay here for now; they move to config in Week 8)
DOT_MS        = 100
DASH_MS       = DOT_MS * 3
SYMBOL_GAP_MS = DOT_MS * 1
LETTER_GAP_MS = DOT_MS * 3
WORD_GAP_MS   = DOT_MS * 7

from morse_codebook import CODEBOOK, ENCODE_MAP, DECODE_MAP
from morse_encoder import encode_message
from morse_decoder import decode_message
import hal_stub as hw

# =============================================================================
# STEP 4 (STRETCH — write a function + meet the HAL)


#         hw.set_led_timed(True, DOT_MS)     # LED on for a dot
#         hw.set_led_timed(False, SYMBOL_GAP_MS)
#     RUN. The HAL is WHY modules matter: swap hal_stub for a future hal_pico
#     (same function names, real pin code) and this program blinks a real LED
#     on a Pi Pico — changing ONE import line and nothing else.
# ============================================================================
print("=" * 52)
print("Morse Translator — Week 7 refactor")
print("=" * 52)
# encode + decode (these calls do NOT change as you refactor — that is the whole point: same behavior, tidier code)
print("\n-- encode / decode --")
for word in ["SOS", "HELLO"]:
    enc = encode_message(word)
    print(f"  {word:6} -> {enc} -> '{decode_message(enc)}'")

# transmit the first letter of SOS — STEP 4 turns this into a function
print("\n-- transmit first letter of SOS --")

first = encode_message("SOS")[0]

def transmit_pattern(pattern):
    for symbol in pattern:
        if symbol == '.':
            print(f"  [LED] ON {DOT_MS}ms (dot), OFF {SYMBOL_GAP_MS}ms")
        elif symbol == '-':
            print(f"  [LED] ON {DASH_MS}ms (dash), OFF {SYMBOL_GAP_MS}ms")

    print(f"  [LED] OFF {LETTER_GAP_MS}ms (letter gap)")
transmit_pattern(first)
print(f"\nVS.")

def transmit_pattern(pattern):
    for symbol in pattern:
        if symbol == '.':
            hw.set_led_timed(True, DOT_MS)
            hw.set_led_timed(False, SYMBOL_GAP_MS)
        elif symbol == '-':
            hw.set_led_timed(True, DASH_MS)
            hw.set_led_timed(False, SYMBOL_GAP_MS)

    hw.set_led_timed(False, LETTER_GAP_MS)
transmit_pattern(first)
# =============================================================================
# CHECKLIST
#   [ ] Ran the BEFORE version and noted the output
#   [ ] STEP 1: codebook moved to morse_codebook.py; output unchanged
#   [ ] STEP 2: encode_message moved to morse_encoder.py; output unchanged
#   [ ] STEP 3: decode functions moved to morse_decoder.py; output unchanged
#   [ ] STEP 4A: wrote transmit_pattern() as a function
#   [ ] STEP 4B: transmit uses the HAL (hw.set_led_timed)
#   [ ] After every step I RAN the program and the output stayed the same
#   [ ] This file is now a short "main" that imports four modules
#

