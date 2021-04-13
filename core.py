# py2
import sys
import os
import re

def find_longest_strand(filename):
	file = open(filename, 'r') # read only

	maxlength = 0; offset = 0
	index = 0
	for line in file:
		l = len(line.rstrip())
		if l > maxlength:
			maxlength = l
			offset = index
		index += 1

	return [filename, maxlength, offset]

# enter the path of binary files
path = r"/Users/SY_Shirley/Desktop/Eluvio Challenge - Core Engineering/files"
os.chdir(path)

maxname = ''; maxlength = 0; maxoffset = 0
for file in os.listdir(path):
	name, length, offset = find_longest_strand(file)
	if length > maxlength:
		maxname = name
		maxlength = length
		maxoffset = offset

print("Filename: %s\nLength: %s\nOffset: %s" % (maxname, maxlength, maxoffset))
