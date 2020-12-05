from Usefulwords import *

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
    entry = app.dayEntry[0].split()
    for word in entry:
        print(word)
        if word != '':
            if word in happyWords:
                day.addHappyWord()
                
            elif word in sadWords:
                day.addSadWord()
            elif word in angryWords:
                day.addAngryWord()
        entry.remove(word)
            

def drawWeeklyAnalysisText(app,canvas,day):
    text = day.printAnalysis()
    canvas.create_text(app.width/2, app.height/2, text = text, font = 'Arial 40 bold')

