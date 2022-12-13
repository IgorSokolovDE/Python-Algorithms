f=open('26-94.txt')
s=f.readline()
a=s.split()
N=int(a[0])
K=int(a[1])
Biletiki=[]
MaxR1e=0
MinR1e=100000000000000
MaxR2e=0
MinR2e=100000000000000
for i in range(N):
    Ne,Nr,Nm=map(int, f.readline().split())
    Biletiki.append([Ne,Nr,Nm])
    if Ne==1:
        MaxR1e=max(MaxR1e,Nr)
    else:
        MaxR2e=max(MaxR2e,Nr)
samolet1=[]
for i in range(MaxR1e+1):
    b=[]
    for j in range(7):
        b.append('0')
    samolet1.append(b)   
samolet2=[]
for i in range(MaxR2e+1):
    b=[]
    for j in range(7):
        b.append('0')
    samolet2.append(b)   
for i in range(N):
    if Biletiki[i][0]==1:
        samolet1[Biletiki[i][1]][Biletiki[i][2]]='1'
    else:
        samolet2[Biletiki[i][1]][Biletiki[i][2]]='1'
MaxR=0
kPodR=0
for i in range(1,MaxR1e+1):
    rad="".join(samolet1[i])
    if rad.count('1')>0:
        rad=rad[2:-1]
        if rad.count('0')==4:
           kPodR+=1
           MaxR=max(MaxR,i)
for i in range(1,MaxR2e+1):
    rad="".join(samolet2[i])
    if rad.count('1')>0:
        rad=rad[2:-1]
        if rad.count('0')==4:
           kPodR+=1
           MaxR=max(MaxR,i)
print( kPodR,MaxR)       
    
        
