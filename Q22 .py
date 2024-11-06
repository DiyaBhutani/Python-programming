roll = (input("Roll_no: "))
name = (input("Name: "))
clas = (input("Class: "))

maths = int((input("Enter marks in maths:")))
english = int((input("Enter marks in english:")))
science = int((input("Enter marks in science:")))
sst = int((input("Enter marks in sst:")))
computer = int((input("Enter marks in computer:")))
Total= maths+english+science+sst+computer
print("______________________________________________")

print(f"Roll No: {roll}")
print(f"Name: {name}")
print(f"Class: {clas}")

print("______________________________________________")
print(f"Total          |100            |{maths}")
print(f"Total          |100            |{english}")
print(f"Total          |100            |{science}")
print(f"Total          |100            |{sst}")
print(f"Total          |100            |{computer}")
print("______________________________________________")
print(f"Total          |500            |{Total}")


marks = Total/5
if marks >= 80 :
    print(" Your grade is O")
elif marks >= 70 :
    print(" Your grade is A+")
elif marks >= 60 :
    print(" Your grade is A")
elif marks >= 50 :
    print(" Your grade is B+")
elif marks >= 40 :
    print(" Your grade is C")
else:
    print(" Your grade is D \n you are fail")

print("Program by Diya Bhutani - 0221BCA041")
