f=open('27-114b.txt')
n=int(f.readline())
A=[]
MaxPodPos=0
for i in range(n):
    x=int(f.readline())
    mn=[]
    dn=2
    while x>1:
        if x%dn==0:
            if not(dn in mn):
                mn.append(dn)
            x//=dn
        else: dn+=1
    A.append(mn)
for i in range(n-1):
    mn=A[i]
    for dn in mn:
        podPos=1
        j=i+1
        while j<n:
            if not(dn in A[j]):
                break
            else:
                podPos+=1
                j+=1
        MaxPodPos=max(podPos,MaxPodPos)
print(MaxPodPos)       
        
            
        
