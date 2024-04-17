#  Write a program that reads number N and print the cube  of each number from 1 to N in new line.
n=int(input())
counter=1
cube_of_number=0
while counter<=n:
    cube_of_number=counter**3
    print(cube_of_number)
    counter=counter+1
