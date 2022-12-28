def DinS(n):
    S=''
    while n>0:
        S=str(n%7)+S
        n//=7
    return S    
A=[]
for red in range(1,7):
    for yellow in range(3,10000):
        yellow7=DinS(yellow)
        if yellow7[0]=='3':
            chS7=str(red)+'21'+yellow7+'5664'
            ch10=int(chS7,7)
            if (ch10<=10**9)and(ch10%333==0):
                A.append(ch10)
A.sort()
for i in A:
    print(i,i//333)
        
