x=0
def setup():
    size(800,600)

def draw():
    global x
    translate(400,300)
    rotate(radians(x))
    strokeWeight(4)
    stroke(202,106,4)
    line(0,0,100,100)
    rectMode(CENTER)
    rect(100,100,100,100)
    ellipse(100,100,90,90)
    ellipse(0,0,50,50)
    x=x+1
