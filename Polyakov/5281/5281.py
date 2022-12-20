k=59
kn=0
while kn<7:
    k+=1
    ch=k*168
    sch=str(ch)
    if len(sch)>=5:
        if (sch[1]=='6') and (sch[-1]=='6'):
            if ('6' in sch[2:-2]):
                print(ch,end=' ')
                Del=[]
                for d in range(1,int(ch**0.5)+1):
                    if ch%d==0:
                        Del.append(d)
                        if d*d!=ch: Del.append(ch//d)
                print(sum(Del))
                kn+=1
                
