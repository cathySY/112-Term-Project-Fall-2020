        #Calm Anime Wallpapers from: https://wallpaperaccess.com/calm-anime
    #url1 = 'https://wallpaperaccess.com/full/2152451.jpg'
    
        #Pastel wallpaper
    url = 'https://static.vecteezy.com/system/resources/previews/000/378/561/original/vector-simple-geometric-pastel-background.jpg'
    app.imageDay1 = app.loadImage(url)
    app.imageDay = app.scaleImage(app.imageDay1, 2/3)

    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.imageDay))
    
    #how much the cursor is dragged in x-direction
    #can be positive or negative
    xdiff = (app.getX - event.x)
    app.theta -= xdiff/app.hTotalCircum * (math.pi*2)
    app.theta %= 2*math.pi
    #print(app.theta)
    #first quadrant:
    #app.povLeft %= app.hTotalCircum
    app.cxSun -= xdiff
    app.cxSun %= app.hTotalCircum
    app.x1 -= xdiff
    app.x4 -= xdiff
    app.x2 -= xdiff*1/4
    app.x3 -= xdiff*1/4
    
    if ((app.theta >= 0 and app.theta < math.pi/2) or (app.theta >= math.pi*3/2 
            and app.theta < math.pi*2)):
        print('1: ', app.theta)
        app.x1 %= app.hTotalCircum
        app.x2 %= app.hTotalCircum*1/4
        (print("app.x1: ", app.x1))
        (print("app.x2: ", app.x2))
        app.x3 %= app.hTotalCircum*1/4
        app.x4 %= app.hTotalCircum 
        if ((app.theta > 4 and app.theta < 5.5)):
            app.frontPath = False
            app.backPath = False
        elif ((app.theta > 5.5 and app.theta < 5)):
            app.frontPath = False
            app.backPath = False
        else:
            app.frontPath = True
            app.backPath = False
    #second quadrant 
    if ((app.theta >= math.pi/2 and app.theta < math.pi*3/2)): 
    #and ((app.theta > 1.5 and app.theta < 4.7)==False)):
        print('2: ',app.theta)
        if (app.theta > 1.5 and app.theta < 2.603):  
            app.frontPath = False
            app.backPath = False
        else:
            print('true')
            app.frontPath = False
            app.backPath = True
        #app.cxSun -= xdiff
        #TRAPEZIUM OF PATH
            #shift angles
        app.bx1 -= xdiff
        app.bx4 -= xdiff
        app.bx2 -= xdiff*1/4
        app.bx3 -= xdiff*1/4
        app.x1 %= app.hTotalCircum
        app.x2 %= app.hTotalCircum*1/4
        app.x3 %= app.hTotalCircum*1/4
        app.x4 %= app.hTotalCircum 
        #print('app.x1: ',app.bx1)
        #print('app.x2: ',app.bx2)
        #print('app.x3: ',app.bx3)
        #print('app.x4: ',app.bx4)
        
        
        app.bx1 %= app.hTotalCircum
        app.bx2 %= app.hTotalCircum*1/4
        app.bx3 %= app.hTotalCircum*1/4
        app.bx4 %= app.hTotalCircum    


    


how much the cursor is dragged in x-direction
    #can be positive or negative
    xdiff = (app.getX - event.x)
    app.theta -= xdiff/app.hTotalCircum * (math.pi*2)
    app.theta %= 2*math.pi
    #print(app.theta)
    #first quadrant:
    #app.povLeft %= app.hTotalCircum
    app.cxSun -= xdiff
    app.cxSun %= app.hTotalCircum
    app.x1 -= xdiff
    app.x4 -= xdiff
    app.x2 -= xdiff*1/4
    app.x3 -= xdiff*1/4
    if (app.theta >= 0 and app.theta < math.pi/2) or (app.theta >= math.pi*3/2 and app.theta < math.pi*2):
        print('app.x1: ',app.x1)
        app.frontPath = False
        app.backPath = False
        if app.x1 < -4000 or app.x1 > 4000:
            print('app.frontPath = False')
            app.frontPath = False
        else:
            app.frontPath = True
        app.x1 %= app.hTotalCircum
        app.x2 %= app.hTotalCircum*1/4
        app.x3 %= app.hTotalCircum*1/4
        app.x4 %= app.hTotalCircum 
    elif (app.theta >= math.pi*3/2 and app.theta < math.pi*2):
        print('app.x1: ',app.x1)
        print('app.x2: ',app.x2)
        print('app.x3: ',app.x3)
        print('app.x4: ',app.x4)
        print('app.theta: ',app.theta)
        pass
        '''
        #app.frontPath = True
        app.backPath = False
        app.x1 %= app.hTotalCircum
        app.x2 %= app.hTotalCircum*1/4
        app.x3 %= app.hTotalCircum*1/4
        app.x4 %= app.hTotalCircum 
        print('app.x1: ',app.x1)
        print('app.x2: ',app.x2)
        print('app.x3: ',app.x3)
        print('app.x4: ',app.x4)
        print('app.theta: ',app.theta)
        '''
        '''
            #shift x
        #if (app.povLeft < app.width - app.hTotalCircum/5 and 
                #app.povLeft > app.width - app.hTotalCircum/4):
            #app.x2 -= xdiff*8
            #app.x3 -= xdiff*8

            #app.x2 %= app.hTotalCircum
            #app.x3 %= app.hTotalCircum
            '''
    #second quadrant 
    elif (app.theta >= math.pi/2 and app.theta < math.pi*3/2):
        app.frontPath = False
        app.backPath = True
        #app.cxSun -= xdiff
        #TRAPEZIUM OF PATH
            #shift angles
        app.bx1 -= xdiff
        app.bx4 -= xdiff
        app.bx2 -= xdiff*1/4
        app.bx3 -= xdiff*1/4
        app.x1 %= app.hTotalCircum
        app.x2 %= app.hTotalCircum*1/4
        app.x3 %= app.hTotalCircum*1/4
        app.x4 %= app.hTotalCircum 
        
        app.bx1 %= app.hTotalCircum
        app.bx2 %= app.hTotalCircum*1/4
        app.bx3 %= app.hTotalCircum*1/4
        app.bx4 %= app.hTotalCircum      


app.x1:  49.0
app.x2:  127.25
app.x3:  967.25
app.x4:  129.0

app.x1:  25091.741228718347
app.x2:  104.75
app.x3:  944.75
app.x4:  39.0


app.theta:  3.944935307179583
app.x4:  10093.0
app.theta:  3.911435307179583
app.x4:  10227.0
app.theta:  3.877685307179583
app.x4:  10362.0
app.theta:  3.8436853071795833
app.x4:  10498.0
app.theta:  3.8091853071795834
app.x4:  10636.0
app.theta:  3.7739353071795834
app.x4:  10777.0
app.theta:  3.7384353071795835
app.x4:  10919.0
app.theta:  3.7026853071795833

app.x4:  11062.0
app.theta:  3.7006853071795835
app.x4:  11070.0
app.theta:  3.6846853071795835
app.x4:  11134.0
app.theta:  3.6584353071795834
app.x4:  11239.0
app.theta:  3.6276853071795836
app.x4:  11362.0
app.theta:  3.590435307179584
app.x4:  11511.0
app.theta:  3.550185307179584
app.x4:  11672.0
app.theta:  3.5096853071795837


    #how much the cursor is dragged in x-direction
    #can be positive or negative
    xdiff = (app.getX - event.x)
    app.theta += xdiff/app.hTotalCircum * (math.pi*2)
    app.theta %= 2*math.pi
    #print(app.theta)
    #first quadrant:
    #app.povLeft %= app.hTotalCircum
    app.cxSun -= xdiff
    app.cxSun %= app.hTotalCircum
    if ((app.theta >= 0 and app.theta < math.pi/2) 
        or (app.theta >= math.pi*3/2 and app.theta < math.pi*2)):
        #print('yes')
        app.backPath = False
        #app.cxSun -= xdiff
        #app.cxSun %= app.hTotalCircum
        #TRAPEZIUM OF PATH
            #shift angles
        app.x1 -= xdiff
        app.x4 -= xdiff
        print('app.x4: ',app.x4)
        print('app.theta: ',app.theta)
        app.x2 -= xdiff*1/4
        app.x3 -= xdiff*1/4
        app.x1 %= app.hTotalCircum
        app.x2 %= app.hTotalCircum
        app.x3 %= app.hTotalCircum
        app.x4 %= app.hTotalCircum 
        '''
            #shift x
        #if (app.povLeft < app.width - app.hTotalCircum/5 and 
                #app.povLeft > app.width - app.hTotalCircum/4):
            #app.x2 -= xdiff*8
            #app.x3 -= xdiff*8

            #app.x2 %= app.hTotalCircum
            #app.x3 %= app.hTotalCircum
            '''
    #second quadrant 
    elif (app.theta >= math.pi/2 and app.theta < math.pi*3/2):
        app.backPath = True
        #app.cxSun -= xdiff
        #TRAPEZIUM OF PATH
            #shift angles
        app.x1 -= xdiff
        app.x4 -= xdiff

        app.bx1 -= xdiff
        app.bx4 -= xdiff
        app.x2 -= xdiff*1/4
        app.x3 -= xdiff*1/4
        app.bx2 -= xdiff*1/4
        app.bx3 -= xdiff*1/4
        app.x1 %= app.hTotalCircum
        app.x2 %= app.hTotalCircum*1/4
        app.x3 %= app.hTotalCircum*1/4
        app.x4 %= app.hTotalCircum 

        app.bx1 %= app.hTotalCircum
        app.bx2 %= app.hTotalCircum*1/4
        app.bx3 %= app.hTotalCircum*1/4
        app.bx4 %= app.hTotalCircum      
       
       

#think of some cool designs!
        #remember to draw shadows for objects on land - to increase realism
        #Add flying birds too! just black birds flapping across the horizon 
        #in the distance

        #note: change path to be a curved path
#maybe even 3-d, going up and down?


#idea inspired by Wordle: http://www.wordle.net/create
#idea was brought up in meeting with TP mentor (Elena)


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



    '''
    cx, cy = app.width/2, app.height/2
    if ((cx-100 <= event.x <= cx+100) and
        (cy+100 <= event.y <= cy+120)):
        app.mode = 'month'
        '''

def drawDayMode(app, canvas):
        #Draw triangle to look like a popup: canvas.create_triangle(app.width/2 - )
    #draw line
        #need to animate line moving down
        #need to animate scrolling if no. of lines exceeds max on a page
            #text moves down as text length exceeds line length


        #canvas.create_text(margin + 500, margin + 20, 
                            #text = 'How was your day today?', 
                            #font = 'Arial 20 ', fill = textColor)
    #canvas.create_text(200, firstTextY + 100, text = 'major events', 
                            #font = 'Arial 40 underline', fill = textColor)          
    #canvas.create_text(200, firstTextY + 150, text = 'Notes', 
                            #font = 'Arial 40 underline', fill = textColor) 

def drawPath(app, canvas):
    #left side
    #canvas.create_line(app.width/2 - 10, app.height/2+2.5, app.width/3.5,
                         #app.height, width = 5, smooth = True)
    #right side
    #canvas.create_line(app.width/2 + 10, app.height/2+2.5, app.width - 
                        #app.width/3.5, app.height, width = 5, smooth = False)

#getMoodNumbersWeek(app) = this result is so beautiful! :D
         
                    if len(app.dayEntry) >= 2:
                if len(app.dayEntry[-2]) < app.maxLineLength:
                    app.dayEntry[-2] += event.key
                else:
                    app.dayEntry[-1] += event.key
        
        def appStarted(app):
        app.dayNames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
                    'Saturday', 'Sunday']
        app.weekDates = getWeek()
        app.currentDay = str(datetime.datetime.now().date())
        app.currentDayName = calendar.day_name[datetime.datetime.now().date().weekday()]
        app.index = app.weekDates.index(app.currentDay)
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
        app.backPath = False
        app.theta = 0
        app.mainCentred = True
    '''
    if app.cxSun == app.width/2 + app.hTotalCircum/4:
        app.x1,app.y1,app.x2,app.y2 = -1,-1,-1,-1
        print(app.cxSun)
        '''
'''
class daysOfWeek(object):
    def __init__(self):
        self.happy = 0 
        self.sad = 0
        self.angry = 0
    def addHappyWord(self):
        self.happy += 1
        return
    def addSadWord(self):
        self.sad += 1
        return
    def addAngryWord(self):
        self.angry += 1
        return
    def printAnalysis(self):
        return (f'# of happy words = {self.happy} \n # of sad words = {self.sad} \n # of angry words = {self.angry}')


def oneDayMoodAnalysis(app,day):
    entry = app.dayEntry[0].split()
    print(entry)
    for word in entry:
        if word != '':
            if word in happyWords:
                day.addHappyWord()
            elif word in sadWords:
                day.addSadWord()
            elif word in angryWords:
                day.addAngryWord()
        #entry.remove(word)
            

def drawWeeklyAnalysisText(app,canvas,day):
    text = day.printAnalysis()
    canvas.create_text(app.width/2, app.height/2, text = text, font = 'Arial 40 bold')

def drawWeeklySummary(app, canvas):
    today = daysOfWeek()
    margin = app.height/8
    popupColor = 'mintCream'
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    #draw popup
    canvas.create_rectangle(x1, y1, x2, y2, fill = popupColor)
    drawWeeklyAnalysisText(app,canvas,today)
    '''



    #how much the cursor is dragged in x-direction
    #can be positive or negative
    xdiff = (app.getX - event.x)
    app.theta += xdiff/app.hTotalCircum * (math.pi*2)
    app.theta %= 2*math.pi
    #print(app.theta)
    #first quadrant:
    #app.povLeft %= app.hTotalCircum
    app.xDiffTotal += xdiff
    print('xDiffTotalapp = ', app.xDiffTotal)
    #app.xDiffTotalChanged = (app.hTotalCircum + app.xDiffTotal)
    app.xDiffTotal %= app.hTotalCircum
    print('xDiffTotalChanged = ', app.xDiffTotal)
    app.cxSun -= xdiff
    app.cxSun %= app.hTotalCircum
    if ((app.theta >= 0 and app.theta < math.pi/2) 
        or (app.theta >= math.pi*3/2 and app.theta < math.pi*2)):
        #print('yes')
        app.backPath = False
        #app.cxSun -= xdiff
        #app.cxSun %= app.hTotalCircum
        #TRAPEZIUM OF PATH
            #shift angles
        app.x1 = app.width/2 - 40 - app.xDiffTotal
        app.x4 = app.width/2 + 40 - app.xDiffTotal
        print('app.x1 = ', app.x1)
        #print('app.x4: ',app.x4)
        #print('app.theta: ',app.theta)
        app.x2 = app.width/5 - app.xDiffTotal*1/4
        app.x3 = app.width*4/5 - app.xDiffTotal*1/4
        #app.x1 %= app.hTotalCircum
        #app.x2 %= app.hTotalCircum
        #app.x3 %= app.hTotalCircum
        #app.x4 %= app.hTotalCircum 
        '''
            #shift x
        #if (app.povLeft < app.width - app.hTotalCircum/5 and 
                #app.povLeft > app.width - app.hTotalCircum/4):
            #app.x2 -= xdiff*8
            #app.x3 -= xdiff*8

            #app.x2 %= app.hTotalCircum
            #app.x3 %= app.hTotalCircum
            '''
    #second quadrant 
    elif (app.theta >= math.pi/2 and app.theta < math.pi*3/2):
        app.backPath = True
        #app.cxSun -= xdiff
        #TRAPEZIUM OF PATH
            #shift angles
        app.x1 -= xdiff
        app.x4 -= xdiff

        app.bx1 -= xdiff
        app.bx4 -= xdiff
        app.x2 -= xdiff*1/4
        app.x3 -= xdiff*1/4
        app.bx2 -= xdiff*1/4
        app.bx3 -= xdiff*1/4
        app.x1 %= app.hTotalCircum
        app.x2 %= app.hTotalCircum*1/4
        app.x3 %= app.hTotalCircum*1/4
        app.x4 %= app.hTotalCircum 

        app.bx1 %= app.hTotalCircum
        app.bx2 %= app.hTotalCircum*1/4
        app.bx3 %= app.hTotalCircum*1/4
        app.bx4 %= app.hTotalCircum 


            #Draw yearly calendar
    #grid code modified from: https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html#exampleGrids
    '''
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            fill = "white" if (app.selection == (row, col)) else "white"
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill)
            '''

    # Lined Paper Texture Images from: https://allfreedesigns.com/lined-paper-texture/
    #url2 = 'https://allfreedesigns.com/wp-content/uploads/2017/04/lined-paper-texture-23.jpg'
    


            '''
            #if no of strings is 2 or more
            if len(app.dayEntry) >= 2:
                #if second-last string is shorter than max length, append a space
                if len(app.dayEntry[-2]) < app.maxLineLength:
                    app.dayEntry[-2] += ' '
                #else, append a space to the last string
                else:
                    app.dayEntry[-1] += ' '
                    '''
           

'''
contentsToWrite = ""
def createEmptyEntries():
    if 
    for n in ['08','09','10','11','12','13']:
        if f'EntriesText/2020-12-{n}-text.txt'.is_file() == False:
            writeFile(f'EntriesText/2020-12-{n}-text.txt', contentsToWrite)


    if f'2020-12-08-text.txt'.is_file()== False:
        writeFile(f'2020-12-08-text.txt', contentsToWrite)
    if f'2020-12-09-text.txt'.is_file() == False:
        writeFile(f'2020-12-09-text.txt', contentsToWrite)
        '''