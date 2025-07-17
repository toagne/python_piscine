import sys

def main():
    try:
        assert len(sys.argv) == 3
        str_arg = sys.argv[1]
        int_arg = int(sys.argv[2])
        words = str_arg.split(' ')
        filtered_words = list(filter(lambda word: len(word) > int_arg, words))
        print(filtered_words)
    except (AssertionError, ValueError):
        print('AssertionError: the arguments are bad')

if __name__ == '__main__':
    main()