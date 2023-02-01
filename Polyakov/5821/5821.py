for x in range(9,-1,-1):
    osn1=int('132'+str(x)+'4')
    y10=(1*osn1+3)-int(('134'+str(x)+'2'),13)
    if y10%30==0:
        print(abs(y10//30))
        break
