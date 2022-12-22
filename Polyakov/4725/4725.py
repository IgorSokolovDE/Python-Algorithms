def F(k1,k2,k3,TekHodIgry,HodPobedy):
    if (k1+k2+k3)>=71:
        return TekHodIgry%2==HodPobedy%2
    if TekHodIgry==HodPobedy:
        return False
    else:
        if (TekHodIgry+1)%2==HodPobedy%2:
            return F(k1+3,k2,k3,TekHodIgry+1,HodPobedy)or\
                   F(k1,k2+3,k3,TekHodIgry+1,HodPobedy)or\
                   F(k1,k2,k3+3,TekHodIgry+1,HodPobedy)or\
                   F(k1*2,k2,k3,TekHodIgry+1,HodPobedy)or\
                   F(k1,k2*2,k3,TekHodIgry+1,HodPobedy)or\
                   F(k1,k2,k3*2,TekHodIgry+1,HodPobedy)
        else:
            return F(k1+3,k2,k3,TekHodIgry+1,HodPobedy)and\
                   F(k1,k2+3,k3,TekHodIgry+1,HodPobedy)and\
                   F(k1,k2,k3+3,TekHodIgry+1,HodPobedy)and\
                   F(k1*2,k2,k3,TekHodIgry+1,HodPobedy)and\
                   F(k1,k2*2,k3,TekHodIgry+1,HodPobedy)and\
                   F(k1,k2,k3*2,TekHodIgry+1,HodPobedy)
print('S ход победы')
for S in range(1,59):
    for hp in range(1,5):
        if F(7,5,S,0,hp):
            print(S,hp)
            break
