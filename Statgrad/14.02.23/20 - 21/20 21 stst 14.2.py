def Igra(k1,k2,tekHod,HodPobedy):
    if (k1+k2)>=46:
        return tekHod%2==HodPobedy%2
    if tekHod==HodPobedy:
        return False
    else:
        Hody=[]
        if k1<k2:
            for i in range(1,k1+1):
                Hody.append(Igra(k1+i,k2,tekHod+1,HodPobedy))
        else:
            for i in range(1,k2+1):
                Hody.append(Igra(k1,k2+i,tekHod+1,HodPobedy))
        if (tekHod+1)%2==HodPobedy%2:
            return any(Hody)
        else:
            return all(Hody)
print('s ход победы')
for s in  range(1,41):
    for hp in range(1,5):
        if Igra(5,s,0,hp):
            print(s,hp)
            break
