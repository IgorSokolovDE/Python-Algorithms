A=[]
for x in range(2,30001):
    Sum=1
    for d in range(2,int(x**0.5)+1):
        if x%d==0:
            Sum+=d
            if d*d!=x:
                 Sum+=x//d
    A.append([x,Sum])
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[j][0]==A[i][1]:
            if A[j][1]==A[i][0]:
                print(A[i][0],A[i][1])
                break
            
    
