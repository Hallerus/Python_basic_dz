class House:
    houses_history = []
    
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)
    
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)
        self.houses_history.append(name)
        
    def __del__(self):
        print(f"{self.name} снеён, но остаётся в истории")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.'

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            return f"Ошибка. Адд тип входных данных: {value}."

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            return f"Ошибка. Адд тип входных данных: {value}."

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            return f"Ошибка. Адд тип входных данных: {value}."

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int):
            if self.number_of_floors == other.number_of_floors:
                return True
            else:
                return False
        else:
            return f"Ошибка. Tип входных данных: {other.number_of_floors}"

    def __lt__(self, other):
        return self.number_of_floors < other

    def __le__(self, other):
        return self.number_of_floors <= other

    def __gt__(self, other):
        return self.number_of_floors > other

    def __ge__(self, other):
        return self.number_of_floors >= other

    def __ne__(self, other):
        return self.number_of_floors != other


    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor+1):
                print(i)



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)