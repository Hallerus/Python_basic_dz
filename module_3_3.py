def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(3,4)
print_params(c='Football')
print_params(b=25)
print_params(c=[1, 2, 3])
print('')

value_list = ['1.0.str', 234, True]
value_dict = {'a':2, 'b':'снова строка', 'c':[3,5,6]}
print_params(*value_list)
print_params(**value_dict)
print('')

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
