def print_params(a: int = 1, b: str = 'строка', c: bool = True):
    return a, b, c


print(*print_params(1, 3, 4))
print(*print_params(1, 3))
print(*print_params(b=''))
print(*print_params(c=[1, 2, 3]))
values_list = [1, 'str', False]
values_dict = {'a': 1, 'b': 'yes', 'c': False}
print(*print_params(*values_list))
print(*print_params(**values_dict))
values_list2 = [1, 'adf']
print(*print_params(*values_list2))
