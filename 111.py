def calculate_structure_sum(*args):
    summ = 0
    list_ = []
    for i in range(len(args)):
        list_.append(args[i])
    print('args =', list, type(list), len(args))
    for i in range(len(args)):
        print(args[i])
        if isinstance(args[i], int):
            print('Int', args[i])
            summ += i
        elif isinstance(args[i], str):
            print('str',args[i])
            summ += len(i)
        elif isinstance(args[i], list):
            print('list')
            list_.remove(args[i])
            return summ + calculate_structure_sum(*list_)
        elif isinstance(args[i], tuple):
            print('tuple',args[i])
            return summ + calculate_structure_sum(*args)
        elif isinstance(args[i], set):
            print('set',args[i])
            return summ + calculate_structure_sum(*args)
        elif isinstance(args[i], dict):
            print('dict',args[i])
            list_.remove(args[i])
            return summ + calculate_structure_sum(*list_)
    return summ


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(*data_structure)
print(result)
