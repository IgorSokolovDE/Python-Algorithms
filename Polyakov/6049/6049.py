k=1
while k*9601<=10**10:
    ch=k*9601
    sCh=str(ch)
    if len(sCh)>=6:
        if (sCh[:2]=='19') and(sCh[-1]=='9'):
            if '105' in (sCh[2:-1]):
                print(ch,k)
        
    k+=1
