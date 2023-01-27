def F(k1,k2,tekHod,hodPobedy):
    if (k1+k2)>=259:
        return tekHod%2==hodPobedy%2
    if tekHod==hodPobedy:
        return False
    hody=[F(k1+1,k2,tekHod+1,hodPobedy),F(k1,k2+1,tekHod+1,hodPobedy),\
          F(k1*2,k2,tekHod+1,hodPobedy),F(k1,k2*2,tekHod+1,hodPobedy)]
    if (tekHod+1)%2==hodPobedy%2:
        return any(hody)
    else:
        return all(hody)
print('s ход победы')
for s in range(1,242):
    for hp in range(1,5):
        if F(17,s,0,hp):
            print(s,hp)
            break
        
