
#Moduels:
#	Globber to grab all the row files
#	Inversion row generator
#	Matrix outputter
#	Row generator

import random

def RowGenerator():
	rowGenerator = []
	myRow = []
	for item in simpleRowYielder():
		rowGenerator.append(item)
	for x in range(0, 12):
		myItem = randRemove(rowGenerator)
		myRow.append(myItem)
	print myRow
	return myRow


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
		note = 12 - item
		myInverse.append(note)
	print "MyInverse is: ", myInverse
	return myInverse

def CalcMatrix(Prime, Inverse):
	myMatrix = Matrix(12, 12)
	myMatrix.setRow(0, Prime)
	for x in range(12):
		offset = Inverse[x]
		print offset


	print myMatrix

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

	def __repr__(self):
		outStr = ""
		for i in range(self.rows):
			outStr += 'Row %s = %s \n' % (i+1, self.Matrix[i])
		return outStr


if __name__ == "__main__":
	P = RowGenerator()
	I = InverseGenerator(P)
	Matrix = CalcMatrix(P, I)
