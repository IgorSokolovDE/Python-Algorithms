f=open('27-115b.txt')
n=int(f.readline())
A=[int(x) for x in f]
A.sort()
Dubli=[]
Unik=[A[0]]
FlagDubli=False
for i in range(1,n):
    if A[i]==Unik[-1]:
       Dubli.append(A[i])
       FlagDubli=True
    else:
       if FlagDubli:
          Dubli.append(Unik[-1])
          Unik.pop(-1)
          FlagDubli=False
       Unik.append(A[i])
Dubli.sort()
Unik.sort()
i=0
while i<len(Dubli)-2:
    if Dubli[i]==Dubli[i+1]==Dubli[i+2]:
        Dubli.pop(i+2)
    else:
        i+=1
print(len(Unik)//2+len(Dubli)//2)
