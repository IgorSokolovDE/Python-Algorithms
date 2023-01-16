N=174
S=0
while N!=3:
    if N%4==0:
        S+=N//4
        N=(N//4)+2
    else:
        N=N+2
        S+=1
        
print(S)    
        
