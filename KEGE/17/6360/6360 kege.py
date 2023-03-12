a=[int(x) for x in open('17_6360.txt')]
kpar=0
MaxSumPary=0
Min7=100000000000000000000000000000000
for x in a:
    if (abs(x))%10==7:
        Min7=min(Min7,x)
for i in range(len(a)-1):
    if abs(a[i])%10==abs(a[i+1])%10:
        if ((a[i]%7==0)and(a[i+1]%7!=0))or((a[i]%7!=0)and(a[i+1]%7==0)):
            if (a[i]**2+a[i+1]**2)<=Min7**2:
                kpar+=1
                MaxSumPary=max(MaxSumPary,(a[i]**2+a[i+1]**2))
print(kpar, MaxSumPary )              
