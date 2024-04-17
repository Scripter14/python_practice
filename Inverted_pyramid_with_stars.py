# given the number N.Write a program to print an Inverted pyramidof N rows using stars("*")
n=int(input())
for i in range( n):
    for j in range(i,n):
        spaces=" "*i
        stars="* " *(n-i)
    print(spaces + stars)
    '''
    Input=4
    output-
* * * * 
 * * * 
  * * 
   *  
    '''