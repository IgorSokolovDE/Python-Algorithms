f=open('24-247.txt')
MaxDlinaCepi=0
bukvaCepi=''
kolBvStr=0
while True:
    s=f.readline()
    if not(s):
        break
    kpov=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            if kpov==0:
                kpov=2
            else:
                kpov+=1
        else:
            if MaxDlinaCepi<kpov:
                MaxDlinaCepi=kpov
                bukvaCepi=s[i]
                kolBvStr=s.count(bukvaCepi)
            else:
                if MaxDlinaCepi==kpov:
                   if  s.count(s[i])>kolBvStr:
                       bukvaCepi=s[i]
                       kolBvStr=s.count(bukvaCepi)
print(kolBvStr)                       
