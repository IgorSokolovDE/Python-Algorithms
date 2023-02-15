s=open('24-215.txt').readline()
MaxkolPod3=0
for start in range(len(s)):
    kolPod3=0
    i=start
    while i < len(s)-2:
        if (s[i] in '123')and (s[i+1] in '123')and(s[i+2] in 'ABC'):
            kolPod3+=1
            i+=3
        else:
            break
    MaxkolPod3=max(MaxkolPod3, kolPod3)
print(MaxkolPod3)    
