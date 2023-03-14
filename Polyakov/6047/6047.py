k=1
W=[]
while k*9573<=10**10:
    Ch=k*9573
    ChS=str(Ch)
    if len(ChS)>=6:
        if (ChS[:3]=='202')and(ChS[-1]=='6')and('47' in ChS[3:-1]):
           W.append(Ch) 
    k+=1
W.sort()
for i in range(len(W)):
    print(W[i],W[i]//9573)
