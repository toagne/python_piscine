import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	height_arr = np.array(height, dtype=float)
	weight_arr = np.array(weight, dtype=float)
	if height_arr.shape != weight_arr.shape:
		raise AssertionError('lenght of the list is not the same')
	bmi = weight_arr / (height_arr ** 2)
	return bmi.tolist()
	# try:
	# 	if len(height) != len(weight):
	# 		raise AssertionError('lenght of the list is not the same')
	# 	bmi_list = []
	# 	for i in range(0, len(height)):
	# 		if not isinstance(height[i], (int, float)) or not isinstance(weight[i], (int, float)):
	# 			raise AssertionError('elements in list mut be int or float')
	# 		bmi_list.append(weight[i] / (height[i] * height[i]))
	# 	return bmi_list
	# except AssertionError as e:
	# 	print(e)
	# 	return []

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	return [val > limit for val in bmi]