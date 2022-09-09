# Worked on in lab
# Lab 03: https://legacy.cs.indiana.edu/classes/a310-dgerman/fall2022/lab03.html
# For more help please view: http://silo.cs.indiana.edu:31415/a310/fall2022/lab03.phps


a = True
b = True

if not (a and b) == (not a) or (not b):
	print("Test 1: True")

if not ((not a) or (not b)):
	print("Test 2: True")

def letter(grade):
    if grade > 4:
        return "too big"
    elif grade == 4:
        return "A"
    elif grade >= 3.7:
        return "A-"
    elif grade >= 3.4:
        return "B+"
    elif grade >= 3.1:
        return "B"
    elif grade >= 2.8:
        return "B-"
    elif grade >= 2.5:
        return "C+"
    elif grade >= 2.2:
        return "C"
    elif grade >= 1.9:
        return "C-"
    elif grade >= 1.6:
        return "D+"
    elif grade >= 1.3:
        return "D"
    elif grade >= 1:
        return "D-"
    else:
        return "F"

class Year:
	def __init__(self, year):
		self.year = year
	def isLeapYear(self):
		if year < 1582:
			return year % 4 == 0
		else:
			if year % 4 == 0:
				if year % 100 == 0:
					if year % 400 == 0:
						return True
					else:
						return False
				else:
					return True
			else:
				return False



# Scalable Four

size = int(input("Please enter the size: "))

if size % 2 == 0:
	for line in range(size):
	  for column in range(size):
	    if line + column == size / 2 or \
	       line == size / 2 and column <= 3 * size / 4 or \
	       column == size / 2 and line >= size / 4:
	        print(" *", end='')
	    else:
	      print("  ", end="")
	  print()
else:
	print("not a valid scalable four size")

# Magic square
import random 

def magic(n):
	m = []

	for i in range(n):
		m.append([0] * n)

	row, col = n-1, n//2

	for k in range(0, n*n):
		m[row][col], newRow, newCol = (k+1), (row + 1) % n, (col + 1) % n
		if m[newRow][newCol] == 0: 
			row, col = newRow, newCol
		else:
			row, col = row - 1, col 
	return m

def show(m): 
	for i in range(len(m)):
		for j in range(len(m)):
			print("  " + str(m[i][j])[-3:], end='')
		print()

z = int(input("Enter size of matrix: "))

if z % 2 == 1:
	l = magic(z)
	show(l)
else:
	print("Not a valid square dimension")


