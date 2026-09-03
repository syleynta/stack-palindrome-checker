# Stack-Based Palindrome Checker & Number Base Converter

A Python program using stack data structures to solve two classic problems: 
checking whether a phrase is a palindrome, and converting decimal numbers to 
octal and hexadecimal.

## Features

**Palindrome Checker**
- Cleans input by removing spaces, punctuation, and capitalization
- Pushes characters onto a stack, then pops them off in reverse order to 
  compare against the original for a palindrome match

**Base Converter**
- Converts a decimal integer to its octal and hexadecimal equivalents
- Uses a stack to reverse the order of remainders from repeated division, 
  producing the correct final digit sequence

## What I Learned
This project showed how a stack's Last-In-First-Out (LIFO) behavior naturally 
solves problems that require reversing order — whether that's characters in a 
string or remainders in a division-based conversion algorithm.

## How to Run
python stack_project.py
