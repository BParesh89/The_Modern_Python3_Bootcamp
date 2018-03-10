# make a function which returns animal sounds but have a default parameter of dog

def speak(animal="dog"):
	if animal == "pig":
		return "oink"
	elif animal == "duck":
		return "quack"
	elif animal == "cat":
		return "meow"
	elif animal == "dog":
		return "woof"
	else:
		return "?"

print(speak())
print(speak("pig"))
print(speak("duck"))
print(speak("cat"))
print(speak("dog"))
