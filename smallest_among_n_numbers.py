# Given two numbers X and N ,Write a program to print the sum of series as follows:
"""
2¹
2³
2

"""
x_integer = int(input())
n_term_integer = int(input())
sum_of_series = 0
power = 1
for i in range(1, n_term_integer + 1):
    series = x_integer ** power
    power = power + 2
    sum_of_series = sum_of_series + series
print(sum_of_series)

