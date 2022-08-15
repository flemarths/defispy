import random

L=['pierre','feuille','ciseaux']

def coupordi():
    a=random.randint(0,2)
    return (L[a])

def coupjoueur():
    coupjoueur=input('quel votre coup ?')
    while coupjoueur != L[0] and coupjoueur != L[1] and coupjoueur != L[2] :
        coupjoueur=input('le coup n\'est pas valide, essaies encore!')

def jeu(scoremax):
    scorejoueur=0
    scoreordi=0
    while scorejoueur<scoremax and scoreordi<scoremax:
        j=coupjoueur()
        o=coupordi()
