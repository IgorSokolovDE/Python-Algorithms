s=open('24 (2).txt').readline()
kTr=0
MaxKtr=0
i=0
while i<len(s)-2:
    if (s[i] in 'BCDF')and(s[i+1] in 'AEU')and(s[i+2] in 'BCDF'):
        kTr+=1
        MaxKtr=max(MaxKtr,kTr)
        i+=3
    else:
        kTr=0
        i+=1
print( MaxKtr)       
