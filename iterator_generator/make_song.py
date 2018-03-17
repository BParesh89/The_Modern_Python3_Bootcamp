def make_song(num=99, bev='soda'):
	i = num
	while True:
		if i == 1:
			yield f"Only 1 bottle of {bev} left!"
		elif i == 0:
			yield f"No more {bev}!"
			break
		else:
			yield f"{i} bottles of {bev} on the wall."
		i -= 1

# testing
tea_song = make_song(4, 'tea')
assert(next(tea_song) == '4 bottles of tea on the wall.')
assert(next(tea_song) == '3 bottles of tea on the wall.')
assert(next(tea_song) == '2 bottles of tea on the wall.')
assert(next(tea_song) == 'Only 1 bottle of tea left!')
assert(next(tea_song) == 'No more tea!')
