f=open('27-53b.txt')
N=int(f.readline())
ost0=[10000000,10000000,10000000]
ost1=[10000000,10000000,10000000]
ost2=[10000000,10000000,10000000]
for i in range(N):
    x=int(f.readline())
    if x%3==0:
        if x<ost0[2]:
            ost0[2]=x
            ost0.sort()
    if x%3==1:
        if x<ost1[2]:
            ost1[2]=x
            ost1.sort()        
    if x%3==2:
        if x<ost2[2]:
            ost2[2]=x
            ost2.sort()
m=min(sum(ost0),sum(ost1),sum(ost2),(ost0[0]+ ost1[0]+ost2[0]))
print(m)
