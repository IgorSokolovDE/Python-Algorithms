for x in range(37):
    y=1*37**3+2*37**2+3*37+x+4*37**3+x*37**2+5*37+9
    if y%36==0:
        print(y//36)
        break
