def is_armstrong(number):
    digits=str(number)
    num_digits=len(digits)
    armstrong_sum=sum(int(digit)**
    num_digits for digit in digits)
    return armstrong_sum==number
number=int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an armstrong number.")
else:
    print(f"{number} is not an armstrong number.")

print("Program by Diya Bhutani - 0221BCA041")
