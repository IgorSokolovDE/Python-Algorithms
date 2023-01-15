for n in range(118811, 118973):
    Del=[]
    for d in range(1,int(n**0.5)+1):
        if n%d==0:
            Del.append(d)
            if d*d!=n:
                Del.append(n//d)
        if len(Del)>6:
            break
    if len(Del)==6:
        Del.sort()
        print(Del[-3],Del[-2])
