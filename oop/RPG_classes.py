class Character:

	def __init__(self, name, hp, level):
		self.name = name
		self.hp = hp
		self.level = level

class NPC(Character):

	def __init__(self, name, hp, level):
		super().__init__(name, hp, level)

	def speak(self):
		return "I heard there were monsters running around last night"

villager = NPC("Bob", 100, 12)

assert(villager.name) == "Bob"
assert(villager.hp) == 100
assert(villager.level) == 12
assert(villager.speak()) == "I heard there were monsters running around last night"
