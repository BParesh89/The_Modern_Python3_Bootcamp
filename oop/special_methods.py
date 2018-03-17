class Train:

	def __init__(self, num):
		self.num = num

	def __repr__(self):
		return f"{self.num} car train"

	def __len__(self):
		return self.num

# testing
train1 = Train(3)
assert(len(train1) == 3)