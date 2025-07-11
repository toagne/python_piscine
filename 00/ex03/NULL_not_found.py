def NULL_not_found(object: any) -> int:
    my_type = type(object)
    readable_type = ''
    if object == None:
        readable_type = 'Nothing'
    elif 'float' in my_type.__name__:
        readable_type = 'Cheese'
    elif object == 0 and 'int' in my_type.__name__:
        readable_type = 'Zero'
    elif object == '':
        readable_type = 'Empty'
        print(f'{readable_type}: {my_type}')
        return 0
    elif object == False:
        readable_type = 'Fake'
    else:
        print('Type not Found')
        return 1
    print(f'{readable_type}: {object} {my_type}')
    return 0