
#from 112 notes: http://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

'''
contentsToWrite = ""
def createEmptyEntries():
    if 
    for n in ['08','09','10','11','12','13']:
        if f'EntriesText/2020-12-{n}-text.txt'.is_file() == False:
            writeFile(f'EntriesText/2020-12-{n}-text.txt', contentsToWrite)


    if f'2020-12-08-text.txt'.is_file()== False:
        writeFile(f'2020-12-08-text.txt', contentsToWrite)
    if f'2020-12-09-text.txt'.is_file() == False:
        writeFile(f'2020-12-09-text.txt', contentsToWrite)
        '''
maxLineLength = 5
def splitString(string):
    string = string
    listOfStrings = []
    while len(string) >= maxLineLength:
            listOfStrings += [string[:maxLineLength]]
            string = string[maxLineLength:]
    listOfStrings += [string]
    return listOfStrings

print(splitString('1234567'))