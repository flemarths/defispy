L=[i for i in range (1,32)]         #mois long
C=[i for i in range (1,31)]         #mois court
FNB=[i for i in range (1,29)]       #fevrier non bissextile
FB=[i for i in range (1,30)]        #fevrier bissextile

semaine=[5,5,8,5,8,6,8]
année_norm=[L,FNB,L,C,L,C,L,L,C,L,C,L]
année_bis=[L,FB,L,C,L,C,L,L,C,L,C,L]
F=[]
annéedépart=2000


def année_normale(D):
    for i in année_norm:
        for j in i:
           # print (j)
            D.append(j)
    return D

def année_bissextile(D):
    for i in année_bis:
        for j in i:
           # print (j)
            D.append(j)
    return D



def dernière(D):
    for i in L:
        D.append(i)
    for i in FNB:
        D.append(i)
    for i in [1,2,3,4,5,6,7,8]:
        D.append(i)
    return D


def années(F, fin):
    année=annéedépart
    while année<fin:
        if année%4==0:
            année_bissextile(F)
            année+=1
        else :
            année_normale(F)
            année+=1
    dernière(F)
    return F


def comptage(F,res):
    nbjours=0
    for i in F:
        #print(semaine[res]+i)
        if (semaine[res]+i)%10==0:
            nbjours+=1
            
        res=(res+1)%7
    return nbjours

print(comptage(années(F,2022),5))



        
        
