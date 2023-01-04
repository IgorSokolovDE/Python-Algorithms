def F(n):
    global k
    k+=1
    if k>100:
        return -10000000000000
    if n<=5:
        return n
    else:
        if n%5==0:
            return n+F(n//5+1)
        else:
            return n+F(n+6)
for n in range(1,100000000):
    k=0
    if F(n)>1000:
        print(n)
        break
