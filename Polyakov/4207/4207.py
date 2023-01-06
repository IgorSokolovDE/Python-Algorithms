def F(k1,k2,k3,tekHod,HodPobedy):
    if (k1+k2+k3)>=73:
        return tekHod%2==HodPobedy%2
    if tekHod==HodPobedy:
        return False
    else:
        if (tekHod+1)%2==HodPobedy%2:
            return F(k1,k2,k3+3,tekHod+1,HodPobedy)or\
                   F(k1,k2,k3+13,tekHod+1,HodPobedy)or\
                   F(k1,k2,k3+23,tekHod+1,HodPobedy)
        else:
            return F(k1,k2,k3+3,tekHod+1,HodPobedy)and\
                   F(k1,k2,k3+13,tekHod+1,HodPobedy)and\
                   F(k1,k2,k3+23,tekHod+1,HodPobedy)
print('s ход победы')
for s in range(1,24):
    for hp in range(1,5):
        if F(2,s,2*s,0,hp):
            print(s,hp)
            break
            
