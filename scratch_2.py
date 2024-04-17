'''
Given a number N,write a program to print a hollow pyramid of N rows using stars(*)
'''

n_rows = int(input())

for i in range(1, n_rows + 1):
    if i == 1:
        spaces = n_rows - 1
        print(" " * spaces + "* ")
    elif i == n_rows:
        print("* " * n_rows)
    else:
        left_space = (n_rows - i)
        hollow_spaces = 2 * (i - 2)

        print(" " * left_space + "* " + " " * hollow_spaces + "* ")


