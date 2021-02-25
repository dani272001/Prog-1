print("1. feladat")
while True:
    try:
        ket_szam = input("Adjon meg 2 egész számot 0-100 között: ")
        a, b = ket_szam.split()
        a, b = int(a), int(b)
        if a < 0 or a > 100 or b < 0 or b > 100:
            raise Exception("Nem megfelelő szám!")
        if (a+b)/2 < 60:
            raise Exception("Megbukott!")
        elif 0 <= a <= 100 and 0 <= b <= 100 and (a+b)/2 >= 60:
            print((a+b)/2)
            break
    except Exception as ex1:
        print(ex1)
    except Exception as ex2:
        print(ex2)
print("\n2. feladat")
def sor_atlag(numbers):
    osszeg = 0
    db = 0
    for number in numbers:
        if int(number) > 0:
            osszeg += int(number)
            db += 1
    if db == 0:
        return("Nem számolható átlag!")
    else:
        return osszeg/db

try:
    in_file=open("szamok.txt", "r")
    for line in in_file:
        numbers = line.split()
        print(sor_atlag(numbers))
    in_file.close()
except FileNotFoundError:
    print("A fájl nem található!")

print("\n3. feladat")
def same_letters(line):
    sor = ""
    import string
    for ch in line:
        if ch not in string.punctuation:
            sor += ch
    words=sor.split()
    for word in words:
        if word[0].isupper():
            word=word.lower()
            if word[0] == word[-1] and len(word) > 1:
                word=word.capitalize()
                print(word, file=out)
        else:
            if word[0] == word[-1] and len(word) > 1:
                print(word, file=out)
try:
    in_file=open("szoveg.txt", "r")
    out=open("output.txt", "w")
    for line in in_file:
        line=line.strip()
        line=same_letters(line)
    if line != None:
        print(line, file=out, end="")
    in_file.close()
    out.close()
except FileNotFoundError:
    print("A fájl nem található!")