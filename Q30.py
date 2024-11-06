# print('Pattern 1')
for i in range(1,6):
    print('* ' * i)

# print('\nPattern 2')
for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# print('\nPattern 3')
for i in range(1,6):
    for j in range(1, i + 1):
        print(i, end=' ')
    print()

print('\nPattern 4')
for i in range(5,0,-1):
    for j in range(1, i+1):
        print('*', end=' ')
    print()

# print('\nPattern 5')
for i in range(5,0,-1):
    for j in range(5,5-i,-1):
        print(j, end=' ')
    print()
#
# print('\nPattern 6')
for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()
# print('\nPattern 7')
for i in range(1, 6):
    print(" " * (5 - i) * 2, end="")
    print("* " * i)

# print('\nPattern 8')
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

# print('\nPattern 9')
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * i)


print("Program by Diya Bhutani - 0221BCA041")