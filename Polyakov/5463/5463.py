s=open('24-223.txt').readline()
MaxDlina=0
for start in range(len(s)):
    Dlina=0
    i=start
    while i<len(s)-2:
        if (s[i:i+2]!='AB')and(s[i:i+3]!='CAC'):
            break
        else:
            if s[i:i+2]=='AB':
                Dlina+=2
                i+=2
            else:
                Dlina+=3
                i+=3
    MaxDlina=max(MaxDlina,Dlina )
print(MaxDlina)                
