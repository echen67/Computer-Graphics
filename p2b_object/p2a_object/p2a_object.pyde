# Animation Example

#Emily Chen
#Instanced object is the spotlight

time = 0   # use time to move objects from one frame to the next

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
def draw():
    global time
    time += 0.01
    
    #global time2
    #time2 += 0.01

    print(frameCount)

    if (frameCount > 940):
        exit()

    if time < 1:
        camera (0, -100, 300, 0, 0, 0, 0,  1, 0)  # position the virtual camera
    elif time > 1 and time < 4.5:
        camera (0, -110+time*10, 340-time*40, 0, 0, 0, 0, 1, 0)
    elif time > 4.5 and time < 6:
        camera (0, -50, 50, 0, 0, 0, 0, 1, 0)
    elif time > 6 and time < 6.4:
        camera (0, -70, 180, 0, 0, 0, 0, 1, 0)
    elif time > 6.4:
        camera (0, -6-time*10, -76+time*40, 0, 0, 0, 0, 1, 0)

    background (0,0,0)  # clear screen and set background to white
    
    # create a directional light source
    #ambientLight(50, 50, 50);
    lightSpecular(100, 100, 150)
    directionalLight (90, 90, 90, -0.3, 0.5, -1)
    #pointLight(200,200,200, 0,-60,0)
    
    colorMode(HSB)
    spotLight((time*200)%356,100,200, 0,-60,0, 0,50,0, PI/2, 2)
    
    colorMode(RGB)
    
    noStroke()
    specular (100, 100, 100)
    #ambient (100, 100, 100)
    emissive (20, 20, 20)
    shininess (10.0)

    # draw piano
    pushMatrix()
    translate(0,10,-10)
    #rotateY(-time/2)
    #rotateX(radians(-45*time/2))
    #rotateX(radians(-45))
    scale(.8)
    piano()
    popMatrix()
    
    # draw stage
    pushMatrix()
    fill(124,83,47)
    translate(0,48,-100)
    box(900,10,400)
    popMatrix()
    
    shininess(100)
    
    # draw back curtain
    pushMatrix()
    fill(26,44,119)
    scale(3,4,2)
    translate(-100,40,-50)
    rotateX(radians(90))
    curtain()
    popMatrix()
    
    # draw front curtains
    pushMatrix()
    fill(131,13,13)
    scale(1.5,3,1.5)
    if time <= 3:
        translate(-10+40*time,30,15)
    elif time > 3 and time < 6.4:
        translate(110,30,15)
    elif time > 6.4:
        translate(366-time*40,30,15)
    rotateX(radians(90))
    curtain()
    popMatrix()
    
    pushMatrix()
    scale(1.5,3,1.5)
    if time <= 3:
        translate(-190-40*time,30,20)
    elif time > 3 and time < 6.4:
        translate(-310,30,20)
    elif time > 6.4:
        translate(-566+time*40,30,20)
    rotateX(radians(90))
    curtain()
    popMatrix()
    
    # draw character
    pushMatrix()
    if time <= 2:
        translate(-150,0,0)
    elif time > 2 and time < 4:
        translate(-230+time*40,0,0)
    elif time > 4 and time < 6.2:
        translate(-70,0,0)
    elif time > 6.2 and time < 6.4:
        translate(-70,-186+time*30,0)
        rotateZ(radians(2480-time*400))
    elif time > 6.4:
        translate(-70,10,0)
        rotateZ(radians(-90))
    character()
    popMatrix()
    
    # draw spotlight; instanced object
    pushMatrix()
    scale(2)
    translate(50,-60,-20)
    rotateX(radians(-45))
    rotateY(radians(-45))
    spotlight()
    popMatrix()
    
    pushMatrix()
    scale(2)
    translate(-50,-60,-20)
    rotateX(radians(-45))
    rotateY(radians(45))
    spotlight()
    popMatrix()

# spotlight
def spotlight():
    fill(0,0,0)
    emissive(20,20,20)
    scale(5)
    cylinder()
    
    pushMatrix()
    translate(1.5,0,1.5)
    rotateX(radians(90))
    rotateZ(radians(45))
    box(1.5,.1,1.5)
    popMatrix()
    
    pushMatrix()
    translate(-1.5,0,1.5)
    rotateX(radians(90))
    rotateZ(radians(-45))
    box(1.5,.1,1.5)
    popMatrix()
    
    fill(255,255,150)
    emissive(255,255,150)
    scale(.7)
    translate(0,0,.5)
    cylinder()

# character
def character():
    fill(255,255,255)
    ellipse(0,-11,20,20)
    rect(-10,0,20,25)
    rect(-10,26,7,7)
    rect(3,26,7,7)

    fill(50,50,50)
    pushMatrix()
    translate(0,0,1)
    ellipse(-4,-12,3,3)
    ellipse(4,-12,3,3)
    popMatrix()

# piano
def piano():
    pushMatrix()
    rotateY(radians(180))
    translate(-50,0,0)
    #translate(0, sin(5*time2)/2, 0)
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
    translate(-2,-1,-10.5)
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
        #octave(i)
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
        if time > 5:
            translate(0, 0, -abs(sin(4*time))/1.5)
        rightKey()
        popMatrix()
        
        pushMatrix()
        rotateX(radians(90))
        translate(1.6,0,0)
        if time > 5:
            translate(0, 0, -abs(sin(1 + 4*time))/1.5)
        middleKey()
        popMatrix()
        
        pushMatrix()
        rotateX(radians(90))
        translate(3.2,0,0)
        if time > 5:
            translate(0, 0, -abs(sin(1.5 + 4*time))/1.5)
        leftKey()
        popMatrix()
        
        pushMatrix()
        rotateX(radians(90))
        translate(4.8,0,0)
        if time > 5:
            translate(0, 0, -abs(sin(2 + 4*time))/1.5)
        rightKey()
        popMatrix()
        
        pushMatrix()
        rotateX(radians(90))
        translate(6.4,0,0)
        if time > 5:
            translate(0, 0, -abs(sin(2.5 + 4*time))/1.5)
        middleKey()
        popMatrix()
        
        pushMatrix()
        rotateX(radians(90))
        translate(8,0,0)
        if time > 5:
            translate(0, 0, -abs(sin(3 + 4*time))/1.5)
        middleKey()
        popMatrix()
        
        pushMatrix()
        rotateX(radians(90))
        translate(9.6,0,0)
        if time > 5:
            translate(0, 0, -abs(sin(3.5 + 4*time))/1.5)
        leftKey()
        popMatrix()
        
    translate(11.2,0,0)
    rotateX(radians(90))
    rightKey()
    translate(1.6,0,0)
    leftKey()
    translate(-0.5,3,1)
    blackKey()

# octave
def octave(i):    
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
    translate(0, 0, sin(i + 1*time)/2)
    rightKey()
    popMatrix()
    
    pushMatrix()
    rotateX(radians(90))
    translate(1.6,0,0)
    translate(0, 0, sin(i +1+ 1*time)/2)
    middleKey()
    popMatrix()
    
    pushMatrix()
    rotateX(radians(90))
    translate(3.2,0,0)
    translate(0, 0, sin(i +2+ 1*time)/2)
    leftKey()
    popMatrix()
    
    pushMatrix()
    rotateX(radians(90))
    translate(4.8,0,0)
    translate(0, 0, sin(i +3+ 1*time)/2)
    rightKey()
    popMatrix()
    
    pushMatrix()
    rotateX(radians(90))
    translate(6.4,0,0)
    translate(0, 0, sin(i +4+ 1*time)/2)
    middleKey()
    popMatrix()
    
    pushMatrix()
    rotateX(radians(90))
    translate(8,0,0)
    translate(0, 0, sin(i +5+ 1*time)/2)
    middleKey()
    popMatrix()
    
    pushMatrix()
    rotateX(radians(90))
    translate(9.6,0,0)
    translate(0, 0, sin(i +6+ 1*time)/2)
    leftKey()
    popMatrix()
    
# curtain
def curtain():
    for i in range(2000):
        beginShape()
        vertex(i/10.0,sin(i/10.0),0)
        vertex((i+1)/10.0,sin((i+1)/10.0),0)
        vertex((i+1)/10.0,sin((i+1)/10.0),90)
        vertex(i/10.0,sin(i/10.0),90)
        endShape()
    
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