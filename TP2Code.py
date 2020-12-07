#################################################
# TP2Code.py
#
# Your name: Yi Sijun Cathy
# Your andrew id: sijuncay
#################################################


#downloaded from CMU 15-112 website
import cs112_f20_week7_linter
import math, copy, random, string, calendar
from datetime import datetime
#from other TP files of mine
from Usefulwords import *
from EntryAnalysis import *
from wordcloud import *
from fileFunctions import *
#from perspective import *
#import perspective 
import EntryAnalysis
import Usefulwords

#downloaded from CMU 15-112 website
from cmu_112_graphics import *

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
    app.dayNames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
                'Saturday', 'Sunday']
    app.weekDates = getWeek()
    app.currentDay = str(datetime.datetime.now().date())
    app.currentDayName = calendar.day_name[datetime.datetime.now().date().weekday()]
    app.index = app.weekDates.index(app.currentDay)
    app.maxLineLength = 100
    app.fileContents = readFile(f'Entries/{app.currentDay}-text.txt')
    app.dayEntry = splitString(app,app.fileContents)
    app.letterPosition = [app.height/8*2 + 20]
    app.textY = (app.height/8)*2 - app.height/50
    app.lineY = (app.height/8)*2
    app.lineMoveCount = 0
    app.dLine = 5
    app.moveTextAndLine = False
    app.textDict = {}
    app.yearChartX, app.yearChartY = app.width/5, app.height/3
    app.rows = 3
    app.cols = 4
    app.margin = 100 # margin around grid
    app.selection = (-1, -1) # (row, col) of selection, (-1,-1) for none
    ### Circle
    app.hDistCovered = 0
    app.hR, app.hFrameCircum = app.height/2, app.width
    app.hTotalCircum = 2*math.pi*app.hR*10
    app.hTotalArea = math.pi * (app.hR)**2
    ###
    app.cxSun, app.cySun, app.rSun = (app.width/2, app.height/2, app.width/10)
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
                        -app.width*3, #x
                        app.height/2+2.5, 
                        -900, #x
                        app.height, 
                        -900  + app.width*3/5, #x
                        app.height,
                        -app.width*3 + 80, #x
                        app.height/2+2.5)
    app.povLeft = app.width
    app.backPath = False
    app.theta = 0
    app.mainCentred = True
    app.timeLastSaved = ['Not saved yet']*7

def resetAll(app):
    app.mode = 'daily summary'
    app.dayNames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
                'Saturday', 'Sunday']
    app.weekDates = getWeek()
    #app.weekDates = createDayObjectsInWeek()
    app.currentDay = str(datetime.datetime.now().date())
    app.currentDayName = calendar.day_name[datetime.datetime.now().date().weekday()]
    app.index = app.weekDates.index(app.currentDay)
    #print(f'{app.currentDay}-text.txt')
    app.maxLineLength = 20
    app.fileContents = readFile(f'Entries/{app.currentDay}-text.txt')
    app.dayEntry = splitString(app,app.fileContents)
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
    app.hTotalCircum = 2*math.pi*app.hR*10
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
                        -app.width*3, #x
                        app.height/2+2.5, 
                        -900, #x
                        app.height, 
                        -900  + app.width*3/5, #x
                        app.height,
                        -app.width*3 + 80, #x
                        app.height/2+2.5)
    app.povLeft = app.width
    app.backPath = False
    app.theta = 0
    app.mainCentred = True
    app.timeLastSaved = ['Not saved yet']*7

#splits a long string into short strings of equal lengths
def splitString(app,string):
    string = string
    listOfStrings = []
    while len(string) >= app.maxLineLength:
        listOfStrings += [string[:app.maxLineLength]]
        string = string[app.maxLineLength:]
    listOfStrings += [string]
    return listOfStrings

#joins short strings into a long string
def listToString(app,list):
    lst = ''
    for string in list:
        lst += string
    return lst

def keyPressed(app, event):
    if event.key == 'Tab':
        resetAll(app)
    if app.mode == 'main':
        if event.key == 'Space':
            app.mode = 'weekly summary'
        #moving from one day to another    
        elif event.key == 'Up':
            if (app.index >= 0) and (app.index <= len(app.weekDates)-2):
                app.index += 1
                app.currentDayName = app.dayNames[app.index]
                app.currentDay = app.weekDates[app.index]
                app.fileContents = readFile(f'Entries/{app.currentDay}-text.txt')
                app.dayEntry = splitString(app,app.fileContents)
                #sun gets bigger
                app.rSun += 20
        elif event.key == 'Down':
            if (app.index >= 1) and (app.index <= len(app.weekDates)-1):
                app.index -= 1
                app.currentDayName = app.dayNames[app.index]
                app.currentDay = app.weekDates[app.index]
                app.fileContents = readFile(f'Entries/{app.currentDay}-text.txt')
                app.dayEntry = splitString(app,app.fileContents)
                #sun gets smaller
                app.rSun += -20
    elif app.mode == 'day':
        #enter main mode
        if event.key == 'Enter':
            app.timeLastSaved[app.index] = app.currentDay + ' ' + str(datetime.datetime.now().time())[:5]
            app.mode = 'main'
            saveFile(app)
        #if current text string is too long/exceeds length of underline
        if len(app.dayEntry[-1]) >= app.maxLineLength:
            #creates new empty string
            app.dayEntry += ['']
            app.moveTextAndLine = True
        if event.key == 'Space':
            app.dayEntry[-1] += ' '
        elif event.key == 'Delete':
            #if entry is empty
            if app.dayEntry[0] == '':
                pass
            else:
                #if last string is empty, delete from second-last string
                if app.dayEntry[-1] == '':
                    app.dayEntry[-2] = app.dayEntry[-2][:-1]
                # if last string is not empty, delete from last string
                app.dayEntry[-1] = app.dayEntry[-1][:-1]
        elif event.key in string.printable:
            app.dayEntry[-1] += event.key
    elif app.mode == 'daily summary':
        if event.key == 'Enter':
            app.mode = 'main'
    elif app.mode == 'weekly summary':
        if event.key == 'Enter':
            app.mode = 'main'

#replaces content in file with content written in entry using a long string
def saveFile(app):
    contents = listToString(app,app.dayEntry)
    writeFile(f'Entries/{app.currentDay}-text.txt',contents)

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
        #year chart expands when clicked
        if ((app.yearChartX <= app.width - 50) and
                (app.yearChartY <= app.height - 50)):
            app.yearChartX += 50
            app.yearChartY += 25
    if app.mode == 'main':
        #year chart shrinks when clicked
        if ((app.yearChartX >= app.width/5) and
                (app.yearChartY >= app.height/3)):
            app.yearChartX -= 50
            app.yearChartY -= 25


def mouseDragged(app, event):
    app.dragging = True
    if ((app.x1,app.y1,app.x2,app.y2,app.x3,app.y3,app.x4,app.y4 == (app.width/2 - 40,
                        app.height/2+2.5, 
                        app.width/5,
                        app.height, 
                        app.width - app.width/5, 
                        app.height,
                        app.width/2 + 40, 
                        app.height/2+2.5))):
        app.mainCentred = True
    app.mainCentred = False
    
    #how much the cursor is dragged in x-direction
    #positive or negative
    xdiff = (app.getX - event.x)
    app.theta += xdiff/app.hTotalCircum * (math.pi*2)
    app.theta %= 2*math.pi
    #first quadrant:
    #app.povLeft %= app.hTotalCircum
    app.cxSun -= xdiff
    if ((app.theta >= 0 and app.theta < math.pi/2) 
        or (app.theta >= math.pi*3/2 and app.theta < math.pi*2)):
        app.backPath = False
        #app.cxSun -= xdiff
        #app.cxSun %= app.hTotalCircum
        #TRAPEZIUM OF PATH
            #shift angles
        app.x1 -= xdiff
        app.x4 -= xdiff
            #app.x1 %= app.hTotalCircum
            #app.x4 %= app.hTotalCircum
            #shift x
        #if (app.povLeft < app.width - app.hTotalCircum/5 and 
                #app.povLeft > app.width - app.hTotalCircum/4):
            #app.x2 -= xdiff*8
            #app.x3 -= xdiff*8
        app.x2 -= xdiff*1/4
        app.x3 -= xdiff*1/4
            #app.x2 %= app.hTotalCircum
            #app.x3 %= app.hTotalCircum
    #second quadrant 
    if (app.theta >= math.pi/2 and app.theta < math.pi*3/2):
        app.backPath = True
        #app.cxSun -= xdiff
        #TRAPEZIUM OF PATH
            #shift angles
        app.x1 -= xdiff
        app.x4 -= xdiff
        app.bx1 -= xdiff
        app.bx4 -= xdiff
            #app.bx1 %= app.hTotalCircum
            #app.bx4 %= app.hTotalCircum
            #shift x
        #if (app.povLeft < app.width - app.hTotalCircum*0.6 and 
                    #app.povLeft > app.width - app.hTotalCircum*3/4):
                #app.bx2 -= xdiff*8
                #app.bx3 -= xdiff*8
        # (app.povLeft <= app.width - app.hTotalCircum/4 and 
                    #app.povLeft > app.width - app.hTotalCircum/4.5):
                #app.bx2 -= xdiff*8
                #app.bx3 -= xdiff*8
        app.x2 -= xdiff*1/4
        app.x3 -= xdiff*1/4
        app.bx2 -= xdiff*1/4
        app.bx3 -= xdiff*1/4
            #app.bx2 %= app.hTotalCircum
            #app.bx3 %= app.hTotalCircum
    #elif (app.povLeft <= app.width - app.hTotalCircum/4 and 
                #app.povLeft > app.width - app.hTotalCircum*3/4):
        #app.backPath = False

def mouseReleased(app,event):
    app.dragging = False

def mousePressed(app, event):
    if app.mode == 'splash':
        app.mode = 'main'
    app.getX = event.x
    app.getY = event.y
    margin = app.height/8
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    #x2-100,y1,x2,y1+100
    if app.mode == 'day':
        if (x2-100 < event.x < x2) and (y1 < event.y < y1+100):
            app.mode = 'daily summary'
    elif app.mode == 'daily summary':
        if (x2-100 < event.x < x2) and (y1 < event.y < y1+100):
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
        if app.mainCentred == True:
            #app.x1*10/11,app.y1*5/3,app.x2+200, app.y2,app.x3-400,app.y3,app.x4*12/11,app.y4*5/3)
            if (app.x2+200 < event.x < app.x3-400) and (app.y1*5/3 < event.y < app.y3):
                app.mode = 'day'
    if app.mode == 'year':
        if (app.width/5 < event.x < app.width - 50) and (app.height/3 < event.y < app.height - 50):
            app.mode = 'main'

# draws the line under the text
def newLine(app, canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill = 'blue', width = 3)

#Day mode: zoom into an entry on a specific day
def drawDayMode(app, canvas):
    margin = app.height/8
    popupColor = 'blanchedAlmond'
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    #draw popup
    canvas.create_rectangle(x1, y1, x2, y2, fill = popupColor)
    newLine(app, canvas, margin*2, app.lineY, app.width - margin*2, app.lineY)
    #draw text
    lineSpacing = 40
    textX = app.width/2
    #draws text above current line
    for n in range(len(app.dayEntry[:-1])):
        textY = (app.height/8)*2 - app.height/50 + lineSpacing*n
        canvas.create_text(textX, textY, text = app.dayEntry[n], 
                                    font = 'Arial 20')
    #draws current line
    canvas.create_text(textX, app.textY, text = app.dayEntry[-1], 
                                font = 'Arial 20')
    drawDefaultDayText(app, canvas)


#draws the default text:
def drawDefaultDayText(app, canvas):
    textColor = 'black'
    margin = app.height/8
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    canvas.create_text(margin + 240, margin + 30, 
                            text = f"Entry date: {app.currentDayName}, {app.currentDay}", 
                            font = 'Arial 30 bold', fill = textColor)
    canvas.create_text(margin + 170, margin + 60, text = f'Time last saved: {app.timeLastSaved[app.index]}', 
                            font = 'Arial 20', fill = textColor)   

#Main mode: draw a sunset and a path leading to it
def drawMainMode(app, canvas):
    drawHorizonAndSun(app, canvas)
    drawPath(app, canvas)
    if app.backPath == True:
        drawBackPath(app,canvas)
    drawTrees(app, canvas)
    drawDailyButtons(app,canvas)
    drawYearChart(app, canvas)
    canvas.create_text(app.width-200,  30, 
                text = f"{app.currentDayName}, {app.currentDay}", 
                font = 'Arial 30 bold', fill = 'black')

def drawYearChart(app, canvas):
    #DRAW YEAR CHART
    canvas.create_rectangle(50, 50, app.yearChartX, app.yearChartY, 
                            fill = 'white')
    #Draw yearly calendar
    #grid code modified from: https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            fill = "white" if (app.selection == (row, col)) else "white"
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)

def drawHorizonAndSun(app, canvas):
    drawHorizon(app, canvas)
    if app.backPath == False:
        drawSun(app, canvas)

def drawHorizon(app, canvas):
    #DRAW SKY and LAND
    canvas.create_rectangle(0, 0, app.width, app.height/2, 
                                    fill = 'aliceBlue')
                                    #rgbString(255, 185, 30))
    canvas.create_rectangle(0, app.height/2, app.width, app.height, 
                                    fill = 'moccasin')    
    
    #DRAW HORIZON
    canvas.create_line(0, app.height/2, app.width, app.height/2, 
                        width = 5, fill = 'orangeRed')

def drawSun(app, canvas):
    m1, m2 = app.width/160, app.width/35
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

def drawPath(app, canvas):
    x1,y1,x2,y2,x3,y3,x4,y4 = (app.x1,app.y1,app.x2,
                         app.y2,app.x3,app.y3,app.x4,app.y4)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill = 'peru')


def drawBackPath(app,canvas):
    x1,y1,x2,y2,x3,y3,x4,y4 = (app.bx1,app.by1,app.bx2,app.by2,app.bx3,
                            app.by3,app.bx4,app.by4)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill = 'peru')

def drawDailyButtons(app,canvas):
    x1,y1,x2,y2,x3,y3,x4,y4 = (app.x1*10/11,app.y1*5/3,app.x2+200,
                         app.y2,app.x3-400,app.y3,app.x4*12/11,app.y4*5/3)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill = 'cyan',)

def drawWeeklySummaryButton(app, canvas):
    margin = app.height/8
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    canvas.create_rectangle(x2-100,y1,x2,y1+100, fill = 'orange')

def drawTrees(app,canvas):
    #maybe use recursion to draw a cool design
    pass

#Year mode: year chart at corner of main mode expands to show 
#the progress made in the entire year
def drawYearMode(app, canvas):
    pass


#pointInGrid(app, x, y) and getCell(app, x, y) and getCellBounds(app, row, col)
# modified from: https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
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

#draws bar chart for moods of each day
def drawBarChart(app,canvas):
    moodDict = getMoodNumbersWeek(app)
    barX = 300
    for day in moodDict:
        moodNums = moodDict[day]
        sumOfNums = sum(moodNums)
        if sumOfNums > 0:
            happy, sad, angry = moodNums[0], moodNums[1], moodNums[2]
            fraction = 200/sumOfNums
            x0,x1 = barX, barX+80
            y0 = 200
            y1 = y0 + happy*fraction, 
            y2 = y0 + (happy+sad)*fraction, 
            y3 = y0 + (happy+sad+angry)*fraction
            canvas.create_rectangle(x0, y0, x1, y1, fill ='yellow', line = 10)
            canvas.create_rectangle(x1, y1, x0, y2, fill ='cornflowerBlue')
            canvas.create_rectangle(x0, y2, x1, y3, fill ='crimson')
            canvas.create_text(x0+(x1-x0)/2, y3 + 20, text = day[:3], font = 'Arial 20')
        barX += ((800-80*7)/6 + 80)

def drawSplashPage(app, canvas):
        canvas.create_text(app.width/2, 250, text='"Life moves pretty fast.', font='Krungthep 35')
        canvas.create_text(app.width/2, 300, text='If you don’t stop and look', font='Krungthep 25')
        canvas.create_text(app.width/2, 350, text='around once in a while,', font = 'Krungthep 25')
        canvas.create_text(app.width/2, 400, text=' you could miss it."', font='Krungthep 50')
        canvas.create_text(app.width/2, 500, text='Click anywhere to begin!', font='Arial 20')

def redrawAll(app, canvas):
    if app.mode == 'splash':
        drawSplashPage(app, canvas)
    elif app.mode == 'day':
        drawDayMode(app, canvas)
        drawWeeklySummaryButton(app, canvas)
    elif app.mode == 'daily summary':
        drawWeeklySummary(app, canvas)
        drawWeeklySummaryButton(app, canvas)
    elif app.mode == 'weekly summary':
        drawBarChart(app,canvas)
    elif app.mode == 'main':
        drawMainMode(app, canvas)
    elif app.mode == 'year' or app.mode == 'main':
        drawMainMode(app, canvas)
        drawYearMode(app, canvas)


runApp(width=1400, height=800)
