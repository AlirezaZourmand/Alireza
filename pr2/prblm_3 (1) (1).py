def to_base_n(number, base):
    result = ""
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number //= base
    return result

def main():
    results = []
    invalid_base_count = 0

    while True:
        divisor_sum = 0
        n, b = map(int, input("Enter the number and base (space-separated): ").split())

        if n + b == -2:
            if invalid_base_count > 0:
                print('Invalid base!')
                return
            elif invalid_base_count == 0:
                break

        if b < 2 or b >= 10:
            invalid_base_count += 1

        # Calculate the sum of divisors
        for i in range(1, n + 1):
            if n % i == 0:
                divisor_sum += (n // i)

        # Convert the divisor sum to the given base and store the result
        results.append(to_base_n(divisor_sum, b))

    # Calculate the total sum of the converted results
    total_sum = sum(int(result, b) for result in results)
    print("Total sum of converted results:", total_sum)

if __name__ == "__main__":
    main()
