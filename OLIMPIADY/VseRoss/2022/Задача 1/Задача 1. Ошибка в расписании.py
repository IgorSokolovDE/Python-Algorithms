# https://sesc.nsu.ru/upload/iblock/922/inf_final_problems%20(1).pdf
f=open('input Задача 1. Ошибка в расписании.txt')
T=int(f.readline())
for t in range(T):
    N=int(f.readline())
    uroki=[]
    for u in range(N):
        s=f.readline()
        time=s.split(':')
        HH=int(time[0])
        MM=int(time[1])
        uroki.append(HH*60+MM)
    VSEok=True
    urokiSort=uroki[:]
    urokiSort.sort()
    if urokiSort!=uroki: #1. времена должны быть отсортированы по возрастанию;
            VSEok=False
        # 3. никакие уроки по времени не пересекаются
    for nU in range(N-1):
       if (uroki[nU]+45)> uroki[nU+1]:
                VSEok=False
        # 4. между подряд идущими уроками всегда должна быть перемена не менее 5 минут;
    for nU in range(N-1):
            if (uroki[nU+1]-(uroki[nU]+45))< 5 :
                VSEok=False
        # 5. если уроков больше трёх, то должна быть хотя бы одна большая перемена длительностью не менее 20 минут.
    if N>3:
            BigPausa=False
            for nU in range(N-1):
                if (uroki[nU+1]-(uroki[nU]+45))>=20 :
                    BigPausa=True
            if BigPausa:    
                VSEok=False
    if  VSEok:
        print('OK')
    else:
        print('ERROR')
