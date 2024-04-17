'''Given numbers M and N. Write a program to print  a rectangle of M rows and N columns using stars(*) in the border and zeros(0)in the middle of the rectangle.
 * * * * * * *
 * 0 0 0 0 0 *
 * 0 0 0 0 0 *
 * * * * * * *'''

m_rows = int(input())
n_columns = int(input())
for i in range(0, m_rows):

    if i == 0:
        print("* " * n_columns)
    elif i == m_rows - 1:
        print("* " * n_columns)
    else:
        zero = "0 " * (n_columns - 2)
        print("* " + zero + "*")
''' input-5 rows 
8 columns
output- 
* * * * * * * * 
* 0 0 0 0 0 0 *
* 0 0 0 0 0 0 *
* 0 0 0 0 0 0 *
* * * * * * * * 



'''
