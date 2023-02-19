def igra(k,tekHod,hodPobedy):
    if k>=165:
        return tekHod%2==hodPobedy%2
    if tekHod==hodPobedy:
        return False
    Hody=[igra(k+1,tekHod+1,hodPobedy),igra(k*2,tekHod+1,hodPobedy)]
    if (tekHod+1)%2==hodPobedy%2:
        return any(Hody)
    else:
        return all(Hody)
print('s hop pobedy')
for s in range(1,164):
    for hp in range(1,5):
        if (igra(s,0,hp)):
            print(s,hp)
            break
