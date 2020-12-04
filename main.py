# Cameron Gibson | Final Project
# R11424503
# Example terminal input: 
# python3 main.py -i matrix.txt -o outfile.txt -t 1

# Imports and Globals
import multiprocessing
import time
import sys
import getopt
fileArray = []
rows = 0
columns = 0

# Function to parse command line args
def parseCommandLine(argv=[]):
	argv = argv[1:]
	inputFile = ''
	outputFile = ''
	# Set default = 1
	threadNum = '1'	
	
	try:
		opts, args = getopt.getopt(argv, 'hi:o:t:')
	except getopt.GetoptError:
		print("Format: Main.py -i <inputFile> -o <outputFile> -t <threadNum>")
		sys.exit(1)

	#Processing command line arguments
	for opt, arg in opts:
		opt = opt.lower()
		if opt in ("-h", "--help"):
			print("Format: Main.py -i <inputFile> -o <outputFile> -t <threadNum>")
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputFile = arg 
		elif opt in ("-o", "--ofile"):
			outputFile = arg 
		elif opt in ("-t", "--threadNum"):
			threadNum = int(arg)
	return inputFile, outputFile, int(threadNum)

# Reads input file line into array
def readLine(line):
	line = line.strip()
	return list(line)

# Temporary matrix for saving 3 rows 
def tempMatrix(matrix):
	nMatrix = list()
	for row in range(rows):
		# Previous, working, next
		holder = [matrix[(row - 1) % rows], matrix[row], matrix[(row + 1) % rows]]
		nMatrix.append(holder)
	matrix = ''
	return nMatrix

# Append the row in the matrix and return an array
def simulation(array):
	global columns, fileArray
	fileArray = array
	columns = len(fileArray[0])
	modifiedArray = list()
	for y in range(columns):    
		modifiedArray += find_neighbor(fileArray[1][y], y)
	return modifiedArray

# Find the eight neighbors
def find_neighbor(cell, currentCol):
	nArray = [0, 0, 0, 0, 0, 0, 0, 0]

	# Grab the left and right Column
	nLeft = (currentCol - 1) % columns
	nRight = (currentCol + 1) % columns

	# Set all neighbors in the array
	nArray = [fileArray[0][nLeft], fileArray[0][(currentCol)], fileArray[0][nRight], fileArray[1][nLeft], 
	fileArray[1][nRight], fileArray[2][nLeft], fileArray[2][(currentCol)], fileArray[2][nRight]]

	nAlive = nArray.count('O')

	# Checking conditions for if cell should be alive on given rules
	if cell == 'O' and (2 == nAlive or 3 == nAlive or nAlive == 4):
		status = 'O'
	elif cell == '.'and nAlive % 2 == 0 and nAlive > 0 :
		status = 'O'
	else:
		status = '.'
	return status

# Append the row in the matrix and return a string
def matrixToString(array):
	global columns, fileArray
	fileArray = array
	columns = len(fileArray[0])
	# Read into a string
	finalString = ''
	for y in range(columns):    
		finalString += find_neighbor(fileArray[1][y], y)
	# Row break
	finalString = finalString + '\n'
	return finalString


def main():
	global fileArray, rows

	# Parse the command line arguments
	inputFile, outputFile, threadNum = parseCommandLine(sys.argv)
	print ("Input file is:", inputFile)
	print ("Output file is:", outputFile)
	print ("Thread Number is:", threadNum, "\n")
	pool = multiprocessing.Pool(processes = threadNum)

	# Open the input file and start reading it
	try:
		with open(inputFile) as f:
			print("Time Step #0: ")
			for line in f:
				print(line, end="")
			f.seek(0)
			fileArray = pool.map(readLine, f)
	except FileNotFoundError:
		print("File does not exist")
		sys.exit()
	print("\n")

	# Simulate the next 100 steps by checking cell
	rows = len(fileArray)
	tempArray = tempMatrix(fileArray) 
	for _ in range(99):
		tempArray = pool.map(simulation, tempArray)
		tempArray = tempMatrix(tempArray)
	# Convert to string
	tempArray = pool.map(matrixToString, tempArray)
	finalString = ''.join(tempArray)
	
	# Create an output file with the given arg as its name
	try:
		with open(outputFile, 'w') as f:
			print("\nTime Step #100: \n", finalString)
			f.write(finalString)
			print("Simulation complete. Final result stored in the output file:", outputFile)	
	except NotADirectoryError:
		print("Directory does not exist")
		sys.exit()


if __name__ == "__main__":
	print("Program :: R11424503")
	start_time = time.time()
	main()
	print("Execution Time:", (time.time() - start_time), "secounds")