import turtle
import random

t = turtle.Turtle()

def printTriangleBorder(point1, point2, point3):
    t.up()
    t.goto(point1[0], point1[1])
    t.down()
    t.dot(10)

    t.up()
    t.goto(point2[0], point2[1])
    t.down()
    t.dot(10)

    t.up()
    t.goto(point3[0], point3[1])
    t.down()
    t.dot(10)

def makeFractal(point1, point2, point3):
    randomStartX = random.randint(-500, 500)
    randomStartY = random.randint(-500, 500)
    randomStart = [randomStartX, randomStartY]

    if (not isInside(point1, point2, point3, randomStart)):
        randomStartX = random.randint(-500, 500)
        randomStartY = random.randint(-500, 500)
        randomStart = [randomStartX, randomStartY]

    # make a point a random distance between randomStart and a random vertex, calling it
    # lastPoint
    randomStartVertex = random.randint(0, 2)
    if (randomStartVertex == 0):
        lastPoint = midpoint(randomStart, point1)
    if (randomStartVertex == 1):
        lastPoint = midpoint(randomStart, point2)
    if (randomStartVertex == 2):
        lastPoint = midpoint(randomStart, point3)

    # draw first point
    t.up()
    t.goto(lastPoint[0], lastPoint[1])
    t.down()
    t.dot(10)

    for i in range(0, 100):
        randomVertex = random.randint(0, 2)
        if (randomVertex == 0):
            # make a point a random distance between lastPoint and vertex1
            lastPoint = midpoint(randomStart, point1)
            t.up()
            t.goto(lastPoint[0], lastPoint[1])
            t.down()
            t.dot(10)
        if (randomVertex == 1):
            # make a point a random distance between lastPoint and vertex2
            lastPoint = midpoint(randomStart, point2)
            t.up()
            t.goto(lastPoint[0], lastPoint[1])
            t.down()
            t.dot(10)
        if (randomVertex == 2):
            # make a point a random distance between lastPoint and vertex3
            lastPoint = midpoint(randomStart, point3)
            t.up()
            t.goto(lastPoint[0], lastPoint[1])
            t.down()
            t.dot(10)

        turtle.done()

def midpoint(point1, point2):
    newPoint = []
    newPoint[0] = (point1[0] + point2[0]) / 2
    newPoint[1] = (point1[1] + point2[1]) / 2
    return newPoint
def area(point1, point2, point3):
    return abs((point1[0] * (point2[1] - point3[1]) + point2[0] * (point3[1] - point1[1]) + point3[0] * (point1[1] - point2[1])) / 2.0)

def isInside(point1, point2, point3, checkPoint):
    areaTriagle = area(point1, point2, point3)
    areaSubTriangle1 = area(checkPoint, point2, point3)
    areaSubTriangle2 = area(point1, checkPoint, point3)
    areaSubTriangle3 = area(point1, point2, checkPoint)

    if (areaTriagle == areaSubTriangle1 + areaSubTriangle2 + areaSubTriangle3):
        return True
    else:
        return False

def main():
    # border triangle size
    point1 = [0, 500]
    point2 = [-500, -500]
    point3 = [500, -500]

    printTriangleBorder(point1, point2, point3)
    makeFractal(point1, point2, point3)

main()