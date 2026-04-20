# Day 2: Conditions and Loops

# 1. if-else example
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# 2. for loop example
print("\nNumbers from 1 to 5:")
for i in range(1, 6):
    print(i)


# 3. while loop example
print("\nCounting using while loop:")
count = 1

while count <= 5:
    print(count)
    count += 1


# 4. Mini task: Even or Odd
number = int(input("\nEnter a number to check even/odd: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
