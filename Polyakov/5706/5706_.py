for N in range(1,10000000000000):
    n2=bin(N)[2:]
    if n2.count('1')%2==0:
        n2=n2+'0'
        n2=n2[2:]
        n2='10'+n2
    else:
        n2=n2+'1'
        n2=n2[2:]
        n2='11'+n2
    R=int(n2,2)
    if R>40:
        print(N)
        break
