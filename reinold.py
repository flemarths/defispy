import numpy as np
import matplotlib.pyplot as plt


#Données et variables

n=100
X=0.6
eps=3
pas=0.01
m=n//2



#Définition des fonctions

def f(x,y):
    return y*x*(1-x)


def iterationlist(x,n):
    L=[x]
    for k in range (0,n):
        L.append(f(L[k],y))
    return L

def iterationX(X,n,y):
    L=[X]
    for k in range(0,n):
        L.append(f(L[k],y))
    return L

def test(L):
    A=[]
    for i in range (m,n):
        for k in range (m,n):
            if round(L[k],eps)==round(L[i],eps) and i!=k:
                if (round(L[i],eps) in A) == False :
                    A.append(round(L[i],eps))
    return A

def trace(L):
    for k in range (0,len(L)):
        for i in range(0,len(L[k])):
            plt.scatter(k*pas+2,L[k][i],color='blue',s=0.5)
    plt.show()

    
#Défintion des listes

abs=[i for i in range (1,n+2)]

L=0.1*np.arange(n)


ly=[2+i*pas for i in range (0,200)]

#Tracés


trace([test(iterationX(X,n,y)) for y in ly])


