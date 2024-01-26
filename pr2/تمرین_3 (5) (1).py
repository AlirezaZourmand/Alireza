# -*- coding: utf-8 -*-
"""Pascal's Triangle

Generates and prints Pascal's triangle.

Original file is located at
    https://colab.research.google.com/drive/1nYyWNwNNoWSbL3MMb0CfBXNvD-o-VA39
"""

def generate_pascals_triangle(rows):
    for line in range(1, rows + 1):
        coefficient = 1
        for i in range(1, line + 1):
            print(coefficient, end=" ")
            coefficient = int(coefficient * (line - i) / i)
        print("")

# Input the number of rows for Pascal's triangle
num_rows = int(input("Enter the number of rows for Pascal's triangle: "))
generate_pascals_triangle(num_rows)
