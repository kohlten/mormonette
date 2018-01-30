from subprocess import Popen, PIPE
from sys import exit
from os import chdir
import ctypes

#-------------ex00----------------#
try:
	chdir("work/ex00")
except OSError:
	print("Done")
	exit(1)



