# -*- coding: utf-8 -*-
"""Text Formatting

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bTHrmvMCJg6DlqutZnc8mfq5cxldrcv9
"""

import re

# Input text and clean up the formatting
input_text = input("Enter the text to format: ")
formatted_text = re.sub(r' +', ' ', input_text.strip())  # Replace multiple spaces with a single space
formatted_text = re.sub(r"\\n", "\n", formatted_text)  # Replace '\n' with a newline character

# Process @ and #
result = []
at_count = 0
for character in formatted_text:
    if character == '@':
        result.append('@')
        at_count += 1
    elif character == '#' and at_count > 0:
        at_count -= 1
    else:
        result.append(character)

# Combine the processed characters into the final formatted text
final_text = ''.join(result)

# Output the formatted text
print('Formatted Text:', final_text)
