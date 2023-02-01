k=0
for n in range(10,100):
    s='1'+'0'*n
    while '10' in s:
        if '10' in s:
            s=s.replace('10','001',1)
        if '1' in s:
             s=s.replace('1','01',1)
    kolS=len(s)
    prost=True
    for d in range(2,kolS):
        if kolS%d==0:
            prost=False
            break
    if prost:
        k+=1
print(k)        
