''' HandGame ROCK-PAPERS-Scissors'''
def Outcome_of_the_game(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        print("Tie")
    elif player1_choice == "Rock" and player2_choice == "Scissors":
         print("Abhinav Wins")
    elif player1_choice == "Scissors" and player2_choice == "Paper":
         print("Abhinav Wins")
    elif player1_choice == "Paper" and player2_choice == "Rock":
         print("Abhinav Wins")
    elif player1_choice == "Scissors" and player2_choice == "Rock":
         print("Anjali Wins")
    elif player1_choice == "Paper" and player2_choice == "Scissors":
        print("Anjali Wins")
    elif player1_choice == "Rock" and player2_choice == "Paper":
        print("Anjali Wins")



player1_choice = input()
player2_choice = input()
Outcome_of_the_game(player1_choice, player2_choice)