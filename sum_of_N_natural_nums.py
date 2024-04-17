#Write a program that reads a number N and prints the sum of N natural numbers.
n=int(input())
counter=1
sum_of_natural_numbers=0
while counter<=n:
    sum_of_natural_numbers=sum_of_natural_numbers+counter
    counter=counter+1
print(sum_of_natural_numbers)

