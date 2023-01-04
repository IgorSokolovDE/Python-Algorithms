f=open('27-92b.txt')
N=int(f.readline())
a=[int(x) for x in f]
B=[]
Sum=0
Min=0
MaxSumPos=-100000000000000000000
for i in range(N):
    Sum+=a[i]
    if (a[i]>0)and(a[i]%2==0):
        PredMin=Min
        Min=min(B)
        Max=max(B)
        MaxSumPos=max(MaxSumPos,(Max-PredMin))
        B=[]
        B.append(Sum)
    else:
       B.append(Sum)
print(MaxSumPos)      
        
    
