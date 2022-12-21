s="АВЕИКМСТШ"
glB="АЕИ"
sglB="ВКМСТШ"
s=s[::-1]
num=0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo=a+b+c+d+e
                    num+=1
                    if slovo==slovo[::-1]:
                        if c in sglB:
                            if a in glB:
                                if b in glB:
                                    if d in glB:
                                        if e in glB:
                                            print(num,slovo)
                                            ii=input()
                                            
                            







