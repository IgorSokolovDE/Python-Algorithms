MinK3=10000000000000000000000000000000000000000000
for n in range(1,2**20):
    Bin=bin(n)[2:]
    Bin='0'*(20-len(Bin))+Bin
    if Bin.count('1')==10:
       S=Bin.replace('0','2')
       S='0'+S+'0'
       while not('00' in S):
           S=S.replace('012','30',1)
           if '011' in S:
               S=S.replace('011','20',1)
               S=S.replace('022','40',1)
           else:
               S=S.replace('01','10',1)
               S=S.replace('02','101',1)
       if (S.count('1')==7) and (S.count('2')==5):
            MinK3=min(MinK3,S.count('3'))
print(MinK3)                      
