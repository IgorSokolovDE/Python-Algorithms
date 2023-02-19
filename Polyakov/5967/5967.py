def F(x,ss):
    S=''
    while x>0:
        if (x%ss)<10:
            S=str(x%ss)+S
        else:
            S=chr((x%ss)+87)+S
        x//=ss
    return S    
for m in range(20,30000):
    M=str(m)
    if M[:2]=='20':
        ch=int(M+'23')
        if ch<=2023**2:
            KolPalindrom=0
            SumSS=0
            for SS in range(2,37):
                NewCh=F(ch,SS)
                if NewCh==NewCh[::-1]:
                    KolPalindrom+=1
                    SumSS+=SS
            if KolPalindrom>=2:
                print(ch,SumSS)
                
            
