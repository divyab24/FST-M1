player1 = input("Enter Player 1 name:")
player2 = input("Enter Player 2 name:")

Player1_answer = input(player1 + ", please choose anyone of these rock, paper or scissors? ").lower()
Player2_answer = input(player2 + ", please choose anyone of these rock, paper or scissors? ").lower()

if Player1_answer == Player2_answer:
    print("It's a tie")
elif Player1_answer == 'rock':
    if Player2_answer == 'scissors':
        print("Rock wins")
    else:
        print("Paper wins")
elif Player1_answer == 'scissors':
    if Player2_answer == 'paper':
        print("Scissors wins")
    else:
        print("Rock wins!")
elif Player1_answer == 'paper':
    if Player2_answer == 'rock':
        print("Paper wins")
    else:
        print("Scissors wins")
else:
    print("Invalid input! You have not entered rock, paper or scissors, try again.")
