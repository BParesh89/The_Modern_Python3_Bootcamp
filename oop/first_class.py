class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


# testing
test = Comment("pepsiman", "I like pepsi", 4)
assert(test.username == "pepsiman")
assert(test.text == "I like pepsi")
assert(test.likes == 4)
