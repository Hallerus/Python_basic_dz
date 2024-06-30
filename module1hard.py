grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
grades[0] = (grades[0][0] + grades[0][1] + grades[0][2] + grades[0][3] + grades[0][4]) / len(grades[0])
grades[1] = (grades[1][0] + grades[1][1] + grades[1][2] + grades[1][3]) / len(grades[1])
grades[2] = (grades[2][0] + grades[2][1] + grades[2][2] + grades[2][3]) / len(grades[2])
grades[3] = (grades[3][0] + grades[3][1] + grades[3][2]) / len(grades[3])
grades[4] = (grades[4][0] + grades[4][1] + grades[4][2] + grades[4][3] + grades[4][4]) / len(grades[4])
dict_ = {students[0]: grades[0], students[1]: grades[1], students[2]: grades[2],
         students[3]: grades[3], students[4]: grades[4]}
print("Мой результат: ", dict_)
print("Целевое реш-ие: {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}")
