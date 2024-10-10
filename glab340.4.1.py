number = int(input("Enter a number: "))
num_str = str(number)
reversed_str = num_str[::-1]

if num_str == reversed_str:
    print(f"{number} is a palindrome number.")
else: 
    print(f"{number} is not a palindrome number.")


n = 5
for i in range(n):
    for j in range(i):
        print('*', end = "")
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print('*', end = "")
    print('')



n = int(input("enter the number of rows for the pyramid: "))

for i in range(1, n + 1):
    for j in range (n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()