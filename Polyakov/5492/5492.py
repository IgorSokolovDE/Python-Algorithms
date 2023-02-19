for x in '0123456789abc':
    y=int('8'+x+'121',13)-int('7'+x+'575',13)
    if y%19==0:
        print(y//19)
        break
