# Given two integers M and N,
# #write a program to print a solid rectangle pattern of M rows and N columns using the asterisk character (*).
M_number_of_rows=int(input())
N_number_of_columns=int(input())
counter=0
while counter <M_number_of_rows:
    print("* " * N_number_of_columns)
    counter=counter+1
