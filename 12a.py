
n = int(input('Please Enter a Number (int) : '))
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print(chr(65 + k), end='')
    print()