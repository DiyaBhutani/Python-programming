#Early Exit with return

def find_first_even(numbers):
 for n in numbers:
    if n % 2 == 0:
        return n
 return None
nums = [1, 3, 5, 8, 9]
first_even = find_first_even(nums)
print(first_even)
print("program by Diya Bhutani- 0221BCA041")

