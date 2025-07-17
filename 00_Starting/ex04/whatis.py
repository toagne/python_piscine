import sys

try:
    if len(sys.argv) == 1:
        exit()
    if len(sys.argv) > 2:
        raise AssertionError('AssertionError: more than one argument is provided')
    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print(e)
except ValueError as v:
    print('AssertionError: argument is not an integer')