x=117
d=2
while x>1:
    if x%d==0:
        #print(d,end=' ')
        x=x//d
    else:
        d+=1
prost=[]        
for x in range(2,100):        
  pr=True
  for d in range(2,x):
      if x%d==0:
          pr=False
          break
  if pr:
      prost.append(x)
#print(prost)
for i in range(len(prost)):
    for j in range(len(prost)):
        for k in range(len(prost)):
            if i!=j!=k:
                ch=prost[i]**12*prost[j]**2*prost[k]**2
                if ch<=10**9:
                    s=str(ch)
                    if (s[:2]==s[-2:])and(s[0]==s[1]):
                        print(ch, end=" ")
                        for d in range(2,ch):
                            if ch%d==0:
                                print(ch//d)
                                break
                                
    
