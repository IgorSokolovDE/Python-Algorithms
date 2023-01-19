def F(k1,k2,TekHod,HodPobedi):
    if (k1+k2)>=67: return TekHod%2==HodPobedi%2
    if TekHod==HodPobedi: return False
    if (TekHod+1)%2==HodPobedi%2:
        return F(k1+1,k2,TekHod+1,HodPobedi)or\
               F(k1,k2+1,TekHod+1,HodPobedi)or\
               F(k1+k2,k2,TekHod+1,HodPobedi)or\
               F(k1,k2+k1,TekHod+1,HodPobedi)
    else:
        return F(k1+1,k2,TekHod+1,HodPobedi)and\
               F(k1,k2+1,TekHod+1,HodPobedi)and\
               F(k1+k2,k2,TekHod+1,HodPobedi)and\
               F(k1,k2+k1,TekHod+1,HodPobedi)
print('s ход победы')
for s in range(1,58):
    for hp in range(1,5):
        if F(9,s,0,hp):
            print(s,hp)
            break
