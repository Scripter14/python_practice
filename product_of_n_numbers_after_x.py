'''
Write a program that reads two numbers X and N and prints
product of Nnumbers after X.
'''
x=int(input())
n=int(input())
product_of_n_numbers=1
counter=0
while counter<n:
    x=x+1
    product_of_n_numbers=product_of_n_numbers*x
    counter=counter+1
print(product_of_n_numbers)
'''
input
4
2
output- 30
'''