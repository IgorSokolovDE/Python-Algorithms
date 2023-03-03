def F(k1,tekHod,Hodp,predHod):
    if k1>=76:
        return tekHod%2==Hodp%2
    if tekHod==Hodp:
        return False
    else:
        if predHod==0:
            hody=[F(k1+1,tekHod+1,Hodp,1),\
                  F(k1+3,tekHod+1,Hodp,2),\
                  F(k1*3,tekHod+1,Hodp,3)]
        else:
            if predHod==1:
                hody=[F(k1+3,tekHod+1,Hodp,2),\
                  F(k1*3,tekHod+1,Hodp,3)]
            else:
                if predHod==2:
                    hody=[F(k1+1,tekHod+1,Hodp,1),\
                          F(k1*3,tekHod+1,Hodp,3)]
                else:
                    if predHod==3:
                        hody=[F(k1+1,tekHod+1,Hodp,1),\
                              F(k1+3,tekHod+1,Hodp,2)]
        if  (tekHod+1)%2==Hodp%2:
            return any(hody)
        else:
            return all(hody)
for s in range(1,76):
    for  hp in range(1,5):
        if F(s,0,hp,0):
            print(s,hp)
            break
