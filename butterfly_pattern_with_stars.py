# Program to print Butterfly pattern using stars("*") in 2*N-1 rows. Given the number N.
n = int(input())
for i in range(1, n + 1):
    print("* " * i, end="")
    print("  " * (n - i) * 2, end="")
    print("* " * i)
    # print(left_side_stars + top_spaces + right_side_stars)
for j in range(1, n + 1):
    bottom_stars_left = "* " * (n - j)
    bottom_spaces = "  " * (j * 2)
    bottom_stars_right = "* " * (n - j)
    print(bottom_stars_left + bottom_spaces + bottom_stars_right)
'''
Input-5
Output- 
5
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
                    


'''
