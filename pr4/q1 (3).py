# -*- coding: utf-8 -*-
"""Matrix Operations

Automatically generated by Colaboratory.
Original file is located at
https://colab.research.google.com/drive/1Qae81InDMn5k4x_eoTSzChiRhbxG9X5Y
"""

import numpy as np

# Read input from file
with open("input.txt", "r") as file:
    input_matrices = []
    first_line = True
    for line in file:
        if ''.join(filter(str.isdigit, line)):
            temp_data = line.replace("\n", "").split(" ")
            if first_line:
                first_line = False
                num_cols = int(temp_data[1])
                for _ in range(int(temp_data[0])):
                    input_matrices.append([])
            else:
                input_matrices[-1].append([float(x) for x in temp_data])

# Matrix operations
best_determinant = None
for i, matrix1 in enumerate(input_matrices):
    for j, matrix2 in enumerate(input_matrices[i + 1:], start=i + 1):
        result_matrix = np.matmul(np.array(matrix1).astype(float), np.array(matrix2).astype(float))
        determinant_value = float(np.linalg.det(result_matrix))
        if best_determinant is None or determinant_value > float(best_determinant["determinant"]):
            best_determinant = {
                "determinant": determinant_value,
                "m1": matrix1,
                "m2": matrix2
            }

# Comparison and rounding of result
if float(np.linalg.det(best_determinant["m1"])) > float(np.linalg.det(best_determinant["m2"])):
    final_multiplication = np.matmul(np.array(best_determinant["m1"]).astype(float), np.array(best_determinant["m2"]).astype(float))
elif float(np.linalg.det(best_determinant["m2"])) > float(np.linalg.det(best_determinant["m1"])):
    final_multiplication = np.matmul(np.array(best_determinant["m2"]).astype(float), np.array(best_determinant["m1"]).astype(float))
else:
    final_multiplication = np.matmul(np.array(best_determinant["m1"]).astype(float), np.array(best_determinant["m2"]).astype(float))

input_array = np.linalg.inv(final_multiplication)
input_array_rounded = np.round(input_array, decimals=3)
for row in input_array_rounded:
    print(" ".join(map("{:.3f}".format, row)))
