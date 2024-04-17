'''Write a program that reads an amount A and  and prints the minimum number of  500,50
10and 1 rupee notes required for the given amount '''
amount_A=int(input())
notes_500_req=amount_A//500
remaining_amount_1=amount_A-(500*notes_500_req)

notes_50_req=remaining_amount_1//50
remaining_amount_2=amount_A-(500*notes_500_req)-(50*notes_50_req)

notes_10_req=remaining_amount_2//10
remaining_amount_3=amount_A-(500*notes_500_req)-(50*notes_50_req)-(10*notes_10_req)
notes_1_req=remaining_amount_3//1

print("500:"+"",notes_500_req,"50:"+"",notes_50_req ,"10:"+"",notes_10_req,"1:"+"",notes_1_req)
'''INPUT 1259
OUTPUT:-
 500: 2 50: 5 10: 0 1: 9
'''