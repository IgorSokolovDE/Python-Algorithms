for i in range(10):
    for j in range(10):
        s='12345'+str(i)+'7'+str(j)+'8'
        ch=int(s)
        if ch%23==0:
            print(ch,ch//23)
