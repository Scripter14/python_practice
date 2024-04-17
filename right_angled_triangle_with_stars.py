#Program that reads a number N and print a right angled triangle of N rows using (*).
N_number_of_rows=int(input())
counter=1
while counter<=N_number_of_rows:
    print("*"*counter)
    counter=counter+1