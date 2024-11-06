myAge= input("Enter your age")
myAge=int(myAge)
if myAge>=18:
    comm="You can vote"
else:
    if myAge>=10:
        comm="You are in middle school"
    else:
        if myAge>=6:
            comm="You are in primary school"
        else:
            comm="You are too small to learn python"
print("At age:" +str(myAge)+ "->" + comm)
print("Program by Diya Bhutani - 0221BCA041")