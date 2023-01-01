def F(k1,k2,TekHodIgry,HodPobedy):
    if (k1+k2)>=81:
        return TekHodIgry%2==HodPobedy%2
    if TekHodIgry==HodPobedy:
        return False
    if k1<k2:
        hody=[F(k1+1,k2,TekHodIgry+1,HodPobedy),\
              F(k1+2,k2,TekHodIgry+1,HodPobedy),\
              F(k1*2,k2,TekHodIgry+1,HodPobedy)]
    else:
        hody=[F(k1,k2+1,TekHodIgry+1,HodPobedy),\
              F(k1,k2+2,TekHodIgry+1,HodPobedy),\
              F(k1,k2*2,TekHodIgry+1,HodPobedy)]
    if  (TekHodIgry+1)%2==HodPobedy%2:
        return any(hody)
    else:
        return all(hody)
print('s ход победы')
for s in range(1,69):
    for hp in range (1,5):
        if F(12,s,0,hp):
            print(s,hp)
            break
