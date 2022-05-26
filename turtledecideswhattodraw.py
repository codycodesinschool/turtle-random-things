import turtle,random
turtle.speed(0)

colorsfile = open("colors.txt","r")
colorslines = colorsfile.read().split(" ")
colors = []
for color in colorslines:
    linecolors = color.split("\n")
    for linecolor in linecolors:
        colors.append(linecolor)
colorsfile.close()

def save():
    cv = turtle.getcanvas()
    cv.postscript(file="auto_drawing_" + str(random.randint(111111,999999)) + ".ps", colormode='color')


while True:
    thing = random.randint(0,10)
    if thing == 0:
        turtle.forward(random.uniform(0,500))
        print("fd")
    elif thing == 1:
        turtle.backward(random.uniform(0,500))
        print("bw")
    elif thing == 2:
        turtle.right(random.uniform(0,180))
        print("rt")
    elif thing == 3:
        turtle.left(random.uniform(0,180))
        print("lt")
    elif thing == 4:
        c = random.choice(colors)
        turtle.color(c)
        print("cr")
    elif thing == 5:
        c = random.choice(colors)
        turtle.bgcolor(c)
        print("bg")
    elif thing == 6:
        turtle.pensize(random.uniform(0,50))
        print("ps")
    elif thing == 7:
        turtle.home()
        print("hm")
    elif thing == 8:
        turtle.begin_fill()
        print("bf")
    elif thing == 9:
        turtle.end_fill()
        print("ef")
    elif thing == 10:
        if random.uniform(0,1) < 0.1:
            save()
            print("DONE")
            break
turtle.done()
