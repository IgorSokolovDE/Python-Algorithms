n=9950
F=n**2-3*(n-1)
n+=1
while n<9999:
    F+=4*n+1
    n+=2
print(F)    
