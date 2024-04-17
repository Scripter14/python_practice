'''
Given an amount, write a program to find a minimum number of currency notes of different denominations that sum to the given amount.
Available note denominations are 1000, 500, 100, 50, 20, 5, 1.
'''
given_integer_n=int(input())
number_of_1000_notes=given_integer_n//1000
amount_left_1=given_integer_n-number_of_1000_notes *1000
number_of_500_notes=amount_left_1//500
amount_left_2=amount_left_1- number_of_500_notes*500
number_of_100_notes= amount_left_2//100
amount_left_3 =amount_left_2 - number_of_100_notes*100
number_of_50_notes= amount_left_3//50
amount_left_4 = amount_left_3 - number_of_50_notes*50
number_of_20_notes=amount_left_4//20
amount_left_5 =amount_left_4 - number_of_20_notes *20
number_of_5_notes=amount_left_5//5
amount_left_6= amount_left_5- number_of_5_notes *5
number_of_1_notes= amount_left_6//1

print("1000:",number_of_1000_notes)
print("500:",number_of_500_notes)
print("100:",number_of_100_notes)
print("50:",number_of_50_notes)

print("20:",number_of_20_notes)
print("5:",number_of_5_notes)
print("1:",number_of_1_notes)
'''INPUT-8593
OUTPUT-1000: 8
500: 1
100: 0
50: 1
20: 2
5: 0
1: 3'''