'''Write a program that reads a three-digit number and checks if all the below conditions are satisfied.
The number contains 1.
The sum of all the digits of the number is less than 12.
The last digit of the number is equal to 5.'''
three_digit_number=int(input())
string=str(three_digit_number)
number_1=int(string[0])
number_2=int(string[1])
number_3=int(string[2])
sum_of_numbers=number_3 + number_2 + number_1

if ((number_3==5) and (sum_of_numbers<12) and (number_1==1 or number_2==1 or number_3==1)):

    print(True)
else:
    print(False)
'''INPUT-315
OUTPUT-True
'''
