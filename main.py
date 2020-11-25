# Cameron Gibson
# R11424503

# Provides access to any command-line arguments via the sys.argv 
import sys, getopt


def main(argv):
	print("Project :: R11424503\n")
	
	# Set user args
	inputfile = ''
	outputfile = ''

	try:
  		opts, args = getopt.getopt(argv,"hi:o:", ["ifile=", "ofile="])
	except getopt.GetoptError:
		print ('test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
				print ('main.py -i <inputfile> -o <outputfile>')
				sys.exit()
		elif opt in ("-i", "--ifile"):
				inputfile = arg
		elif opt in ("-o", "--ofile"):
				outputfile = arg
	
	print ('Input file is: ', inputfile)
	print ('Output file is: ', outputfile)


	# Open if exists, if not error
	try:
		f = open(inputfile)
		# Read a matrix from a file 
		f.read()
    
		f.close()

	# If file path DNE error
	except FileNotFoundError:
		print("File does not exist")
	
	# Write the matrix into a file
	try:
		with open(outputfile, 'w') as f:
			f.write(outputfile)
	
	# If file path DNE error
	except DirNotFoundError:
		print("Directory does not exist")


if __name__ == '__main__':
    main(sys.argv[1:])


#TODO:
# Read only O's and .'s else error

# Validate user args
# get -> define -> retrieve

# If an “alive” square has exactly two, three, or four living neighbors, then it continues to be “alive” in the next time step.

# If a “dead” square has an even number greater than 0 living neighbors, then it will be “alive” in the next time step.

# Every other square dies or remains dead, causing it to be “dead” in the next time step.
