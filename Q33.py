def is_armstrong(num):
    num_str=str(num)
    power=len(num_str)
    total=sum(int(digit) ** power for digit in num_str)
    return total==num

num=int(input("Enter a number to start checking the Armstrong numbers from: "))
y=int(input("Enter the number of armstrong numbers you want to print: "))
count=0

while count<y:
      num+=1
      if is_armstrong(num):
          print(num)
          count+=1

print(f"Count: {count}")
print("Program by Diya Bhutani - 0221BCA041")
