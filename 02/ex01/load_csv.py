import pandas as pd

def load(path: str) -> pd.DataFrame:
	if not path.endswith('.csv'):
		return None
	try:
		data = pd.read_csv(path)
	except FileNotFoundError:
		return None
	print(f'Loading dataset of dimentions {data.shape}')
	return data