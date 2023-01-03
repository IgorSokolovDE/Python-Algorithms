N=1234_5678_9101_1121
while True:
    N+=1
    S=str(N)
    S=S[::-1]
    SumCifrChetPos=0
    SumCifrNEChetPos=0
    for i in range(len(S)):
        if i%2==0:
            SumCifrChetPos+=int(S[i])
        else:
            SumCifrNEChetPos+=(((int(S[i])*2)//10)+((int(S[i])*2)%10))
    if (SumCifrChetPos+SumCifrNEChetPos)%10==0:
         print(str(N)[-8:])
         break
        
    
    
