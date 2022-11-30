# x=0
# changeX=1
# def setup():
#     size(800,600)
# def draw():
#     background(100)
#     global x,changeX
#     img = loadImage("6017b47bd655fc000170fc3b.jpg")
#     image(img,x+x+x,100,150,100)
#     img = loadImage("cattouch.jpg")
#     image(img,x,300,150,100)
#     img = loadImage("maybach-s-class-222.jpg")
#     image(img,x+x,500,150,100)
#     x=x+changeX
#     if x+x+x==600:
#         noLoop()
#         text(u"Выиграл БМВ!!! Приз:Пожизненный запас моторного масла",400,300)
x=0
y=-300
changeX=1
changeY=1
def setup():
    size(1000,800)
def draw():
    background(150)
    translate(500,400)
    global x,changeX
    global y,changeY
    x=x+changeX
    y=y+changeY
    img = loadImage("Belarus-1999-Bill-5000000-Reverse.jpg")
    image(img,0,y,200,100)
    img = loadImage("deb.jpg")
    image(img,0,0,x,x)
    if y==0:
        x+1
a
