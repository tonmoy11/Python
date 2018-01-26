from sys import *
#previously it was > from sys import argv
from os.path import exists
#

script, from_file, to_file = argv

print "Copying form %s tp %s" % (from_file, to_file)

#I could do these two on one line too, how?

in_file = open(from_file) #opens the from file which is test.txt
indata = in_file.read() #read the file from from_file

print "The input file is %d bytes long" % len(indata) #prints the size of file

print "Does the output file exists? %r" % exists(to_file) #does the file its going to write from the original file exists or not
print "Ready, hit RETURN to continue, CTRL-C tp abort."
raw_input() #takes input if you want to process the data or not.

out_file = open(to_file, 'wr') # changing the chmod and opening to_file to write
out_file.write(indata) # authoriz to write data from the exercise which was done before

print "Alright, all done."

out_file.close()
in_file.close()
