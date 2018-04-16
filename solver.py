def get_table():
    table = {0: [6, 9], 1: [], 2: [3], 3: [2, 5], 4: [], 5: [3], 6: [0, 9], 7: [], 8: [], 9: [0, 6]}
    return table


def solve_1(left, right):
    table = get_table()

    if right in table[left]:
        right = left
    elif left in table[right]:
        left = right

    return left, right


def assembler(left, right):
    result = solve_1(left, right)
    return str(result[0]) + "=" + str(result[1])
