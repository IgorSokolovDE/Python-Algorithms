a=[int(x) for x in open('17-328.txt')]
maxKr50=0
for x in a:
    if x%50==0:
        maxKr50=max(maxKr50,x)
k3=0
maxSum3=0
for i in range(len(a)-2):
    sum1=str(a[i]+a[i+1])
    sum2=str(a[i]+a[i+2])
    sum3=str(a[i+1]+a[i+2])
    if (sum1==sum1[::-1])and(sum2==sum2[::-1])and(sum2==sum2[::-1]):
        maxSum=max((a[i]+a[i+1]),(a[i]+a[i+2]),(a[i+1]+a[i+2]))
        if maxSum<maxKr50:
            k3+=1
            maxSum3=max(a[i+2]+a[i+1]+a[i],maxSum3)
print(k3,maxSum3)            
