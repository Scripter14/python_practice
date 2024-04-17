#Given the number N, wite a python Program to print the pyramid of  2*N-1 rows using "+" and "#" .
n=int(input())
for i in range(n+1):
    spaces="  " *(n-i)
    pluses="+ "*i
    hashes ="# "*(1)
    print(spaces + pluses +hashes )
bottom_pyramid= 2*n-1
for j in range(1,n-1):
    bottom_spaces="  " *(j)
    bottom_pluses="+ "*(n-j)
    bottom_hashes ="# "*(1)
    print(bottom_spaces +bottom_pluses +bottom_hashes )
    '''
    Input-5
    output:-
          # 
        + # 
      + + # 
    + + + # 
  + + + + # 
+ + + + + # 
  + + + + # 
    + + + # 
      + + # 
        + # 
          # 
'''