def F(a,b):
    if (a==0)and(b==0):
        return 0
    else:
        if a > b:
            return F(a-1,b)+b
        else:
            return F(a,b-1)+a
#for a in range(11,15):
#    for b in range(11,15):
#        print(a,b,F(a,b))
kolA=0
X=18522000
for d in range(1,int(X**0.5)+1):
    if X%d==0:
        kolA+=1
        if d**2 !=X:
            kolA+=1
print(kolA)            
