def DinS(n):
    S=''
    while n>0:
        S=str(n%7)+S
        n//=7
    return S    

k=1
while k*333<=10**9:
    ch10=k*333
    chS7=DinS(ch10)
    if len(chS7)>=8:
        if (chS7[-4:]=='5664')and(chS7[1:4]=='213'):
            print(ch10,k)
    k+=1        

        
