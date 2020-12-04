
def helper(lst):
    newList = ''
    for word in lst:
        newList += word
    return newList

#synonyms taken from https://www.thesaurus.com/browse/happy
rawHappy = ['''happy
cheerful
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
captivated
chipper
chirpy
content
convivial
exultant
gay
gleeful
gratified
intoxicated
jolly
laughing
light
'looking good'
mirthful
'on cloud nine'
peppy
perky
playful
sparkling
sunny
tickled
'tickled pink'
up
'walking on air'
''']

#from https://www.thesaurus.com/browse/sad?s=t
rawSad = ['''
sad
bitter
dismal
heartbroken
melancholy
mournful
pessimistic
somber
sorrowful
sorry
wistful
bereaved
blue
cheerless
dejected
despairing
despondent
disconsolate
distressed
doleful
down
'down in dumps'
downcast
forlorn
gloomy
glum
grief-stricken
grieved
heartsick
heavyhearted
hurting
'in doldrums'
'in grief'
'in the dumps'
languishing
low
low-spirited
lugubrious
morbid
morose
out of sorts
pensive
sick at heart
troubled
weeping
woebegone
''']

#from https://www.thesaurus.com/browse/angry?s=t
rawAngry = ['''angry
annoyed
bitter
enraged
exasperated
furious
heated
impassioned
indignant
irate
irritable
irritated
offended
outraged
resentful
sullen
uptight
affronted
antagonized
chafed
choleric
convulsed
cross
displeased
exacerbated
ferocious
fierce
fiery
fuming
galled
hateful
hot
huffy
ill-tempered
incensed
inflamed
infuriated
irascible
ireful
maddened
nettled
piqued
provoked
raging
riled
sore
splenetic
storming
sulky
tumultous
tumultuous
turbulent
vexed
wrathful''']



happyWords = helper(rawHappy)
sadWords = helper(rawSad)
angryWords = helper(rawAngry)
