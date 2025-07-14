import sys

def main():
	try:
		morse_code = {'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ',
				'F': '..-. ', 'G': '--. ', 'H': '--. ', 'I': '.. ', 'J': '.--- ',
				'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ',
				'P': '.--. ', 'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
				'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ', 'Y': '-.-- ',
				'Z': '--.. ', ' ': "/ ", '0': '----- ', '1': '.---- ', '2': '..--- ',
				'3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ',
				'8': '---.. ', '9': '----. '}
		if len(sys.argv) != 2 or 'str' not in type(sys.argv[1]).__name__:
			raise AssertionError('AssertionError: the arguments are bad')
		morse_str = ''
		for char in sys.argv[1]:
			char = char.upper()
			if char not in morse_code:
				raise AssertionError('AssertionError: the arguments are bad')
			morse_str += morse_code[char]
		print(morse_str.strip())
	except AssertionError as e:
		print(e)

if __name__ == '__main__':
	main()