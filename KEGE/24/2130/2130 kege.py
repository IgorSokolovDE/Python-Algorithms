def F(s):
    global  MaxkTk
    kTk=0
    i=0
    while i<len(s)-3:
        if (0<=int(s[i:i+2])<=23)and(0<=int(s[i+2:i+4])<=59):
            kTk+=1
            MaxkTk=max(MaxkTk,kTk)
            i+=4
        else:
            kTk=0
            i+=1
f=open('24 (4).txt')
s=f.readline()
for i in range(6,10):
    s=s.replace(str(i)+str(i),' ')
A=s.split()    
kTk=0
MaxkTk=0
predDlina=4*2502
for s in A:
    if len(s)>=predDlina:
        for i in range(len(s)-predDlina):
            podS=s[i:]
            F(podS)
print(MaxkTk)            
        
        

    

