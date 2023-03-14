k=0
for x in range(1,9):
    yPink=(x/(3**0.5))
    yBlue=-x/(3**0.5)
    for y in range(-11,12):
        if yBlue<y<yPink:
            k+=1
print(k) 
