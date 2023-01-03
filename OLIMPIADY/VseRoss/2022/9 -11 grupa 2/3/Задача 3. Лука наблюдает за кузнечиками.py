n=int(input())
k=int(input())
jamp=n//(k+1)
while True:    
    if n%(k+1)==0:
        print(jamp)
        break
    else:
        if ((k+1)*jamp)%n > jamp:
            jamp+=1
        else:
            print(jamp)
            break
