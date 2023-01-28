def F(k,tekHod,HodPobedy):
    if k<=10:
        return tekHod%2==HodPobedy%2
    if tekHod==HodPobedy:
        return False
    hody=[F(k//3,tekHod+1,HodPobedy),F(k-10,tekHod+1,HodPobedy)]
    if (tekHod+1)%2==HodPobedy%2:
        return any(hody)
    else:
        return all(hody)
print('s ход победы')
for s in range(11,600):
    for hp in range(1,5):
        if F(s,0,hp):
            print(s,hp)
            break
