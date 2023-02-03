s=open('24-225.txt').readline()
Max=0
s=s.replace('CC',' ')
words=s.split()
for w in words:
    if len(w)==12:
        podhodit=True
        for s1 in w:
            if not(s1 in '0123456789'):
                podhodit=False
                break
        if podhodit:
            if (w[:3]=='234')and(w[-1]=='8') and(w[6:8]=='57'):
                Max=max(int(w),Max)
SMax=str(Max)
Pr=1
for s1 in SMax:
    cifr=int(s1)
    if cifr%2!=0:
        Pr*=cifr
print(Pr)        
