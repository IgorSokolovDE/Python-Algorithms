k=0
for x10 in range(int('10000',8),int('77777',8)):
    x8=oct(x10)[2:]
    if x8.count('6')==1:
        x8='0'+x8+'0'
        numPos6=x8.index('6')
        if (int(x8[numPos6-1])%2==0)and (int(x8[numPos6+1])%2==0):
            k+=1
print(k)            
        
                 
