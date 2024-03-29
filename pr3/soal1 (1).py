# -*- coding: utf-8 -*-
"""Sort and Print Strings

Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1erRbUp1Z8q44tbH5u_RX4jWeq1wSdbqK
"""

# Input a string containing space-separated words
input_string = str(input("Enter a space-separated string: "))

def sort_and_print_strings():
    # Split the string by spaces and sort based on the numeric part of each word
    words = input_string.split(' ')
    words.sort(key=lambda x: int(x[1:]))  # Sort based on the numeric part of each word
    for word in words:
        print(word[0], end='')

# Output the sorted and printed strings
sort_and_print_strings()
