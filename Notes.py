#COLORS       
'''
https://academy.cs.cmu.edu/docs#colors
for notes: 'cornSilk' 'blanchedAlmond' 'bisque' 'navajoWhite' 'wheat'
for bg: rgbString(10, 40, 130)
colorList = # pastel colors
            ['ivory','mintCream','floralWhite',
            'aliceBlue', 'lavenderBlush', 'seashell', 'honeydew']
            # sun colors
            ['lightYellow','lemonChiffon','lightGoldenrodYellow','papayaWhip',
            'moccasin','peachPuff','paleGoldenrod']

#note: extent = (n+1) * (180/7)
             #for n in [0,1,4,6] draws a pattern that vaguely 
                #resembles a pokeball! cool.

      
            textLength = len(app.letterPosition)
            spacing = 10
            if event.key in 'mwMW':
                spacing = 14
                
                #app.letterPosition.append(app.letterPosition[textLength - 1] 
                        #+ spacing)
            elif event.key in 'ijlI':
                spacing = 7
                #app.letterPosition.append(app.letterPosition[textLength - 1] 
                        #+ spacing)
            else:
                spacing = 10
                #app.letterPosition.append(app.letterPosition[textLength - 1] 
                        #+ spacing)
            app.textDict[event.key] = 
            #app.letterPosition.append(app.letterPosition[textLength - 1] 
                        #+ spacing)   
            
            if event.key in 'mwMW':
                app.letterPosition += 14
            elif event.key in 'ijlI':
                app.letterPosition += 7
            else:
                app.letterPosition += 10
                '''

'''
    if app.dayEntry == '':
        textX = x1*2 + 10
    elif app.dayEntry[-1] in 'mwMW':
        textX = x1*2 + len(app.dayEntry)*6.5
    elif app.dayEntry[-1] in 'ijlItn':
        textX = x1*2 + len(app.dayEntry)*4.5
    else:
        textX = x1*2 + len(app.dayEntry)*5.6
'''

happyWords = ['''cheerful
contented
delighted
ecstatic
elated
glad
joyful
joyous
jubilant
lively
merry
overjoyed
peaceful
pleasant
pleased
thrilled
upbeat
blessed
blest
blissful
blithe
can't complain
captivated
chipper
chirpy
content
convivial
exultant
flying high
gay
gleeful
gratified
intoxicated
jolly
laughing
light
looking good
mirthful
on cloud nine
peppy
perky
playful
sparkling
sunny
tickled
tickled pink
up
walking on air
''']

def helper(lst):
    newList = ''
    for word in lst:
        newList += word
    return newList

finalList = helper(happyWords)
