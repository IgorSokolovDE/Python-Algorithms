def F(n):
    global kPr
    if n>45:
        return
    if n==45:
        kPr+=1
        return
    else:
        if not('6' in str(n+1)):
            F(n+1)
        if not('6' in str(n+3)):
            F(n+3)    
           

kPr=0
F(1)
print(kPr)
