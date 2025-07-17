import sys
from string import ascii_uppercase, ascii_lowercase, punctuation, digits


def main():
    """takes a single string argument and displays the sums of
    its upper-case characters, lower-case characters,
    punctuation characters, digits and spaces.
    If None or nothing is provided, the user is prompted to provide a string.

    Raises:
        AssertionError: If more than one argument is provided to the program
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError('AssertionError: more than one argument is provided')
        if len(sys.argv) == 1 or sys.argv[1] == '':
            print('What is the text to count?')
            my_str = sys.stdin.read()
        else:
            my_str = sys.argv[1]
        lower = 0
        upper = 0
        punct = 0
        spaces = 0
        my_digits = 0
        for char in my_str:
            if char in ascii_lowercase:
                lower += 1
            elif char in ascii_uppercase:
                upper += 1
            elif char in punctuation:
                punct += 1
            elif char in (' ', '\n', '\r'):
                spaces += 1
            elif char in digits:
                my_digits += 1
            else:
                print(f'quello strano: {char}')
        print(f'The text contains {len(my_str)} characters:')
        print(f'{upper} upper letters')
        print(f'{lower} lower letters')
        print(f'{punct} punctuation marks')
        print(f'{spaces} spaces')
        print(f'{my_digits} digits')
    except AssertionError as e:
        print(e)


if __name__ == '__main__':
    main()
