for x in '123456789a':
    if (int('3364'+x,11)+int(x+'7946',12))==int('55'+x+'87',14):
        print(int('55'+x+'87',14))
        break
        
