'''
Given an integer N, write a program which reads N inputs and prints the sum of the given input integers.
'''
n_given_integers=int(input())
sum_of_given_integers= 0
for i in range(n_given_integers):
    n_inputs=int(input())
    sum_of_given_integers=sum_of_given_integers + n_inputs
print(sum_of_given_integers)
'''
no. of given integers=3
no. of inputs-
8
11
25
output-44(sum of all three input numbers)
'''