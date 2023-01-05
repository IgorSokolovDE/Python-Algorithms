s=open('24-228.txt').readline()
pods=''
a=[]
for i in range(len(s)-1):
    pods+=s[i]
    if s[i]=='X' and s[i+1]=='X':
      a.append(pods)
      pods=''
a.pop(0)
a.pop(-1)
MaxCh=0
for i in range(len(a)):
    if len(a[i])>=11:
        pods=a[i]
        for j in range(len(pods)-11):
            b=pods[j:j+11]
            if (b[0]=='3')and (b[5:7]=='78')and(b[-2:]=='45'):
                
                VseCifri=True
                for s1 in b:
                    if not(s1 in '0123456789'):
                        VseCifri=False
                        break  
                if VseCifri:
                    MaxCh=max(MaxCh,int(''.join(b)))                  
pr=1
sumNech=0
while MaxCh>0:
    if (MaxCh%10)%2==0:
        pr=pr*(MaxCh%10)
    else:  sumNech+=(MaxCh%10)  
    MaxCh//=10    
print(pr+sumNech)
                
