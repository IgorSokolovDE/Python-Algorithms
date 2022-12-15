s=open('24-209.txt').readline()
k=''
MaxK=''
for i in range(len(s)-1):
    if (s[i]+s[i+1]) in ['AB','CB','BC','BA']:
        if len(k)==0: k=(s[i]+s[i+1])
        else:
            k+=s[i+1]
            if len(MaxK)<=len(k):
                MaxK=k
    else:
        k=''
print(len(MaxK)-1)        
