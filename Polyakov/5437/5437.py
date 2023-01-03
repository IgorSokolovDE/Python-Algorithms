def Crazy(n):
    x=n
    i=0
    SumChRazr=0
    SumNeChRazr=0
    while x>0:
        if i%2==0:
            SumChRazr+=x%10
        else:
            SumNeChRazr+=x%10
        i+=1
        x=x//10
    if  SumChRazr==0:
        return False
    else:
       return(SumNeChRazr%SumChRazr)==0
A=[int(x) for x in open('17-343.txt')]
kTR=0
MinSumElTR=100000000000000000000000000
for i in range(len(A)-2):
    if Crazy(A[i])and Crazy(A[i+1])and Crazy(A[i+2]):
        kTR+=1
        MinSumElTR=min(MinSumElTR,(A[i]+A[i+1]+A[i+2]))
print(kTR,MinSumElTR)        
