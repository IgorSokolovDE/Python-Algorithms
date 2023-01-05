def F(nachaloB):
    global Kol_Blokov
    global Max_kol_koln_v_bloke
    Naschli=True
    IschemB=nachaloB
    while Naschli:
        Naschli=False
        if IschemB:
                for i in range(len(kontenerB)):
                    if (Blok[-1]-kontenerB[i])>=7:
                       Blok.append(kontenerB[i])
                       kontenerB.pop(i)
                       Naschli=True
                       IschemB=False
                       break
        else:
                for i in range(len(kontenerA)):
                    if (Blok[-1]-kontenerA[i])>=7:
                       Blok.append(kontenerA[i])
                       kontenerA.pop(i)
                       Naschli=True
                       IschemB=True
                       break
    Kol_Blokov+=1
    Max_kol_koln_v_bloke=max(Max_kol_koln_v_bloke,len(Blok))
        
f=open('26.txt')
kontenerA=[]
kontenerB=[]
while True:
    s=f.readline()
    if not(s): break
    a=s.split()
    if a[1]=='A':
        kontenerA.append(int(a[0]))
    else:
        kontenerB.append(int(a[0]))
        
kontenerA.sort()
kontenerA=kontenerA[::-1]

kontenerB.sort()
kontenerB=kontenerB[::-1]

Kol_Blokov=0
Max_kol_koln_v_bloke=0
while (len(kontenerA)+len(kontenerB))>0:
  if (len(kontenerA)>0 and len(kontenerB))>0:  
        if kontenerA[0]>kontenerB[0]:
            #тогда начинаем с А
            Blok=[kontenerA[0]]
            kontenerA.pop(0)
            F(True)
            
        else:
            #тогда начинаем с B
            Blok=[kontenerB[0]]
            kontenerB.pop(0)
            Naschli=True
            F(False)
  else:
      if len(kontenerA)>0:
          #тогда начинаем с А
            Blok=[kontenerA[0]]
            kontenerA.pop(0)
            F(True)
      else:
          #тогда начинаем с B
            Blok=[kontenerB[0]]
            kontenerB.pop(0)
            Naschli=True
            F(False)        
print(Kol_Blokov,Max_kol_koln_v_bloke)        
