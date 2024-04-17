'''
Write a program that reads a number N and prints the sum of squares of N number starting from 1.
'''
number = int(input())
counter = 1
sum_of_squares = 0
while counter <= number:
    sum_of_squares += (counter * counter)
    counter = counter + 1

print(sum_of_squares)
'''
input-4
output-30'''