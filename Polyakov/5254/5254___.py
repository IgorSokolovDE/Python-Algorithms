f=open('26-84.txt')
N=int(f.readline())
Stud=[int(x) for x in f.readline().split()]
MestVAud=[int(x) for x in f.readline().split()]
Stud.sort()
MestVAud.sort()
kGrupVAud=[0]*N
i=0
for j in range(N-1):
    while i<(N):
      if Stud[i]<=MestVAud[j]:
        kGrupVAud[j]+=1
        i+=1
      else:
        break
    kGrupVAud[j+1]=kGrupVAud[j]
kVar=kGrupVAud[0]
for i in range(1,N):
    kVar*=(kGrupVAud[i]-(i))   
print(kVar%100000007,kGrupVAud[0])    

