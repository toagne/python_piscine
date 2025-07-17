class LoadingBar:
	def __init__(self, start = '|[', body = '=', arrow = '>', end = ']|', tot_n_of_body = 93):
		self.start = start
		self.body = body
		self.arrow = arrow
		self.end = end
		self.tot_n_of_body = tot_n_of_body

	def update(self, step: int):
		i = int(self.tot_n_of_body * step / 100)
		return f'{self.start}{i * self.body + self.arrow}{(self.tot_n_of_body - i) * " "}{self.end}'

def ft_tqdm(lst: range) -> None:
	tot = len(lst)
	step = 100 / (tot - 1)
	loading_bar = LoadingBar()
	progress = 0
	for val in lst:
		percent = min(int(progress), 100)
		bar = loading_bar.update(percent)
		current = int(percent * tot / 100)
		print(f'{percent:3d}%{bar} {current}/{tot}', end='\r')
		progress += step
		yield val
	print(f'100%{loading_bar.update(100)} {tot}/{tot}')
