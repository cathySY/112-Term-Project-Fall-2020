#COLORS  
# 
#   app.skyColors = ['peachPuff','moccasin','papayaWhip','lemonChiffon','lightYellow','aliceBlue','lightCyan']
#     app.sunColors = ['darkOrange', 'darkOrange', 'orange', 'orange', 'moccasin','lightGoldenrodYellow','lightCyan']     

    app.tree3orig = app.loadImage('Images/tree3.png')
    app.tree3z = app.scaleImage(app.tree3orig, 0.5/5)
    app.tree3a = app.scaleImage(app.tree3orig, 1/5)
    app.tree3c = app.scaleImage(app.tree3orig, 2/5)


""" 
#quotes copied from: https://www.coburgbanks.co.uk/blog/friday-funnies/50-funny-motivational-quotes/
RawQuotes =
[
“People often say that motivation doesn’t last. Well, neither does bathing – that’s why we recommend it daily.” Zig Ziglar

“I always wanted to be somebody, but now I realise I should have been more specific.” Lily Tomlin

 “I am so clever that sometimes I don’t understand a single word of what I am saying.” Oscar Wilde

“People say nothing is impossible, but I do nothing every day.” Winnie the Pooh

“You can’t have everything. Where would you put it?” Steven Wright


 “If you think you are too small to make a difference, try sleeping with a mosquito.” Dalai Lama


 “Bad decisions make good stories.” Ellis Vidler

 “I’ll probably never fully become what I wanted to be when I grew up, but that’s probably because I wanted to be a ninja princess.” Cassandra Duffy


 “A clear conscience is a sure sign of a bad memory.” Mark Twain

 “I used to think I was indecisive, but now I’m not so sure.” Unknown

“Don’t worry about the world coming to an end today. It’s already tomorrow in Australia.” Charles Schulz


“Optimist: someone who figures that taking a step backward after taking a step forward is not a disaster, it’s more like a cha-cha.” Robert Brault

 “The question isn’t who is going to let me, it’s who is going to stop me.” Ayn Rand.

 “You’re only given a little spark of madness. You mustn’t lose it.” Robin Williams

 “I am an early bird and a night owl… so I am wise and I have worms” Michael Scott

 “If you let your head get too big, it’ll break your neck.” Elvis Presley

“The road to success is dotted with many tempting parking spaces.” Will Rogers

“Leadership is the art of getting someone else to do something you want done because he wants to do it.” Dwight D. Eisenhower

“Live each day like it’s your second to the last. That way you can fall asleep at night.” Jason Love

“Even a stopped clock is right twice every day. After some years, it can boast of a long series of successes.” Marie Von Ebner-Eschenbach

 “Honest criticism is hard to take, particularly from a relative, a friend, an acquaintance, or a stranger.” Franklin P. Jones

“I am an early bird and a night owl… so I am wise and I have worms” Michael Scott #quotes

“I believe that if life gives you lemons, you should make lemonade… And try to find somebody whose life has given them vodka, and have a party.” Ron White

“Opportunity is missed by most people because it is dressed in overalls and looks like work.” Thomas Eddison


 “By working faithfully eight hours a day you may eventually get to be boss and work twelve hours a day.” Robert Frost

“The trouble with having an open mind, of course, is that people will insist on coming along and trying to put things in it.” Terry Pratchett

“Age is of no importance unless you’re a cheese.” Billie Burke

“When tempted to fight fire with fire, remember that the Fire Department usually uses water.” Unknown]

 """

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
