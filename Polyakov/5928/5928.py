def Igra(KolKamnei,TekHodIgry,HodPobedy):
    if KolKamnei>=82:
        return TekHodIgry%2==HodPobedy%2
    if TekHodIgry==HodPobedy:
        return False
    if (TekHodIgry+1)%2==HodPobedy%2:
        return Igra(KolKamnei+10,TekHodIgry+1,HodPobedy)or Igra(KolKamnei*2,TekHodIgry+1,HodPobedy)
    else:
        return Igra(KolKamnei+10,TekHodIgry+1,HodPobedy)and Igra(KolKamnei*2,TekHodIgry+1,HodPobedy)
print('s ход победы')
for s in range(1,82):
    for hp in range(1,4):
        if Igra(s,0,hp):
            print(s,hp)
            break
