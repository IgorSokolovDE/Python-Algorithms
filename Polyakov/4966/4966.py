k=0
for R in range(0,27):
    for Y in range(R+1,28):
        for G in range(Y+1,29):
            for B in range(G+1,30):
                DV=['0']*30
                DV[R]='1'
                DV[Y]='1'
                DV[G]='1'
                DV[B]='1'
                if int(''.join(DV),2)<=500_000_000:
                    k+=1
print(k)                    
                
