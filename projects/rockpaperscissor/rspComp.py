#assigning a random choice to the computer opponent
from random import randint

play_again = "y"


while play_again == "y":
	winning_score = int(input("What do you want the winning score to be? "))
	
	player_wins = 0
	computer_wins = 0

	print("...rock...\n...scissors...\n...paper...\n")

	while player_wins < winning_score and computer_wins < winning_score:
		if player_wins == 0 and computer_wins == 0:
			pass
		else:
			print(f"------\nplayer wins ({player_wins}) computer wins ({computer_wins})\n-------")
		
		computer = randint(0,2)
		if computer == 0:
			computer = "rock"
		elif computer == 1:
			computer = "scissors"
		else:
			computer = "paper"

		#player 1 entering their choice
		player = input("enter your choice: ").lower()

		#checking to see if entered a valid choice
		while player != "rock" and player != "paper" and player != "scissors" and player != "quit":
				player = input("please enter a valid choice: ")

		if player == "quit":
			break

		#printing what the computer was randomly assigned
		print(f"The computer was assigned: {computer}")

		#checking who wins		
		if player == computer:
			print("DRAW")

		elif player == "rock":
			if computer == "scissors the round":
				print("You win")
				player_wins += 1
			else:
				print("Computer wins the round")
				computer_wins += 1

		elif player == "paper":
			if computer == "scissors":
				print("Computer wins the round")
				computer_wins += 1
			else:
				print("You win the round")
				player_wins += 1

		elif player == "scissors":
			if computer == "rock":
				print("Computer wins the round")
				computer_wins += 1
			else:
				print("You win the round")
				player_wins += 1

		else:
			print("Not a legitimate game")

	if player_wins > computer_wins:
		play_again = input("You win the game!! \nDo you want to play again? (y/n) ")
	elif player_wins == computer_wins:
		play_again = input("It's a tie! \nDo you want to play again? (y/n) ")
	else:
		play_again = input("You lose the game. \nDo you want to play again? (y/n) ")

	while True:
		if play_again == "y" or play_again == "n":
			break
		else:
			play_again = input("Please enter a valid option: (y/n) ")

	if play_again == "n":
		print("Thank you for playing")
