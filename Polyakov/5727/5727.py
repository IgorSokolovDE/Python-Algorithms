for x in range(1,100):
    s='1'*x+'2'*x+'3'*x
    if len(s)>=50:
        if s[49]=='2':
            print(x*3)
            # break
