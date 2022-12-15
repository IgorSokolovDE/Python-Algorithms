f=open('27-126b.txt')
N=int(f.readline())
TP=[]
for i in range(N):
    nomer,ratig=map(int, f.readline().split())
    TP.append([nomer,ratig])
MaxR=0    
for i in range(N-1):
    for j in range(i+1,N):
        if TP[j][1]>TP[i][1]:
            R=j-i
            MaxR=max(MaxR,R)
            break
print(MaxR)        
