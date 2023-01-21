x=0
y=50
a=0
mode="влево"
mode2="черный"

def setup():
    size(800,600)

def draw():
    background(200)
    global x,y,mode,a
    global mode2
    ellipse(x,300,y,y)
    
    if mode=="вправо":
        x=x+3
        y=y+3        
    if x>=775:
        mode="влево"
    if mode=="влево":
        x=x-3
        y=y-3
    if x<=25:
        mode="вправо"
    

    if mode2="белый":
        a=a+1
        fill(a,255)
    if a==255:
        mode2="черный"
    if mode2="черный":
        a=a-1
        fill(0,a)
    if a==0:
        mode2="белый"
    
    
    
