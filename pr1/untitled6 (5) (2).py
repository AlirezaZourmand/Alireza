# Calculate the Hamming distance between two integers

# Input the two integers
integer_a = int(input("Enter the first integer: "))
integer_b = int(input("Enter the second integer: "))

# Calculate the Hamming distance
hamming_distance = bin(integer_a ^ integer_b)  # XOR to get the differing bits
hamming_distance_count = hamming_distance.count('1')  # Count the differing bits

# Output the Hamming distance
print("The Hamming distance between", integer_a, "and", integer_b, "is:", hamming_distance_count)
