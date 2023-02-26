for N in range(1,10000000000000000):
    S1=0
    S2=0
    S=str(N)
    for i in range(len(S)):
        if (int(S[i]))%2!=0:
            S1+=int(S[i])
        if i%2!=0:
            S2+=int(S[i])
    R=abs(S1-S2)
    if R==30:
        print(N)
        break
