s=open('24-212.txt').readline()
kPar=0
MaxKpar=0
i=0
while i<(len(s)-1):
    if (s[i] in 'BCD')and(s[i+1] in 'AO'):
        kPar+=1
        MaxKpar=max(MaxKpar,kPar)
        i+=2
    else:
        kPar=0
        i+=1
print(MaxKpar)        
