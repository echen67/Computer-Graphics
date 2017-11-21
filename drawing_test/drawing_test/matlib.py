# Matrix Stack Library -- Use your code from Project 1A

#Emily Chen

#Using a list as a stack and the var top to keep track of the last matrix added
aStack = []
top = 0

class Matrix():
    def __init__(self, r1, r2, r3, r4):    #r1 etc are the rows of the matrix
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
        
    def matrixPrint(self):
        print(self.r1)    
        print(self.r2)
        print(self.r3)
        print(self.r4)
        
    def matrixMult(self, other):
        dotProd = 0
        newMatrix = Matrix([1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1])
        for k in range(1,5):
            for j in range(1,5):
                dotProd = 0
                for i in range(1,5):
                    a = self.matrixGet(j,i)
                    b = other.matrixGet(i,k)
                    dotProd += (a*b)
                    newMatrix.matrixSet(j,k,dotProd)
        return newMatrix
    
    #row and col should be thought in of regular terms, not zero-indexed
    def matrixGet(self, row, col):
        if row == 1:
            return self.r1[col-1]
        elif row == 2:
            return self.r2[col-1]
        elif row == 3:
            return self.r3[col-1]
        elif row == 4:
            return self.r4[col-1]
        
    def matrixSet(self, row, col, item):
        if row == 1:
            self.r1[col-1] = item
        elif row == 2:
            self.r2[col-1] = item
        elif row == 3:
            self.r3[col-1] = item
        elif row == 4:
            self.r4[col-1] = item
            
    def matrixCopy(self):
        new = Matrix(self.r1, self.r2, self.r3, self.r4)
        return new

def gtInitialize():
    global aStack
    global top
    aStack = []
    top = 0
    aMatrix = Matrix([1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1])
    aStack.append(aMatrix)
    top += 1

def gtPushMatrix():
    global aStack
    global top
    oldctm = aStack[top-1]
    duplicate = oldctm.matrixCopy()
    aStack.append(duplicate)
    top += 1

def gtPopMatrix():
    global top
    if top == 1:
        print("Error: There is only one matrix on the stack; cannot pop it off")
    aStack.pop()
    top -= 1

def gtTranslate(x, y, z):
    global aStack
    global top
    translateMatrix = Matrix([1,0,0,x], [0,1,0,y], [0,0,1,z], [0,0,0,1])
    oldctm = aStack[top-1]
    newctm = oldctm.matrixMult(translateMatrix)
    aStack[top-1] = newctm

def gtScale(x, y, z):
    global aStack
    global top
    scaleMatrix = Matrix([x,0,0,0], [0,y,0,0], [0,0,z,0], [0,0,0,1])
    oldctm = aStack[top-1]
    newctm = oldctm.matrixMult(scaleMatrix)
    aStack[top-1] = newctm

def gtRotateX(theta):
    global aStack
    global top
    theta = radians(theta)
    rotationMatrix = Matrix([1,0,0,0], [0,cos(theta),-sin(theta),0], [0,sin(theta),cos(theta),0], [0,0,0,1])
    oldctm = aStack[top-1]
    newctm = oldctm.matrixMult(rotationMatrix)
    aStack[top-1] = newctm

def gtRotateY(theta):
    global aStack
    global top
    theta = radians(theta)
    rotationMatrix = Matrix([cos(theta),0,sin(theta),0], [0,1,0,0], [-sin(theta),0,cos(theta),0], [0,0,0,1])
    oldctm = aStack[top-1]
    newctm = oldctm.matrixMult(rotationMatrix)
    aStack[top-1] = newctm

def gtRotateZ(theta):
    global aStack
    global top
    theta = radians(theta)
    rotationMatrix = Matrix([cos(theta),-sin(theta),0,0], [sin(theta),cos(theta),0,0], [0,0,1,0], [0,0,0,1])
    oldctm = aStack[top-1]
    newctm = oldctm.matrixMult(rotationMatrix)
    aStack[top-1] = newctm
    
def gtGetMatrix():
    return aStack[top-1]