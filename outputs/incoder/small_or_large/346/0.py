
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "small" if n >= 15 (and None if 10 <= n < 15).
    """
    if n < 10:
        return "mouse"
    elif n >= 15:
        return "small"
    else:
        return None


# ______________________________________________________________________________
# Problem 5
# ______________________________________________________________________________


def compute_sum_of_squares(A):
    """
        Compute sum of squares from matrix A.
    """
    return sum([sum(i**2) for i in A])


# ______________________________________________________________________________
# Problem 6
# ______________________________________________________________________________


def matrix_multiplication(p_mat1, p_mat2):
    """
        Matrix multiplication between matrix p_mat1 and p_mat2.
        For example, p_mat1 = [[1, 2], [3,4]] and p_mat2 = [[5, 6], [7, 8]],
        then matrix_multiplication should return [[53, 66], [91, 102]].
    """
    result = [[0 for x in range(len(p_mat1[0]))] for y in range(len(p_mat2))]
    for i in range(len(p_mat1)):
        for j in range(len(p_mat1[0])):
            for k in range(len(p_mat2)):
                result[k][j] += p_mat1[i][k] * p_mat2[k][j]
    return result


# ______________________________________________________________________________
# Problem 7
# ______________________________________________________________________________


def matrix_multiplication_transpose(p_mat1, p_mat2):
    """
        Matrix multiplication between matrix p_mat1 and p_mat2.
        For example, p_mat1 = [[1, 2], [3,4]] and p_mat2 = [[5, 6], [7, 8]],
        then matrix_multiplication_transpose(p_mat1, p_mat2) should return [[1, 3, 5], [2, 4, 7], [3, 6, 9], [4, 8, 12]].
    """
    result = [[0 for x in range(len(p_mat1[0]))] for y in range(len(p_mat1))]
    for i in range(len(p_mat1)):
        for j in range(len(p_mat1[0])):
            for k in range(len(p_mat2)):
                result[i][j] += p_mat1[i][k] * p_mat2[k][j]
    return result


# ______________________________________________________________________________
# Problem 8
# ______________________________________________________________________________


def inverse_matrix(matrix):
    """
        Find the inverse of the square matrix using LU decomposition.
    """
    L, D, U = lu(matrix)
    inverse = inverse_lu(L, D)
    for i in range(len(inverse)):
        inverse[i][i] = 1
        inverse[i][-1] = -1
        for j in range(len(inverse[i])):
            inverse[i][j] /= U[i, j]
    return inverse


def inverse_lu(L, D):
    """
        Inverse the matrix using LU decomposition.
    """
    inverse = []
    for i in range(len(L)):
        inverse.append([])
        for j in range(len(L[i])):
            inverse[i].append(L[i][j] / 