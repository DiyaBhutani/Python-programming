#1. Positional Arguments

def greet(name, age):
 print(f"Hello, {name}! You are {age} years old.")
greet("Alice", 30) # Output: Hello, Alice! You are 30 years old.

#2. Keyword Arguments

def greet(name, age):
 print(f"Hello, {name}! You are {age} years old.")
greet(name="Alice", age=30) # Output: Hello, Alice! You are 30 years old.
greet(age=30, name="Alice") # Output: Hello, Alice! You are 30 years old.

#3. Default Arguments

def greet(name, age=25):
 print(f"Hello, {name}! You are {age} years old.")
greet("Alice") # Output: Hello, Alice! You are 25 years old.
greet("Bob", 30) # Output: Hello, Bob! You are 30 years old.

#4. Variable-Length Arguments

#Using *args
def sum_numbers(*args):
 return sum(args)
print(sum_numbers(1, 2, 3)) # Output: 6
print(sum_numbers(4, 5, 6, 7, 8)) # Output: 30

#Using **kwargs
def print_info(**kwargs):
  for key, value in kwargs.items():
   print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
print("program by Diya Bhutani- 0221BCA041")