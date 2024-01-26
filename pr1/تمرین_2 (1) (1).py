# Define a function to add two numbers using bitwise operations
def add_with_bitwise(x, y):
    while y != 0:
        carry = x & y  # Calculate the carry
        x = x ^ y  # Calculate the sum without the carry
        y = carry << 1  # Shift the carry to the left (to be added in the next iteration)
    return x

# Input the numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
target_sum = int(input("Enter the target sum: "))

# Add the numbers and check if the result matches the target sum
result = add_with_bitwise(num1, num2)
print("The result of adding", num1, "and", num2, "is:", result)

if result == target_sum:
    print("The result matches the target sum:", target_sum)
else:
    print("The result does not match the target sum:", target_sum)
