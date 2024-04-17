'''
Given a number N,, write a program that reads N inputs and
prints the average of n inputs.
'''
n=int(input())

sum_of_n_inputs=0
counter=0
while counter<n:
    given_input= int(input())
    sum_of_n_inputs= sum_of_n_inputs+given_input
    counter=counter+1
average_of_n_inputs=sum_of_n_inputs/n
print(average_of_n_inputs)
'''
Input-5

3
2
5
6
1
3.4
'''