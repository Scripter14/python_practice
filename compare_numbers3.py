'''Write a program that reads a four-digit number and checks if the first two digits of the number is 19
and the last two digits of the number is between 30 and 60'''
four_digit_number=int(input())
string=str(four_digit_number)
number_1=int(string[0:2])
number_2=int(string[2:])


first_two_digits=number_1
last_two_digits=number_2

if ((first_two_digits==19) and (last_two_digits>30 and last_two_digits<60)) :
    print(True)
else:
    print(False)