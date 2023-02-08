s=open('24-232.txt').readline()
maxDlina=0
SumCifrmaxDlina=0
a=s.split('0')
a.pop(0)
a.pop(-1)
for w in a:
    SumCifr=0
    for sym in w: SumCifr+=int(sym)
    if SumCifr%5==0:
        if len(w)>maxDlina:
            maxDlina=len(w)
            SumCifrmaxDlina=SumCifr
print(SumCifrmaxDlina)            
        
        
