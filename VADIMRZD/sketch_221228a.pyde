x=0
def setup():
    size(800,600)
    frameRate(10)
def draw():
    push()
    global x
    x=x+5
    translate(400,200)
    rectMode(CENTER)
    fill(107,69,40)
    noStroke()
    rect(0,235,30,70)
    for step in range(3):
        fill(HSB, 120,100,200)
        noStroke()
        triangle(-100,0,100,0,0,-100)
        translate(0,100)
    pop()
    for step in range(floor(random(0,800))):
        stroke(255)
        translate(20,0)
        point(random(0,800),x)
        strokeWeight(random(0,10))
        
# def setup():
#     size(800,600)
# def draw():
#     background(150)
#     push()
#     fill(120,100,50)
#     noStroke()
#     translate(400,300)
#     for step in range(4):
#         triangle(60,0,-60,0,0,-60)
#         translate(0,60)
def setup():
    size(800,600)
def draw():
    global x
    x=x+50
    rotate(radians(x))
    ellipse(400,300,400,60)

    
            
        

    
