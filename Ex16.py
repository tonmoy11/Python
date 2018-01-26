from sys import argv

#arguments that we shall pass
script, filename = argv

#taking the file to be edited _filename
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL- C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
print "Opening the file..."
target = open(filename, 'w') #w stands for writing the file, like in unix rwx
#once you pass the name of your targeted file it will open it.
#asd = open(filename) #this is a demo if I want it to work it will pass ass.write(line1)

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")#input each line for text.txt
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1) #on the created file it will write the lines as line1, line2, line3
target.write("\n")

target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
