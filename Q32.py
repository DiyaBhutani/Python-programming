def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    total =sum(int(digit)** power for digit in num_str)
    return total == num
low_limit = int(input("Enter the lower limit of the range to check for armstrong number: "))
upp_limit = int(input("Enter the upper limit of the range to check for armstrong number: "))
counter =0
for i in range(low_limit,upp_limit +1):
    if is_armstrong(i):
        print(i)
        counter = counter + 1
        print(f"counter: {counter}")

print("Program by Diya Bhutani - 0221BCA041")
