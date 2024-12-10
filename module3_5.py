def get_multiplied_digits(number: int) -> int:
    str_number = str(number).replace('0', '')
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
