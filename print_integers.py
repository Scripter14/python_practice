'''
Given an integer N.Write a program to print  integers from N to 1.
'''
number = int(input())
counter = 0
while counter < number:
    print(number - counter)

    counter = counter + 1
'''
input-5

5
4
3
2
1
'''