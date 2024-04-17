'''
Given a number N, write a program to print right angled hollow triangle of N rows using stars(*)
'''
n = int(input())
for i in range(1, n + 1):
    if i == 1:
        print("* ")
    elif i == n:
        print(("* ") * n)
    else:
        hollow_spaces = (" ") * (2 * (i - 2))
        spaces = ("* " + hollow_spaces + "* ")

        print(spaces)
'''
INPUT N=5
OUTPUT
* 
* * 
*   * 
*     * 
* * * * * 
'''