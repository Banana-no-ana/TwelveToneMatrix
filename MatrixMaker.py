
#Moduels:
#	Globber to grab all the row files
#	Inversion row generator
#	Matrix outputter
#	Row generator

import random

#Generates a row
#TODO: Need to normalize prime to 0
def RowGenerator():
	rowGenerator = []
	myRow = []
	for item in simpleRowYielder():
		rowGenerator.append(item)
	for x in range(0, 12):
		myItem = randRemove(rowGenerator)
		myRow.append(myItem)

	myRow = normalizeRow(myRow)
	print myRow
	return myRow

def calcNormalized(item, prime):
	note = (item + 12 - prime) % 12
	return note

def normalizeRow(row):
	prime = row[0]
	newRow = []
	for item in row:
		newRow.append(calcNormalized(item, prime))
	return newRow

def randRemove(myList):
	index = random.randint(0, len(myList)-1)
	if len(myList) == 1:
		return myList.pop(0)
	return myList.pop(index)

def printRow(myRow):
	for item in myRow:
		print item

def simpleRowYielder():
	for x in range(0, 12):
		yield x

def InverseGenerator(myRow):
	myInverse = []
	for item in myRow:
		note = (12 - item) % 12
		myInverse.append(note)
	print "MyInverse is: ", myInverse
	return myInverse

def CalcMatrix(Prime, Inverse):
	myMatrix = Matrix(12, 12)
	myMatrix.setRow(0, Prime)
	for x in range(1, 12):
		offset = Inverse[x]
		myrow = calcRow(Prime, offset)
		#Add myrow to matrix
		myMatrix.setRow(x, myrow)
	print myMatrix

def calcRow(row, offset):
	#Add offset to prime
	newRow = []
	for item in row:
		 newRow.append((item + offset) % 12)
	return newRow

class Matrix(object):
	def __init__(self, cols, rows):
		self.cols = cols
		self.rows = rows

		self.Matrix = []
		for i in range(rows):
			ea_row = []
			for j in range(cols):
				ea_row.append(0)
			self.Matrix.append(ea_row)
	def getItem(self, col, row):
		return self.Matrix[col-1][row-1]

	def setItem(self, col, row, thing):
		self.Matrix[col-1][row-1] = thing

	def setRow(self, col, myRow):
		self.Matrix[col] = myRow

	def rowREPR(self, mylist):
		outstring = '[ '
		for item in mylist:
			outstring = outstring + str(item) + ',  '
		#Remove last comma
		outstring = outstring[0:-2]
		outstring = outstring + '] '
		return outstring

	def __repr__(self):
		outStr = ""
		for i in range(self.rows):
			outStr += 'Row %s \t = %s \n' % (i+1, self.rowREPR(self.Matrix[i]))
		return outStr


if __name__ == "__main__":
	P = RowGenerator()
	I = InverseGenerator(P)
	Matrix = CalcMatrix(P, I)
