for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(1,200):
                m=str(d)
                if m[0]=='1':
                    ch=int('1'+str(a)+'1'+str(b)+'1'+str(c)+m+'1')
                    if ch%2023==0:
                        Sch=str(ch)
                        sumCifr=0
                        for s1 in Sch:
                            sumCifr+=int(s1)
                        if sumCifr==22:
                            print(ch,ch//2023)
            
