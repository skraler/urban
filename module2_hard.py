from random import randint


def crack_a_code(main_num: int) -> str:
    my_list = [x for x in range(1, 20)]
    res = ''
    for i in range(len(my_list)):
        for x in range(i + 1, len(my_list)):
            if main_num % (my_list[i] + my_list[x]) == 0:
                pair_num = str(my_list[i]) + str(my_list[x])
                res += pair_num
    return res


dict_with_answer = {3: '12', 4: '13', 5: '1423', 6: '121524', 7: '162534', 8: '13172635', 9: '1218273645',
                    10: '141923283746', 11: '11029384756', 12: '12131511124210394857', 13: '112211310495867',
                    14: '1611325212343114105968',
                    15: '1214114232133124115106978', 16: '1317115262143531341251161079', 17: '11621531441351261171089',
                    18: '12151811724272163631545414513612711810', 19: '118217316415514613712811910',
                    20: '13141911923282183731746416515614713812911'}

for x in dict_with_answer.keys():
    assert crack_a_code(x) == dict_with_answer[x]