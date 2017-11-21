# Drawing Routines, like OpenGL

#Emily Chen

from matlib import *

aList = []        #we will use this to keep track of all the vertices
projection = 0    #choose which type of projection we are using, 0 for ortho and 1 for persp

class Vertex():
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        
    #ignore this
    def multiplyTrans(self, matrix):
        v1 = 0
        v1 += matrix.matrixGet(1,1) * self.x
        v1 += matrix.matrixGet(1,2) * self.y
        v1 += matrix.matrixGet(1,3) * self.z
        v1 += matrix.matrixGet(1,4) * self.w
        
        v2 = 0
        v2 += matrix.matrixGet(2,1) * self.x
        v2 += matrix.matrixGet(2,2) * self.y
        v2 += matrix.matrixGet(2,3) * self.z
        v2 += matrix.matrixGet(2,4) * self.w
        
        v3 = 0
        v3 += matrix.matrixGet(3,1) * self.x
        v3 += matrix.matrixGet(3,2) * self.y
        v3 += matrix.matrixGet(3,3) * self.z
        v3 += matrix.matrixGet(3,4) * self.w
        
        v4 = 0
        v4 += matrix.matrixGet(4,1) * self.x
        v4 += matrix.matrixGet(4,2) * self.y
        v4 += matrix.matrixGet(4,3) * self.z
        v4 += matrix.matrixGet(4,4) * self.w
        
        newVertex = Vertex(v1, v2, v3, v4)
        return newVertex
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getZ(self):
        return self.z
    
    def setX(self, newX):
        self.x = newX
    
    def setY(self, newY):
        self.y = newY

def gtOrtho(left, right, bottom, top, near, far):
    global projection
    projection = 0
    #ignore lol
    #r1 = [800.0/(right-left), 0, 0, -left]    #800.0 is hardcoded for now, should change later
    #r2 = [0, 800.0/(top-bottom), 0, -bottom]
    #r3 = [0, 0, 1, 0]
    #r4 = [0, 0, 0, 1]
    #global orthoMatrix
    #orthoMatrix = Matrix(r1, r2, r3, r4)
    
    global l
    global r
    global t
    global b
    l = left
    r = right
    t = top
    b = bottom

def gtPerspective(fov, near, far):
    global projection
    projection = 1

    fov = radians(fov)
    global k
    k = tan(fov/2.0)

def gtBeginShape():
    global aList
    aList = []

def gtEndShape():
    global aList
    i = 0
    j = 1
    for k in range(len(aList)/2):
        x1 = aList[i].getX()
        y1 = aList[i].getY()
        
        x2 = aList[j].getX()
        y2 = aList[j].getY()
        
        line(x1, y1, x2, y2)
        
        i += 2
        j += 2

def gtVertex(x, y, z):
    global aList
    aVertex = Vertex(x, y, z, 1)
    
    ctm = gtGetMatrix()
    aVertex = aVertex.multiplyTrans(ctm)
    
    #apply ortho or persp using equations from class
    if (projection == 0):
        global l
        global r
        global t
        global b
        
        x = aVertex.getX()
        y = aVertex.getY()
        z = aVertex.getZ()
        
        x1 = (800.0/(r-l)) * (x-l)
        y1 = (800.0/(t-b)) * (y-b)
        
        aVertex.setX(x1)
        aVertex.setY(y1)
        
        oldY = aVertex.getY()
        oldY = 800.0 - oldY
        aVertex.setY(oldY)
        
    elif (projection == 1):
        global k
        
        x = aVertex.getX()
        y = aVertex.getY()
        z = aVertex.getZ()
        
        x1 = float(x) / abs(z)
        y1 = float(y) / abs(z)
        x2 = (x1 + k) * (800.0 / (2*k))
        y2 = (y1 + k) * (800.0 / (2*k))
        
        y2 = 800.0 - y2
        
        aVertex.setX(x2)
        aVertex.setY(y2)
    
    aList.append(aVertex)