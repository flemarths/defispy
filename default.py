import random
import string

def  password(n):
    word=''
    abc=string.ascii_lowercase
    for i in range (0,n):
        word+=abc[random.randint(0,len(abc)-1)]
    return word

print(password(10))
        
