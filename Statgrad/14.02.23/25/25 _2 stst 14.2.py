for v in range(10):
    for m in range(6,7000):
        s=str(m)
        if s[0]=='6':
            ch=int('1'+str(v)+'724'+s+'1')
            if ch%4173==0:
                print(ch)
