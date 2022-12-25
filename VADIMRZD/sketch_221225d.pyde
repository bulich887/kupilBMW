x=0
changeX=1
def setup():
    size(800,600)
    frameRate(20)
def draw():
    background(150)
    global x, changeX
    global y,changeY
    x=x+changeX
    y=y+changeY
    translate(400,300)
    ellipse(0,x,50,50)
    if x==300:
        changeX=-1
    if x==-300:
        changeX=1
    translate(-400,-300)
    line(0,0,x,y)
    line(0,0,x,y)
    translate(400,300)
    fill(0,0,51)
    
    rotate(radians(x))
    fill(0,255,255)
    ellipse(0,90,50,100)
    fill(0,102,255)
    rect(0,160,50,20)
    fill(0,0,255)
    ellipse(0,200,50,50)
    
    rotate(radians(x))
    fill(0,255,255)
    ellipse(0,90,50,100)
    fill(0,102,255)
    rect(0,160,50,20)
    fill(0,0,255)
    ellipse(0,200,50,50)
    
    rotate(radians(x))
    fill(0,255,255)
    ellipse(0,90,50,100)
    fill(0,102,255)
    rect(0,160,50,20)
    fill(0,0,255)
    ellipse(0,200,50,50)
    
    rotate(radians(45))
    fill(0,255,255)
    ellipse(0,90,50,100)
    fill(0,102,255)
    rect(0,160,50,20)
    fill(0,0,255)
    ellipse(0,200,50,50)
    
    rotate(radians(x))
    fill(0,255,255)
    ellipse(0,90,50,100)
    fill(0,102,255)
    rect(0,160,50,20)
    fill(0,0,255)
    ellipse(0,200,50,50)
    
    rotate(radians(x))
    fill(0,255,255)
    ellipse(0,90,50,100)
    fill(0,102,255)
    rect(0,160,50,20)
    fill(0,0,255)
    ellipse(0,200,50,50)
    
    rotate(radians(x))
    fill(0,255,255)
    ellipse(0,90,50,100)
    rect(0,160,50,20)
    fill(0,0,255)
    ellipse(0,200,50,50)
    
    rotate(radians(x))
    fill(0,255,255)
    ellipse(0,90,50,100)
    fill(0,102,255)
    rect(0,160,50,20)
    fill(0,0,255)
    ellipse(0,200,50,50)
