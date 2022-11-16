# y=0
# changeY=1
# def setup():
#     size(600,600)
# def draw():
#     global y,changeY
#     background(125)
#     translate(300,300)
#     rectMode(CENTER)
#     rect(0,0,y,y)
#     y=y+changeY
#     if y==300:
#         changeY=-1
#     if y==20:
#         changeY=1

y=0
changeY=1
def setup():
    size(600,600)
def draw():
    global y,changeY
    background(125)
    fill(0,200,0)
    ellipse(y,y,60,60)
    y=y+changeY
    if y==600:
        changeY=-1
    if y==0:
        changeY=1
    
    
