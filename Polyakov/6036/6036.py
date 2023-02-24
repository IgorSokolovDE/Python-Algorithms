def F(n,s):
    global kpr
    if n<2: return
    if n==2:
        if s[1]==('A')and(s[-3:-1]=='CB')and(len(s)>=5):
            if not('AA' in s):
                if not('BB' in s):
                    if not('CC' in s):
                        kpr+=1
        return
    else:
        F(n-1,s+'A')
        F(n-2,s+'B')
        F(n//2,s+'C')
kpr=0
F(34,'')
print(kpr)
