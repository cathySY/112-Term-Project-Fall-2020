from Usefulwords import *

class daysOfWeek(object):
    def __init__(self):
        self.happy = 0 
        self.sad = 0
        self.angry = 0
    def addHappyWord(self):
        self.happy += 1
    def addSadWord(self):
        self.sad += 1
    def addAngryWord(self):
        self.angry += 1
    def printAnalysis(self):
        return (f'# of happy words = {self.happy} \n # of sad words = {self.sad} \n # of angry words = {self.angry}')

'''
Monday = daysOfWeek()
Tuesday = daysOfWeek()
Wednesday = daysOfWeek()
Thursday = daysOfWeek()
Friday = daysOfWeek()
Saturday = daysOfWeek()
Sunday = daysOfWeek()
'''

def oneDayMoodAnalysis(app,day):
    for word in app.dayEntry:
        if word in happyWords:
            day.addHappyWord()
        elif word in sadWords:
            day.addSadWord()
        elif word in angryWords:
            day.addAngryWord()

def drawWeeklyAnalysisText(app,canvas,day):
    text = day.printAnalysis()
    canvas.create_text(app.width/2, app.height/2, text = text, font = 'Arial 40 bold')

today = daysOfWeek()
def drawWeeklySummary(app, canvas):
    margin = app.height/8
    popupColor = 'mintCream'
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    #draw popup
    canvas.create_rectangle(x1, y1, x2, y2, fill = popupColor)
    oneDayMoodAnalysis(app,today)
    drawWeeklyAnalysisText(app,canvas,today)