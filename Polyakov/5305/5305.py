def f(k,tekHod,HodP):
    if k>=166:
        return tekHod%2==HodP%2
    if tekHod==HodP:
        return False
    else:
        hody=[f(k+2,tekHod+1,HodP),f(k+10,tekHod+1,HodP)]
        Mn=2
        while(Mn*k-k)<=80:
            hody.append(f(k*Mn,tekHod+1,HodP))
            Mn+=1
        if  (tekHod+1)%2==HodP%2:
            return any(hody)
        else:
            return all(hody)
print('s ход победы')
for s in range(1,166):
    for hp in range(1,5):
        if f(s,0,hp):
            print(s,hp)
            break
