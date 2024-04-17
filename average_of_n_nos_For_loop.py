'''
Write a program that reads a number N and prints the average of numbers form 1 to N.
'''
n_given_number=int(input())
sum_of_numbers=0
average_of_n_given_number=0
for i in range(n_given_number+1):
   sum_of_numbers=sum_of_numbers+i
   average_of_n_given_number=sum_of_numbers/n_given_number
print(average_of_n_given_number)
