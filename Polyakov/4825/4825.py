def F(k,TekHodIgry,HodPobedy,predH):
    if k>=43:
        return TekHodIgry%2==HodPobedy%2
    if TekHodIgry==HodPobedy:
        return False
    if predH==0: hody=[F(k+1,TekHodIgry+1,HodPobedy,1),
                       F(k+2,TekHodIgry+1,HodPobedy,2),
                       F(k*2,TekHodIgry+1,HodPobedy,3)]
    if predH==1: hody=[F(k+2,TekHodIgry+1,HodPobedy,2),
                       F(k*2,TekHodIgry+1,HodPobedy,3)]
    if predH==2: hody=[F(k+1,TekHodIgry+1,HodPobedy,1),
                       F(k*2,TekHodIgry+1,HodPobedy,3)]
    if predH==3: hody=[F(k+1,TekHodIgry+1,HodPobedy,1),
                       F(k+2,TekHodIgry+1,HodPobedy,2)]
    if (TekHodIgry+1)%2==HodPobedy%2:
        return any(hody)
    else:
        return all(hody)
print('s ход победы')
for s in range(1,43):
    for hodPobedy in range(1,5):
        if F(s,0,hodPobedy,0):
            print(s,hodPobedy)
            break
