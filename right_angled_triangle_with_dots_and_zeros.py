#Given a number N. Write a program to print right angled triangle with dots(.) at the borders and zeros(0) in the middle of the triangle.
given_number_n = int(input())
for i in range(1, given_number_n + 1):
    if i == 1:
        print(". " * i)
    elif i == 2:
        print(". " * i)
    elif i == given_number_n:
        print(". " * given_number_n)
    else:
        print(". " + "0 " * (i - 2) + ". ")
''' 
INPUT- 8
output 
. 
. . 
. 0 . 
. 0 0 . 
. 0 0 0 . 
. 0 0 0 0 . 
. 0 0 0 0 0 . 
. . . . . . . . 


'''
