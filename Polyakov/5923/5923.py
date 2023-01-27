Pr=1
for n in range(1030,1025,-1):
   Pr=Pr*(3**(n%5)/(3**(n%7)))
print(1/Pr)   
