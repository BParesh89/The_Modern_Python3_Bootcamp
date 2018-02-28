#practice of while loop

msg = input("What's the secret password? ")
while msg != "bananas":
	print("WRONG")
	msg = input("What's the secret password? ")
print("CORRECT!")
