from itertools import product
p=product('ВЕРОНИКА',repeat=6)
c=0
for x in p:
    s=''.join(x)
    SGL=x.count('В')+x.count('Р')+x.count('Н')+x.count('К')
    GL=x.count('Е')+x.count('О')+x.count('И')+x.count('А')
    if GL>SGL: c+=1
print(c)
