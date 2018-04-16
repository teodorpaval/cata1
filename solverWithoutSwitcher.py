from copy import deepcopy
from solver import sum_lists
from solver import move

def solver_2(r_l,a_l,r_r,a_r, original_left, original_right):

    si_r = sum(original_right)
    si_l = sum(original_left)
    suma_needed = 0
    if(si_r >si_l):
        suma_needed = si_r-si_l
    else:
        suma_needed = si_l - si_r
    for i in r_l:
        for j in a_l:
            if si_l + i + j == si_r:
                for k in range(0, len(original_left)):
                    if original_left[k] == r_l[i][0]:
                        original_left[k] = r_l[i][1]
                    if original_left[k] == a_l[j][0]:
                        original_left[k] = a_l[j][1]
                return original_left, original_right

        for j in a_r:
            if si_l + i == si_r + j:
                for k in range(0, len(original_left)):
                    if original_left[k] == r_l[i][0]:
                        original_left[k] = r_l[i][1]
                for k in range(0, len(original_right)):
                    if original_right[k] == a_r[j][0]:
                        original_right[k] = a_r[j][1]
                return original_left, original_right

    for i in r_r:
        for j in a_l:
            if si_r + i == si_l + j:
                for k in range(0, len(original_right)):
                    if original_right[k] == r_r[i][0]:
                        original_right[k] = r_r[i][1]
                for k in range(0, len(original_left)):
                    if original_left[k] == a_l[j][0]:
                        original_left[k] = a_l[j][1]
                return original_left, original_right

        for j in a_r:
            if si_r + i + j == si_r:
                for k in range(0, len(original_right)):
                    if original_right[k] == r_r[i][0]:
                        original_right[k] = r_r[i][1]
                    if original_right[k] == a_r[j][0]:
                        original_right[k] = a_r[j][1]
                return original_left, original_right

