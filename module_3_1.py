def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()
    tuple_ = len(string), string.upper(), string.lower()
    return tuple_


def is_contains(string: str, list_to_search: list):
    count_calls()
    for list_ in list_to_search:
        if string.lower() == str(list_).lower():
            return True
    return False


calls = 0
print(string_info("Kom4atKA"))
print(is_contains("dd", ['2', 'fgsd', 'dd']))
print(is_contains("dd", [2, 'fgsd', 'gf']))
print(string_info("IzpodvipODverTa"))
print(is_contains("mo", ['m0', 'fd', 'dd', 87, "Mol"]))
print(f'Количество вызовов функций: {calls}')
