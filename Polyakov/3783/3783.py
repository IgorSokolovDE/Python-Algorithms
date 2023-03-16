from string import ascii_uppercase
with open('24-s1.txt') as f:
    data = f.readlines()
al = ascii_uppercase
a = []
b = []
m = 9999999999999999
superSt=''
for st in data:
    superSt+=st
    k = 0
    for i in range(len(st)-1):
        if  (ord(st[i+1])-ord(st[i]))==1:
            k+=1
    if (k>0) and (k<m):
        m=k
        sst=st
MC=0
Bukva=''
for i in range(65,92):
    if sst.count(chr(i))>=MC:
        MC=sst.count(chr(i))
        Bukva=chr(i)
print(Bukva,superSt.count(Bukva))        
        
