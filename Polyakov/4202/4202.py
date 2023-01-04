n = 10_000_000
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
blizneci=0
for i in range(len(lst)-1):
    if lst[i]>3_000_000:
        if (lst[i+1]-lst[i])==2:
            blizneci+=1
            avg=(lst[i+1]+lst[i])/2
print(blizneci,avg)            
   
