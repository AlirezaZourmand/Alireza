# -*- coding: utf-8 -*-
"""Sum of Pairs

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bTHrmvMCJg6DlqutZnc8mfq5cxldrcv9
"""

# Input the list of numbers and the target sum
numbers_input = input("Enter the list of numbers separated by space: ")
target_sum = int(input("Enter the target sum: "))

# Process the input and find pairs with the target sum
numbers_list = numbers_input.split()
index_map = {}  # Map numbers to their indices
pairs_sum_indices = {}  # Map pair tuples to their sums

for index, number in enumerate(numbers_list):
    number = int(number)
    index_map[number] = index
    complement = target_sum - number
    if complement in index_map and complement != number:
        pair_sum_indices = index + index_map[complement]
        pairs_sum_indices[(min(number, complement), max(number, complement))] = pair_sum_indices

# Output the pair sums sorted
if not pairs_sum_indices:
    print("Not Found!")
else:
    sorted_pair_sums = sorted(pairs_sum_indices.values())
    for pair_sum in sorted_pair_sums:
        print(pair_sum)
