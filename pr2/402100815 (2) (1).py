def main():
    # Get the operation and numbers as input
    operation = input("Enter the operation (sum, average, min, max, lcm, gcd): ")
    numbers = []
    print("Enter the numbers (type 'end' when finished):")
  
    # Collect input until 'end' is entered
    while True:
        user_input = input()
        if user_input != "end":
            numbers.append(int(user_input))
        else:
            break
  
    # Calculate the LCM and GCD
    def find_lcm(a, b):
        return a * b // math.gcd(a, b)
  
    lcm = functools.reduce(find_lcm, numbers)
  
    def find_gcd(numbers):
        gcd = numbers[0]
        for num in numbers[1:]:
            gcd = math.gcd(gcd, num)
        return gcd
  
    result = find_gcd(numbers)
  
    # Perform the specified operation
    if operation == "sum":
        print("Sum:", sum(numbers))
    elif operation == "average":
        print("Average:", round(sum(numbers) / len(numbers), 2))
    elif operation == "min":
        print("Minimum:", min(numbers))
    elif operation == "max":
        print("Maximum:", max(numbers))
    elif operation == "lcm":
        print("LCM:", lcm)
    elif operation == "gcd":
        print("GCD:", result)
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
