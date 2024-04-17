'''Given a number N separated by a space as shown in the sample output.
, write a program to print all the factors of N

'''
given_number_n = int(input())
factors = str()
for i in range(1, given_number_n + 1):
    if given_number_n % i == 0:
        factors = factors + str(i) + " "
print(factors)

