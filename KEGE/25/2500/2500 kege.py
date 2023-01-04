s=open('24 (3).txt').readline()
kPod=0
for i in range(len(s)-3):
    if (s[i]=="G")and(s[i+2]=='M') and(s[i+3]=='E'):
        kPod+=1
print(kPod)        
