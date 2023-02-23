def F(n):
    global kPr
    if n>555:
        return
    if n==555:
        kPr+=1
        return
    else:
        F(n+1)
        F(n*10+1)
kPr=0
F(1)
print(kPr)
        
