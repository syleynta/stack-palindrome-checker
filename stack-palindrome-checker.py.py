#Palindrome part
from inspect import stack
from operator import truediv


def palindromeCheck(phrase):
    stack = []
    phrase = phrase.lower()
    clean_phrase = ""
    for char in phrase:
        if char.isalnum():
            clean_phrase = clean_phrase + char

    for char in clean_phrase:
        stack.append(char)

    for char in clean_phrase:
        output = stack.pop()
        if char != output:
            return False
    return True   # only reached if every character matched

for i in range(10):
    word = input("Enter a word: ")
    print(palindromeCheck(word))





#Part 2 - Decimal to octal/hex using stack

def convertToBase (number, base):
    stack = []
    digits = "0123456789ABCDEF"
    output = ""

    while number > 0:
        remainder = number % base
        stack.append(remainder)
        number = number // base
    while stack:
        value = stack.pop()
        output = output + digits[value] #finds the corresponding character in digits
    return output

for i in range(10):
    num = int(input("Enter an integer number: "))
    octal = convertToBase(num, 8)
    hex = convertToBase(num, 16)
    print("Octal:", octal)
    print("Hex:", hex)
