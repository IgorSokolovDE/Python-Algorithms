for N in range(1,100000):
    x=bin(N)[2:]
    if x.count('1')%2==0:
        x='1'+x+'00'
    else:
        x='11'+x
    R=int(x,2)
    if R>=412:
        print(N)
        break
