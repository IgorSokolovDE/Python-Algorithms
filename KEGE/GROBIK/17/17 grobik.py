f=open('17 (2).txt')
Vse=[]
while True:
    s=f.readline()
    if not(s):
        break
    ss=1
    for s1 in s:
        if not(s1 in '0123456789'):
            cifra=(ord(s1)-55)
        else:
            cifra=int(s1)
        ss=max(cifra,ss)
    ss+=1
    stepen=0
    s=s[::-1]
    Ch10=0
    for s1 in s:
        if not(s1 in '0123456789'):
            cifra=(ord(s1)-55)
        else:
            cifra=int(s1)
        Ch10+=cifra*ss**stepen
        stepen+=1
    Vse.append([ss, Ch10])
Vse.sort()
kPar=0
MaxSumPary=0
for i in range(len(Vse)-1):
    for j in range(i+1,len(Vse)):
        if (Vse[j][0]-Vse[i][0])<=2:
            kPar+=1
            MaxSumPary=max(MaxSumPary,(Vse[j][1]+Vse[i][1]))
        else:
            break
print(kPar,MaxSumPary)     
        
            
    

        
