def F(k1,k2,k3,tekHod,HodP):
    if (k1+k2+k3)>=71:
        return tekHod%2==HodP%2
    if tekHod==HodP:
        return False
    else:
        hody=[F(k1+3,k2,k3,tekHod+1,HodP),\
              F(k1,k2+3,k3,tekHod+1,HodP),\
              F(k1,k2,k3+3,tekHod+1,HodP),\
              F(k1*2,k2,k3,tekHod+1,HodP),\
              F(k1,k2*2,k3,tekHod+1,HodP),\
              F(k1,k2,k3*2,tekHod+1,HodP)]
        if (tekHod+1)%2==HodP%2:
            return any(hody)
        else:
            return all(hody)
for s in range(1,59):
    for hp in range(1,5):
        if F(7,5,s,0,hp):
            print(s,hp)
            break
