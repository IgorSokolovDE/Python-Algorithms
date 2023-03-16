for N in range(3,1000):
    N2=bin(N)[2:]
    if N2.count('1')%2==0:
        N2=N2+'0'
        N2= N2[2:]
        N2='10'+N2
    else:
        N2=N2+'1'
        N2 =N2[2:]
        N2='11'+N2
    R=int(N2,2)
    if R>=16:
        print(N)
        break
