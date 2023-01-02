# http://tasks.olimpiada.ru/upload/files/tasks/73/2022/task-info-9;11-gr2-sch-sirius-22-23.pdf

t=int(input())
r=int(input())
l=int(input())
p1=int(input())
p2=int(input())
p3=int(input())
r=r-(t//l)
t=t%l
PNado=r*l-t
kTovarov=(PNado//(p1+p2+p3))*3
if PNado-((p1+p2+p3)*(kTovarov//3))<=p1:
    kTovarov+=1
else:
    if PNado-((p1+p2+p3)*(kTovarov//3))<=(p1+p2):
        kTovarov+=2
    else:
        kTovarov+=3
print(kTovarov)        
