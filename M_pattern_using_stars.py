# Given the number N. Write a program to print  pattern M of N rows with two solid pyramids using stars("*) .There is a space after every star.
n = int(input())
for i in range(1, n + 1):
    left_pyramid_spaces = " " * (n - i)
    left_pyramid_stars = "* " * i
    left_pyramid = left_pyramid_spaces + left_pyramid_stars
    spaces_between_pyramids = " " * (n - i)
    right_pyramid_spaces = "  " * (n - i)
    right_pyramid_stars = "* " * i
    right_pyramid = right_pyramid_spaces + right_pyramid_stars
    print(left_pyramid + right_pyramid)
'''Input-5
Output- 
    *         * 
   * *       * * 
  * * *     * * * 
 * * * *   * * * * 
* * * * * * * * * * 
'''