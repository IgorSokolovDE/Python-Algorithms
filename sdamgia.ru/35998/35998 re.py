f=open('inf_26_04_21_24.txt')
MaxR=0
while True:
    s=f.readline()
    if not(s): break
    if s.count('A')<25:
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    MaxR=max(MaxR,(j-i))
print(MaxR)                    
                    
