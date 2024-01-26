# Convert input integers to binary and pad with zeros
binary_a = bin(int(input("Enter the first number: ")))[2:]
binary_b = bin(int(input("Enter the second number: ")))[2:]
padding_a = "0" * (32 - len(binary_a))
padding_b = "0" * (32 - len(binary_b))
combined_binary = padding_b + binary_b + padding_a + binary_a

# Check for specific bits
num_of_checks = int(input("Enter the number of checks:"))
for _ in range(num_of_checks):
    position = int(input("Enter the bit position to check:"))
    if int(combined_binary[-position - 1]) == 1:
        print("Bit at position", position, "is: yes")
    else:
        print("Bit at position", position, "is: no")
