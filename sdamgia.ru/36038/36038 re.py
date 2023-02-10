n=452021
kn=0
while kn<5:
    n+=1
    M=0
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            MinDel=d
            if d*d!=n:
                MaxDel=n//d
            else:
                MaxDel=d
            M=MinDel+MaxDel    
            break
    if M%7==3:
         print(n,M)
         kn+=1
        
        
