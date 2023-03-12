s=open('24 (8).txt').readline()
MaxDLina=0
for start in range(len(s)-1):
    i=start
    kolCherd=0
    if s[start]=='E':
        while i<len(s)-1:
            if s[i:i+2]=='EF':
                kolCherd+=1
                i+=2
            else:
                if s[i]=='E':
                    Dlina=kolCherd*2+1
                    break
                else:
                    Dlina=kolCherd*2
                    break
        MaxDLina=max(MaxDLina,Dlina)
    else:
       if s[start]=='F':
        while i<len(s)-1:
            if s[i:i+2]=='FE':
                kolCherd+=1
                i+=2
            else:
                if s[i]=='F':
                    Dlina=kolCherd*2+1
                    break
                else:
                    Dlina=kolCherd*2
                    break
        MaxDLina=max(MaxDLina,Dlina)
print(MaxDLina)       
