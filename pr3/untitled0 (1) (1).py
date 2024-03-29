# -*- coding: utf-8 -*-
"""Extract and Sort Substrings

Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1erRbUp1Z8q44tbH5u_RX4jWeq1wSdbqK
"""

# Input the number of strings
num_strings = int(input("Enter the number of strings: "))
unique_substrings = set()  # Store unique substrings

# Extract '@' followed substrings from the input strings
for _ in range(num_strings):
    string = input("Enter a string: ")
    for i in range(len(string)):
        if string[i] == "@":
            unique_substrings.add(string[i + 1:])

unique_substrings.discard("1")  # Remove '1' if it exists
sorted_substrings = sorted(unique_substrings)  # Sort the unique substrings

# Output the sorted unique substrings
for substring in sorted_substrings:
    print(substring)
