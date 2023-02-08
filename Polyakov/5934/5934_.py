for m in range(45,5000):
    Ms=str(m)
    if (Ms[0]=='4')and('5' in Ms[1:]):
        s='12'+Ms+'79'
        sumNeChCifr=0
        sumVseCifr=0
        for sym in s:
            sumVseCifr+=int(sym)
            if int(sym)%2!=0:
                 sumNeChCifr+=int(sym)
        if sumNeChCifr>0:         
           if int(s)%sumNeChCifr ==0:
               print(s,sumVseCifr)
               
