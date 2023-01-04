f=open('27-B (3).txt')
N,M=map(int, f.readline().split())
mn=[]
x=M
d=2
while x>1:
    if x%d==0:
        mn.append(d)
        x=x//d
    else:
        d+=1
A=[int(x) for x in f]
KolPodPos=0
for i in range(N):
    ClonMN=mn[:]
    for j in range(i,N):
        x=A[j]
        d=2
        while x>1:
            if x%d==0:
              if d in ClonMN:
                  num=ClonMN.index(d)
                  ClonMN.pop(num)
              x=x//d
            else:
              d+=1
        if  len(ClonMN)==0: break
        KolPodPos+=1
print(KolPodPos)        
    


