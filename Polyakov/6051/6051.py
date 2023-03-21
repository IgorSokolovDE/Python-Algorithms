s=open('24-241.txt').readline()
maxKIPGS=0
for start in range(len(s)-2):
    KIPGS=0
    i=start
    while True:
        if (s[i] in 'BCDF') and(s[i+1] in 'BCDF') and(s[i+2] in 'AEO') :
            KIPGS+=1
            i+=3
        else:
            break
    maxKIPGS=max(maxKIPGS,KIPGS)
print( maxKIPGS)   
