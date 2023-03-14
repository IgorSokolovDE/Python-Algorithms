kA=0
for A in range(1,1000):
    ok=True
    for x in range(1,1000):
        if ((160<=x<=180)<=((x%35==0)<=(x%A==0)))==False:
            ok=False
            break
    if ok:
        kA+=1
print(kA)        
