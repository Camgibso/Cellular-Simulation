# Cameron Gibson
# R11424503

import sys, getopt

def parseCommandLine(argv=[]):
    argv = argv[1:]
    inputFile = ''
    outputFile = ''
	# Default = 1
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
        
    print ('Input file is: ', inputFile)
    print ('Output file is: ', outputFile)
    print ('Thread Number is: ', threadNum)
	#return(inputFile)


def main():
	parseCommandLine(sys.argv)
	#print("Returned: ", inputFile)
	#try:
	#	f = open(inputfile)
		# Read a matrix from a file 
	#	f.read(inputfile)
    
	#	f.close()

	# If file path DNE error
	#except FileNotFoundError:
	#	print("File does not exist")
	
	# Write the matrix into a file
	#try:
	#	with open(outputfile, 'w') as f:
	#		f.write(outputfile)
	
	# If file path DNE error
	#except NotADirectoryError:
	#	print("Directory does not exist")

# For repl.it
if __name__ == '__main__':
	main()