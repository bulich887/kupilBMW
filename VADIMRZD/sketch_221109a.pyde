# x=0
# def setup():
#     size(600,600)
# def draw():
#     global x
#     background(100)
#     ellipse(x,x,50,50)
#     x=x+1
#     if x==600:
#         x=x-600


        

# x=0
# sizeEllipse=0
# def setup():
#     size(600,600)
# def draw():
#     global x
#     global sizeEllipse
#     ellipse(x,x,sizeEllipse,sizeEllipse)
#     sizeEllipse=sizeEllipse+1
#     if sizeEllipse==400:
#         noLoop()
#     x=x+1

x=0
def setup():
    size(600,600)
def draw():
    global x
    fill(x)
    if x==255:
        x=x-255
    ellipse(300,300,100,100)
    x=x+1
    
    


    
