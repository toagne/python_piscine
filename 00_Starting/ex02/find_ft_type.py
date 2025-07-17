def all_thing_is_obj(object: any) -> int:
    my_type = type(object)
    readable_type = my_type.__name__.capitalize()
    if 'str' in my_type.__name__:
        readable_type = f'{object} is in the kitchen'
    if 'int' in my_type.__name__:
        print('Type not found')
        return 42
    print(f'{readable_type} : {my_type}')
    return 42