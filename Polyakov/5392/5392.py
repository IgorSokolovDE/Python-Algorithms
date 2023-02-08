s=open('24-215.txt').readline()
Maxk3=0
for start in range(len(s)):
    k3=0
    i=start
    while i<len(s)-2:
        if (s[i] in 'ABC')and(s[i+1] in '123')and (s[i+2] in 'ABC'):
            k3+=1
            i+=3
        else:
            break
    Maxk3=max(Maxk3,k3)
print(Maxk3)    
