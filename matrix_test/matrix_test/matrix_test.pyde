# Matrix Commands

from matrix_stack import *

def setup():
    size (100, 100)
    background (255, 255, 255)
    mat_test()
    #deleteMe()

def deleteMe():
    #gtInitialize()
    #print_ctm()
    
    #m1 = Matrix([3,6,2,5], [3,7,6,1], [1,9,3,2], [1,8,7,9])
    #m2 = Matrix([1,9,6,9], [2,3,7,1], [4,7,4,2], [8,7,4,7])
    #m3 = m1.matrixMult(m2)
    #m3.matrixPrint()
    
    gtInitialize()
    #print_ctm()
    gtScale(2,3,4)
    print_ctm()
    return

# this routine tests the matrix stack command that you will implement
def mat_test():
    
    gtInitialize()
    print_ctm()
    
    gtInitialize()
    gtTranslate(3,2,1.5)
    print_ctm()

    gtInitialize()
    gtScale(2,3,4)
    print_ctm()

    gtInitialize()
    gtRotateX(90)
    print_ctm()

    gtInitialize()
    gtRotateY(-15)
    print_ctm()

    gtInitialize()
    gtPushMatrix()
    gtRotateZ(45)
    print_ctm()
    gtPopMatrix()
    print_ctm()

    gtInitialize()
    gtTranslate(1.5,2.5,3.5)
    gtScale(2,2,2)
    print_ctm()

    gtInitialize()
    gtScale(2,2,2)
    gtTranslate(1.5,2.5,3.5)
    print_ctm()

    gtInitialize()
    gtScale(2,2,2)
    gtPushMatrix()
    gtTranslate(1.5,2.5,3.5)
    print_ctm()
    gtPopMatrix()
    print_ctm()

    gtInitialize()
    gtPopMatrix()

def draw():
    pass