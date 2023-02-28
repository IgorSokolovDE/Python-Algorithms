for n in range(1,10000000000000000):
    s='>2'+'12'*n+'<'
    while not(('>2<' in s)or('><' in s)):
        s=s.replace('>1','>2',1)
        s=s.replace('12<','1<2',1)
        s=s.replace('>21','1>',1)
        s=s.replace('1<','<2',1)
    if ('>2<' in s):    
        SumCifr=0
        for s1 in s:
            if s1!='<' and s1!='>':
                SumCifr=SumCifr+int(s1)
        if SumCifr>103:
            print(n)
            break
    
