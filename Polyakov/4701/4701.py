def F7(x):
    S7=''
    while x>0:
        S7=str(x%7)+S7
        x//=7
    return ('36' in S7)    
A=[int(x) for x in open('17-243.txt')]
Max107=0
for x in A:
    if x%107==0:
        Max107=max(Max107,x)
kPar=0
minSum=1000000000000000000000000000000000000
for i in range(len(A)-1):
    if (A[i]>Max107)or(A[i+1]>Max107):
        if F7(A[i]) or F7(A[i+1]):
            kPar+=1
            minSum=min(minSum,(A[i]+A[i+1]))
print( kPar,minSum)           
        
        
