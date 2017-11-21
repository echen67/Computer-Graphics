# Animation Example

#Emily Chen

time = 0   # use time to move objects from one frame to the next

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
def draw():
    global time
    time += 0.01

    camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position the virtual camera

    background (255, 255, 255)  # clear screen and set background to white
    
    # create a directional light source
    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    
    noStroke()
    specular (100, 100, 100)
    #ambient (100, 100, 100)
    emissive (20, 20, 20)
    shininess (10.0)

    # draw piano
    translate(0,10,-10)
    rotateY(-time/2)
    rotateX(radians(-45))
    scale(.8)
    piano()

# piano
def piano():
    pushMatrix()
    rotateY(radians(180))
    translate(-50,0,0)
    keyboard()
    popMatrix()
    
    fill(100,100,100)
    
    #bottom
    pushMatrix()
    rotateX(radians(90))
    translate(-2,-8,-2)
    box(90,20,5)
    popMatrix()
    
    #cover
    pushMatrix()
    rotateX(radians(-70))
    translate(-2,9,-13)
    box(89,2,15)
    popMatrix()
    
    #under cover
    pushMatrix()
    translate(-2,0,-11)
    box(89,5,5)
    popMatrix()
    
    #high left
    pushMatrix()
    rotateX(radians(90))
    translate(-48,-6,0.5)
    box(3,21,10)
    popMatrix()
    
    #high right
    pushMatrix()
    rotateX(radians(90))
    translate(44,-6,0.5)
    box(3,21,10)
    popMatrix()
    
    #left leg
    pushMatrix()
    translate(-48,20,0)
    box(2,35,4)
    popMatrix()
    
    #right leg
    pushMatrix()
    translate(44,20,0)
    box(2,35,4)
    popMatrix()
    
    #left
    pushMatrix()
    translate(-48,20,-13)
    box(3,35,7)
    popMatrix()
    
    #right
    pushMatrix()
    translate(44,20,-13)
    box(3,35,7)
    popMatrix()
    
    #low left
    pushMatrix()
    translate(-48,40,-6)
    box(3,5,22)
    popMatrix()
    
    #low right
    pushMatrix()
    translate(44,40,-6)
    box(3,5,22)
    popMatrix()
    
    #pedal bar
    pushMatrix()
    translate(0-2,40,-18)
    box(93,5,5)
    popMatrix()
    
    #back
    pushMatrix()
    translate(-2,5,-25)
    box(95,75,17)
    popMatrix()
    
    #right pedal
    pushMatrix()
    scale(1.5)
    translate(2,27,-6.5)
    rotateX(radians(-90))
    rightPedal()
    popMatrix()
    
    #left pedal
    pushMatrix()
    scale(-1.5,1.5,1.5)
    translate(2,27,-6.5)
    rotateX(radians(-90))
    rightPedal()
    popMatrix()
    
    #middle pedal
    pushMatrix()
    scale(1.5)
    translate(0,27.5,-9)
    box(1.5,1,5)
    popMatrix()

# keyboard
def keyboard():
    for i in range(7):
        translate(11.2,0,0)
        octave()
    translate(11.2,0,0)
    rotateX(radians(90))
    rightKey()
    translate(1.6,0,0)
    leftKey()
    translate(-0.5,3,1)
    blackKey()

# octave
def octave():
    #black keys
    pushMatrix()
    rotateX(radians(90))
    translate(1.05,3,1)
    blackKey()
    translate(1.6,0,0)
    blackKey()
    translate(3.2,0,0)
    blackKey()
    translate(1.6,0,0)
    blackKey()
    translate(1.6,0,0)
    blackKey()
    popMatrix()
       
    #white keys
    pushMatrix()
    rotateX(radians(90))
    translate(0,0,0)
    rightKey()
    translate(1.6,0,0)
    middleKey()
    translate(1.6,0,0)
    leftKey()
    translate(1.6,0,0)
    rightKey()
    translate(1.6,0,0)
    middleKey()
    translate(1.6,0,0)
    middleKey()
    translate(1.6,0,0)
    leftKey()
    popMatrix()

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
    
#right pedal
def rightPedal():
    fill(255,255,0)
    
    #top
    beginShape()
    vertex(0,0,1)
    vertex(0,5,1)
    vertex(1,5,1)
    vertex(1.5,2,1)
    vertex(1.5,0,1)
    endShape()
    #bottom
    beginShape()
    vertex(0,0,0)
    vertex(0,5,0)
    vertex(1,5,0)
    vertex(1.5,2,0)
    vertex(1.5,0,0)
    endShape()
    
    #largest side
    beginShape()
    vertex(0,0,0)
    vertex(0,0,1)
    vertex(0,5,1)
    vertex(0,5,0)
    endShape()
    #bottom side
    beginShape()
    vertex(0,0,0)
    vertex(0,0,1)
    vertex(1.5,0,1)
    vertex(1.5,0,0)
    endShape()
    #top side
    beginShape()
    vertex(0,5,0)
    vertex(0,5,1)
    vertex(1,5,1)
    vertex(1,5,0)
    endShape()
    #top slant side
    beginShape()
    vertex(1,5,0)
    vertex(1,5,1)
    vertex(1.5,2,1)
    vertex(1.5,2,0)
    endShape()
    #bottom slant side
    beginShape()
    vertex(1.5,2,0)
    vertex(1.5,2,1)
    vertex(1.5,0,1)
    vertex(1.5,0,0)
    endShape()
    
# right white key
def rightKey():
    fill(255,255,255)
    #top
    beginShape()
    vertex(0,0,2)
    vertex(0,8,2)
    vertex(1,8,2)
    vertex(1,3,2)
    vertex(1.5,3,2)
    vertex(1.5,0,2)
    endShape(CLOSE)
    #bottom
    beginShape()
    vertex(0,0,0)
    vertex(0,8,0)
    vertex(1,8,0)
    vertex(1,3,0)
    vertex(1.5,3,0)
    vertex(1.5,0,0)
    endShape(CLOSE)
    
    #largest side
    beginShape()
    vertex(0,0,0)
    vertex(0,0,2)
    vertex(0,8,2)
    vertex(0,8,0)
    endShape(CLOSE)
    #bottom side
    beginShape()
    vertex(0,0,0)
    vertex(0,0,2)
    vertex(1.5,0,2)
    vertex(1.5,0,0)
    endShape(CLOSE)
    #top side
    beginShape()
    vertex(0,8,0)
    vertex(0,8,2)
    vertex(1,8,2)
    vertex(1,8,0)
    endShape(CLOSE)
    #top half side
    beginShape()
    vertex(1,8,0)
    vertex(1,8,2)
    vertex(1,3,2)
    vertex(1,3,0)
    endShape(CLOSE)
    #bottom half side
    beginShape()
    vertex(1.5,0,0)
    vertex(1.5,0,2)
    vertex(1.5,3,2)
    vertex(1.5,3,0)
    endShape(CLOSE)
    #smallest side
    beginShape()
    vertex(1,3,0)
    vertex(1,3,2)
    vertex(1.5,3,2)
    vertex(1.5,3,0)
    endShape(CLOSE)
    
# left white key
def leftKey():
    fill(255,255,255)
    #top
    beginShape()
    vertex(0,0,2)
    vertex(0,3,2)
    vertex(0.5,3,2)
    vertex(0.5,8,2)
    vertex(1.5,8,2)
    vertex(1.5,0,2)
    endShape()
    #bottom
    beginShape()
    vertex(0,0,0)
    vertex(0,3,0)
    vertex(0.5,3,0)
    vertex(0.5,8,0)
    vertex(1.5,8,0)
    vertex(1.5,0,0)
    endShape()
    
    #top side
    beginShape()
    vertex(0.5,8,0)
    vertex(0.5,8,2)
    vertex(1.5,8,2)
    vertex(1.5,8,0)
    endShape()
    #bottom side
    beginShape()
    vertex(0,0,0)
    vertex(0,0,2)
    vertex(1.5,0,2)
    vertex(1.5,0,0)
    endShape()
    
    #largest side
    beginShape()
    vertex(1.5,0,0)
    vertex(1.5,0,2)
    vertex(1.5,8,2)
    vertex(1.5,8,0)
    endShape()
    #top half side
    beginShape()
    vertex(0.5,3,0)
    vertex(0.5,3,2)
    vertex(0.5,8,2)
    vertex(0.5,8,0)
    endShape()
    #smallest side
    beginShape()
    vertex(0,3,0)
    vertex(0,3,2)
    vertex(0.5,3,2)
    vertex(0.5,3,0)
    endShape()
    #bottom half side
    beginShape()
    vertex(0,0,0)
    vertex(0,0,2)
    vertex(0,3,2)
    vertex(0,3,0)
    endShape()
    
# middle white key
def middleKey():
    fill(255,255,255)
    #top
    beginShape()
    vertex(0,0,2)
    vertex(0,3,2)
    vertex(0.5,3,2)
    vertex(0.5,8,2)
    vertex(1,8,2)
    vertex(1,3,2)
    vertex(1.5,3,2)
    vertex(1.5,0,2)
    endShape(CLOSE)
    #bottom
    beginShape()
    vertex(0,0,0)
    vertex(0,3,0)
    vertex(0.5,3,0)
    vertex(0.5,8,0)
    vertex(1,8,0)
    vertex(1,3,0)
    vertex(1.5,3,0)
    vertex(1.5,0,0)
    endShape(CLOSE)
    
    #bottom side
    beginShape()
    vertex(0,0,0)
    vertex(0,0,2)
    vertex(1.5,0,2)
    vertex(1.5,0,0)
    endShape(CLOSE)
    #top side
    beginShape()
    vertex(0.5,8,0)
    vertex(0.5,8,2)
    vertex(1,8,2)
    vertex(1,8,0)
    endShape()
    
    #left bottom half
    beginShape()
    vertex(0,0,0)
    vertex(0,0,2)
    vertex(0,3,2)
    vertex(0,3,0)
    endShape()
    #left smallest
    beginShape()
    vertex(0,3,0)
    vertex(0,3,2)
    vertex(0.5,3,2)
    vertex(0.5,3,0)
    endShape(CLOSE)
    #left top half
    beginShape()
    vertex(0.5,3,0)
    vertex(0.5,3,2)
    vertex(0.5,8,2)
    vertex(0.5,8,0)
    endShape()
    
    #right top half
    beginShape()
    vertex(1,3,0)
    vertex(1,3,2)
    vertex(1,8,2)
    vertex(1,8,0)
    endShape()
    #right smallest
    beginShape()
    vertex(1,3,0)
    vertex(1,3,2)
    vertex(1.5,3,2)
    vertex(1.5,3,0)
    endShape()
    #right bottom half
    beginShape()
    vertex(1.5,0,0)
    vertex(1.5,0,2)
    vertex(1.5,3,2)
    vertex(1.5,3,0)
    endShape()
    
# black piano key
def blackKey():
    fill(100,100,100)
    #bottom
    beginShape()
    normal(0,0,-1)
    vertex(0,0,0)
    vertex(1,0,0)
    vertex(1,5,0)
    vertex(0,5,0)
    endShape(CLOSE)
    #top
    beginShape()
    normal(0,0,1)
    vertex(0,1,2)
    vertex(1,1,2)
    vertex(1,5,2)
    vertex(0,5,2)
    endShape(CLOSE)
    
    #leftside
    beginShape()
    vertex(0,5,2)
    vertex(0,5,0)
    vertex(0,0,0)
    vertex(0,0,1)
    vertex(0,1,2)
    endShape(CLOSE)
    #rightside
    beginShape()
    vertex(1,5,2)
    vertex(1,5,0)
    vertex(1,0,0)
    vertex(1,0,1)
    vertex(1,1,2)
    endShape(CLOSE)
    
    #slanttop
    beginShape()
    vertex(0,1,2)
    vertex(1,1,2)
    vertex(1,0,1)
    vertex(0,0,1)
    endShape(CLOSE)
    #slantbottom
    beginShape()
    vertex(0,0,0)
    vertex(1,0,0)
    vertex(1,0,1)
    vertex(0,0,1)
    endShape(CLOSE)
    
    #back
    beginShape()
    vertex(0,5,0)
    vertex(1,5,0)
    vertex(1,5,2)
    vertex(0,5,2)
    endShape(CLOSE)