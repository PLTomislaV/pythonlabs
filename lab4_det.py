import random
import numpy


def determinant_recursive(A, total=0):
    indices = list(range(len(A)))

    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    for fc in indices:
        As = A
        As = As[1:]
        height = len(As)

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc + 1:]

        sign = (-1) ** (fc % 2)
        sub_det = determinant_recursive(As)
        total += sign * A[0][fc] * sub_det

    return total


def determinant_fast(A):
    n = len(A)
    AM = A

    for fd in range(n):
        for i in range(fd + 1, n):
            if AM[fd][fd] == 0:
                AM[fd][fd] == 1.0e-18
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
    product = 1.0
    for i in range(n):
        product *= AM[i][i]

    return product


w, h = 8, 8

Matrix1 = [[random.randint(-100, 100) for x in range(w)] for y in range(h)]
Matrix2 = Matrix1
Matrix3 = Matrix1
res = numpy.linalg.det(Matrix1)

out = determinant_fast(Matrix2)

out2 = determinant_recursive(Matrix3)

print(Matrix1)
print(res)
print(out)
print(out2)