#Write a program that reads two numbers M and N, and prints a rectangle of M rows and N columns using *.
M_number_of_rows=int(input())
N_number_of_columns=int(input())
counter=1
while counter<=M_number_of_rows:
    print("*"*N_number_of_columns)
    counter=counter+1