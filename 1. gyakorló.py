print("1. feladat")
while True:
    szam=input("A háromszög első oldalának hossza:" )
    if szam=="end":
        break
    szam2=input("A háromszög második oldalának hossza:" )
    if szam2=="end":
        break
    szam3=input("A háromszög harmadik oldalának hossza: ")
    if szam3=="end":
        break
    szam, szam2, szam3 = float(szam), float(szam2), float(szam3)
    if szam+szam2>szam3 and szam2+szam3>szam and szam+szam3>szam2:
        print("A háromszög egyenlőtlenség teljesül, vagyis szerkeszthető háromszög ezekkel az adatokkal.")
    else:
        print("A háromszög nem szerkeszthető meg.")
print()
print("2. feladat")
import math
def terulet(szam, szam2, szam3):
    s=(szam+szam2+szam3)/2
    t=s*(s-szam)*(s-szam2)*(s-szam3)
    T=math.sqrt(t)
    return T

while True:
    szam=input("A háromszög első oldalának hossza:" )
    if szam=="end":
        break
    szam2=input("A háromszög második oldalának hossza:" )
    if szam2=="end":
        break
    szam3=input("A háromszög harmadik oldalának hossza: ")
    if szam3=="end":
        break
    szam, szam2, szam3 = float(szam), float(szam2), float(szam3)
    if szam+szam2>szam3 and szam2+szam3>szam and szam+szam3>szam2:
        print("A háromszög egyenlőtlenség teljesül, vagyis szerkeszthető háromszög ezekkel az adatokkal.")
        print("A háromszög területe:", terulet(szam, szam2, szam3))
    else:
        print("A háromszög nem szerkeszthető meg.")
print()
print("3. feladat")
def mgh_kereso(szoveg):
    mgh=["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]
    db=0
    szoveg=szoveg.lower()
    for betu in szoveg:
        if betu in mgh:
            db += 1
    return db

szoveg=input("Írjon be egy sztringet: ")
print(f"A megadott sztringben {mgh_kereso(szoveg)} db magánhangzó van.")