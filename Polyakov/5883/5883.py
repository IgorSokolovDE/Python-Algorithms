for x in range(17):
    y=(1*17**3+x*17) +(15*17**4+x*17**2+15*17+15)
    if y % 13==0:
        print(y//13)
        break
