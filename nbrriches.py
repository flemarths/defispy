def liste(x):
    L = []
    carre = str(x**2)
    cube = str(x**3)
    for k in carre :
        L.append(k)
    for k in cube :
        L.append(k)
    return L


def testrich(L):
    temoin = [1 for i in range (0,10)]
    sujet = []
    for k in range (0,10):
        xk = 0
        for l in L:
            if str(l) == str(k) :
                xk = 1
        sujet.append(xk)
    return temoin == sujet


def main(xmin,xmax):
    L = []
    for k in range (xmin,xmax+1):
        if testrich(liste(int(k))):
            L.append(k)
    return L

min,max = int(input('Quel est le min ? :')), int(input('Quel est le max ? :'))

print((main(min,max))
