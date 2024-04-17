#Program that reads a number N and prints a square of N rows and N columns using numbers starting from 1
number = int(input())
counter = 1
number_of_rows = 0
number_of_cols = 0
while counter <= number:
    value = str(counter)
    print(value * number)
    counter = counter + 1
