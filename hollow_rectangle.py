''' Given two numbers M and N , write a program to print a rectangle of M_rows and N_columns using stars(*)'''
m_rows = int(input())
n_columns = int(input())
for i in range(1, m_rows + 1):
    if i == 1 or i == m_rows:
        print("* " * n_columns)
    else:
        double_spaces = "  " * (n_columns - 2)
        middle_spaces = "* " + double_spaces + "* "
        print(middle_spaces)
''' output -
9
6
* * * * * * 
*         * 
*         * 
*         * 
*         * 
*         * 
*         * 
*         * 
* * * * * * 


'''