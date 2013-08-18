from optparse import OptionParser


def get_options_args():
    parser = OptionParser()
    parser.add_option("-i", dest="inputFile", help="the file to remove tabs from")
    parser.add_option("-o", dest="outputFile", help="the output file")
    return parser.parse_args()


def rem_tabs_from_file():

    (options, args) = get_options_args()
    
    fileIn = open(options.inputFile, "r")
    fileOut = open(options.outputFile, "w")
    line = True
    count = 0

    while line:
        line = fileIn.readline()
        if line.find("\t") != -1:
    	count += 1

    	print count, "tab found"
            line = line.replace("\t", "    ")       

        fileOut.write( '{str}'.format(str=line) )
    
    fileOut.close()
    fileIn.close()


if __name__ == '__main__':
    rem_tabs_from_file()
