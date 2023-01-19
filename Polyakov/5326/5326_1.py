for M in range(4,5000):
    Mask=str(M)
    if Mask[0]=='4':
        ch=int('123'+Mask+'7')
        if ch%141==0:
            print(ch,ch//141)
