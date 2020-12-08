
#from 112 notes: http://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

maxLineLength = 5
def splitString(string):
    string = string
    listOfStrings = []
    while len(string) >= maxLineLength:
            listOfStrings += [string[:maxLineLength]]
            string = string[maxLineLength:]
    listOfStrings += [string]
    return listOfStrings
