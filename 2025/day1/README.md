# Password Dial Position Tracker

This solution set is designed to solve **Day 1 Advent of Code challenge (2025)**. 

This challenge simulates a rotating combination lock (0-99), and requires reading sequential turn instructions from a text file to determine a lock's password behavior.

This challenge involved two variations of password deduction, each dependant on how the dial interacts with **position 0**. 

---

## Problem Summary
Analyze the document and utilize the rotation sequence to determine the correct password. Starting position and lock behavior is consistent in both challenges, but the password is obtained following different instructions.
- Inital `position = 50`
- Rotation sequence can be found in attached document, where `L` or `R` represents direction of rotation followed by a **distance** value indiciting the number of steps.  
    - `"L10"` ->  rotation `left` **10** spaces
    - `"R5"` -> rotation `right` **5** spaces 
- The circular behavior of the dial creates a range of 100 (0-99), rotation that exceeds this range results in the the dial to wrap around continueing movement
    - `"L1"` from position **0** -> dial position **99**
    - `"R1"` from position **99** -> dial position **0**

---

## Concepts Demonstrated
**Python file handling**
- `Path(__file__).parent` -> ensures file path reliability 
- `with open()` -> safe external file read

**String parsing logic**
- `line.strip` -> cleaning read values
- `line[0]` -> extract `"L"` and `"R"` (direction) 
- `int(line[1:])` -> extract rotation / distance

**Algorithmic techniques**
- Modular arithmetic -> `(position +/- distance) & 100`
- State tracking variables -> `position` + `zero_count`
- Two-pass problem solving -> Iterative refinement (Part 1 -> Part 2)

---

## Files

### `"part1.py"` 
Inital logic: determine the number of times the rotation leads to the dial pointing to **0**

### `"part2.py"` 
Extended logic: The number of times the dial interacts with position **0**, either landing on or passing during rotation

### `"input.txt"` 
Turn instruction document containing rotation sequence

---

