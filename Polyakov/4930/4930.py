for N in range(1,10000):
    N2=bin(N)[2:]
    if N%2==0:
        SumCifr2=N2.count('1') #сумма цифр его двоичной записи
        SumCifr2_2=bin(SumCifr2)[2:]#в двоичном виде сумма цифр его двоичной записи;
        N2=N2+SumCifr2_2 #к нему справа приписывается в двоичном виде сумма цифр его двоичной записи;
    else:
        N2='1'+N2+'00'# то к нему справа приписываются два нуля, а слева единица.
    R=int(N2,2)
    if R>215:
        print(N)
        break