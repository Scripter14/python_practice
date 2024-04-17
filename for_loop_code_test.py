#Print odd numbers from N to M , N is always greater than or equal to M
m = int(input())
n = int(input())
for i in range(n, m - 1, -1):
    if i % 2 == 1:
        odd_number = i
        print(str(odd_number), "", end='')

#output:
#9,7,5,3,1