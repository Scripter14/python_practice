'''
Given two integers M and N, write a program to print a solid rectangle pattern of M rows and N columns using the asterisk character (*).
'''
m_rows = int(input())
n_columns = int(input())
for i in range(m_rows):
    print("* " * n_columns)
'''
INPUT1--5
INPUT2--3
* * * 
* * * 
* * * 
* * * 
* * * 
'''