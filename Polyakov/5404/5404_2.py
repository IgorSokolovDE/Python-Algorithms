def F(n):
    global k
    if n<10:
        if n==8:
            k+=1
        return
    else:
        F((n//10)+(n%10))
        F((n//10)*(n%10))
        
kolCh=0
for n in range(10,100):
    k=0
    F(n)
    if k>0: kolCh+=1
print(kolCh)    
