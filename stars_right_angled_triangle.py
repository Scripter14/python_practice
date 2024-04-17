'''
Write a program that reads a number  N and prints two-right angled triangles, each of Nrows using(*)stars.
'''
number = int(input())
counter_1 = 1
counter_2 = 1
while counter_1 <= number:
    print(("*" + " ") * counter_1)

    counter_1 = counter_1 + 1
while counter_2 <= number:
    print(("*" + " ") * counter_2)
    counter_2 = counter_2 + 1
'''
input
4
* 
* * 
* * * 
* * * * 
* 
* * 
* * * 
* * * * 
'''