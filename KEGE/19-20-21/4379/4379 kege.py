def F(k,TekHod,HodP):
    if k>=51:
        return TekHod%2==HodP%2
    if TekHod==HodP:
        return False
    else:
        Hody=[F(k+1,TekHod+1,HodP),F(k+2,TekHod+1,HodP)]
        if (60-k)>=k:
            Hody.append(F(k*2,TekHod+1,HodP))
        if  (TekHod+1)%2==HodP%2:
            return any(Hody)
        else:
            return all(Hody)
print('s ход победы')
for s in range(1,51):
    for hp in range (1,7):
        if F(s,0,hp):
            print(s,hp)
            break
        
