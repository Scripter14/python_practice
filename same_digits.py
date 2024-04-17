'''Write a program that reads a three-digit number and checks if all the digits of the number are the same.'''
three_digit_number = int(input())
string = str(three_digit_number)
first_number = string[0]
second_number = string[1]
third_number = string[2]
if first_number == second_number and second_number == third_number and third_number == first_number:
    print(True)
else:
    print(False)
