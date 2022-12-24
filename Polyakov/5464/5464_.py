s=open('24-224.txt').readline()
MaxK3=0
for j in range(len(s)-2):
    i=j
    k3=0    
    while True:
        if ((s[i]=='B')and(s[i+1]=='A')and(s[i+2]=='C'))or\
           ((s[i]=='C')and(s[i+1]=='A')and(s[i+2]=='B')):
                k3+=1
                MaxK3=max(MaxK3,k3)
                i+=3
        else:
            break        
        if i>len(s)-2:
            break
    
print(MaxK3*3)        
