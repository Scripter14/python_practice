#Program that reads a number N and prints a square of N rows and N columns using stars(*).
N_number=int(input())
counter=0
while counter<N_number:
    print(("*" + " ")* N_number)
    counter=counter+1
'''INPUT-5
OUTPUT-
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * '''