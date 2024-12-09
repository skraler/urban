calls = 0


def count_calls() -> int:
    global calls
    calls += 1


def string_info(test_string: str) -> tuple:
    list_info = [len(test_string), test_string.upper(), test_string.lower()]
    count_calls()
    return tuple(list_info)


def is_contains(test_string: str, list_case: list) -> bool:
    count_calls()
    if test_string.lower() in [x.lower() for x in list_case]:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)