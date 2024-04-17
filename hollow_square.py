'''    Given a number N, write a program to print a Square of N rows using stars(*)'''
n=int(input())
for i in range(1, n+1):
    if i ==1 or i==n:
       print("* "*n)
    else:
        middle_rows ="  " * (n-2)
        rows="* " + middle_rows +"* "
        print(rows)
'''
output- 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 





'''