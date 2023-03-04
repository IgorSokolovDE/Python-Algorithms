def F(k,tekHod,HodP):
    if k==42:
        return tekHod%2==HodP%2
    if tekHod==HodP:
        return False
    else:
        if k<42:
           hody=[F(k+1,tekHod+1,HodP),\
                 F(k+3,tekHod+1,HodP),\
                 F(k+7,tekHod+1,HodP)]
        else:
            hody=[F(k-1,tekHod+1,HodP),\
                 F(k-3,tekHod+1,HodP),\
                 F(k-7,tekHod+1,HodP)]
        if (tekHod+1)%2==HodP%2 :
            return any(hody)
        else:
            return any(hody)
for s in range(1,60):
    for hp in range(1,5):
        if F(s,0,hp):
            print(s,hp)
            break
