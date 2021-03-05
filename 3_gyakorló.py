print("1. feladat")
import sys

def list_selecter(n, args):
    list1 = []
    list2 = []
    for arg in args[2:]:
        if len(arg) < n:
            list1.append(arg)
        elif len(arg) > n:
            list2.append(arg)
        #elif len(arg) == n:
        else:
            list1.append(arg)
    #return(f"list1 = {list1}, list2 = {list2}")
    return("list1 = {}, list2 = {}".format(list1, list2))

#n = int(sys.argv[1])
#print(list_selecter(n, sys.argv))

print("\n2. feladat")
import random
def number_generator(n, output):
    list1 = []
    list2 = []
    for i in range(n):
        list1.append(random.randint(0, 10))
        list2.append(random.randint(0, 10))
    print("Első lista: ", file=output, end="")
    for elem in list1:
        print(elem, file=output, end=" ")
    print("\nMásodik lista: ", file=output, end="")
    for elem2 in list2:
        print(elem2, file=output, end=" ")
    reversed_list2 = list2[::-1]
    result = []
    for i in range(n):
        result.append(list1[i]*reversed_list2[i])
    print("\nEredmény: ", file=output, end="")
    for er in result:
        print(er, file=output, end=" ")

# output=open(sys.argv[2], "w")
# number_generator(int(sys.argv[1]), output)
# output.close()

print("3. feladat")
def monograms(word1, word2):
    msh = ["cs", "dz", "gy", "ly", "sz", "ty", "zs"]
    msh2 = ["c", "d", "g", "l", "s", "t", "z"]
    db = 0
    if len(word1) == len(word2):
        seged = ""
        seged2 = ""
        kapcsolo = False
        for ch in word1:
            seged = ch
            if seged in msh2:
                seged2 += seged
                seged = ""
                if len(seged2) == 2:
                    if seged2 in word2:
                        db += 1
                        seged2 = ""
                    elif seged2 not in msh:
                        seged = seged2[0]
                        seged2 = ""
                        if seged in word2:
                            db += 1
                            kapcsolo = True
                            seged = ""
                elif len(seged2) == 1 and seged2 in word2 and kapcsolo == False:
                    db += 1
                    continue
            elif seged in word2:
                db += 1
                seged = ""
        if db == len(word1):
            return "Igaz"
        else:
            return "Hamis"
    else:
        return "Hamis"

#print(monograms(sys.argv[1], sys.argv[2]))