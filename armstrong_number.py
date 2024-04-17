'''
Write a program that reads a number N and checks if the number N is an Armstrong Number
'''


n = int(input())
convert_number_into_string = str(n)
length = len(convert_number_into_string)

sum_of_power_of_all_digits = 0
for i in convert_number_into_string:
    digit = int(i)
    sum_of_power_of_all_digits = sum_of_power_of_all_digits + digit ** length
if sum_of_power_of_all_digits == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
