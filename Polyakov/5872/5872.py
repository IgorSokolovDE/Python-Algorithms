def F(k,predH,predpredH,tekHod,hodPobedy):
    if k>=121:
        return tekHod%2==hodPobedy%2
    if tekHod==hodPobedy:
        return False
    if predpredH==0:
        hody=[F(k+2,1,predH,tekHod+1,hodPobedy),F(k+5,2,predH,tekHod+1,hodPobedy),F(k+12,3,predH,tekHod+1,hodPobedy),F(k*2,4,predH,tekHod+1,hodPobedy)]
    if predpredH==1:
        hody=[F(k+5,2,predH,tekHod+1,hodPobedy),F(k+12,3,predH,tekHod+1,hodPobedy),F(k*2,4,predH,tekHod+1,hodPobedy)]
    if predpredH==2:
        hody=[F(k+2,1,predH,tekHod+1,hodPobedy),F(k+12,3,predH,tekHod+1,hodPobedy),F(k*2,4,predH,tekHod+1,hodPobedy)]
    if predpredH==3:
        hody=[F(k+2,1,predH,tekHod+1,hodPobedy),F(k+5,2,predH,tekHod+1,hodPobedy), F(k*2,4,predH,tekHod+1,hodPobedy)]
    if predpredH==4:
        hody=[F(k+2,1,predH,tekHod+1,hodPobedy),F(k+5,2,predH,tekHod+1,hodPobedy), F(k+12,3,predH,tekHod+1,hodPobedy)]
    if (tekHod+1)%2==hodPobedy%2: return any(hody)
    else: return all(hody)
print('s ход победы')
for s in range(1,121):
    for hp in range(1,7):
        if F(s,0,0,0,hp):
            print(s,hp)
            break
        
