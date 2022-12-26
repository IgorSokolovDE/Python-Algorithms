def VazimnoProst(x,y):
    for D in range(min(x,y),0,-1):
        if (x%D==0)and(y%D==0):
            break
    if D==1:
        return True
    else:
        return False
kn=0    
for n in range(100_000_000,150_000_000):
    Del=[]
    for D in range(2,int(n**0.5)+1):
        if n%D==0:
            Del.append(D)
            if D*D!=n:
                Del.append(n//D)
        if  len(Del)>=6:
            break
    if len(Del)>=3:
        Del.sort()
        if VazimnoProst(Del[0],Del[1])and\
           VazimnoProst(Del[0],Del[2])and\
           VazimnoProst(Del[2],Del[1]):
            kn+=1
            print(n,Del[-1])
            if kn>6:
                break
        
