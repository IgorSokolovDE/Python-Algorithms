def F(x,y):
    if y==0:
        return x
    else:
        return F(y,x%y)
k=0
for x in range(1,1001):
    if F(x,48)==1:
        k+=1
print(k)        
