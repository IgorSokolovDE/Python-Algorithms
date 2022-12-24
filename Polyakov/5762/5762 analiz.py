for n in range(1,10000000):
    Del=[]
    for d in range(1,int(n**0.5)+1):
        if n%d==0:
            Del.append(d)
            if d*d!=n:
                Del.append(n//d)
        if len(Del)>39:
            break
    if len(Del)==39:
         Del.sort()
         print(n,Del)
         mn=[1]
         x=n
         d=2
         while x>1:
             if x%d==0:
                 mn.append(d)
                 x=x//d
             else:
                 d+=1
         print(mn)
         print()
