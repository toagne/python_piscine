def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	try:
		if len(height) != len(weight):
			raise AssertionError('lenght of the list is not the same')
		bmi_list = []
		print(len(height))
		for i in range(0, len(height)):
			if not isinstance(height[i], (int, float)) or not isinstance(weight[i], (int, float)):
				raise AssertionError('elements in list mut be int or float')
			bmi_list.append(weight[i] / (height[i] * height[i]))
		return bmi_list
	except AssertionError as e:
		print(e)
		return []
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	return [val > limit for val in bmi]