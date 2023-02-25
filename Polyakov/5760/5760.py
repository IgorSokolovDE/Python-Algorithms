from itertools import product
Glasnii='АИУОЯ'
k=0
for i in range(1,6):
  p=product('АНТИУОПЯ',repeat=i)
  
  
  for x in p:
     s=''.join(x)
     
     kolGlLeft=0
     for GlBukvaL in Glasnii:
        kolGlLeft+=s.count(GlBukvaL)   
     j=6-i
     p2=product('АНТИУОПЯ',repeat=j)
     
     for y in p2:
         s2=''.join(y)
         kolGlRight=0 
         for GlBukvaR in Glasnii:
             kolGlRight+=s2.count(GlBukvaR)
         if abs(kolGlLeft-kolGlRight)==1:
             k+=1
krai=0             
p=product('АНТИУОПЯ',repeat=6)
for x in p:
    s=''.join(x)
    kolGl=0 
    for GlBukvaR in Glasnii:
          kolGl+=s.count(GlBukvaR)
    if kolGl == 1:
      krai+=1
    
print(k+krai*2)             
        
     
