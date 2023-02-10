s=open('24-235.txt').readline()
seredki=''
for i in range(len(s)-2):
    if s[i]=='X' and s[i+2]=='P':
       seredki+=s[i+1]
b='XYZWOP'
maxKol=0
bb=''
for bukvi in b:
    if seredki.count(bukvi)>maxKol:
        maxKol=seredki.count(bukvi)
        
print(maxKol)        
    
