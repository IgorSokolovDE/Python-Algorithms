k=1
while k*4173<10**10:
    ch=k*4173
    s=str(ch)
    if (s[0]=='1')and(s[-1]=='1')and(len(s)>=7):
        if s[2:6]=='7246':
            print(ch)
    k+=1

    
