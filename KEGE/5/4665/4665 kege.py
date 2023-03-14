MaxR=0
for N in range(1,16):
    N2=bin(N)[2:]
    if N2.count('1')%2==0:
        N2=N2+'1'
        N2=N2[2:]
        N2='10'+N2
    else:
        N2=N2+'0'
        N2=N2[2:]
        N2='11'+N2
    R=int(N2,2)
    MaxR=max(MaxR,R)
print(MaxR)    
    
