def F(n):
    global kPr
    if n>49:
        return
    if n==49:
        kPr+=1
        return
    else:
        if not('5' in str(n+1)):
            F(n+1)
        if not('5' in str(n+3)):
            F(n+3)    
        if not('5' in str(n*3)):
            F(n*3)    

kPr=0
F(1)
print(kPr)
