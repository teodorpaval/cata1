table_move = {0: [6, 9], 2: [3], 3: [2, 5], 5: [3], 6: [0, 9], 9: [0, 6],
              -2: [-3], -3: [-2, -5], -5: [-3], -6: [0, -9], -9: [0, -6]}
table_add = [[8], [7], [], [9], [], [6, 9], [8], [], [], [8]]
table_remove = [[], [], [], [], [], [], [5], [1], [0, 6, 9], [3, 5]]

def solve_1(left, right):

    result = move(left, right)
    if len(result) > 0:
        return result
    else:
        result = move(right, left)
        if len(result) > 0:
            return result

    return left, right


def move(left, right):

    for i in range(0, len(left)):
        if left[i] in table_move.keys():
            aux = left[i]
            for j in table_move[aux]:
                left[i] = j
                if sum(left) == sum(right):
                    return left, right
            left[i] = aux

    return []


def differences(l, t):
    res = {}
    for i in l:
        for j in t[abs(i)]:
            if i < 0:
                diff = -j - i
                res[diff] = [i, -j]
            else:
                diff = j - i
                res[diff] = [i, j]
    return res


def sum_lists(left, right):

    left_remove = differences(left, table_remove)
    left_add = differences(left, table_add)
    right_remove = differences(right, table_remove)
    right_add = differences(right, table_add)

    return left_remove, left_add, right_remove, right_add
