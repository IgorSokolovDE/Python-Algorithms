M = 4_043_520
mn=[]
x=M
d=2
while x>1:
   if x%d==0:
       mn.append(d)
       x=x//d
   else:
       d+=1
f=open('27-104b.txt')
N=int(f.readline())
KolPodPos=0
A=[int(x) for x in f]
for i in range(N):
    MN=mn[:]
    j=i
    while j<N:
        x=A[j]
        if x==1:
            KolPodPos+=1
            j+=1
        else:    
            d=2
            berem=True
            while x>1:
               if x%d==0:
                  if (d in MN):
                      num=MN.index(d)
                      MN.pop(num)
                      x=x//d
                  else:
                      berem=False
                      break
                      
               else:
                  d+=1
            if berem:
                  KolPodPos+=1
                  j+=1
            else:
                  break
print(KolPodPos)       
