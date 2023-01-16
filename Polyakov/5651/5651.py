A=[]
for x in range(10):
    for y in range(3,4000):
        yS=str(y)
        if yS[0]=='3':
            S=yS+'52'+str(x)
            ch=int(S)
            Del=[]
            for d in range(1,int(ch**0.5)+1):
                if ch%d==0:
                    Del.append(d)
                    if d*d!=ch:
                        Del.append(ch//d)
            Del.sort()
            Del=Del[::-1]
            if len(Del)%2!=0:
                A.append([ch,Del[1]])
A.sort()
for i in range(len(A)):
    print(A[i][0],A[i][1])
