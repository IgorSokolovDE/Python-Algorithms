def F(k,superH,tekHod,HodPobedy):
    if k>=20:
        return tekHod%2==HodPobedy%2
    if tekHod==HodPobedy:
        return False
    hody=[F(k*2,superH,tekHod+1,HodPobedy),F(k+2,superH,tekHod+1,HodPobedy)]
    if superH==0:
         hody.append(F(k,1,tekHod+1,HodPobedy))
    if (tekHod+1)%2==HodPobedy%2:
        return any(hody)
    else:
        return all(hody)
print('s ход победы')
for s in range(1,20):
    for hp in range(1,10):
        if F(s,0,0,hp):
            print(s,hp)
            break
