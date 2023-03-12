a=[int(x) for x in open('17_6049.txt')]
max9=-10000000000000000000000000000000
for x in a:
    if str(x)[-1]=='9':
        max9=max(max9,x)
kpar=0
MinSumKv=10000000000000000000000000000
for i in range(len(a)-1):
   if ((str(a[i])[-1]=='9')and(str(a[i+1])[-1]!='9'))or \
      ((str(a[i])[-1]!='9')and(str(a[i+1])[-1]=='9')):
       if (a[i]**2+a[i+1]**2)< max9**2:
           kpar+=1
           MinSumKv=min(MinSumKv,(a[i]**2+a[i+1]**2))
print(kpar, MinSumKv)      
