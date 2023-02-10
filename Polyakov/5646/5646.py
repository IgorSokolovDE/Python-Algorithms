s=open('24-230.txt').readline()
cifr='0123456789'
M=0
words=s.split("KK")
for w in words:
    if len(w)==11:
        tolkoCifri=True
        for sym in w:
            if not(sym in cifr):
                tolkoCifri=False
                break
        if tolkoCifri:
            if (w[:2]=='43')and(w[-2:]=='34')and(w[4:6]=='78'):
                M=max(M,int(w))
s=str(M)
pr=1
for s1 in s:
    if int(s1)%2!=0:
        pr*=int(s1)
print(pr)        
