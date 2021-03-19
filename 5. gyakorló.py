import numpy as np
print("1.feladat")
def rendez_n_elott_utan(a, n):
    for i in range(n):
        for j in range(i + 1, n + 1):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    for i in range(n + 1, a.size - 1):
        for j in range(i + 1, a.size):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a

a = np.random.randint(1, 16, 20)
#print(a)
#print(rendez_n_elott_utan(a, 7))

print("\n2.feladat")
def fele(mtx):
    avg = np.average(mtx)
    print(avg)
    for j in range(mtx.shape[1]):
        sum = 0
        for i in range(mtx.shape[0]):
            sum += mtx[i, j]
        if sum / mtx.shape[0] > avg:
            mtx[:, j] = mtx[:, j] / 2
    return mtx

def fele2(mtx):
    avg = np.average(mtx)
    print(avg)
    oszlop_atlag = np.average(mtx, axis=0)
    print(oszlop_atlag)
    for j in range(len(oszlop_atlag)):
        if oszlop_atlag[j] > avg:
            mtx[:, j] = mtx[:, j] / 2
    return mtx

sor = int(input("A sorok száma: "))
oszlop = int(input("Az oszlopok száma: "))
b = np.random.randint(1, 81, (sor, oszlop))
print(b)
#print(fele(b))
print(fele2(b))

print("\n3. feladat")
def szimmetrikus_e(mtx):
    for i in range(mtx.shape[0]):
        for j in range(mtx.shape[1]):
            if mtx[i, j] != mtx[j, i]:
                return "Hamis"
    return "Igaz"

c = np.random.randint(1, 10, (3, 3))
#print(c)
#print(szimmetrikus_e(c))

print("\n4. feladat")
def multiplier(vec, mtx):
    res = np.zeros((mtx.shape[0], mtx.shape[1]))
    for i in range(mtx.shape[0]):
        for j in range(mtx.shape[1]):
            res[i, j] = mtx[i, j] * vec[i]
    return res

try:
    vec = np.random.randint(2, 4, 3)
    matrix = np.random.randint(1, 10, (3, 4))
    print("Bekért vektor: \n", vec)
    print("Bekért mátrix: ")
    print(matrix)
    if vec.size != matrix.shape[0]:
        raise Exception("Nem megoldható!")
    else:
        print(multiplier(vec, matrix))
except Exception as ex1:
    print(ex1)