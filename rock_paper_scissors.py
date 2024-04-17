'''
Abhinav and Anjali are playing a game called -Rock-Paper-Scissors.
. It's a hand game usually played between two people.
 In this game, they both show their hands in one of three ways: Rock-Paper or Scissors.

'''
shape_chosen_by_abhinav = input()
shape_chosen_by_anjali = input()
if shape_chosen_by_abhinav == shape_chosen_by_anjali:
    print("Tie")

elif shape_chosen_by_abhinav == "Rock" and shape_chosen_by_anjali == "Scissors":
    print("Abhinav Wins")

elif shape_chosen_by_abhinav == "Scissors" and shape_chosen_by_anjali == "Paper":
    print("Abhinav Wins")

elif shape_chosen_by_abhinav == "Paper" and shape_chosen_by_anjali == "Rock":
    print("Abhinav Wins")
else:
    print("Anjali Wins")
