'''
Write a program that reads 10 inputs and prints the sum  and average of 10 inputs
'''
sum_of_n_numbers = 0

for i in range(1, 11):
    n_numbers = int(input())

    sum_of_n_numbers = sum_of_n_numbers + n_numbers
    average_of_n_numbers = sum_of_n_numbers / i

print(sum_of_n_numbers)
print(average_of_n_numbers)