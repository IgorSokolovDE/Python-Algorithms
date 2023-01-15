def F(k,tekHod,HodPobed,NPerdHod):
    if k>=62:
        return tekHod%2==HodPobed%2
    if tekHod==HodPobed:
        return False
    else:
        if NPerdHod==0:
            hody=[F(k+1,tekHod+1,HodPobed,1),F(k+2,tekHod+1,HodPobed,2),F(k*3,tekHod+1,HodPobed,3)]
        if NPerdHod==1:
            hody=[F(k+2,tekHod+1,HodPobed,2),F(k*3,tekHod+1,HodPobed,3)]
        if NPerdHod==2:
            hody=[F(k+1,tekHod+1,HodPobed,1),F(k*3,tekHod+1,HodPobed,3)]
        if NPerdHod==3:
            hody=[F(k+1,tekHod+1,HodPobed,1),F(k+2,tekHod+1,HodPobed,2)]
        if (tekHod+1)%2==HodPobed%2:
            return any(hody)
        else:
            return all(hody)
print('s hp')
for s in range(1,62):
    for hp in range(1,5):
        if F(s,0,hp,0):
            print(s,hp)
            break
