k=1
while k*141<=10**8:
    S=str(k*141)
    if len(S)>=5:
        if (S[-1]=="7")and(S[:4]=="1234"):
            print(S,k)
    k+=1        
            
