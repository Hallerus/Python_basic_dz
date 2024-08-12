def calculate_structure_sum(data_structure:list):
    summ = 0
    val = []
    if data_structure == []:
        return summ
    elif isinstance(data_structure[0], dict):
        print(f"На ВХОДЕ: {data_structure[0]}, Тип: {type(data_structure[0])}, Сумма: {summ}")
        val = data_structure[0]
        for key, value in val.items():
            if isinstance(key, int):
                summ += key
            else:
                summ += len(key)
            if isinstance(value, str):
                summ += len(value)
            else:
                summ += value
        print(f'На выходе: {data_structure[0]}, Тип: {type(data_structure[0])}, Сумма: {summ}')
        data_structure.remove(val)
        return summ + calculate_structure_sum(data_structure)
    else:
        val = data_structure[0]
        print(f"На ВХОДЕ: {val}, Тип VAL: {type(val)}, Сумма: {summ}")
        for i in val:
            if isinstance(i, int):
                summ += i
            elif isinstance(i, str):
                summ += len(i)
            elif isinstance(val, tuple):
                for j in val:
                    if isinstance(j, int):
                        summ += j
                    elif isinstance(j, str):
                        summ += len(j)
                    elif isinstance(j, dict):
                        for key, value in j.items():
                            if isinstance(key, int):
                                summ += key
                            else:
                                summ += len(key)
                            if isinstance(value, str):
                                summ += len(value)
                            else:
                                summ += value
                    elif isinstance(j, list):
                        return summ + calculate_structure_sum(j)
            elif isinstance(val, set):
                return summ + calculate_structure_sum(list(val))
            else:
                print('ХУЯК!!')
        print(f'На выходе: {data_structure[0]}, Тип: {type(data_structure[0])}, Сумма: {summ}')
        data_structure.remove(val)
        return summ + calculate_structure_sum(data_structure)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
