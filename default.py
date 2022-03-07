import random

def  password(n):
    word=''
    for i in range (0,n):
        word+=str(random.randint(0,10))
    return word

print(password(10))
        
