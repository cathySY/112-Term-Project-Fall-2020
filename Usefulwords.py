#splits each long string into into strings of words
def helper(string):
    newList = string.split()
    newList = set(newList)
    newList = list(newList)
    return newList

# most synonyms copied from https://www.thesaurus.com/browse/happy
rawHappy = '''
satisfied
:)
:D
:-)
happy
haha
ha
hahaha
hahahaha
HAHA
HA
laugh
laughed
fun
great
celebrated
celebrate
HAHAHA
HAHAHAHA
LOL
lol
lmao
Lol
LMAO
awesome
good 
great
incredible
cool
amazing
pumped
excited 
merry
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
gleeful
gratified
jolly
laughing
light
mirthful
peppy
perky
playful
sparkling
sunny
tickled
pleasant
'''

#copied from https://www.thesaurus.com/browse/sad?s=t
rawSad = '''
:(
:-(
sad
sucks
cried
depressed
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
downcast
forlorn
gloomy
glum
grief-stricken
grieved
heartsick
heavyhearted
hurting
languishing
low
low-spirited
lugubrious
morbid
morose
pensive
troubled
weeping
woebegone
cry
cried
tears
unpleasant
'''

#copied from https://www.thesaurus.com/browse/angry?s=t
rawAngry = '''>:(
angry
rage
hate
sulked
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
fumed
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
wrathful'''


happyWords = helper(rawHappy)
#happyWords.extend(['looking good','on cloud nine','tickled pink'])
sadWords = helper(rawSad)
#sadWords.extend(['feeling down','down in the dumps','in doldrums','in grief','in the dumps','out of sorts'])
angryWords = helper(rawAngry)


#most words copied from: https://www.englishclub.com/grammar/prepositions-list.htm
rawNotUseful = '''
aboard
about
above
across
after
against
along
amid
among
anti
around
as
at
before
behind
below
beneath
beside
besides
between
beyond
but
by
concerning
considering
despite
down
during
except
excepting
excluding
following
for
from
in
inside
into
like
minus
near
of
off
on
onto
opposite
outside
over
past
per
plus
regarding
round
save
since
than
through
to
toward
towards
under
underneath
unlike
until
up
upon
versus
via
with
within
without
a
an
the 
those
he 
she 
I 
her
him
his 
her
they
them
their
that
my 
and
it
'''


notUseful = helper(rawNotUseful)
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