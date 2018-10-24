import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	inFile = open(file, "r")
	dictList = []
	for line in inFile:
		tempDict = {}
		lineVals = line.split(",")
		firstName = lineVals[0]
		lastName = lineVals[1]
		email = lineVals[2]
		classYear = lineVals[3]
		dOB = lineVals[4].rstrip()

		if firstName == "First":
			continue
		else:
			tempDict["First"] = firstName
			tempDict["Last"] = lastName
			tempDict["Email"] = email
			tempDict["Class"] = classYear
			tempDict["DOB"] = dOB
			dictList.append(tempDict)

	inFile.close()
	return dictList

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	sortedList = sorted(data, key = lambda k: k[col], reverse = False)
	finalName = sortedList[0]["First"] + " " + sortedList[0]["Last"]

	return finalName



def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	srTotal = 0
	jrTotal = 0
	sophTotal = 0
	frTotal = 0
	tupleList = []

	for person in data:
		if person["Class"] == "Senior":
			srTotal = srTotal + 1
		elif person["Class"] == "Junior":
			jrTotal = jrTotal + 1
		elif person["Class"] == "Sophomore":
			sophTotal = sophTotal + 1
		elif person["Class"] == "Freshman":
			frTotal = frTotal + 1

	srTuple = ("Senior", srTotal)
	tupleList.append(srTuple)

	jrTuple = ("Junior", jrTotal)
	tupleList.append(jrTuple)

	sophTuple = ("Sophomore", sophTotal)
	tupleList.append(sophTuple)

	frTuple = ("Freshman", frTotal)
	tupleList.append(frTuple)

	tupleList = sorted(tupleList, key = lambda k: k[1], reverse = True)
	return tupleList


def findMonth(a):
# Find the most common birth month from this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	janCnt = 0
	febCnt = 0
	marCnt = 0
	aprCnt = 0
	mayCnt = 0
	junCnt = 0
	julCnt = 0
	augCnt = 0
	sepCnt = 0
	octCnt = 0
	novCnt = 0
	decCnt = 0
	for person in a:
		if person["DOB"][0:2] == "1/":
			janCnt = janCnt + 1
		elif person["DOB"][0:2] == "2/":
			febCnt = febCnt + 1
		elif person["DOB"][0:2] == "3/":
			marCnt = marCnt + 1
		elif person["DOB"][0:2] == "4/":
			aprCnt = aprCnt + 1
		elif person["DOB"][0:2] == "5/":
			mayCnt = mayCnt + 1
		elif person["DOB"][0:2] == "6/":
			junCnt = junCnt + 1
		elif person["DOB"][0:2] == "7/":
			julCnt = julCnt + 1
		elif person["DOB"][0:2] == "8/":
			augCnt = augCnt + 1
		elif person["DOB"][0:2] == "9/":
			sepCnt = sepCnt + 1
		elif person["DOB"][0:2] == "10":
			octCnt = octCnt + 1
		elif person["DOB"][0:2] == "11":
			novCnt = novCnt + 1
		elif person["DOB"][0:2] == "12":
			decCnt = decCnt + 1

	monthList = [(1, janCnt), (2, febCnt), (3, marCnt), (4, aprCnt),
				(5, mayCnt), (6, junCnt), (7, julCnt), (8, augCnt),
				(9, sepCnt), (10, octCnt), (11, novCnt), (12, decCnt)]

	monthList = sorted(monthList, key = lambda k: k[1], reverse = True)

	return monthList[0][0]



def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	inFile = open(fileName, "w")

	sortedList = sorted(a, key = lambda k: k[col], reverse = False)
	
	for person in sortedList:
		inFile.write(person["First"] + "," + person["Last"] + "," + person["Email"] + "\n")

	inFile.close()


def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	print(data)
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))


# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()


