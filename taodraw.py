import turtle
tao=turtle.Pen()
tao.shape('turtle')
tao.color('green')
for i in range(4):
    tao.penup()
    tao.forward(60)
    tao.pendown()
    tao.circle(30)

    
tao.penup()
tao.goto(0,-5)
for i in range(4):
    tao.penup()
    tao.forward(60)
    tao.pendown()
    tao.circle(10)

    
tao.penup()
tao.goto(253,40)
tao.pendown()
tao.circle(6)
tao.penup()
tao.goto(240,60)
tao.left(60)
tao.pendown()
tao.forward(20)
tao.penup()
tao.goto(240,60)
tao.left(10)
tao.pendown()
tao.forward(20)
