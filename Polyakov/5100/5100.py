for N in range(1,10000000):
    x=bin(N)[2:]
    if N%2==0:
        x=x+'10'
    else:
        x='1'+x+'01'
    m=int(x,2)
    if m>516:
        print(N)
        break
