# Program to print letter W with N rows using stars(*).There is space after every star.
n=int(input())

print('* ' * ((2*n)-1))
hollow_spaces_count = 0
for i in range(1, n):
    spaces_in_the_beginning = i
    stars_count = n-i
    print(' ' * spaces_in_the_beginning, end = '')
    print('* ' * stars_count, end = '')
    print(' ' * hollow_spaces_count, end = '')
    print('* ' * stars_count, end = '')
    print()
    hollow_spaces_count = hollow_spaces_count + 2
'''input -5
output-
* * * * * * * * * 
 * * * * * * * * 
  * * *   * * * 
   * *     * * 
    *       * '''