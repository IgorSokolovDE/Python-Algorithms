from itertools import product
import datetime
now = datetime.datetime.now()
print (str(now))
p=product('АМФИБРХЙ',repeat=10)
c=0
for x in p:
    slovo=''.join(x)
    if slovo.count('А')==2:
        if slovo.count('И')==2:
           if slovo.count('М')==1:
               if slovo.count('Ф')==1:
                   if slovo.count('Б')==1:
                       if slovo.count('Р')==1:
                           if slovo.count('Х')==1:                                                       
                                if slovo.count('Й')==1:
                                    if ('АА' in slovo)or('ИИ' in slovo)or('ИА' in slovo)or('АИ' in slovo):
                                        c+=1
print(c)    
now = datetime.datetime.now()
print (str(now))
