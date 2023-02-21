f=open('24.txt')
MaxDlinaCep=0
BukvaCep=''
k=0
while True:
    s=f.readline()
    if not(s):
        break
    
    kpod=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            if kpod==0:
                kpod=2
            else:
                kpod+=1
        else:
            if kpod>MaxDlinaCep:
                MaxDlinaCep=kpod
                BukvaCep=s[i]
                k=s.count(BukvaCep)
            else:
                if kpod==MaxDlinaCep:
                    if s.count(BukvaCep)< s.count(s[i]):
                        BukvaCep=s[i]
                        k=s.count(BukvaCep)
            kpod=0
print(k)            
