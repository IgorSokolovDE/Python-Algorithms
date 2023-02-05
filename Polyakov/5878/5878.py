s=open('24-237.txt').readline()
maxK3=0
for start in range(len(s)):
    k3=0
    i=start
    while i<len(s)-2:
        if s[i]==s[i+1]==s[i+2]:
            k3+=1
            i+=3
        else:
            break
    maxK3=max(k3, maxK3)
print(maxK3*3)
        
