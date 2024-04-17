#Given an integer N, write a program which reads  N inputs and print the sum of given numbers.
given_integer=int(input())
sum_of_given_integers=0
counter=0
while counter<given_integer:
    reads_N_inputs=int(input())
    sum_of_given_integers=sum_of_given_integers +reads_N_inputs
    counter=counter+1
print(sum_of_given_integers)