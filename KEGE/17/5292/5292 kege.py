a=[int(x) for x in open('17_5292.txt')]
min123=10000000000000000000000000000000
for x in a:
    if x%123==0:
        min123=min(min123,x)
kPar=0
MaxSumEl=0
for i in range(len(a)-1):
    if ((a[i]%2023>=min123)and(a[i+1]%2023<min123))or\
       ((a[i]%2023<min123)and(a[i+1]%2023>=min123)):
        kPar+=1
        MaxSumEl=max(MaxSumEl,(a[i]+a[i+1]))
print(kPar , MaxSumEl)       
