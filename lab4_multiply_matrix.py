import random
import numpy

w, h = 8, 8

Matrix1 = [[random.randint(-100, 100) for x in range(w)] for y in range(h)]
Matrix2 = [[random.randint(-100, 100) for x in range(w)] for y in range(h)]
Matrix_out = [[0 for x in range(w)] for y in range(h)]


for i in range(len(Matrix1)):
    for j in range(len(Matrix2[0])):
        for k in range(len(Matrix2)):
            Matrix_out[i][j] += Matrix1[i][k] * Matrix2[k][j]

res = numpy.dot(Matrix1, Matrix2)

print(Matrix2)
print(Matrix1)
print(Matrix_out)
print(res)