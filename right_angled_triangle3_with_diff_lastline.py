#Write a program that reads a number N and prints a right angled triangle of N rows using stars(*) and plus(+)
#The first N-1 row contains stars and Nth row contains plus.
#output
'''*
* *
* * *
+ + + +'''

N_number_of_rows=int(input())
counter=1
Nth_row =N_number_of_rows
while counter<N_number_of_rows:
    print((("*") +" ") *counter)
    counter=counter+1
print((("+")+" ")*Nth_row)

