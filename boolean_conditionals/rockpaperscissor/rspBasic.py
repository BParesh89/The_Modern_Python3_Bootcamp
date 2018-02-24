print("...rock...\n...scissors...\n...paper...\n")

#player 1 entering their choice
player1 = input("player 1 enter your choice: ").lower()

#checking to see if entered a valid choice
while player1 != "rock" and player1 != "paper" and player1 != "scissors":
		player1 = input("please enter a valid choice: ").lower()

#a little thing to stop cheating
print("\n" * 22)

#player 2 entering their choice
player2 = input("player 2 enter your choice: ").lower()

#checking to see if entered a valid choice
while player2 != "rock" and player2 != "paper" and player2 != "scissors":
		player2 = input("please enter a valid choice: ").lower()

#checking who wins		
if player1 == player2:
	print("DRAW")

elif player1 == "rock":
	if player2 == "scissors":
		print("Player 1 wins")
	else:
		print("Player 2 wins")

elif player1 == "paper":
	if player2 == "scissors":
		print("Player 2 wins")
	else:
		print("Player 1 wins")

elif player1 == "scissors":
	if player2 == "rock":
		print("Player 2 wins")
	else:
		print("Player 1 wins")

else:
	print("Not a legitimate game")