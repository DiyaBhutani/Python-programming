def is_prime(n):
    if n<=1:
       return False
    if n==2:
       return True
    if n%2==0:
       return False
    for i in range(3,int(n**0.5)+1,2):
             if n%i==0:
               return False
    return True
def sum_of_cubes_of_primes(start,end):
    sum_cubes=0
    for num in range(start,end+1):
        if is_prime(num):
            sum_cubes+=num**3
    return sum_cubes
start=int(input("Enter the start of the range:"))
end=int(input("Enter the end of the range:"))
result= sum_of_cubes_of_primes(start,end)
print(f"The sum of cubes of all prime numbers between {start} and {end} is {result}")
print("Program by Diya Bhutani - 0221BCA041")


            
