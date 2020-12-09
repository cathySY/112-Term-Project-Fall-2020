from Usefulwords import *
#from datetime 
import datetime
import calendar,string
from fileFunctions import *


class dayMoods(object):
    def __init__(self, date):
        self.date = date
        self.happy = 0 
        self.sad = 0
        self.angry = 0
        self.dayEntry = ''
    def addHappyWord(self):
        self.happy += 1
    def addSadWord(self):
        self.sad += 1
    def addAngryWord(self):
        self.angry += 1
    def printAnalysis(self):
        return (f'# of happy words = {self.happy} \n # of sad words = {self.sad} \n # of angry words = {self.angry}')
    def addDayEntry(self, dayEntry):
        self.dayEntry = dayEntry
    def allMoodNumbers(self):
        return (self.happy, self.sad, self.angry)
    def __repr__(self):
        return f'{self.date}'

def listToString(app,list):
    lst = ''
    for string in list:
        lst += string
    return lst

#returns a list of all the no of times a mood word appears for each mood
def oneDayMoodAnalysis(app,day):
    index = app.dayNames.index(str(day))
    date = app.weekDates[index]
    if str(day) != app.currentDayName:
        contents = readFile(f'Entries/{date}-text.txt')
    else:
        contents = listToString(app,app.dayEntry)
    words = contents.split()
    for word in words:
        if word != '':
            if (word in happyWords) or (word[:-1] in happyWords):
                day.addHappyWord()
            elif (word in sadWords) or (word[:-1] in sadWords):
                day.addSadWord()
            elif (word in angryWords) or (word[:-1] in angryWords):
                day.addAngryWord()
    return [day.happy, day.sad, day.angry]


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
        day = dayMoods(day)

createDayObjectsInWeek()

#prints the text
def drawWeeklyAnalysisText(app,canvas,day):
    text = day.printAnalysis()
    canvas.create_text(app.width/2, app.height/2, text = text, font = 'Arial 40 bold')


def drawWeeklySummary(app, canvas):
    day = dayMoods(app.currentDayName)
    oneDayMoodAnalysis(app,day)
    margin = app.height/8
    popupColor = 'white'
    x1, y1, x2, y2 = margin, margin, app.width - margin, app.height - margin
    #draw popup
    canvas.create_rectangle(x1, y1, x2, y2, fill = popupColor) 
    drawWeeklyAnalysisText(app,canvas,day)

#returns a dictionary with each key mapping to a list of frequencies of mood words
def getMoodNumbersWeek(app):
    moodDict = {}
    for day in app.dayNames:
        moodDict[day] = getMoodNumbersDay(app, day)
    return moodDict

#helper function
def getMoodNumbersDay(app, day):
    day = dayMoods(day)
    return oneDayMoodAnalysis(app,day)

#returns a long string of all the words in the 7 daily entries
def combineFiles():
    weekDates = getWeek()
    combinedString = ''
    for date in weekDates:
        entry = readFile(f'Entries/{date}-text.txt')
        combinedString += entry
    return combinedString

#returns a dictionary for useful words in all the entries + their frequencies
def textAnalysis():
    wordsDict = {}
    combinedText = combineFiles()
    words = combinedText.split()
    for word in words:
        word = word.lower()
        if (word in notUseful) or (word[:-1] in notUseful) :
            combinedText.replace(word, " ")
        elif (word in wordsDict):
            wordsDict[word] += 1
        elif (word[:-1] in wordsDict):
            wordsDict[word[:-1]] += 1
        else:
            if (word[-1] in string.punctuation) and (len(word) > 1):
                wordsDict[word[:-1]] = 1
            else:
                wordsDict[word] = 1
    return wordsDict


def getMostFrequentWords(dictionary):
    words = []
    numbers = []
    #put key and values into separate lists
    for key in dictionary: 
        words += [key]
        numbers += [dictionary[key]]
    newWords = []
    #combines a word with its frequency number in order to use .sort
    for i in range(len(words)):
        newWord = str(numbers[i]) + words[i]
        newWords += [newWord]
    newWords.sort()
    mostFrequent = newWords[-5:]
    word = ''
    listOfWords = []
    #remove numbers
    for newWord in newWords[-5:]:
        splitString = list(newWord)
        for char in splitString:
            if char not in string.digits:
                word += char
        listOfWords.append(word)
        word = ''
    return listOfWords

def overallAnalysis():
    wordsDict = textAnalysis()
    return getMostFrequentWords(wordsDict)
