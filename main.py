import sys

def printWordsFromArray(words: list):
  for i in words:
    print(i)
  return

def lexicographicSort(words: list): # Todo. Make it faster?
  lenOfWords = len(words)
  for i in range(lenOfWords):
    for j in range(0, lenOfWords - i - 1):
      if words[j] > words[j + 1]:
        words[j], words[j+1] = words[j+1], words[j]
  return words

def radixSort(words: list):
  return

def clearDuplicatedWords(words: list):
  listOfUniqueWords: list = []
  for i in words:
    if i not in listOfUniqueWords:
      listOfUniqueWords.append(i)
  return listOfUniqueWords

def splitWordsToArray(words: str):
  splittedContent: list = words.split('\n')
  return splittedContent

def openFile(fileName: str):
  try:
    file = open(fileName, 'r')
  except FileNotFoundError:
    raise Exception('File not found, check that the file exists in that path')
  else:
    return file

def readFile(fileName: str):
  file = openFile(fileName)
  if file:
    fileContent: str = file.read()
    file.close()
    return fileContent
  else:
    return

def readFileAndSortWords(fileName: str, isUnique: bool):
  fileContent: str = readFile(fileName)
  fileContentArray: list = splitWordsToArray(fileContent)
  if (isUnique):
    fileContentArray: list = clearDuplicatedWords(fileContentArray)
  sortedFileContent: list = lexicographicSort(fileContentArray)
  return sortedFileContent;

def checkArgumentLen(arguments: list):
  if len(arguments) < 2:
    raise Exception('Too few arguments, provide at least file name')
  else:
    return

def readPassedArguments(arguments: list):
  lastArgument: str = arguments[len(arguments) - 1]
  argumentObject: dict = {
    'fileName': lastArgument,
    'isUnique': False
  }
  for i in arguments:
    if i == '-u':
      argumentObject['isUnique'] = True
  return argumentObject

checkArgumentLen(sys.argv)
arguments: dict = readPassedArguments(sys.argv)
fileName: str = arguments['fileName']
isUnique: bool = arguments['isUnique']
sortedWords: list = readFileAndSortWords(fileName, isUnique)
printWordsFromArray(sortedWords)