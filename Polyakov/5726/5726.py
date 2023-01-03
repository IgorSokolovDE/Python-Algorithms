for m in range(1,100000000000):
    s='>'+'1'*17+'2'*34+'3'*m
    while ('>1' in s)or('>2' in s)or('>3' in s):
        if ('>1' in s):
            s=s.replace('>1','22>',1)
        if ('>2' in s):
            s=s.replace('>2','2>',1)
        if ('>3' in s):
            s=s.replace('>3','1>',1)
    SumCifr=0
    for i in range(len(s)-1):
        SumCifr+=int(s[i])
    Del=[]
    for d in range(2,int(SumCifr**0.5)+1):
        if SumCifr%d==0:
            Del.append(d)
            if d*d != SumCifr:
                Del.append(SumCifr//d)
        if len(Del)>3:
            break
    if len(Del)==3:
         print(m)
         break
