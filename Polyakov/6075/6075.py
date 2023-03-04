def F(n):
    if n==0:
        return 0
    else:
        return F(n//10)+(n%10)
k=0
for n in range(15,630):
   if F(n)>F(n+1):
       k+=1
print(k)       
       
