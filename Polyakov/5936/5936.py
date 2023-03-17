s=open('24-239.txt').readline()
MaxDlinaPodS=0
for start in range(len(s)-2):
    i=start
    DlinaPodS=0
    while i<(len(s)-2):
        if ((s[i]=='X')and(s[i+1]=='Y'))or\
           ((s[i]=='Y')and(s[i+1]=='Z'))or\
           ((s[i]=='Y')and(s[i+1]=='Z')and(s[i+2]=='Z')):
            if ((s[i]=='X')and(s[i+1]=='Y')):
                i+=2
                DlinaPodS+=2
                MaxDlinaPodS=max(MaxDlinaPodS,  DlinaPodS)
            else:
                if (s[i]=='Y')and(s[i+1]=='Z')and(s[i+2]=='Z'):
                    i+=3
                    DlinaPodS+=2
                    MaxDlinaPodS=max(MaxDlinaPodS,  DlinaPodS)
                else:
                    i+=2
                    DlinaPodS+=2
                    MaxDlinaPodS=max(MaxDlinaPodS,  DlinaPodS)
            
        else:
            break
    
print(MaxDlinaPodS)     
