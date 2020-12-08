#splits each long string into into strings of words
def helper(string):
    newList = string.split()
    return newList

# most synonyms copied from https://www.thesaurus.com/browse/happy
rawHappy = '''
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
HAHAHA
HAHAHAHA
LOL
lol
lmao
Lol
LMAO
awesome
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
'''

#copied from https://www.thesaurus.com/browse/sad?s=t
rawSad = '''
:(
:-(
sad
sucks
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
'''


notUseful = helper(rawNotUseful)


