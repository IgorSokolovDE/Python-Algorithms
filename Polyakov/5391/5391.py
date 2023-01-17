s=open('24-215.txt').readline()
i=0
k3=0
MaxK3=0
while i<=len(s)-2:
    if (s[i] in '123')and(s[i+1] in 'ABC')and(s[i+2] in '123'):
        k3+=1
        MaxK3=max(MaxK3,k3)
        i+=3
    else:
        k3=0
        i+=1
print(MaxK3)        
