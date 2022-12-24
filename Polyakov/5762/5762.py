n = 1000
lst=[2]
for  i in range(3,n+1,2):
    if (i>10) and(i%10==5):
        continue
    for j in lst:
        if j*j-1>i:
            lst.append(i)
            break
        if (i%j==0):
            break
    else:
        lst.append(i)
A=[]
for i in range(4):
    for j in range(len(lst)):
        if i!=j:
            Ch=lst[i]**12*lst[j]**2
            if Ch>1000_000_000:
                break
            else:
                if Ch>=100_000_000:
                    A.append(Ch)
A.sort()
for i in range(5):
    x=A[i]
    d=2
    while (x%2)==0:
        x=x//2
    print(A[i],x)    
for i in range(-5,0):
    x=A[i]
    d=2
    while (x%2)==0:
        x=x//2
    print(A[i],x) 

               
