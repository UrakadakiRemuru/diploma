from typing import List, Any

A = [[-2, 3, -3], [1, 1, -3], [2, -1, -4]]

def format_matrix(A: List[List]) -> List[List]:
    A = [[el * (-1) if ind != len(row) - 1 else el for ind, el in enumerate(row)] for row in A]
    return A
def find_row(list1: List, list2: List) -> int:
    min_val = min([i for i in list1])
    index = list1.index(min_val)
    if min_val == 0 and list2[index][0] > 0:
        return list2[index][1]
    elif min_val == 0:
        list1 = list1.pop(index)
        list2 = list2.pop(index)
        return find_row(list1, list2)
    else:
        return list2[index][1]
def choose_element(matrix: List[List]) -> Any:
    resolving_col = None
    ratio = []
    denom_ind = []
    for r, row in enumerate(matrix):
        if resolving_col is None:
            for c, el in enumerate(row):
                if el < 0:
                    resolving_col = c
                    break
                elif c == len(row) - 1:
                    break
            if resolving_col is not None:
                nom = matrix[r][len(matrix[0]) - 1]
                if nom <= 0:
                    cur = nom / matrix[r][resolving_col]
                    if cur >= 0:
                        ratio.append(cur)
                        denom_ind.append([matrix[r][resolving_col], r])
    if ratio:
        return [find_row(ratio, denom_ind), resolving_col]
    else:
        return None





def modified_jordan_method(A: List[List]) -> Any:
    A_r =[[0 for col in row] for row in A]
    marker = True
    while marker:
        tmp = choose_element(A)
        if tmp is not None:
            r, c = tmp
            print('разрешающий элемент', A[r][c])
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if i == r and j == c:
                        A_r[i][j] = 1 / A[r][c]
                    elif i == r and j != c:
                        A_r[i][j] = - A[r][j] / A[r][c]
                    elif i != r and j == c:
                        A_r[i][j] = A[i][r] / A[r][c]
                    else:
                        A_r[i][j] = (A[i][j] * A[r][c] - A[i][c] * A[r][j]) / A[r][c]
            A = A_r
            print(A)
        else:
            marker = False
            return A


A = format_matrix(A)
print(A)
new_A = modified_jordan_method(A)
print(new_A)