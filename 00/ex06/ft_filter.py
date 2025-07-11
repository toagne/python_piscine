def even(n):
    return n % 2 == 0

def ft_filter(f, sequence: list):
    return [element for element in sequence if f(element) == True]

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    b = ft_filter(even, a)
    print(b)