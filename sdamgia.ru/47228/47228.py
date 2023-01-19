s=open('24 (6).txt').readline()
kpip=0
Maxkpip=0
i=0
while i<len(s)-1:
    if (s[i] in 'CDF')and(s[i+1] in 'AO'):
        kpip+=1
        Maxkpip=max(Maxkpip,kpip)
        i+=2
    else:
        kpip=0
        i+=1
print(Maxkpip)        
