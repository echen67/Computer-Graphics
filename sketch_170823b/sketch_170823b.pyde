calList = []

def setup():
  size(500,500)

def draw():
    background(255,255,255)
    global calList
    calList = [(0,0), (1,0)]
    amount = 10
    calculate(amount)
    drawFractal(amount)

def calculate(power):
    global calList
    real = (mouseX * (4.0/500)) - 2
    imag = (mouseY * (4.0/500)) - 2
    if power == 1:
        calList.append((real,imag))
        return (real,imag)
    else:
        prev = calculate(power-1)
        prevR = prev[0]
        prevI = prev[1]
        finalR = (prevR * real) - (prevI * imag)
        finalI = (prevR * imag) + (prevI * real)
        calList.append((finalR, finalI))
        return (finalR, finalI)
    return

def drawFractal(power):        
    global calList
    if power == 0:
        r = calList[1][0]
        i = calList[1][1]
        pointList = [(r,i),(-r,-i)]
        for j in range(len(pointList)):
            x = pointList[j][0]
            y = pointList[j][1]
            ellipse((x+2)*(500.0/4), (y+2)*(500.0/4), 1, 1)
        return pointList
    else:
        prevList = drawFractal(power-1)
        r = calList[power+1][0]
        i = calList[power+1][1]
        pointList = []
        for j in range(len(prevList)):            
            pr = prevList[j][0]
            pi = prevList[j][1]
            x = pr + r
            y = pi + i
            pointList.append((x,y))
            fill(255,0,0)
            stroke(255,0,0)
            ellipse((x+3)*(500.0/6), (y+3)*(500.0/6), 1, 1)
            x = pr - r
            y = pi - i
            pointList.append((x,y))
            fill(0,0,255)
            stroke(0,0,255)
            ellipse((x+3)*(500.0/6), (y+3)*(500.0/6), 1, 1)
        return pointList
    return