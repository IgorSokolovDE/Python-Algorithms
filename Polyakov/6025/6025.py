mn=1
while mn*53<=10**7:
    ch=mn*53

    s=str(ch)
    if s==s[::-1]:
        netu2v2=True
        for v in '0123456789':
            if ('2'+v+'2') in s:
                netu2v2=False
                break
        if not(netu2v2):
            Del=[]
            for d in range(1,int(ch**0.5)+1):
                if ch%d==0:
                    Del.append(d)
                    if d**2!=ch:
                        Del.append(ch//d)
            if len(Del)>30:
                print(ch,sum(Del))

    mn=mn+1
