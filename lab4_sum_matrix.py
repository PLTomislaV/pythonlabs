import random

w, h = 128, 128

Matrix1 = [[random.randint(-100, 100) for x in range(w)] for y in range(h)]
Matrix2 = [[random.randint(-100, 100) for x in range(w)] for y in range(h)]
Matrix_out = [[0 for x in range(w)] for y in range(h)]

print(Matrix2)
print(Matrix1)
print(Matrix_out)

for x in range(len(Matrix1)):  # rows
    for y in range(len(Matrix1[0])):  # column
        Matrix_out[x][y] = Matrix1[x][y] + Matrix2[x][y]

print("Result matrix:")
print(Matrix_out)
