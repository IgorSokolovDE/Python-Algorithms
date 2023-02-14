s=open('24-213.txt').readline()
MaxkolNPOPNO=0
for start in range(len(s)-2):
    i=start
    kolNPOPNO=0
    while i<len(s)-2:
        if ((s[i]=='N')and(s[i+1]=='P')and (s[i+2]=='O')) or\
           ((s[i]=='P')and(s[i+1]=='N')and (s[i+2]=='O')):
            kolNPOPNO+=1
            i+=3
        else:
            break
    MaxkolNPOPNO=max(MaxkolNPOPNO,kolNPOPNO)
print(MaxkolNPOPNO)    
