f=open('27-108b.txt')
MinDlina=1000000000000000000000000
n,k=map(int, f.readline().split())
UNikPrMn=[]
kolUNikPrMn=[]
Nabor=[]
for i in range(n):
    x=int(f.readline())
    y=x
    prMn=[]
    d=2
    while y>1:
        if y%d==0:
            if not(d in prMn):
                prMn.append(d)
            y=y//d
        else:
            d+=1
    #добавляем новый элемент в набор
    Nabor.append(prMn)
    for j in range(len(prMn)):
        if not(prMn[j] in UNikPrMn):
            UNikPrMn.append(prMn[j])
            kolUNikPrMn.append(1)
        else:
            num=UNikPrMn.index(prMn[j])
            kolUNikPrMn[num]+=1
    if len(UNikPrMn)>=k:
      ubiratMoschno=True  
      while ubiratMoschno:  
        #можно ли убрать первый элемент набора
        kolUbrMn=0
        for j in range(len(Nabor[0])):
             num=UNikPrMn.index(Nabor[0][j]) 
             if kolUNikPrMn[num]==1:
                 kolUbrMn+=1
        if (len(UNikPrMn)- kolUbrMn)>=k:
            ubiratMoschno=True
        else:
            ubiratMoschno=False
        if  ubiratMoschno:
            for j in range(len(Nabor[0])):
               num=UNikPrMn.index(Nabor[0][j])
               if kolUNikPrMn[num]==1:
                   UNikPrMn.pop(num)
                   kolUNikPrMn.pop(num)
               else:
                   kolUNikPrMn[num]-=1
            Nabor.pop(0)        
        MinDlina=min(MinDlina,len(Nabor))
print(MinDlina)        
            


    

