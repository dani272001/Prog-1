import numpy as np
print("1. feladat")

def dist_from_average(a, atlag):
    b = np.array(abs(a[0] - atlag))
    for i in range(1, a.size):
        b = np.append(b, abs(a[i] - atlag))
    return b

a = np.random.randint(1, 10, 10)
atlag = np.average(a)
#print(a)
#print("Átlag:", atlag)
#print(dist_from_average(a, atlag))

print("\n2. feladat")

five = np.random.randint(1, 91, 5)
print(five)
while True:
    try:
        tipp = int(input("Kérem írjon be egy számot 1 és 90 között: "))
        if tipp in five:
            print("Találat!")
            break
        #if tipp <= 0 or tipp > 90:
            #raise Exception("1 és 90 közti számot adj meg!")
        elif tipp not in five:
            raise Exception("Nem talált!")
    except Exception as not_found:
        print(not_found)
    #except Exception as joke:
        #print(joke)

print("\n3. feladat")
def neg_four(vec):
    four = 0
    for i in range(vec.size):
        if vec[i] % 4 == 0:
            vec[i] = -4
            four += 1
    return b, four

b = np.arange(1, 301, 3)
#print(b)
# vector, darab = neg_four(b)
# print(vector)
# print(f"{darab} darab számot kellett átváltoztatni -4-re.")
#másik megoldás
# b[b % 4 == 0] = -4
# print(b)
# minusz_negy = b[b == -4]
# print(f"{minusz_negy.size} darab számot kellett átváltoztatni -4-re.")

print("\n4. feladat")
#file_name = input("Adja meg a fájl nevét .txt kiterjesztésben: ")
#g = open(file_name, "w")
#b = np.random.randint(1, 11, 50)
##print(np.bincount(b).argmax())   #megadja, hogy melyik a leggyakoribb
#x = np.bincount(b)  #megszámolja, hogy az adott elemek hányszor fordulnak elő + 1 elemmel ad vissza listát
#print(b, file=g)
#y = x[1:]
#print(y)
#ind = np.where(y == y.max())
#print("A legtöbbet szereplő szám:", int(ind[0])+1, file=g)
#max_ertek = y.max()
#print("Előfordulások száma:", max_ertek, file=g)
#g.close()

print("\n5. feladat")
harom_adat = input("Adja a kezdőpontot, végpontot és az elemek számát: ")
kpont, vpont, elem = harom_adat.split()
kpont, vpont, elem = int(kpont), int(vpont), int(elem)
vector = np.random.randint(kpont, vpont, elem)
print("Vektor:", vector)
atlag = np.average(vector)
ertek = vector[(vector < atlag) & (vector % 2 == 0)]
indexek = np.where((vector < atlag) & (vector % 2 == 0))
print("Elemek:", ertek)
print("Helyeik:", indexek)