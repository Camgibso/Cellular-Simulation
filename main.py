# Cameron Gibson
# R11424503
# Example terminal input: 
#python3 main.py -i matrix.txt -o outfile.txt -t 4

import sys, getopt

def parseCommandLine(argv=[]):
	argv = argv[1:]
	inputFile = ''
	outputFile = ''
	# Set Default = 1
	threadNum = '1'	

	try:
		  opts, args = getopt.getopt(argv, 'hi:o:t:')
	except getopt.GetoptError:
		print ("Requires -i <inputFile> -o <outputFile> -t <optionalThreads>")
		sys.exit(1)

	#Processing command line arguments
	#print opts
	for opt, arg in opts:
		opt = opt.lower()
		if opt in ("-h", "--help"):
			print ("Format: Main.py -i <inputFile> -o <outputFile> -t <numThreads>")
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputFile = arg 
		elif opt in ("-o", "--ofile"):
			outputFile = arg 
		elif opt in ("-t", "--threadNum"):
			threadNum = int(arg) 

	return inputFile, outputFile, threadNum


def main():
	inputFile, outputFile, threadNum = parseCommandLine(sys.argv)
	print ('Input file is   :', inputFile)
	print ('Output file is  :', outputFile)
	print ('Thread Number is:', threadNum)
	
	try:
		f = open(inputFile)
		# Read the file into lines
		lines = f.readlines()
		print ("File Contents:", lines)
		# Read a matrix from a file 

	#TODO:
	# search python f.read TypeError: argument should be integer or None, not 'str'
		#f.read(inputFile)

		f.close()

	# If file path DNE error
	except FileNotFoundError:
		print("File does not exist")
	
	# Write the matrix into a file
	try:
		with open(outputFile, 'w') as f:
			i = str(lines)
			f.write(i)
	
	# If file path DNE error
	except NotADirectoryError:
		print("Directory does not exist")

# For repl.it 
if __name__ == '__main__':
	main()