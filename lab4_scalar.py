


a = [1,2,12,4]
b = [2,4,2,8]

if len(a) == len(b):
    print('vectors are equal, calculating......')
    i = 0
    c = []
    for number in a:
        z = a[i] * b[i]
        c.append(z)
        i += 1
    print("Output:")
    print(c)
else:
    print("ERROR VECTORS ARE NOT EQUAL, CANNOT DOT PRODUCT")