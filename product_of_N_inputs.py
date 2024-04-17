#Given a number N,, write a program that reads N numbers  as input and prints the product of given N numbers.
number = int(input())
product_of_given_N_nums = 1
counter = 0
while counter < number:
    given_n_nums = int(input())

    product_of_given_N_nums = product_of_given_N_nums * given_n_nums

    counter = counter + 1
print(product_of_given_N_nums)