# Given the number N. Write a program to print a  diamond of 2*(N-1) rows using stars("*")
n=int(input())
for i in range(1, n + 1):
    top_triangle_spaces = " " * (n - i)
    top_triangle_stars = "* " * i
    print(top_triangle_spaces + top_triangle_stars)
for j in range(1, n + 1):
    bottom_triangle_spaces = " " * (j)
    bottom_triangle_stars = "* " * (n - j)
    print(bottom_triangle_spaces + bottom_triangle_stars)
'''
Input-3
Output-
  * 
 * * 
* * * 
 * * 
  * 


'''