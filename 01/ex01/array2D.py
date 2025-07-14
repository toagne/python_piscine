def slice_me(family: list, start: int, end: int) -> list:
	try:
		if not isinstance(family, list):
			raise AssertionError('first parameter is not a list')
		if not isinstance(start, int) or not isinstance(end, int):
			raise AssertionError('second or third parameter is not an int')
		y_len = len(family)
		x_len = len(family[0])
		new_y_len = end - start
		if end <= start:
			new_y_len = start
		print(f'My shape is : ({y_len}, {x_len})')
		print(f'My new shape is : ({new_y_len}, {x_len})')
		return family[start:end]
	except AssertionError as e:
		print(e)