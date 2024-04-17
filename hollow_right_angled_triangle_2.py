''' Given  number N, print a right angled triangle of N rows using ---- dashes, | pipes, / forward slashes'''
n_rows = int(input())
print("_" * (n_rows + 1))
for i in range(1, n_rows + 1):
    hollow_spaces = " " * (n_rows - i)
    blocks = "|"
    slashes = "/"
    print(blocks + hollow_spaces + slashes)
    '''INPUT-5 
    output- 
    5
______
|    /
|   /
|  /
| /
|/

    
    '''
