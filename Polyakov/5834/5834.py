for N in range(1,100000000000000000):
    N16=hex(N)[2:]
    #==========================
    if N%2==0:        #а) Если число чётное,
        N16=N16+'f'   #   справа приписывается максимально возможная цифра,
    else:
        N16=N16+'0'   #   в противном случае справа приписывается 0.
    #==========================
    SumCifr16=0
    for cifr in N16:
        SumCifr16+=int(cifr,16)
    N16=N16+(hex(SumCifr16%16) [2:]) #Справа приписывается шестнадцатеричная цифра
                                     #– остаток от деления суммы цифр шестнадцатеричной записи на 16.
    #==========================
    SumCifr16=0
    for cifr in N16:
        SumCifr16+=int(cifr,16)
    N16=N16+(hex(SumCifr16%16) [2:]) #Справа приписывается шестнадцатеричная цифра
                                     #– остаток от деления суммы цифр шестнадцатеричной записи на 16.
    #==========================
    MaxCifra=0
    MinCifra=15
    for cifr in N16:
       MaxCifra=max(int(cifr,16),MaxCifra)
       MinCifra=min(int(cifr,16),MinCifra)
    MaxCifra16=hex(MaxCifra)[2:]
    MinCifra16=hex(MinCifra)[2:]
    if N16.count(MaxCifra16)/N16.count(MinCifra16)==5:
        print(N)
        break
