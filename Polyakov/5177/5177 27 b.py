f=open('27-107b.txt')
N=int(f.readline())
stena=[]
for i in range(N):
    s=f.readline()
    a=s.split()
    stena.append([int(a[0]),int(a[1]),int(a[1])-int(a[0])])
 
stena.sort()
for ss in range(2000):
    i=0
    while i<len(stena)-1:
        if (stena[i][0]<=stena[i+1][0])and(stena[i][1]>=stena[i+1][1]):
            stena.pop(i)
        else:
            if (stena[i+1][0]<=stena[i][0])and(stena[i+1][1]>=stena[i][1]):
              stena.pop(i+1)
            else:
                i+=1          
Min=100000000000000000000000000000000000
for i in range(len(stena)):
    if stena[i][2]<Min:
        Min=stena[i][2]
        NunMin=i
i=NunMin
VipStena=[]
VipStena.append(stena[NunMin])
k=0
while i <len(stena)-1:
    if stena[i][0]<VipStena[k][1]: i+=1
    else:
        VipStena.append(stena[i])
        k+=1
i=NunMin
VipStena2=[]
VipStena2.append(stena[NunMin])
k=0
while i >=0:
    if stena[i][1]<=VipStena2[k][0]:
       VipStena2.append(stena[i])
       k+=1 
    else:         i-=1
print(len(VipStena)+len(VipStena2)-1)
