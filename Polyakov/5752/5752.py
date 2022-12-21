for x in range(53,600000):
    s=str(x)
    if (s[0]=='5')and('3' in s):
        ch=int('1'+s+'09')
        Delit=[]
        for D in range(1,int(ch**0.5)+1):
            if ch%D==0:
                Delit.append(D)
                if D*D!=ch: Delit.append(ch//D)
            if len(Delit)>9: break
        if len(Delit)==9:
            Delit.sort()
            print(ch,Delit[-2])
                
                    
