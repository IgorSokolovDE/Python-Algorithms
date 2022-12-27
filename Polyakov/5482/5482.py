def F(k1,k2,tekHod,HodPobedy):
    if (k1+k2)>=231: return tekHod%2==HodPobedy%2
    if tekHod==HodPobedy: return False
    hody=[F(k1+2,k2,tekHod+1,HodPobedy),F(k1,k2+2,tekHod+1,HodPobedy),\
          F(k1*2,k2,tekHod+1,HodPobedy),F(k1,k2*2,tekHod+1,HodPobedy)]
    if (tekHod+1)%2==HodPobedy%2: return any(hody)
    else: return all(hody)
print('s hod pobedy')
for s in range(1,214):
    for hp in range(1,5):
        if F(17,s,0,hp):
            print(s,hp)
            break
