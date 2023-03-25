f=open('26-79.txt')
N,K=map(int, f.readline().split())
Les=[]
for i in range(N):
    R,P=map(int, f.readline().split())
    Les.append([R,P])
MaxR=0
MinNepr=0
Les.sort()
for i in range(N-1):
    if Les[i][0]==Les[i+1][0]:
        kNepr=(Les[i+1][1]-Les[i][1]-1)
        if kNepr==K:
            NR=Les[i][0]
            NStNepr=Les[i][1]+1
            if NR>MaxR:
                MaxR=NR
                MinNepr=NStNepr
print(MaxR,  MinNepr)              
            
