import unittest
import io
import sys

from main import lexicographicSort
from main import readFile
from main import readFileAndSortWords
from main import openFile
from main import printWordsFromArray
from main import clearDuplicatedWords
from main import splitWordsToArray
from main import checkArgumentLen
from main import readPassedArguments
from main import radixSort
from main import radixBucketSort
from main import createBuckets
from main import flatten
from main import lexicographicSortOnChar

TEST_DATA_1: list = ['a', 'a', 'b', 'c', 'c', 'c', 'd', 'e']
TEST_DATA_2: list = ['e', 'd', 'c', 'c', 'c', 'b', 'a', 'a']
TEST_DATA_3: str = 'a\na\nb\nc\nc\nc\nd\ne'
TEST_DATA_4: list = ['main.py']
TEST_DATA_5: list = ['main.py', 'words.txt']
TEST_DATA_6: list = ['main.py', '-u', 'words.txt']
TEST_DATA_7: list = ['tuple', 'anyone', 'bass', 'ananas', 'anywhere', 'The', 'banana']
TEST_DATA_8: list = [[['ananas']], ['banana'],[['bass', 'basso']]]
TEST_DATA_9: list = ['ananas', 'pineapple', 'banana']
TEST_DATA_10: list = ['main.py', '-u', 'sort=radix', 'words.txt']
TEST_DATA_11: list = ['tuple', 'anyone', 'bass', 'ananas', 'anywhere', 'The', 'banana']
EXPECTED_1: str = 'a\na\nb\nc\nc\nc\nd\ne\n'
EXPECTED_2: str = 'Short text'
EXPECTED_3: list = ['a', 'b', 'c', 'd', 'e']
EXPECTED_4: list = ['a', 'a', 'b', 'c', 'c', 'c', 'd', 'e']
EXPECTED_5: dict = {'fileName': 'words.txt', 'isUnique': False, 'sortAlgorithm': 'default'}
EXPECTED_6: dict = {'fileName': 'words.txt', 'isUnique': True, 'sortAlgorithm': 'default'}
EXPECTED_7: list = ['ananas', 'anyone', 'anywhere', 'banana', 'bass', 'The', 'tuple']
EXPECTED_8: list = ['ananas', 'banana', 'bass', 'basso']
EXPECTED_9: list = [['tuple', 'The'], ['anyone', 'ananas', 'anywhere'], ['bass', 'banana']]
EXPECTED_10: list = ['banana', 'pineapple', 'ananas']
EXPECTED_11: dict = {'fileName': 'words.txt', 'isUnique': True, 'sortAlgorithm': 'radix'}
EXPECTED_12: list = ['anyone', 'ananas', 'anywhere', 'bass', 'banana', 'tuple', 'The']
EXCEPTION_1: str = 'File not found, check that the file exists in that path'
EXCEPTION_2: str = 'Too few arguments, provide at least file name'
EXCEPTION_3: str = 'Given index is out of range'
TEST_FILE_1: str = 'testing/this-file-should-not-exist.txt'
TEST_FILE_2: str = 'testing/short-text.txt'
TEST_FILE_3: str = 'testing/short-words.txt'

class TestClass(unittest.TestCase):
  # Prints can be tested with io and sys
  def test_printWordsFromArray(self):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    testData: list = TEST_DATA_1
    expectedValue: str = EXPECTED_1
    printWordsFromArray(testData)
    sys.stdout = sys.__stdout__
    self.assertEqual(expectedValue, capturedOutput.getvalue())

  def test_openNotExistingFile(self):
    expectionMessage: str = EXCEPTION_1
    testFile: str = TEST_FILE_1
    with self.assertRaises(Exception) as context:
      openFile(testFile)
    self.assertTrue(expectionMessage in str(context.exception))

  # Here we also test that the file is opened and can be read
  def test_readFile(self):
    testFile: str = TEST_FILE_2
    expectedValue: str = EXPECTED_2
    readFileContent: str = readFile(testFile)
    self.assertEqual(expectedValue, readFileContent)

  def test_sortLexicographically(self):
    testData: list = TEST_DATA_2
    expectedValue: list = EXPECTED_4
    sortedData: list = lexicographicSort(testData)
    self.assertEqual(expectedValue, sortedData)

  def test_readFileAndSortContentWithFalseUniqueness(self):
    testFile: str = TEST_FILE_3
    expectedValue: list = EXPECTED_4
    readAndSortedContent: list = readFileAndSortWords(testFile, False, 'default')
    self.assertEqual(expectedValue, readAndSortedContent)

  def test_readFileAndSortContentWithTrueUniqueness(self):
    testFile: str = TEST_FILE_3
    expectedValue: list = EXPECTED_3
    readAndSortedContent: list = readFileAndSortWords(testFile, True, 'default')
    self.assertEqual(expectedValue, readAndSortedContent)

  def test_clearDuplicatedWords(self):
    testData: list = TEST_DATA_1
    expectedValue: list = EXPECTED_3
    uniqueList: list = clearDuplicatedWords(testData)
    self.assertEqual(expectedValue, uniqueList)

  def test_splitWordsToArray(self):
    testData: str = TEST_DATA_3
    expectedValue: list = EXPECTED_4
    wordsInArray: list = splitWordsToArray(testData)
    self.assertEqual(expectedValue, wordsInArray)

  def test_checkArgumentLenWithTooFewArgs(self):
    expectionMessage: str = EXCEPTION_2
    with self.assertRaises(Exception) as context:
      checkArgumentLen(TEST_DATA_4)
    self.assertTrue(expectionMessage in str(context.exception))

  def test_readPassedArgumentsFilenameIsProvided(self):
    testData: list = TEST_DATA_5
    expectedValue: dict = EXPECTED_5
    argumentsObject: dict = readPassedArguments(testData)
    self.assertEqual(expectedValue, argumentsObject)

  def test_readPassedArgumentsFilenameAndUniqueIsProvided(self):
    testData: list = TEST_DATA_6
    expectedValue: dict = EXPECTED_6
    argumentsObject: dict = readPassedArguments(testData)
    self.assertEqual(expectedValue, argumentsObject)

  def test_readPassedArgumentsFilenameUniqueAndAlgorithmIsProvided(self):
    testData: list = TEST_DATA_10
    expectedValue: dict = EXPECTED_11
    argumentsObject: dict = readPassedArguments(testData)
    self.assertEqual(expectedValue, argumentsObject)

  def test_radixSort(self):
    testData: list = TEST_DATA_7
    expectedValue: list = EXPECTED_7
    radixSortedData: list = radixSort(testData)
    self.assertEqual(expectedValue, radixSortedData)

  def test_radixBucketSort_earlyReturn(self):
    bucketSortedData = radixBucketSort(['ananas'], 1, 1, False)
    self.assertEqual(['ananas'], bucketSortedData)

  def test_radixBucketSort_lexAndReturn(self):
    testData: list = TEST_DATA_9
    expectedValue: list = EXPECTED_10
    bucketSortedData: list = radixBucketSort(testData, 3, 0, True)
    self.assertEqual(expectedValue, bucketSortedData)

  # def test_radixBucketSort(self):

  def test_createBuckets(self):
    testData: list = TEST_DATA_7
    expectedValue: list = EXPECTED_9
    buckets: list = createBuckets(testData, 0)
    self.assertEqual(expectedValue, buckets)

  def test_flatten(self):
    testData: list = TEST_DATA_8
    expectedValue: list = EXPECTED_8
    flattenedArray: list = flatten(testData)
    self.assertEqual(expectedValue, flattenedArray)

  def test_lexicographicSortOnChar(self):
    testData: list = TEST_DATA_11
    expectedValue: list = EXPECTED_12
    sortedData: list = lexicographicSortOnChar(testData, 0)
    self.assertEqual(expectedValue, sortedData)

  def test_lexicographicSortOnCharOutOfIndex(self):
    expectionMessage: str = EXCEPTION_3
    testData: list = TEST_DATA_11
    with self.assertRaises(Exception) as context:
      lexicographicSortOnChar(testData, 100)
    self.assertTrue(expectionMessage in str(context.exception))