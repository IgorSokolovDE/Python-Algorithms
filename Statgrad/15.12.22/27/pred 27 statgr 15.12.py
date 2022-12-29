n=6561
d=2
while n>1:
    if n%d==0:
        print(d)
        n=n//d
    else:
        d+=1
    
    
