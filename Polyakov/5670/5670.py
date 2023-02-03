kA=0
for A in range(1,1000):
    OK=True
    for x in range(1,1000):
        if ((x%12==0)and(70<=x<=80)and(x%A!=0)):
            OK=False
            break
    if OK:
        kA+=1
print(kA)      
