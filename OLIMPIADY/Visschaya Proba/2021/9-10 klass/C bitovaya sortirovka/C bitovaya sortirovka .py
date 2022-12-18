def NeUbiv():
    DecASort=DecA[:]
    DecASort.sort()
    return (DecASort==DecA)
def zameni(kzamen):
    NASCHLI=False        
    for i in range(n):
        for j in range(k):
            if BinA[i][j]=='0':
                 BinA[i][j]='1'
            else:
                 BinA[i][j]='0'
            DecA[i]=int(''.join(BinA[i]),2)
            if kzamen>1:
                NASCHLI2=zameni(kzamen-1)
                if NASCHLI2:
                    NASCHLI=True
            if NeUbiv():
                NASCHLI=True
                break
            if BinA[i][j]=='0':
                 BinA[i][j]='1'
            else:
                 BinA[i][j]='0'
            DecA[i]=int(''.join(BinA[i]),2)     
        if NASCHLI:
                break     
    return NASCHLI        
    
f=open('data.txt')
t=int(f.readline())
for T in range(t):
    #n,k=map(int, f.readline().split())
    s=f.readline()
    a=s.split()
    n=int(a[0])
    k=int(a[1])
    BinA=[]
    for i in range(n):
        binCifr=[]
        s=f.readline()
        for j in range(len(s)-1):
           binCifr.append(s[j])
        BinA.append(binCifr)  
    DecA=[]
    for i in range(n):
        DecA.append(int(''.join(BinA[i]),2))

    kzamen=0
    while True:
        if n==1:
            print(kzamen)
            break
        kzamen+=1
        if zameni(kzamen):
           print(kzamen)
           break
      
