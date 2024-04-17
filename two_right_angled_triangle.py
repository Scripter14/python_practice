#Program that reads a number N and prints two right angled triangles of N rows using that number starting from 1.
N_numberof_rows=int(input())
counter_1=1
counter_2=1
while counter_1<=N_numberof_rows:
    value=str(counter_1)
    print(value*counter_1)
    counter_1=counter_1+1
if counter_1>N_numberof_rows:
    while counter_2<=N_numberof_rows:
        value2=str(counter_2)
        print(value2*counter_2)
        counter_2=counter_2+1


'''Input-4
output-
1
22
333
4444
1
22
333
4444'''
