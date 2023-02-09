def F(n,s):
    global kPr
    if n>27: return
    if n==27:
        if 'BCA' in s:
            kPr+=1
        return
    else:
        F(n+1,s+'A')
        F(n*2,s+'B')
        F(n*3,s+'C')
kPr=0
F(2,'')
print(kPr)
