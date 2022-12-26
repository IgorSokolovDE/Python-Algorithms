A=[]
for m in range(4,50000):
    sm=str(m)
    if sm[0]=='4':
        for cifr1 in range(10):
            Ch=int(sm+'1'+str(cifr1)+'009')
            if Ch<=10**10:
                if (int(Ch**0.5))**2==Ch:
                    A.append(int(Ch**0.5))
A.sort()
for i in range(len(A)):
    print(A[i],A[i]**2)
                
