# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is perfect
def is_perfect(n):
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    armstrong_sum = sum([int(digit) ** power for digit in num_str])
    return armstrong_sum == n

# Function to find the prime, perfect, and armstrong numbers smaller than input number
def find_special_numbers(n):
    prime = None
    perfect = None
    armstrong = None

    # Iterate backwards from n-1
    for i in range(n-1, 1, -1):
        if prime is None and is_prime(i):
            prime = i
        if perfect is None and is_perfect(i):
            perfect = i
        if armstrong is None and is_armstrong(i):
            armstrong = i

        # If we have found all three, we can stop
        if prime and perfect and armstrong:
            break

    return prime, perfect, armstrong

# Input number
number = int(input("Enter a number: "))

# Get the special numbers smaller than the input number
prime, perfect, armstrong = find_special_numbers(number)

# Print the results
print(f"Prime number just smaller than {number}: {prime}")
print(f"Perfect number just smaller than {number}: {perfect}")
print(f"Armstrong number just smaller than {number}: {armstrong}")

print("program by Diya Bhutani- 0221BCA041")