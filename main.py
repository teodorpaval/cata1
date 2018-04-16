from solver import *
from solverWithoutSwitcher import *

original_left = [9,2,-3,-1]
original_right = [8,-4]

list = move(original_left, original_right)

if list == []:
    lists = sum_lists(original_left, original_right)
    print(solver_2(lists[0], lists[1], lists[2], lists[3], original_left, original_right))
else:
    print(list)