for n in range(3532000, 3532161):
    prost=True
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            prost=False
            break
    if prost:
        print(n)
