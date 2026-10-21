# Stack-Based Palindrome Checker & Number Base Converter

A Python project demonstrating stack operations through palindrome detection and decimal-to-octal/hexadecimal conversion. Created for a Data Structures course.

## Features

### Palindrome Checker

Checks whether a word or phrase reads the same forward and backward.

- Converts input to lowercase.
- Removes spaces, punctuation, and other non-alphanumeric characters.
- Pushes characters onto a stack and pops them for reverse-order comparison.
- Returns `True` for a palindrome and `False` otherwise.

**Examples:**
```text
Enter a word: racecar
True

Enter a word: A man, a plan, a canal: Panama!
True

Enter a word: python
False
```

### Number Base Converter

Converts positive decimal integers to octal (base 8) and hexadecimal (base 16).

- Uses repeated division and modulo arithmetic to calculate digits.
- Stores remainders in a stack.
- Pops remainders to construct the result in the correct order.
- Uses uppercase letters A–F for hexadecimal digits.

**Example:**
```text
Enter an integer number: 255
Octal: 377
Hex: FF
```

## How to Run

Requires Python 3. No additional packages are needed.

Run the following command from the folder containing the source file:

```bash
python stack-palindrome-checker.py
```

If your system uses `python3`:

```bash
python3 stack-palindrome-checker.py
```

The program first prompts for **10 words or phrases**, then prompts for **10 integers** to convert to octal and hexadecimal.

## Concepts Practiced

- Stacks and last-in, first-out (LIFO) behavior
- Python lists using `append()` and `pop()`
- String processing and normalization
- Loops, conditionals, and functions
- Integer division and modulo arithmetic
- Number base conversion

## Current Limitations

- The converter expects positive integers. Zero and negative integers currently produce empty results.
- Non-integer input during conversion causes an error.
- Input consisting only of punctuation or spaces is treated as a palindrome because its cleaned form is empty.
