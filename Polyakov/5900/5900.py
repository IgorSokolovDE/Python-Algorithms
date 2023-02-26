k=0
for N in range(100,201):
    N2=bin(N)[2:]
    if len(N2)%2==0:
        N2=N2+'10'
    else:
        N2='11'+N2
    R=int(N2,2)
    if R%2==0:
        k+=1
print(k)    
