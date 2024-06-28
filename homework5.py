immutable_var = 3.2, "Kid", 12
print(immutable_var)

#immutable_var[1] = 0
#print(immutable_var)
print("Элементы кортежа можно менять, если они являются изменяемыми.")

mutable_list = ["1", 1, 1.0], 2, 3.0
print("До:",mutable_list)
mutable_list[0][0] = '4'
mutable_list[0][2] = 4.0
print("После:",mutable_list)
