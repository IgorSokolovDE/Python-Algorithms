for x in range(2023,2023**2+1):
    S=str(x)
    if '2' in S:
        N2=S.index('2')
        S2=S[N2:]
        if '0' in S2:
            N0=S2.index('0')
            S3=S2[N0:]
            if '2' in S3:
                N2=S3.index('2')
                S4=S3[N2:]
                if '3' in S4:
                    X2=bin(x)[2:]
                    X8=oct(x)[2:]
                    if (X2==X2[::-1])and(X8==X8[::-1]):
                        sumCifr=0
                        for ss8 in X8:
                            sumCifr+=int(ss8)
                        print(x,sumCifr)
        
