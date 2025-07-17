from typing import Any
from math import sqrt

def get_median_index(numbers: list):
    return numbers.index(numbers[len(numbers) // 2])

def get_var(numbers: list):
    mean = get_mean(list(numbers))
    dev = [(n - mean) * (n - mean) for n in numbers]
    variance = get_mean(dev)
    return variance

def get_mean(numbers: list):
    return sum(numbers) / len(numbers)

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    sorted_args = list(args)
    sorted_args.sort()
    for key, value in kwargs.items():
        if len(args) == 0:
            print('ERROR')
            continue
        if value =='mean':
            print(f'mean : {get_mean(list(args))}')
        elif value =='median':
            print(f'median : {sorted_args[get_median_index(sorted_args)]}')
        elif value =='quartile':
            first_q = sorted_args[get_median_index(sorted_args[:get_median_index(sorted_args)])]
            third_q = sorted_args[get_median_index(sorted_args) + get_median_index(sorted_args[get_median_index(sorted_args):])]
            print(f'quartile : {[float(first_q), float(third_q)]}')
        elif value =='std':
            print(f'std : {sqrt(get_var(list(args)))}')
        elif value =='var':
            print(f'var : {get_var(list(args))}')