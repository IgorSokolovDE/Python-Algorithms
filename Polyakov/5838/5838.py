from itertools import product
p=product('АИЙ',repeat=5)
kol=0
for x in p:
    s=''.join(x)
    if (s.count('А')==2)and(s.count('И')==2)and(s.count('Й')==1):
        kol+=1
print(5*4*3*2*kol)        
        
