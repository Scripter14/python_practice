'''Write a program that reads a three-digit number and checks if any of the below conditions is satisfied.
Each digit of the given number is greater than 7.
The product of any two digits is always less than or equal to 30.
'''
three_digit_number = int(input())
string = str(three_digit_number)
number_1 = int(string[0])
number_2 = int(string[1])
number_3 = int(string[2])
product_of_1st_two_numbers = number_1 * number_2
product_of_last_two_numbers = number_2 * number_3
product_of_1st_and_last_numbers = number_1 * number_3
if ((number_1 > 7 and number_2 > 7 and number_3 > 7) or (
        product_of_1st_two_numbers <= 30 and product_of_last_two_numbers <= 30 and product_of_1st_and_last_numbers <= 30)):
    print(True)
else:
    print(False)
'''INPUT-832
OUTPUT- True'''