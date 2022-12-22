for N in range(1,10000000000000000):
    x=bin(N)[2:]
    if N%2==0: x='10'+x+'1'
    else: x='1'+x+'01'
    R=int(x,2)
    if R>420:
        print(N)
        break
        
