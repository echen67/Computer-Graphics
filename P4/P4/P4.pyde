# Project 4 base code (GPU shaders)
# Emily Chen

def setup():
    global catTexture, mountainTexture
    size(640, 640, P3D)
    noStroke()
    
    catTexture = loadImage("data/cat.png")
    mountainTexture = loadImage("data/green_mountain.jpg")
    
    loadShaders()

# load the vertex and fragment shaders (four of each)
def loadShaders():
    global shaders
    shaders = []
    for i in range(4):
        shader = loadShader("data/shader" + str(i) + ".frag", "data/shader" + str(i) + ".vert")
        shaders.append(shader)
        pass

# draw the whole scene
def draw():
    
    noLights()
    background(0, 0, 0)
    camera (0, 0, 400, 0, 0, 0, 0, 1, 0)

    pushMatrix()
    
    # rotate the scene based on the mouse position
    dirY = (mouseY / float(height) - 0.5) * 2
    dirX = (mouseX / float(width) - 0.5) * 2
    rotate(-dirY, 1, 0, 0)
    rotate(dirX * 3, 0, 1, 0)
    
    # draw the various shaded quadrilaterals
    ground_plane()
    mandelbrot()
    edge_detection()
    green_mountain()
    swiss_cheese()
    
    popMatrix()

# Draw Quad 0 (Swiss Cheese)
def swiss_cheese():
    fill(200, 30, 200)  # purple indicates a broken shader
    pushMatrix()
    translate(100, 0, 120)
    translate(0, 80, 0)
    scale(0.7, 0.7, 0.7)
    shader(shaders[0])
    beginShape()
    vertex(-100, -100, 0, 0, 0)
    vertex( 100, -100, 0, 1, 0)
    vertex( 100, 100,  0, 1, 1)
    vertex(-100, 100,  0, 0, 1)
    endShape()
    popMatrix()

# Draw Quad 1 (Edge Detection)
def edge_detection():
    fill(200, 30, 200)  # purple indicates a broken shader
    pushMatrix()
    translate(-100, 0, 120)
    translate(0, 80, 0)
    scale(0.7, 0.7, 0.7)
    shader(shaders[1])
    textureMode(NORMAL)
    beginShape()
    texture(catTexture)
    vertex(-100, -100, 0, 0, 0)
    vertex( 100, -100, 0, 1, 0)
    vertex( 100, 100,  0, 1, 1)
    vertex(-100, 100,  0, 0, 1)
    endShape()
    popMatrix()

# Draw Quad 2 (Mandelbrot Set)
def mandelbrot():
    fill(200, 30, 200)  # purple indicates a broken shader
    pushMatrix()
    translate(100, 0, -120)
    translate(0, 80, 0)
    scale(0.7, 0.7, 0.7)
    textureMode(NORMAL)
    shader(shaders[2])
    beginShape()
    vertex(-100, -100, 0, 0, 0)
    vertex( 100, -100, 0, 1, 0)
    vertex( 100, 100,  0, 1, 1)
    vertex(-100, 100,  0, 0, 1)
    endShape()
    popMatrix()

# Draw Quad 3 (Green Mountain) -- You will need to modify this routine to chop up the quad into pieces
def green_mountain():
    fill(200, 30, 200)  # purple indicates a broken shader
    pushMatrix()
    translate(-100, 0, -120)
    translate(0, 80, 0)
    scale(0.7, 0.7, 0.7)
    shader(shaders[3])
    textureMode(NORMAL)
    for i in range(40):
        for j in range(40):
            beginShape()
            texture(mountainTexture)
            # 20 quads
            # vertex(0+10*i-100, 0+10*j-100, 0, (0+i)/20.0, (0+j)/20.0)
            # vertex(10+10*i-100, 0+10*j-100, 0, (1+i)/20.0, (0+j)/20.0)
            # vertex(10+10*i-100, 10+10*j-100, 0, (1+i)/20.0, (1+j)/20.0)
            # vertex(0+10*i-100, 10+10*j-100, 0, (0+i)/20.0, (1+j)/20.0)
            
            # 40 quads
            vertex(0+5*i-100, 0+5*j-100, 0, (0+i)/40.0, (0+j)/40.0)
            vertex(5+5*i-100, 0+5*j-100, 0, (1+i)/40.0, (0+j)/40.0)
            vertex(5+5*i-100, 5+5*j-100, 0, (1+i)/40.0, (1+j)/40.0)
            vertex(0+5*i-100, 5+5*j-100, 0, (0+i)/40.0, (1+j)/40.0)
            
            # vertex(0+10*i-100, 0+10*j-100, 0, 0, 0)
            # vertex(10+10*i-100, 0+10*j-100, 0, 1, 0)
            # vertex(10+10*i-100, 10+10*j-100, 0, 1, 1)
            # vertex(0+10*i-100, 10+10*j-100, 0, 0, 1)
            endShape()
    # beginShape()
    # texture(mountainTexture)
    # vertex(-100, -100, 0, 0, 0)
    # vertex( 100, -100, 0, 1, 0)
    # vertex( 100, 100,  0, 1, 1)
    # vertex(-100, 100,  0, 0, 1)
    # endShape()
    popMatrix()

# Draw the ground plane
def ground_plane():
    noStroke()
    fill(200, 200, 200)
    pushMatrix()
    translate(0, 150, 0)
    rotate(PI/2, 1, 0, 0)
    scale(2.0, 2.0, 2.0)
    resetShader()  # de-activate any shader that was previously in use
    beginShape()
    vertex(-100, -100, 0, 0, 0)
    vertex( 100, -100, 0, 1, 0)
    vertex( 100, 100, 0, 1, 1)
    vertex(-100, 100, 0, 0, 1)
    endShape()
    popMatrix()