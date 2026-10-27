# bug_week7.py
# BUG OF THE WEEK - Week 7: Functions
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Bug 1: Find with the console error message.
# Bug 2: Find with the VS Code Debugger.
# Bug 3: Find with the VS Code Debugger + test cases.
# Bug 4: Can ONLY be found by a thoughtful test case —
#         the one the test file (test_week7.py) will catch.
#
# ============================================================
# STANDARD DEBUGGING PROCESS (review):
#   STEP 1: Run — read error type and line number.
#   STEP 2: Fix ONE bug, save, run again.
#   STEP 3: Repeat until no crashes.
#   STEP 4: CHECK YOUR OUTPUT. Running != correct.
#
# VS CODE DEBUGGER (review):
#   Set breakpoint : click gray margin left of line number
#   Start          : F5  ->  Python File
#   Step Into      : F11  <- NEW THIS WEEK: follows execution
#                          INSIDE the function body
#   Step Over      : F10  (run current line, pause on next)
#   Continue       : F5
#   Stop           : Shift+F5
#   Variables panel: left sidebar while paused


# NEW THIS WEEK: THE TEST FILE
#
# A second file — test_week7.py — IMPORTS this file as a
# module and checks each function: it calls the function,
# compares the result to the expected answer with
# if / elif / else, and prints PASS or FAIL.
#
# To run the tests:
#   Open test_week7.py and click Run  — OR —
#   in the VS Code terminal, from the folder holding both files,
#   type: python test_week7.py   and press Enter.
#
# PASS = the function gave back exactly what was expected
# FAIL = it didn't — the line shows what was expected
#        and what the function actually gave back.
#
# Bug 4 in this file will PASS a visual check of the output.
# It will only be caught by one specific test (TEST 8).
# Run the tests, read the FAIL line, and trace back
# to the function to find and fix the bug.
#
# ============================================================
# NEW THIS WEEK: THE  if __name__ == "__main__"  GUARD
#
# Notice that all the demo calls (the print statements that
# show each function in action) now live at the BOTTOM of this
# file, inside a block that starts with:
#
#     if __name__ == "__main__":
#
# Here is why. test_week7.py needs to IMPORT this file to get
# at your functions. When Python imports a file, it runs every
# line in it from top to bottom. Without this guard, importing
# bug_week7.py would also run all the demo calls — including the
# ones with bugs in them. If one of them crashed, the test file
# would never even get to run your tests.
#
# The guard means: "only run the demo code when this file is
# run DIRECTLY (python bug_week7.py), NOT when it is imported."
#   - You run it directly  -> demos run, you see the bugs.
#   - test_week7.py imports it -> demos are skipped, tests run cleanly.
#
# This is the bridge between a standalone script and a reusable
# module. You'll use this same pattern in the in-class project.
# ============================================================


# ============================================================
# BUG 1 — The student_id argument is missing from the function call. To fix it I added the student_id argument to the function call in the demo block. The corrected line is:
# label = format_student("jordan", "smith", "S001")

def format_student(first_name, last_name, student_id):
    """Return a formatted student label."""
    return f"{last_name.title()}, {first_name.title()}  (ID: {student_id})"


# ============================================================
# BUG 2 — The function format_schedule() is missing the student_name argument in the function call. To fix it I added the student_name argument to the function call in the demo block. The corrected line is:
# return result = f"Schedule for {student_name.title()}:\n"

def format_schedule(student_name, course_list):
    """Return a formatted schedule string for a student."""
    result = f"Schedule for {student_name.title()}:\n"

    if not course_list:
        result += "  No courses scheduled.\n"
    else:
        for course in course_list:
            result += f"  - {course}\n"

    return result
# MAKE A PRINT FOR EMPTY COURSE LIST
# ============================================================
# BUG 3 — To fix this bug I changed the discount calculation from 20% to the actual discount_percent passed to the function. The corrected line is:
# discounted = price - (price * discount_percent / 100)
#
#   | Test Case        | price  | discount | Expected  | Actual | Pass? |
#   |------------------|--------|----------|-----------|--------|-------|
#   | A: 10% off $100  | 100.00 |   10     |   80.00   |  80.0  |  yes  |
#   | B: 0% (no disc.) | 100.00 |    0     |   100.00  |  100.0 |  yes  |
#   | C: 100% off      | 100.00 |  100     |     0.00  |  0.0   |  yes  |
#   | D: 20% off $50   |  50.00 |   20     |    40.00  |  30.0  |  No   |
#   | E: BOUNDARY 1%   | 100.00 |    1     |    99.00  |  99.0  |  yes  |

def apply_discount(price, discount_percent):
    """Return price after applying a percentage discount."""
    discounted = price - (price * discount_percent / 100) # The fix is here.
    return round(discounted, 2)


# ============================================================
# BUG 4 — Find with: TEST CASES (test_week7.py catches this)

def build_roster(course_name, students=None):
    """Return a roster dictionary for a course."""
    if students is None:
        students = []
    students.append("(enrolled)")
    return {course_name: students}

# ============================================================
# DEMO BLOCK 

if __name__ == "__main__":

    # --- Bug 1 demo ---
    print("--- Student Label ---")
    label = format_student("jordan", "smith", "S001") # The fix is here.
    print(label)

    # --- Bug 2 demo ---
    print("\n--- Course Schedule ---")
    name    = "maria"
    courses = ["Python", "Circuits", "Technical Writing"]
    schedule = format_schedule(name, courses)
    print(schedule)

    # --- Bug 3 demo: change the numbers to run the test cases ---
    print("\n--- Discount Calculator ---")
    result = apply_discount(100.00, 20)
    print(f"20% off $100.00 -> ${result}")

    # --- Bug 4 demo ---
    print("\n--- Course Roster ---")
    roster1 = build_roster("Python")
    print(roster1)
    roster2 = build_roster("Circuits")
    print(roster2)

 # --- Empty Course Roster ---
    print("\n--- Empty Course Roster ---")
    roster3 = build_roster("Empty Course", [])
    print(roster3)