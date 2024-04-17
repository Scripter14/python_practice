#Program that reads a number N and prints a right angled triangle of N rows using number starting from 1.
N_number_of_rows=int(input())
counter=1
while counter<=N_number_of_rows:
    value=(str(counter)+" ")*counter
    print(value)
    counter=counter+1
'''Input- 5
Output-numbers should have space between them
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5'''