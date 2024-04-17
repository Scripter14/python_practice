#Write a program that reads two numbers M and N and prints the sum of N numbers from M
m = int(input())
n = int(input())
counter = 0
sum_of_numbers = 0
while counter < n:
    sum_of_numbers = sum_of_numbers + m

    m = m + 1
    counter = counter + 1
print(sum_of_numbers)