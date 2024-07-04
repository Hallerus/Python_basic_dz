my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num_start = int(0)
while num_start < len(my_list):
    if my_list[num_start] == 0:
        num_start += 1
    elif my_list[num_start] > 0:
        print(my_list[num_start])
        num_start += 1
        continue
    else:
        break
