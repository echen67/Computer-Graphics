# In the routine below, you should draw your initials in perspective

#Emily Chen

from matlib import *
from drawlib import *

def persp_initials():
    gtInitialize()
    gtPerspective(60, -100, 100)
    gtPushMatrix()
    gtTranslate(-.5,-2.5,-10)
    ec2()
    gtPopMatrix()
    
def ec2():
    gtBeginShape()
    
    #E
    gtVertex(-1,0,2)
    gtVertex(0,0,2)
    
    gtVertex(-1,0,2)
    gtVertex(-1,0,1)
    
    gtVertex(-1,0,1)
    gtVertex(0,0,1)
    
    gtVertex(-1,0,1)
    gtVertex(-1,0,0)
    
    gtVertex(-1,0,0)
    gtVertex(0,0,0)
    
    #C
    gtVertex(1,0,2)
    gtVertex(2,0,2)
    
    gtVertex(1,0,2)
    gtVertex(1,0,0)
    
    gtVertex(1,0,0)
    gtVertex(2,0,0)
    
    gtEndShape()
    
def ec():
    gtBeginShape()
    
    #E top
    gtVertex(-2,5,1)
    gtVertex(0,5,1)
    
    gtVertex(0,5,1)
    gtVertex(0,4,1)
    
    gtVertex(0,4,1)
    gtVertex(-1,4,1)
    
    gtVertex(-1,4,1)
    gtVertex(-1,3,1)
    
    gtVertex(-1,3,1)
    gtVertex(0,3,1)
    
    gtVertex(0,3,1)
    gtVertex(0,2,1)
    
    gtVertex(0,2,1)
    gtVertex(-1,2,1)
    
    gtVertex(-1,2,1)
    gtVertex(-1,1,1)
    
    gtVertex(-1,1,1)
    gtVertex(0,1,1)
    
    gtVertex(0,1,1)
    gtVertex(0,0,1)
    
    gtVertex(0,0,1)
    gtVertex(-2,0,1)
    
    gtVertex(-2,0,1)
    gtVertex(-2,5,1)
    
    #E bottom
    gtVertex(-2,5,-1)
    gtVertex(0,5,-1)
    
    gtVertex(0,5,-1)
    gtVertex(0,4,-1)
    
    gtVertex(0,4,-1)
    gtVertex(-1,4,-1)
    
    gtVertex(-1,4,-1)
    gtVertex(-1,3,-1)
    
    gtVertex(-1,3,-1)
    gtVertex(0,3,-1)
    
    gtVertex(0,3,-1)
    gtVertex(0,2,-1)
    
    gtVertex(0,2,-1)
    gtVertex(-1,2,-1)
    
    gtVertex(-1,2,-1)
    gtVertex(-1,1,-1)
    
    gtVertex(-1,1,-1)
    gtVertex(0,1,-1)
    
    gtVertex(0,1,-1)
    gtVertex(0,0,-1)
    
    gtVertex(0,0,-1)
    gtVertex(-2,0,-1)
    
    gtVertex(-2,0,-1)
    gtVertex(-2,5,-1)
    
    #E connections
    gtVertex(-2,5,1)
    gtVertex(-2,5,-1)
    
    gtVertex(0,5,1)
    gtVertex(0,5,-1)
    
    gtVertex(0,4,1)
    gtVertex(0,4,-1)
    
    gtVertex(-1,4,1)
    gtVertex(-1,4,-1)
    
    gtVertex(-1,3,1)
    gtVertex(-1,3,-1)
    
    gtVertex(0,3,1)
    gtVertex(0,3,-1)
    
    gtVertex(0,2,1)
    gtVertex(0,2,-1)
    
    gtVertex(-1,2,1)
    gtVertex(-1,2,-1)
    
    gtVertex(-1,1,1)
    gtVertex(-1,1,-1)
    
    gtVertex(0,1,1)
    gtVertex(0,1,-1)
    
    gtVertex(0,0,1)
    gtVertex(0,0,-1)
    
    gtVertex(-2,0,1)
    gtVertex(-2,0,-1)
    
    #C top
    gtVertex(1,5,1)
    gtVertex(3,5,1)
    
    gtVertex(3,5,1)
    gtVertex(3,4,1)
    
    gtVertex(3,4,1)
    gtVertex(2,4,1)
    
    gtVertex(2,4,1)
    gtVertex(2,1,1)
    
    gtVertex(2,1,1)
    gtVertex(3,1,1)
    
    gtVertex(3,1,1)
    gtVertex(3,0,1)
    
    gtVertex(3,0,1)
    gtVertex(1,0,1)
    
    gtVertex(1,0,1)
    gtVertex(1,5,1)
    
    #C bottom
    gtVertex(1,5,-1)
    gtVertex(3,5,-1)
    
    gtVertex(3,5,-1)
    gtVertex(3,4,-1)
    
    gtVertex(3,4,-1)
    gtVertex(2,4,-1)
    
    gtVertex(2,4,-1)
    gtVertex(2,1,-1)
    
    gtVertex(2,1,-1)
    gtVertex(3,1,-1)
    
    gtVertex(3,1,-1)
    gtVertex(3,0,-1)
    
    gtVertex(3,0,-1)
    gtVertex(1,0,-1)
    
    gtVertex(1,0,-1)
    gtVertex(1,5,-1)
    
    #C connections
    gtVertex(1,5,1)
    gtVertex(1,5,-1)
    
    gtVertex(3,5,1)
    gtVertex(3,5,-1)
    
    gtVertex(3,4,1)
    gtVertex(3,4,-1)
    
    gtVertex(2,4,1)
    gtVertex(2,4,-1)
    
    gtVertex(2,1,1)
    gtVertex(2,1,-1)
    
    gtVertex(3,1,1)
    gtVertex(3,1,-1)
    
    gtVertex(3,0,1)
    gtVertex(3,0,-1)
    
    gtVertex(1,0,1)
    gtVertex(1,0,-1)
    
    gtEndShape()