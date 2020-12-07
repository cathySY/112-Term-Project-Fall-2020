from Usefulwords import *
#from datetime 
import datetime
import calendar

class dayMoods(object):
    def __init__(self):
        self.happy = 0 
        self.sad = 0
        self.angry = 0
        self.dayEntry = ''
    def addHappyWord(self):
        print('yes')
        self.happy += 1
    def addSadWord(self):
        self.sad += 1
    def addAngryWord(self):
        self.angry += 1
    def printAnalysis(self):
        return (f'# of happy words = {self.happy} \n # of sad words = {self.sad} \n # of angry words = {self.angry}')
    def addDayEntry(self, dayEntry):
        self.dayEntry = dayEntry
    
    def dictWordFrequency(self):
        pass


'''
Monday = daysOfWeek()
Tuesday = daysOfWeek()
Wednesday = daysOfWeek()
Thursday = daysOfWeek()
Friday = daysOfWeek()
Saturday = daysOfWeek()
Sunday = daysOfWeek()
'''

def oneDayMoodAnalysis(app,file):
    words = file.split()
    for word in words:
        if word != '':
            if word in happyWords:
                day.addHappyWord()
            elif word in sadWords:
                day.addSadWord()
            elif word in angryWords:
                day.addAngryWord()

'''
today = entryMoodFrequency()
dayEntry = [' angry sad sad ']
oneDayMoodAnalysis(today,dayEntry)
print (today.printAnalysis())
'''

#todayDate = datetime.datetime.now().date()
#print(todayDate)
#print(calendar.day_name[todayDate.weekday()])

#datetime learnt from https://www.dataquest.io/blog/python-datetime-tutorial/
def getWeek():
    myDate = '2020-12-07' #datetime.datetime.now()
    myDate = datetime.datetime.strptime(myDate, "%Y-%m-%d")
    weekDates = [str(myDate.date())]
    for n in range(6):
        myDate += datetime.timedelta(days=1)
        dateOnly = myDate.date() #calendar.day_name[date.weekday()]
        weekDates += [str(dateOnly)]
    return weekDates

def createDayObjectsInWeek():
    days = getWeek()
    for day in days:
        day = dayMoods()

createDayObjectsInWeek()

def createFiles():
    pass

#prints the text
def drawWeeklyAnalysisText(app,canvas,day):
    text = day.printAnalysis()
    canvas.create_text(app.width/2, app.height/2, text = text, font = 'Arial 40 bold')

currentDay = dayMoods()

def drawWeeklySummary(app, canvas):
    margin = app.height/8
    popupColor = 'mintCream'
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    #draw popup
    canvas.create_rectangle(x1, y1, x2, y2, fill = popupColor)
    oneDayMoodAnalysis(app,app.fileContents)
    drawWeeklyAnalysisText(app,canvas,currentDay)

#print(str(datetime.datetime.now().date()))
#print(str(datetime.datetime.now().date()))