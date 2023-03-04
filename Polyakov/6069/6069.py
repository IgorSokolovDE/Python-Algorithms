a=[int(x) for x in open('17-354.txt')]
Min2=100000000000000000000000000000000
for x in a:
    if abs(x)%10==2:
       Min2=min(Min2,x)
kolPar=0
MinPlusSum=100000000000000000000000000
for i in range(len(a)-1):
    if abs((int(str(a[i])[-1]))-(int(str(a[i+1])[-1]))  )==1:
        if ((a[i]%5==0)and(a[i+1]%5 !=0))or\
           ((a[i]%5!=0)and(a[i+1]%5 ==0)):
            if (a[i]**2+a[i+1]**2)>Min2**2:
                kolPar+=1
                Sum=(a[i]+a[i+1])
                if Sum>0:
                   MinPlusSum=min(MinPlusSum,Sum)
print(kolPar,MinPlusSum)                   
