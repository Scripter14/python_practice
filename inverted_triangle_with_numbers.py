#program to print inverted right angle triangle as follows:
'''4444
 333
 22
  1'''
n = int(input())
for i in range(1, n + 1):
    spaces = " " * (i - 1)
    number = ((n + 1) - i)
    numbers = str(number) * number

    print(spaces + numbers)