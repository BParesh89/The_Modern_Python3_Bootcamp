class BankAccount:
	def __init__(self, owner):
		self.owner = owner
		self.balance = 0.0

	def deposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

# testing

acct = BankAccount("Tim")
assert(acct.owner == "Tim")
assert(acct.balance == 0.0)
assert(acct.deposit(15) == 15.0)
assert(acct.withdraw(3) == 12.0)
assert(acct.balance == 12.0)
