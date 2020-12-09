#################################################
# TP3Code.py
#
# Your name: Yi Sijun Cathy
# Your andrew id: sijuncay
#################################################


#downloaded from CMU 15-112 website: https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
import cs112_f20_week7_linter
from cmu_112_graphics import *

import math, copy, random, string, calendar
from datetime import datetime

from Usefulwords import *
from EntryAnalysis import *
from fileFunctions import *

# “Life moves pretty fast. If you don’t stop and look around 
#  once in a while, you could miss it.”
#                                             Ferris Bueller

#rgbString(r, g, b) copied from: https://www.cs.cmu.edu/~112/notes/notes-graphics.html
#creates custom colors
def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

#make2dList(rows, cols, string) copied from 112 website: https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html#creating2dLists
def make2dList(rows, cols, string):
    emptyColor = string
    return [ ([emptyColor] * cols) for row in range(rows) ]

def appStarted(app):
    app.mode = 'splash'
    app.dayNames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
                'Saturday', 'Sunday']
    app.skyColors = ['peachPuff','papayaWhip','lemonChiffon','aliceBlue',
                    'paleTurquoise','skyBlue','thistle']
    app.sunColors = ['darkOrange', 'orange', 'peachPuff', 'lightYellow', 
                    'paleTurquoise','skyBlue','thistle']
    app.weekDates = getWeek()
    app.currentDay = str(datetime.datetime.now().date())
    app.currentDayName = calendar.day_name[datetime.datetime.now().date().weekday()]
    app.index = app.weekDates.index(app.currentDay)
    app.maxLineLength = 100
    app.fileContents = readFile(f'Entries/{app.currentDay}-text.txt')
    app.dayEntry = splitString(app,app.fileContents)
    app.letterPosition = [app.height/8*2 + 20]
    app.textY = app.height/4+30 - app.height/50 + 40*(len(app.dayEntry)-1)
    app.lineY = app.height/4+30 + 40*(len(app.dayEntry)-1)
    app.lineMoveCount = 0
    app.dLine = 5
    app.moveTextAndLine = False
    app.textDict = {}
    app.yearChartX, app.yearChartY = app.width/3.5, app.height/3
    app.rows = 3
    app.cols = 4
    ### Calculations for rotation
    app.hDistCovered = 0
    app.hR, app.hFrameCircum = app.height/2, app.width
    app.hTotalCircum = 2*math.pi*app.hR*10
    app.hTotalArea = math.pi * (app.hR)**2
    ###
    app.cxSun, app.cySun = (app.width/2, app.height/2-3)
    app.rSun = app.width/15 + 40*app.index
    app.dMove = 150
    app.dragging = False
    app.getX = 0
    app.getY = 0
    #coordinates for front path
    app.x1,app.y1,app.x2,app.y2,app.x3,app.y3,app.x4,app.y4 = (
                        app.width/2 - 40,
                        app.height/2+2.5, 
                        app.width/5,
                        app.height, 
                        app.width - app.width/5, 
                        app.height,
                        app.width/2 + 40, 
                        app.height/2+2.5)
    #coordinates for back path, rotating to the left
    app.bx1,app.by1,app.bx2,app.by2,app.bx3,app.by3,app.bx4,app.by4 = (
                        -app.width*3, #x
                        app.height/2+2.5, 
                        -900, #x
                        app.height, 
                        -900  + app.width*3/5, #x
                        app.height,
                        -app.width*3 + 80, #x
                        app.height/2+2.5)
    #coordinates for back path, rotating to the right
    app.cx1,app.cy1,app.cx2,app.cy2,app.cx3,app.cy3,app.cx4,app.cy4 = (
                        5520, #x
                        app.height/2+2.5,                       
                        1460, #x
                        app.height,
                        2300, #x
                        app.height,
                        5600, #x
                        app.height/2+2.5)
    app.backPath = False
    app.frontPath = True
    app.theta = 0
    app.mainCentred = True
    app.timeLastSaved = ['']*7
    app.isPopUpBox = False
    app.areLinesMoving = False 
    app.buttonColor = 'cyan'
    app.dayChX1, app.dayChY1, app.dayChX2, app.dayChY2 = 597.5,400,797.5,600 #calculated values
    app.weekMainMood = ''
    app.xDiffTotal = 0
    app.xDiffTotalChanged = 0
    app.treeLevel = 0
    app.trunkX, app.trunkY1, app.trunkY2 = app.cxSun+200, app.cySun+120, app.cySun+60
    app.treeSize = 50
    app.isInstructions = False
    app.cloudx = app.x1
    #Lined Notebook Paper from: https://allfreedesigns.com/lined-paper-texture/
    app.imageSplash1 = app.loadImage('Images/lined-paper-texture-27.jpg')
    #Pastel wallpaper from: https://www.itl.cat/wallview/ihwbJbb_pastel-wallpaper-4k/
    app.imageSplash3 = app.loadImage('Images/Final splash bg.jpg')
    app.imageSplash2 = app.scaleImage(app.imageSplash3, 1.2/3)
    #SIMPLE VECTOR GEOMETRIC BACKGROUND WHITE from: https://onlyvectorbackgrounds.com/vector-geometric-background-white/
    app.weekly1 = app.loadImage('Images/geometric bg.png')
    app.weekly = app.scaleImage(app.weekly1, 1.85/3)
    #Cumulus Cloud from: https://www.clipartkey.com/view/wRmxTT_clipart-cloud-cumulus-cloud-transparent-background-clipart-transparent/
    app.cloudA = app.loadImage('Images/cloud2.png')
    app.cloud2 = app.scaleImage(app.cloudA, 1/15)
    #Clouds from: https://www.clipartkey.com/view/wRmxTT_clipart-cloud-cumulus-cloud-transparent-background-clipart-transparent/
    app.cloudB = app.loadImage('Images/cloud3.png')
    app.scale = 0.1*app.index
    app.cloud1 = app.scaleImage(app.cloudB, (0.5+app.scale)/15)
    app.cloud1small = app.scaleImage(app.cloudB, (0.5+app.scale)/21)

    #tree from: https://pngio.com/images/png-a1066587.html
    app.tree1orig = app.loadImage('Images/purpletree2.png')
    app.tree1z = app.scaleImage(app.tree1orig, 0.5/5)
    app.tree1a = app.scaleImage(app.tree1orig, 1/5)
    app.tree1c = app.scaleImage(app.tree1orig, 2/5)

    #tree from: https://www.pngitem.com/middle/hRxiiiR_cherry-pink-tree-painted-tree-purple-portadas-de/
    app.tree2orig = app.loadImage('Images/purpletree1.png')
    app.tree2z = app.scaleImage(app.tree2orig, 0.5/5)
    app.tree2a = app.scaleImage(app.tree2orig, 1/5)
    app.tree2c = app.scaleImage(app.tree2orig, 2/5)

    #rainbow from: https://gallery.yopriceville.com/Free-Clipart-Pictures/Rainbows-PNG/Transparent_Rainbow_PNG_Free_Clip_Art_Image#.X9CjxukzY6g
    app.rainbowOrig = app.loadImage('Images/rainbow.png')
    app.rainbow = app.scaleImage(app.rainbowOrig, 1/20)

    

def resetAll(app):
    app.mode = 'main'
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
    app.yearChartX, app.yearChartY = app.width/3.5, app.height/3
    app.rows = 3
    app.cols = 4
    ### Calculations for rotation
    app.hDistCovered = 0
    app.hR, app.hFrameCircum = app.height/2, app.width
    app.hTotalCircum = 2*math.pi*app.hR*10
    app.hTotalArea = math.pi * (app.hR)**2
    ###
    app.cxSun, app.cySun, app.rSun = (app.width/2, app.height/2-3, app.width/10)
    app.dMove = 150
    app.dragging = False
    app.getX = 0
    app.getY = 0
    #coordinates for front path
    app.x1,app.y1,app.x2,app.y2,app.x3,app.y3,app.x4,app.y4 = (
                        app.width/2 - 40,
                        app.height/2+2.5, 
                        app.width/5,
                        app.height, 
                        app.width - app.width/5, 
                        app.height,
                        app.width/2 + 40, 
                        app.height/2+2.5)
    #coordinates for back path, rotating to the left
    app.bx1,app.by1,app.bx2,app.by2,app.bx3,app.by3,app.bx4,app.by4 = (
                        -app.width*3, #x
                        app.height/2+2.5, 
                        -900, #x
                        app.height, 
                        -900  + app.width*3/5, #x
                        app.height,
                        -app.width*3 + 80, #x
                        app.height/2+2.5)
    #coordinates for back path, rotating to the right
    app.cx1,app.cy1,app.cx2,app.cy2,app.cx3,app.cy3,app.cx4,app.cy4 = (
                        5520, #x
                        app.height/2+2.5,                       
                        1460, #x
                        app.height,
                        2300, #x
                        app.height,
                        5600, #x
                        app.height/2+2.5)
    app.backPath = False
    app.frontPath = True
    app.theta = 0
    app.mainCentred = True
    app.timeLastSaved = ['']*7
    app.isPopUpBox = False
    app.areLinesMoving = False 
    app.buttonColor = 'cyan'
    app.dayChX1, app.dayChY1, app.dayChX2, app.dayChY2 = 597.5,400,797.5,600 #calculated values
    app.weekMainMood = ''
    app.xDiffTotal = 0
    app.xDiffTotalChanged = 0
    app.treeLevel = 0
    app.trunkX, app.trunkY1, app.trunkY2 = app.cxSun-200, app.cySun+120, app.cySun+60
    app.treeSize = 50
    app.isInstructions = False

#splits a long string into a list of short strings of equal lengths
def splitString(app,string):
    string = string
    listOfStrings = []
    while len(string) >= app.maxLineLength:
        listOfStrings += [string[:app.maxLineLength]]
        string = string[app.maxLineLength:]
    listOfStrings += [string]
    return listOfStrings

#joins short strings in a list into a long string
def listToString(app,list):
    lst = ''
    for string in list:
        lst += string
    return lst

def keyPressed(app, event):
    maxLevel = 6
    if event.key == 'Tab':
        resetAll(app)
    if app.mode == 'main':
        #moving from one day to another    
        if event.key == 'Up':
            app.areLinesMoving = True
            #if index is possible
            if (app.index >= 0) and (app.index <= len(app.weekDates)-2):
                #move the trees
                app.trunkX += 35
                app.trunkY1 += 30
                app.trunkY2 += 30
                app.treeSize += 20
                #move index of day
                app.index += 1
                #change day entry contents
                app.currentDayName = app.dayNames[app.index]
                app.currentDay = app.weekDates[app.index]
                app.fileContents = readFile(f'Entries/{app.currentDay}-text.txt')
                app.dayEntry = splitString(app,app.fileContents)
                #sun gets bigger
                app.rSun += 30
                #clouds get bigger
                app.scale = 0.1*app.index
                app.cloud1 = app.scaleImage(app.cloudB, (0.5+app.scale)/15)
                app.cloud1small = app.scaleImage(app.cloudB, (0.5+app.scale)/21)
        elif event.key == 'Down':
            if (app.index >= 1) and (app.index <= len(app.weekDates)-1):
                app.trunkX -= 35
                app.trunkY1 -= 30
                app.trunkY2 -= 30
                app.treeSize -= 20
                app.index -= 1
                app.currentDayName = app.dayNames[app.index]
                app.currentDay = app.weekDates[app.index]
                app.fileContents = readFile(f'Entries/{app.currentDay}-text.txt')
                app.dayEntry = splitString(app,app.fileContents)
                #sun gets smaller
                app.rSun += -30
                #clouds get smaller
                app.scale = 0.1*app.index
                app.cloud1 = app.scaleImage(app.cloudB, (0.5+app.scale)/15)
                app.cloud1small = app.scaleImage(app.cloudB, (0.5+app.scale)/21)
            
    elif app.mode == 'day':
        if event.key == 'Right':
            app.mode = 'daily summary'
        #if current text string is too long/exceeds length of underline
        elif len(app.dayEntry[-1]) >= app.maxLineLength:
            #creates new empty string
            app.dayEntry += ['']
            app.moveTextAndLine = True
        #text editing:
        #add a space
        elif event.key == 'Space':
            app.dayEntry[-1] += ' '
        #delete a character
        elif event.key == 'Delete':
            #if entry is empty
            if app.dayEntry[0] == '':
                return
            else:
                #if last string is empty, remove that string
                if app.dayEntry[-1] == '':
                    app.dayEntry.pop()
                    app.lineY -= 40
                    app.textY -= 40
                # if last string is not empty, delete from last string
                app.dayEntry[-1] = app.dayEntry[-1][:-1]
        #add a character
        elif event.key in string.printable:
                app.dayEntry[-1] += event.key
    elif app.mode == 'daily summary':
        if event.key == 'Left':
            app.mode = 'day'

#replaces content in file with content written in entry using a long string
def saveFile(app):
    contents = listToString(app,app.dayEntry)
    writeFile(f'Entries/{app.currentDay}-text.txt',contents)

def timerFired(app):
    app.timerDelay = 10
    app.cloudx += 3
    #moves text and line downwards at the same pace until a new line is reached
    if app.moveTextAndLine == True:
        app.lineY += 5
        app.textY += 5
        app.lineMoveCount += 1
    if app.lineMoveCount >= 40/5:
        app.moveTextAndLine = False
        app.lineMoveCount = 0
    #expands path button to day entry
    app.timerDelay = 5
    if app.mode == 'main to day':
        x1, y1, x2, y2 = app.height/8, app.height/8, app.width - app.height/8, app.height - app.height/8
        if ((app.dayChX1 >= x1) and (app.dayChY1 >= y1)) and ((
                (app.dayChX2 <= x2) and (app.dayChY2 <= y2))):
            app.dayChX1 -= 38
            app.dayChY1 -= 26
            app.dayChX2 += 38
            app.dayChY2 += 10
        else:
            app.dayChX1, app.dayChY1, app.dayChX2, app.dayChY2 = 597.5,400,797.5,600
            app.textY = app.height/4+30 - app.height/50 + 40*(len(app.dayEntry)-1)
            app.lineY = app.height/4+30 + 40*(len(app.dayEntry)-1)
            app.mode = 'day'
    if app.mode == 'weekly summary':
        getMostFrequentMood(app)

      
#rotation about a fixed centre point, can rotate 180 degrees in both directions
def mouseDragged(app, event):
    app.dragging = True
    #how much the cursor is dragged in x-direction
    #can be positive or negative
    xdiff = (app.getX - event.x)
    app.theta -= xdiff/app.hTotalCircum * (math.pi*2)
    app.cloudx -= xdiff
    app.cloudx %= app.hTotalCircum
    app.thetaMOD = app.theta % (2*math.pi)
    #front half of circle
    if (app.thetaMOD >= 0 and app.thetaMOD < math.pi/2) or ((app.thetaMOD >= math.pi*3/2) and (app.thetaMOD < math.pi*2)): 
        app.trunkX -= xdiff
        app.cxSun -= xdiff
        app.cxSun %= app.hTotalCircum
        app.frontPath = True
        app.backPath = False
        app.x1 -= xdiff
        app.x4 -= xdiff
        app.x2 -= xdiff*1/4
        app.x3 -= xdiff*1/4
    elif ((app.thetaMOD >= math.pi/2 and app.thetaMOD < math.pi*3/2)): 
        app.frontPath = False
        app.backPath = True
        #back half of circle, if rotated to the left
        if app.theta > 0:
            app.bx1 -= xdiff
            app.bx4 -= xdiff
            app.bx2 -= xdiff*1/4
            app.bx3 -= xdiff*1/4
        #back half of circle, if rotated to the right
        else:
            app.cx1 -= xdiff
            app.cx4 -= xdiff
            app.cx2 -= xdiff*1/4
            app.cx3 -= xdiff*1/4


def mouseReleased(app,event):
    app.dragging = False

def mouseMoved(app,event):
    #values for pup-up trapezium on path
    #pops up if mouse hovers over it
    x1,y1,x2,y2,x3,y3,x4,y4 = (app.x1,app.y1,app.x2,app.y2,app.x3,app.y3,app.x4,app.y4)
    grad1 = (y2-y1)/(x2+250-(x1+30))
    grad2 = (y3-y4)/(x3-250-(x4-30))
    lineX1 = (1/grad1)*(650-y1)+(x1+25)
    lineX2 = (1/grad2)*(650-y3)+(x3-250)
    if (lineX1 <= event.x <= lineX2) and (650 <= event.y <= app.height):
        app.isPopUpBox = True
    else:
        app.isPopUpBox = False

def mousePressed(app, event):
    app.getX = event.x  
    app.getY = event.y
    margin = app.height/8
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    if app.mode == 'splash':
        app.mode = 'main'
    elif app.mode == 'day':
        #day entry is automatically saved when it is closed using the close button
        if (x2-100 < event.x < x2) and (y1 < event.y < y1+100):
            app.timeLastSaved[app.index] = app.currentDay + ' ' + str(datetime.datetime.now().time())[:5]
            app.mode = 'main'
            saveFile(app)
            app.mode = 'main'
    elif app.mode == 'main':
        #if click on weekly summary chart
        if (50 < event.x < app.width/3.5) and (50 < event.y < app.height/3):
            app.mode = 'weekly summary'
        x1,y1,x2,y2,x3,y3,x4,y4 = (app.x1,app.y1,app.x2,app.y2,app.x3,app.y3,app.x4,app.y4)
        grad1 = (y2-y1)/(x2+250-(x1+30))
        grad2 = (y3-y4)/(x3-250-(x4-30))
        lineX1 = (1/grad1)*(650-y1)+(x1+25)
        lineX2 = (1/grad2)*(650-y3)+(x3-250)
        #if user clicks the rectangle inside the trapezium, transition to day entry
        if (lineX1 <= event.x <= lineX2) and (650 <= event.y <= app.height):
            app.mode = 'main to day'
            app.isPopUpBox = False
        #open and close the instructions
        if (app.width-220 <= event.x <= app.width-20) and (720 <= event.y <= 770):
            app.isInstructions = not app.isInstructions
    elif app.mode == 'year':
        if (app.width/5 < event.x < app.width - 50) and (app.height/3 < event.y < app.height - 50):
            app.mode = 'main'
    elif app.mode == 'weekly summary':
        margin = app.height/12
        x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
        if (x2-60 < event.x < x2) and (y1 < event.y < y1+60): 
            app.mode = 'main'
    elif app.mode == 'daily summary':
        if (x2-100 < event.x < x2) and (y1 < event.y < y1+100):
            app.timeLastSaved[app.index] = app.currentDay + ' ' + str(datetime.datetime.now().time())[:5]
            app.mode = 'main'
            #saves file automatically
            saveFile(app)
            app.mode = 'main'


# draws the line under the text
def newLine(app, canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill = 'blue', width = 3)

def drawDayMode(app, canvas):
    margin = app.height/8
    popupColor = 'blanchedAlmond'
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    #draw background
    canvas.create_rectangle(x1, y1, x2, y2, fill = 'white')
    newLine(app, canvas, margin*2, app.lineY, app.width - margin*2, app.lineY)
    #draw text
    lineSpacing = 40
    textX = app.width/2
    #draws text above current line
    for n in range(len(app.dayEntry[:-1])):
        textY = app.height/4 + 30 - app.height/50 + lineSpacing*n
        canvas.create_text(textX, textY, text = app.dayEntry[n], 
                                    font = 'Arial 20')
    #draws current line
    canvas.create_text(textX, app.textY, text = app.dayEntry[-1], 
                                font = 'Arial 20')
    drawDefaultDayText(app, canvas)


#draws the default day entry text:
def drawDefaultDayText(app, canvas):
    textColor = 'black'
    margin = app.height/8
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    canvas.create_text(margin + 240, margin + 30, 
                            text = f"Date: {app.currentDayName}, {app.currentDay}", 
                            font = 'Krungthep 25', fill = textColor)
    canvas.create_text(margin + 170, margin + 60, text = f'Last saved today: {app.timeLastSaved[app.index][-5:]}', 
                            font = 'Krungthep 20', fill = textColor)   

#Main mode: draw a sunset and a path leading to it
def drawMainMode(app, canvas):
    drawHorizonAndSun(app, canvas)
    drawClouds(app, canvas)
    if app.frontPath == True:
        drawPath(app, canvas)
    if app.backPath == True:
        if app.theta > 0:
            drawBackPath(app,canvas,app.bx1,app.by1,app.bx2,app.by2,app.bx3,
                            app.by3,app.bx4,app.by4) 
        else:
            drawBackPath(app,canvas,app.cx1,app.cy1,app.cx2,app.cy2,app.cx3,
                            app.cy3,app.cx4,app.cy4) 
    drawSummaryChart(app, canvas)
    canvas.create_text(app.width-200,  30, 
                text = f"Welcome! You are on the date", 
                font = 'Krungthep 20', fill = 'black')
    canvas.create_text(app.width-200,  80, 
                text = f"{app.currentDayName}, {app.currentDay}", 
                font = 'Krungthep 30 ', fill = 'black')

    drawLandTrees(app,canvas)
    
    #draw fractal trees
    fractalTree(app, canvas, app.trunkX+50, app.trunkY1, app.trunkX+50, app.trunkY2, app.treeSize, 0)
    fractalTree(app, canvas, app.trunkX, app.trunkY1-50, app.trunkX, app.trunkY2-50, app.treeSize, 0)

def drawClouds(app,canvas):
    #clouds wrap around
    canvas.create_image((app.cloudx-500)%(app.width+100), 100, image=ImageTk.PhotoImage(app.cloud1small))
    canvas.create_image((app.cloudx-50)%(app.width+100), 250, image=ImageTk.PhotoImage(app.cloud1))
    canvas.create_image((app.cloudx+500)%(app.width+100), 200, image=ImageTk.PhotoImage(app.cloud1))
    #canvas.create_image(app.cloudx, 200, image=ImageTk.PhotoImage(app.cloud2))
            
def drawLandTrees(app,canvas):
    canvas.create_image(app.x1-200, 420, image=ImageTk.PhotoImage(app.tree1z))
    canvas.create_image(app.x1-500, 450, image=ImageTk.PhotoImage(app.tree1a)) 
    canvas.create_image(app.x1-1200-2200, 400, image=ImageTk.PhotoImage(app.tree1a))    
    canvas.create_image(app.x1-1800-1000, 550, image=ImageTk.PhotoImage(app.tree1c)) 

    canvas.create_image(app.x1-200-1300, 420, image=ImageTk.PhotoImage(app.tree2z))
    canvas.create_image(app.x1-500-2000, 450, image=ImageTk.PhotoImage(app.tree2a))
    canvas.create_image(app.x1-1200-2500, 400, image=ImageTk.PhotoImage(app.tree2a))    
    canvas.create_image(app.x1-1800-2800, 550, image=ImageTk.PhotoImage(app.tree2c))    

    canvas.create_image(app.x1+200+1300, 420, image=ImageTk.PhotoImage(app.tree2z))
    canvas.create_image(app.x1+500+2000, 450, image=ImageTk.PhotoImage(app.tree2a))
    canvas.create_image(app.x1+1200+2500, 400, image=ImageTk.PhotoImage(app.tree2a))    
    canvas.create_image(app.x1+1800+2800, 550, image=ImageTk.PhotoImage(app.tree2c))  

    # canvas.create_image(app.x1-200-2800, 420, image=ImageTk.PhotoImage(app.tree1z))
    # canvas.create_image(app.x1-500-2800, 450, image=ImageTk.PhotoImage(app.tree1a))
    # canvas.create_image(app.x1-1200-2800, 400, image=ImageTk.PhotoImage(app.tree1a))    
    # canvas.create_image(app.x1-1800-2800, 550, image=ImageTk.PhotoImage(app.tree1c))    

    
            

def drawSummaryChart(app, canvas):
    #DRAW Summary CHART
    canvas.create_rectangle(50, 50, app.yearChartX, app.yearChartY, 
                            fill = 'white')
    canvas.create_text((50+app.yearChartX)/2, (50+app.yearChartY)/2-10, 
                        text = 'Click me for your', font = 'Krungthep 25')
    canvas.create_text((50+app.yearChartX)/2, (50+app.yearChartY)/2+20, 
                        text = 'weekly summary!', font = 'Krungthep 25')
                            


def drawHorizonAndSun(app, canvas):
    drawHorizon(app, canvas)
    if app.backPath == False:
        drawSun(app, canvas)

def drawHorizon(app, canvas):
    #DRAW SKY and LAND
    canvas.create_rectangle(0, 0, app.width, app.height/2, 
                                    fill = app.skyColors[app.index])
                                    #rgbString(255, 185, 30))
    canvas.create_rectangle(0, app.height/2, app.width, app.height, 
                                    fill = 'moccasin')    
    
    #DRAW HORIZON
    canvas.create_line(0, app.height/2, app.width, app.height/2, 
                        width = 5, fill = app.sunColors[app.index])

def drawSun(app, canvas):
    m1, m2 = app.width/160, app.width/35
    cx, cy, r = app.cxSun, app.cySun, app.rSun
    canvas.create_arc(cx-r-m2, cy-r-m2, cx+r+m2, cy+r+m2, start=0, 
                                extent=180, fill=app.sunColors[app.index], 
                                outline = app.sunColors[app.index])     
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
    canvas.create_polygon(x1+15,y1,x2+60,y2,x3-60,y3,x4-15,y4, fill = 'pink')
    canvas.create_polygon(x1+25,y1,x2+80,y2,x3-80,y3,x4-25,y4, fill = 'plum')
    canvas.create_polygon(x1+30,y1,x2+250,y2,x3-250,y3,x4-30,y4, fill = 'lightBlue')
    #draw straight lines across
    if ((x3-80-(x4-25))) != 0:
        grad1 = (y2-y1)/(x2+80-(x1+25))
    if ((x3-80-(x4-25))) != 0:
        grad2 = (y3-y4)/(x3-80-(x4-25)) 
    for y in [650,520,450]:
        lineX1 = (1/grad1)*(y-y1)+(x1+25)
        lineX2 = (1/grad2)*(y-y3)+(x3-80)
        canvas.create_line(lineX1, y, lineX2, y, width = 5, fill = 'plum')
    #if mouse hovers over the trapezium, it changes color
    if app.isPopUpBox == True:
        grad1 = (y2-y1)/(x2+250-(x1+30))
        grad2 = (y3-y4)/(x3-250-(x4-30))
        lineX1 = (1/grad1)*(650-y1)+(x1+25)
        lineX2 = (1/grad1)*(app.height-y1)+(x1+25)
        lineX4 = (1/grad2)*(650-y3)+(x3-250)
        lineX3 = (1/grad2)*(app.height-y3)+(x3-250)
        canvas.create_polygon(lineX1-10, 640, lineX2-10, app.height, lineX3+10,
            app.height, lineX4+10, 640, fill = app.buttonColor)

        #creates entry pop-up
        canvas.create_rectangle((lineX1-10+lineX4+10)/2-100,400,(lineX1-10+lineX4+10)/2+100,600, fill = 'white')


def drawBackPath(app,canvas,x1,y1,x2,y2,x3,y3,x4,y4):
    if app.theta > 0:
        canvas.create_image((app.bx1+app.bx4)/2, 300, image=ImageTk.PhotoImage(app.rainbow))
    else:
        canvas.create_image((app.cx1+app.cx4)/2, 300, image=ImageTk.PhotoImage(app.rainbow))
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill = 'peru')
    canvas.create_polygon(x1+15,y1,x2+60,y2,x3-60,y3,x4-15,y4, fill = 'pink')
    canvas.create_polygon(x1+25,y1,x2+80,y2,x3-80,y3,x4-25,y4, fill = 'lightCoral')
    canvas.create_polygon(x1+30,y1,x2+250,y2,x3-250,y3,x4-30,y4, fill = 'lightBlue')
    #draw straight lines across
    grad1 = -2
    grad1 = -2
    if ((x3-80-(x4-25))) != 0:
        grad1 = (y2-y1)/(x2+80-(x1+25))
    if ((x3-80-(x4-25))) != 0:
        grad2 = (y3-y4)/(x3-80-(x4-25)) 
    for y in [650,520,450]:
        lineX1 = (1/grad1)*(y-y1)+(x1+25)
        lineX2 = (1/grad2)*(y-y3)+(x3-80)
        canvas.create_line(lineX1, y, lineX2, y, width = 5, fill = 'peru')

def drawSummaryCloseButton(app, canvas):
    margin = app.height/12
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    canvas.create_rectangle(x2-60,y1,x2,y1+60, fill = 'orange')
    canvas.create_line(x2-60,y1,x2,y1+60)

def drawCloseButton(app, canvas):
    margin = app.height/8
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    canvas.create_rectangle(x2-60,y1,x2,y1+60, fill = 'orange')
    canvas.create_line(x2-60,y1,x2,y1+60)


#draws bar chart for moods of each day
def drawBarChart(app,canvas):
    #draw background
    margin = app.height/12
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    canvas.create_rectangle(x1, y1, x2, y2, fill = 'white')
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.weekly))
    #draw heading
    canvas.create_text(app.width/2, app.height/12 + 40, text = 'Weekly Summary', font = 'Krungthep 40')
    #draw key for bar chart
    canvas.create_text(200, 260, text = 'KEY', font = 'Krungthep 18')
    canvas.create_text(200, 280, text = 'yellow: happy', font = 'Krungthep 15')
    canvas.create_text(200, 300, text = 'blue: sad', font = 'Krungthep 15')
    canvas.create_text(200, 320, text = 'red: angry', font = 'Krungthep 15')
    #draw bar chart
    moodDict = getMoodNumbersWeek(app)
    barX = 300
    for day in moodDict:
        moodNums = moodDict[day]
        sumOfNums = sum(moodNums)
        x0,x1 = barX, barX+80
        y3 = 400
        if sumOfNums > 0:
            happy, sad, angry = moodNums[0], moodNums[1], moodNums[2]
            fraction = 200/sumOfNums
            y0 = 200
            y1 = y0 + happy*fraction, 
            y2 = y0 + (happy+sad)*fraction, 
            y3 = y0 + (happy+sad+angry)*fraction
            canvas.create_rectangle(x0, y0, x1, y1, fill ='yellow', outline = 'white')
            canvas.create_rectangle(x1, y1, x0, y2, fill ='cornflowerBlue', outline = 'white')
            canvas.create_rectangle(x0, y2, x1, y3, fill ='crimson', outline = 'white')
        barX += ((800-80*7)/6 + 80)
        canvas.create_text((x1+x0)/2, y3 + 20, text = day[:3], font = 'Krungthep 20')

def getMostFrequentMood(app):
    summation = 0
    (happyN, sadN, angryN) = (0,0,0)
    moods = ['happy', 'sad', 'angry']
    moodDict = getMoodNumbersWeek(app)
    for day in moodDict:
        #get sum of all instances
        summation += sum(moodDict[day])
        #split instances
        happyN += moodDict[day][0]
        sadN += moodDict[day][1]
        angryN += moodDict[day][2]
    #get max no of times a mood word was written
    maxNum = max(happyN, sadN, angryN)
    for i in range(3):
        if ((happyN, sadN, angryN)[i] == maxNum) and (moods[i] not in app.weekMainMood):
            app.weekMainMood += moods[i]
            app.weekMainMood += ' '

def drawPiechart(app,canvas):
    summation = 0
    (happyN, sadN, angryN) = (0,0,0)
    moodDict = getMoodNumbersWeek(app)
    for day in moodDict:
        summation += sum(moodDict[day])
        happyN += moodDict[day][0]
        sadN += moodDict[day][1]
        angryN += moodDict[day][2]
    cx, cy, r = (490, 600, app.width/14)
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=0, 
                                extent=(happyN/summation)*360, fill='yellow', 
                                outline = 'black')     
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=(happyN/summation)*360, 
                                extent=(sadN/summation)*360, fill='blue',
                                outline = 'black')                       
    canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start=((sadN+happyN)/summation)*360, 
                                extent=(angryN/summation)*360, fill='red',
                                outline = 'black') 
    canvas.create_text(230, 590, text = 'mood distribution', font = 'Krungthep 18')
    canvas.create_text(230, 620, text = 'for the entire week', font = 'Krungthep 18')

def drawWordSummary(app,canvas):
    mostFrequentWords = overallAnalysis()
    count = 0
    time = 0
    for date in app.weekDates:
        if readFile(f'Entries/{date}-text.txt') != '':
            count += 1
    canvas.create_text(app.width-400,  520, 
                text = f"Most frequently used words: ", 
                font = 'Krungthep 30 bold', fill = 'black')
    canvas.create_text(app.width-400,  570, 
                text = f"{mostFrequentWords}", 
                font = 'Krungthep 25 bold', fill = 'black')
    canvas.create_text(app.width-400,  620, 
                text = f"Number of journal entries: {count}/7", 
                font = 'Krungthep 30 bold', fill = 'black')    
    emoji = ''
    if app.weekMainMood == 'happy ': 
        emoji = ':)' 
    elif app.weekMainMood == 'sad ': 
        emoji = ':(' 
    elif app.weekMainMood == 'angry ': 
        emoji = '>:('     
    canvas.create_text(app.width-400,  670, 
                text = f"Main mood(s): {app.weekMainMood} {emoji}", 
                font = 'Krungthep 30 bold', fill = 'black')

def drawSplashPage(app, canvas):
        canvas.create_text(app.width/2, 250, text='"Life moves pretty fast.', font='Krungthep 35')
        canvas.create_text(app.width/2, 300, text='If you don’t stop and look', font='Krungthep 25')
        canvas.create_text(app.width/2, 350, text='around once in a while,', font = 'Krungthep 25')
        canvas.create_text(app.width/2, 400, text=' you could miss it."', font='Krungthep 50')
        canvas.create_text(app.width/2, 450, text='Ferris Bueller', font='Krungthep 20')
        canvas.create_text(app.width/2, 550, text='Click anywhere to begin!', font='Arial 20')
        
        #my credits! :)
        canvas.create_text(app.width-300, app.height-20, text="All the Write Moves, by Cathy Yi (Fall'19 112 TP)", font='Arial 20')

def treeBranch(app, canvas, x1, y1, x2, y2):
    #draw line
    canvas.create_line(x1, y1, x2, y2, width = 8, fill = 'brown')

#recursive function
#heavily modified from fractalTeddy 
#inspiration for the design of this fractal tree from: http://www.lukaszkroenke.net/projects/1.html
def fractalTree(app, canvas, x1, y1, x2, y2, length, level, angle = math.radians(20)):
    maxLevel = 6
    xDiff1 = length*math.sin(angle*level)
    yDiff1 = length*math.cos(angle*level)
    #base case
    if level == app.index:
        treeBranch(app, canvas, x1, y1, x2,y2)
    #recursive case
    else:
        #left branch
        fractalTree(app, canvas, x1 - xDiff1, y1 - yDiff1, x1, y1, length*0.8, level+1)
        #right branch
        fractalTree(app, canvas, x1 + xDiff1, y1 - yDiff1, x1, y1, length*0.8, level+1)
        treeBranch(app, canvas, x1, y1, x2,y2)

def drawInstructionsBox(app,canvas):
    canvas.create_rectangle(app.width-220,720,app.width-20,770, fill = 'beige')
    canvas.create_text(app.width-125,745, text = 'Instructions', font = 'Krungthep 25')

def drawInstructions(app,canvas):
    canvas.create_text(app.width-190,745-40*4, text = 'Click on bottom centre trapezium', font = 'Krungthep 20')
    canvas.create_text(app.width-190,745-40*3, text = 'to open daily entries. Use', font = 'Krungthep 20')
    canvas.create_text(app.width-190,745-40*2, text = 'Up and Down keys to toggle', font = 'Krungthep 20')
    canvas.create_text(app.width-190,745-40*1, text = 'through each day of the week.', font = 'Krungthep 20')

def redrawAll(app, canvas):
    if app.mode == 'splash':
        app.imageSplash2
        canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.imageSplash2))
        canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.imageSplash1))
        drawSplashPage(app, canvas)
    elif app.mode == 'day':
        drawMainMode(app, canvas)
        drawDayMode(app, canvas)
        drawCloseButton(app, canvas)
    elif app.mode == 'main to day':
        drawMainMode(app, canvas)
        canvas.create_rectangle(app.dayChX1, app.dayChY1, app.dayChX2, app.dayChY2, fill = 'white')
    elif app.mode == 'daily summary':
        drawMainMode(app, canvas)
        drawWeeklySummary(app, canvas)
        drawCloseButton(app, canvas)
    elif app.mode == 'weekly summary':
        drawMainMode(app, canvas)
        drawBarChart(app,canvas)
        drawPiechart(app,canvas)
        drawWordSummary(app,canvas)
        drawSummaryCloseButton(app, canvas)
    elif app.mode == 'main':
        drawMainMode(app, canvas)
        drawInstructionsBox(app,canvas)
        if app.isInstructions:
            drawInstructions(app,canvas)


runApp(width=1400, height=800)
