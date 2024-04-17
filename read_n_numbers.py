#Write a program that reads number N and print the average of N numbers from 1.
N= int(input())
counter = 1
sum_of_N = 0

while counter <= N:
    sum_of_N = sum_of_N + counter
    counter = (counter + 1)
average_of_N = ((sum_of_N) / N)
print(average_of_N)
