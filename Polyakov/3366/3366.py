s=open('24-4.txt').readline()
Dlina=0
MaxDlina=0
for i in range(len(s)-1):
    if ord(s[i+1])>ord(s[i]):
        if Dlina==0:
            Dlina=2
        else:
            Dlina+=1
            MaxDlina=max(MaxDlina,Dlina)
    else:
        Dlina=0
print( MaxDlina)       
