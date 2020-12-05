#################################################
# TP2 Code.py
#
# Your name: Yi Sijun Cathy
# Your andrew id: sijuncay
#################################################


#downloaded from CMU 15-112 website
import cs112_f20_week7_linter
import math, copy, random, string
#from other TP files of mine
from Usefulwords import *
from EntryAnalysis import *
#from perspective import *
#import perspective 
import EntryAnalysis
import Usefulwords

#downloaded from CMU 15-112 website
from cmu_112_graphics import *

''' add this quote as a splash page after TP2? '''
# “Life moves pretty fast. If you don’t stop and look around 
#  once in a while, you could miss it.”
#                                             Ferris Bueller

#from 112 course notes 
#https://www.cs.cmu.edu/~112/notes/notes-graphics.html
#creates custom colors
def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

#from 112 website: 
#https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html#creating2dLists
#makes 2d lists
def make2dList(rows, cols, string):
    emptyColor = string
    return [ ([emptyColor] * cols) for row in range(rows) ]

def appStarted(app):
    app.mode = 'main'
    app.dayEntry = ['']
    app.maxLineLength = 100
    app.letterPosition = [app.height/8*2 + 20]
    app.textY = (app.height/8)*2 - app.height/50
    app.lineY = (app.height/8)*2
    app.lineMoveCount = 0
    app.dLine = 5
    app.moveTextAndLine = False
    app.textDict = {}
    app.yearChartX, app.yearChartY = app.width/5, app.height/3
    #from CMU course notes about drawing a grid:
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
    #I modified the parameters
    app.rows = 3
    app.cols = 4
    app.margin = 100 # margin around grid
    app.selection = (-1, -1) # (row, col) of selection, (-1,-1) for none
    ### Circle
    app.hDistCovered = 0
    app.hR, app.hFrameCircum = app.height/2, app.width
    app.hTotalCircum = 2*math.pi*app.hR*8
    app.hTotalArea = math.pi * (app.hR)**2
    ###
    app.cxSun, app.cySun, app.rSun = (app.width/2, 
                                app.height/2, app.width/10)
    app.dMove = 150
    app.dragging = False
    app.getX = 0
    app.getY = 0
    app.x1,app.y1,app.x2,app.y2,app.x3,app.y3,app.x4,app.y4 = (
                        app.width/2 - 40,
                        app.height/2+2.5, 
                        app.width/5,
                        app.height, 
                        app.width - app.width/5, 
                        app.height,
                        app.width/2 + 40, 
                        app.height/2+2.5)
    app.bx1,app.by1,app.bx2,app.by2,app.bx3,app.by3,app.bx4,app.by4 = (
                        -app.width,
                        app.height/2+2.5, 
                        app.width/5,
                        app.height, 
                        app.width - app.width/5, 
                        app.height,
                        -app.width + 80, 
                        app.height/2+2.5)
    app.povLeft = app.width
    app.backPath = False


def resetAll(app):
    app.mode = 'main'
    app.dayEntry = ['']
    app.maxLineLength = 100
    app.letterPosition = [app.height/8*2 + 20]
    app.textY = (app.height/8)*2 - app.height/50
    app.lineY = (app.height/8)*2
    app.lineMoveCount = 0
    app.dLine = 5
    app.moveTextAndLine = False
    app.textDict = {}
    app.yearChartX, app.yearChartY = app.width/5, app.height/3
    #from CMU course notes about drawing a grid:
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
    #I modified the parameters
    app.rows = 3
    app.cols = 4
    app.margin = 100 # margin around grid
    app.selection = (-1, -1) # (row, col) of selection, (-1,-1) for none
    ### Circle
    app.hDistCovered = 0
    app.hR, app.hFrameCircum = app.height/2, app.width
    app.hTotalCircum = 2*math.pi*app.hR
    app.hTotalArea = math.pi * (app.hR)**2
    ###
    app.cxSun, app.cySun, app.rSun = (app.width/2, 
                                app.height/2, app.width/10)
    app.dMove = 150
    app.dragging = False
    app.getX = 0
    app.getY = 0
    app.x1,app.y1,app.x2,app.y2,app.x3,app.y3,app.x4,app.y4 = (
                        app.width/2 - 40,
                        app.height/2+2.5, 
                        app.width/5,
                        app.height, 
                        app.width - app.width/5, 
                        app.height,
                        app.width/2 + 40, 
                        app.height/2+2.5)
    app.bx1,app.by1,app.bx2,app.by2,app.bx3,app.by3,app.bx4,app.by4 = (
                        -app.width,
                        app.height/2+2.5, 
                        app.width/5,
                        app.height, 
                        -app.width - app.width/5, 
                        app.height,
                        app.width/2 + 40, 
                        app.height/2+2.5)


def keyPressed(app, event):
    if event.key == 'Tab':
        resetAll(app)
    if app.mode == 'main':
        #enter year mode
        if event.key == 'Enter':
            app.mode = 'year'
        #enter week mode
        elif event.key == 'w':
            app.mode = 'week'
        elif event.key == 'd':
            app.mode = 'day'
    elif app.mode == 'day':
        #enter main mode
        if event.key == 'Enter':
            app.mode = 'main'
        #if current text string is too long/exceeds length of underline
        if len(app.dayEntry[-1]) >= app.maxLineLength:
            #create new empty string
            app.dayEntry += ['']
            app.moveTextAndLine = True
        if event.key == 'Space':
            app.dayEntry[-1] += ' '
        elif event.key == 'Delete':
            app.dayEntry[-1] = app.dayEntry[-1][:-1]
        elif event.key in string.printable:
            app.dayEntry[-1] += event.key
'''       
def oneDayMoodAnalysis(app,canvas,day):
    for word in app.dayEntry:
        if word in happyWords:
            addHappyWord(day)
        elif word in sadWords:
            addSadWord(day)
        elif word in angryWords:
            addAngryWord(day)
def drawWeeklyAnalysisText(app,canvas,day):
    text = day.printAnalysis()
    canvas.create_text(app.width/2, app.height/2, text = text)
    '''

def timerFired(app):
    #moves text and line downwards at the same pace until a new line is reached
    if app.moveTextAndLine == True:
        app.lineY += app.dLine
        app.textY += app.dLine
        app.lineMoveCount += 1
    if app.lineMoveCount >= 40/app.dLine:
        app.moveTextAndLine = False
        app.lineMoveCount = 0
    if app.mode == 'year':
        if ((app.yearChartX <= app.width - 50) and
                (app.yearChartY <= app.height - 50)):
            app.yearChartX += 42
            app.yearChartY += 20
    #if app.mode == 'weekly summary':
        #oneDayMoodAnalysis(app,today)

def mouseDragged(app, event):
    app.dragging = True
    '''
    if app.cxSun == app.width/2 + app.hTotalCircum/4:
        app.x1,app.y1,app.x2,app.y2 = -1,-1,-1,-1
        print(app.cxSun)
        '''
    #how much the cursor is dragged in x-direction
    #positive or negative
    xdiff = app.getX - event.x
    #first quadrant:
    app.povLeft -= xdiff
    if (app.povLeft <= app.width and 
                app.povLeft > app.width - app.hTotalCircum/4):
        if event.x <= app.getX:
            #position of sun
            app.cxSun += xdiff
            app.cxSun %= app.hTotalCircum
        #TRAPEZIUM OF PATH
            #shift angles
            app.x1 += xdiff
            app.x4 += xdiff
            app.x1 %= app.hTotalCircum
            app.x4 %= app.hTotalCircum
            #shift x
            if (app.povLeft < app.width - app.hTotalCircum/5 and 
                    app.povLeft > app.width - app.hTotalCircum/4.5):
                app.x2 += xdiff
                app.x3 += xdiff
            app.x2 += xdiff*1/8
            app.x3 += xdiff*1/8
            app.x2 %= app.hTotalCircum
            app.x3 %= app.hTotalCircum
    #second quadrant 
    elif (app.povLeft <= app.width - app.hTotalCircum/4 and 
                app.povLeft > app.width - app.hTotalCircum/2):
        app.backPath = True
        if event.x <= app.getX:
            #position of sun
            app.cxSun = -500
            app.cxSun = -500
        #TRAPEZIUM OF PATH
            #shift angles
            app.bx1 += xdiff
            app.bx4 += xdiff
            app.bx1 %= app.hTotalCircum
            app.bx4 %= app.hTotalCircum
            #shift x
            if (app.povLeft < app.width - app.hTotalCircum/5 and 
                    app.povLeft > app.width - app.hTotalCircum/4.5):
                app.bx2 += xdiff*2/3
                app.bx3 += xdiff*2/3
            app.bx2 += xdiff*1/8
            app.bx3 += xdiff*1/8
            app.bx2 %= app.hTotalCircum
            app.bx3 %= app.hTotalCircum
'''
    else:
        app.x1 -= app.dMove
        app.x4 -= app.dMove
        #app.x2 -= app.dMove*4/5
        #app.x3 -= app.dMove*4/5
        app.x1 %= app.hTotalCircum
        app.x4 %= app.hTotalCircum
        #app.x2 %= app.hTotalCircum
        #app.x3 %= app.hTotalCircum
        
        app.cxSun -= app.dMove
        app.cxSun %= app.hTotalCircum
    #if event.x = app.width/2:
        #indication that this is the centre
    '''
'''
        if app.cxSun > app.width/2:
            app.rSun -= 6
        else: 
            app.rSun += 6
        #length of end of path
        if app.cxSun < app.width/2:
            app.x1 -= 5
            app.x4 += 5
        else: 
            app.x1 += 5
            app.x4 -= 5

        if app.cxSun < app.width/2:
            app.rSun -= 6
        else: 
            app.rSun += 6

        if app.cxSun > app.width/2:
            app.x1 -= 5
            app.x4 += 5
        else: 
            app.x1 += 5
            app.x4 -= 5
            '''

def mouseReleased(app,event):
    if app.dragging == False:
        return
    app.dragging = False

def mousePressed(app, event):
    app.getX = event.x
    app.getY = event.y
    if app.mode == 'day':
        if (0 < event.x < app.height/8) and (0 < event.y < app.height/8):
            app.mode = 'weekly summary'
    elif app.mode == 'weekly summary':
        if (0 < event.x < app.height/8) and (0 < event.y < app.height/8):
            app.mode = 'day'
    #DRAW YEAR CHART
    if app.mode == 'main':
        #if click on year chart
        if (50 < event.x < app.width/5) and (50 < event.y < app.height/3):
            app.mode = 'year'
    #canvas.create_rectangle(50, 50, app.width/5, app.height/3, fill = 'white')
        (row, col) = getCell(app, event.x, event.y)
    # select this (row, col) unless it is selected
        if (app.selection == (row, col)):
            app.selection = (-1, -1)
        else:
            app.selection = (row, col)
    '''
    cx, cy = app.width/2, app.height/2
    if ((cx-100 <= event.x <= cx+100) and
        (cy+100 <= event.y <= cy+120)):
        app.mode = 'month'
        '''




def newLine(app, canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill = 'blue', width = 3)

#Day mode: zoom into an entry on a specific day
def drawDayMode(app, canvas):
    margin = app.height/8
    popupColor = 'blanchedAlmond'
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    #draw popup
    canvas.create_rectangle(x1, y1, x2, y2, fill = popupColor)
        #Draw triangle to look like a popup: canvas.create_triangle(app.width/2 - )
    #draw line
        #need to animate line moving down
        #need to animate scrolling if no. of lines exceeds max on a page
    newLine(app, canvas, margin*2, app.lineY, app.width - margin*2, app.lineY)
    #draw text
        #text moves down as text length exceeds line length
    lineSpacing = 40
    textX = app.width/2
    for n in range(len(app.dayEntry[:-1])):
        textY = (app.height/8)*2 - app.height/50 + lineSpacing*n
        canvas.create_text(textX, textY, text = app.dayEntry[n], 
                                    font = 'Arial 20')
    canvas.create_text(textX, app.textY, text = app.dayEntry[-1], 
                                font = 'Arial 20')
    drawDefaultDayText(app, canvas)

#draws the default text:
#1. date
#2. prompt(?)
def drawDefaultDayText(app, canvas):
    textColor = 'black'
    margin = app.height/8
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    canvas.create_text(margin + 130, margin + 20, 
                            text = 'Today: [That day\'s date]', 
                            font = 'Arial 20', fill = textColor)
    canvas.create_text(margin + 300, margin + 20, text = 'time created', 
                            font = 'Arial 15', fill = textColor)
    canvas.create_text(margin + 140, margin + 50, 
                            text = 'How was your day today?', 
                            font = 'Arial 20 bold', fill = textColor)
    #canvas.create_text(200, firstTextY + 100, text = 'major events', 
                            #font = 'Arial 40 underline', fill = textColor)          
    #canvas.create_text(200, firstTextY + 150, text = 'Notes', 
                            #font = 'Arial 40 underline', fill = textColor)    

#Main mode: draw a sunset and a path leading to it
def drawMainMode(app, canvas):
    drawHorizonAndSun(app, canvas)
    drawPath(app, canvas)
    if app.backPath == True:
        drawBackPath(app,canvas)
    drawTrees(app, canvas)
    drawYearChart(app, canvas)

def drawYearChart(app, canvas):
    #DRAW YEAR CHART
    canvas.create_rectangle(50, 50, app.yearChartX, app.yearChartY, 
                            fill = 'white')
    #Draw yearly calendar
    #from CMU course notes about drawing a grid:
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
    #some code is modified
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            fill = "white" if (app.selection == (row, col)) else "white"
            #fill = 'white'
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)
    #canvas.create_text(app.width/2, app.height/2 - 15, text="Click in cells!",
                       #font="Arial 26 bold", fill="darkBlue")

def drawHorizonAndSun(app, canvas):
    drawHorizon(app, canvas)
    drawSun(app, canvas)

def drawHorizon(app, canvas):
    #DRAW SKY and LAND
    canvas.create_rectangle(0, 0, app.width, app.height/2, 
                                    fill = rgbString(255, 185, 30))
    canvas.create_rectangle(0, app.height/2, app.width, app.height, 
                                    fill = 'moccasin')    
    
    #DRAW HORIZON
    canvas.create_line(0, app.height/2, app.width, app.height/2, 
                        width = 5, fill = 'orangeRed')

def drawSun(app, canvas):
        #think of some cool designs!
        #remember to draw shadows for objects on land - to increase realism
        #Add flying birds too! just black birds flapping across the horizon 
        #in the distance
    m1, m2 = app.rSun/16, app.rSun/3.5
    cx, cy, r = app.cxSun, app.cySun, app.rSun
    canvas.create_arc(cx-r-m2, cy-r-m2, cx+r+m2, cy+r+m2, start=0, 
                                extent=180, fill='darkOrange', 
                                outline = 'darkOrange')     
    canvas.create_arc(cx-r-m1, cy-r-m1, cx+r+m1, cy+r+m1, start=0, 
                                extent=180, fill='gold',
                                outline = 'gold')                       
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=0, 
                                extent=180, fill='orangeRed',
                                outline = 'orangeRed') 
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=10, 
                                extent=180-10*2, fill='orange', style='chord',
                                outline = 'orange') 
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=20, 
                                extent=180-20*2, fill='moccasin', style='chord',
                                outline = 'moccasin') 
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=30, 
                                extent=180-30*2, fill='lightYellow', style='chord',
                                outline = 'lightYellow')

#note: change path to be a curved path
#maybe even 3-d, going up and down?
def drawPath(app, canvas):
    #left side
    #canvas.create_line(app.width/2 - 10, app.height/2+2.5, app.width/3.5,
                         #app.height, width = 5, smooth = True)
    #right side
    #canvas.create_line(app.width/2 + 10, app.height/2+2.5, app.width - 
                        #app.width/3.5, app.height, width = 5, smooth = False)
    x1,y1,x2,y2,x3,y3,x4,y4 = (app.x1,app.y1,app.x2,
                         app.y2,app.x3,app.y3,app.x4,app.y4)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill = 'peru')


def drawBackPath(app,canvas):
    x1,y1,x2,y2,x3,y3,x4,y4 = (app.bx1,app.by1,app.bx2,app.by2,app.bx3,
                            app.by3,app.bx4,app.by4)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill = 'peru')



def drawWeeklySummaryButton(app, canvas):
    canvas.create_rectangle(0,0,app.height/8,app.height/8, fill = 'orange')

#idea inspired by Wordle: http://www.wordle.net/create
#idea was brought up in meeting with TP mentor (Elena)



def drawTrees(app,canvas):
    #maybe use recursion to draw a cool design
    pass

#Year mode: year chart at corner(?) of main mode expands to show 
#the progress made in the entire year
def drawYearMode(app, canvas):
    pass
            #if app.mode = 'year':
               # app.isYear = True

#from CMU course notes about drawing a grid:
#https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
#I modified some code such as the parameters and 
#how the graph expands together with the year chart page
def pointInGrid(app, x, y):
    # return True if (x, y) is inside the grid defined by app.
    return ((app.margin <= x <= app.width-app.margin) and
            (app.margin <= y <= app.height-app.margin))

def getCell(app, x, y):
    # aka "viewToModel"
    # return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
    if (not pointInGrid(app, x, y)):
        return (-1, -1)
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows

    # Note: we have to use int() here and not just // because
    # row and col cannot be floats and if any of x, y, app.margin,
    # cellWidth or cellHeight are floats, // would still produce floats.
    row = int((y - app.margin) / cellHeight)
    col = int((x - app.margin) / cellWidth)

    return (row, col)

def getCellBounds(app, row, col):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.yearChartX - 2*app.margin
    gridHeight = app.yearChartY - 2*app.margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin + row * cellHeight
    y1 = app.margin + (row+1) * cellHeight
    return (x0, y0, x1, y1)


def redrawAll(app, canvas):
    if app.mode == 'day':
        drawDayMode(app, canvas)
        drawWeeklySummaryButton(app, canvas)
    if app.mode == 'weekly summary':
        drawWeeklySummary(app, canvas)
        drawWeeklySummaryButton(app, canvas)
    elif app.mode == 'main':
        drawMainMode(app, canvas)
    elif app.mode == 'year':
        drawMainMode(app, canvas)
        drawYearMode(app, canvas)


runApp(width=1400, height=800)