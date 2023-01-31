def F(k,tekHod,hodProing):
    if k>=82:
        return tekHod%2==hodProing%2
    if tekHod==hodProing:
        return False
    if (tekHod+1)%2!=hodProing%2:
        return F(k+10,tekHod+1,hodProing)or F(k*2,tekHod+1,hodProing)
    else:
        return F(k+10,tekHod+1,hodProing)and F(k*2,tekHod+1,hodProing)
print('s ход победы')
for s in range(1,82):
    for hp in range(1,5):
        if F(s,0,hp):
            print(s,hp-1)
            break
    
