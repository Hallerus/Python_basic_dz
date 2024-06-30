#Dictionary
my_dict = dict({"Russia": 'Moscow',
                "USA": 'Washington',
                "China": 'Beijing'})
print('Dict:', my_dict)
print('Existing_Value:', my_dict["China"])
print('Not existing value:', my_dict.get('Germany'))
my_dict.update({"France": 'Paris',
                "Germany": 'Berlin'})
print('Deleted value:', my_dict.pop("USA"))
print('Modified dictionary:', my_dict, '\n')

#set
my_set = {'1', 2, 4, '2', 6, 9, 5.4, True, 4, True, '2', 6, '7'}
print('Set:', my_set)
my_set.add((3, 6, 7))
my_set.add(0)
my_set.add(1) #почему не добавляется 1  ????????
my_set.remove(5.4)
print('Modified Set:', my_set)
