from Usefulwords import *
from EntryAnalysis import *
from datetime import datetime
import calendar


def wordCloud(entry):
    cleanEntry = entry
    for word in entry:
        if word in prepositions:
            cleanEntry.remove(word)
        elif word in articles:
            cleanEntry.remove(word)
    return cleanEntry




'''
print('Day of Month:', my_date.day)

# to get name of day(in number) from date
print('Day of Week (number): ', my_date.weekday())

# to get name of day from date
print('Day of Week (name): ', calendar.day_name[my_date.weekday()])'''