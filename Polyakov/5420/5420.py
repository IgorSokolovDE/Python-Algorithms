MaxS=''
for pered in range(0,204):
    posle=203-pered
    s='1'*pered+'2'+'1'*posle
    while ('111' in s)or('222' in s):
        if ('111' in s):
            s=s.replace('111','22',1)
        else:
            s=s.replace('222','11',1)
           
    if len(s)>len(MaxS):
        MaxS=s
print(MaxS)        
