import turtle as T
T.left(90)
for i in range(2):
    T.left(120)
    T.color('black')
    for j in range(10):
        T.right(30)
        T.forward(40)
        T.right(60)
    T.color('red')
    T.left(150)
    T.back(20)
    T.left(90)
    T.back(20)
