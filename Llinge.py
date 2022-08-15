def Llinge(a):
    b=a
    for k in range (0, len(b)-2):
        if b[k]==(b[k+1].lower()):
            b=b[0:k]+b[k+2:len(b)-1]
    print(b)
            
Llinge('aAuqigbBcd')
