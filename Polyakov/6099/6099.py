s=open('24-249.txt').readline()
MinDlina=1000000000000000000000000
for start in range(len(s)):
    cifr16=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    bilo=[0]*16
    for i in range(start,len(s)):
        if (sum(bilo)==16)or((i-start)>MinDlina):
            break
        if (s[i] in cifr16):
            numer=cifr16.index(s[i])
            if bilo[numer]==0:
                bilo[numer]=1
    if  sum(bilo)==16:
        if (i-start)<MinDlina:
            MinDlina=i
print(Mindlina)            
