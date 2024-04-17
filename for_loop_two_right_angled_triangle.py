'''
Write a program that reads a number N and prints two right angled triangles of N rows, using numbers starting from 1.
'''
n_rows = int(input())
for i in range(1, n_rows + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()

for i in range(1, n_rows + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()
'''
Input-4
Output-
1
22
333
4444
1
22
333
4444
'''

'''