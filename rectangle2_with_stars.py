#Program that reads two numbers M and N, and prints a Rectangle  of M rows and N columns using pluses(+)
M_number_of_rows=int(input())
N_number_of_columns=int(input())
counter=1
while counter<=M_number_of_rows:
    print(("+" + " ")* N_number_of_columns)
    counter=counter+1
'''Input1-3
Input2-5
Output-
+ + + + + 
+ + + + + 
+ + + + + 
'''
