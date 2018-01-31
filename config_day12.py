#!/usr/bin/python

import subprocess
import os
import sys

#--------------------------ex01--------------------------
os.chdir("work/ex00")
text = "Hello world!\n" * 10
file = open("test.txt", "w")
file.write(text);
file.close()

#Make
pipe = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = pipe.communicate()[0]

if "ft_display_file" not in os.listdir("."):
	print("ex00: " + output)
	print("DUM DUM DUM DUM DUM DUM: Make FAILED. File ft_display_file not found. " + ' '.join(os.listdir(".")))
	sys.exit(1)

subprocess.call(["chmod", "u+x", "ft_display_file"])
#Display output text of files

pipe = subprocess.Popen(["./ft_display_file"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = pipe.communicate()[0]

if output != "File name missing.\n":
	print("Error on ex00")
	print("I GOT: " + output.replace("\n", "\\n"))
	print("WHAT I EXPECTED: File name missing\\n")
	print("DUM DUM DUM DUM DUM DUM!")
	sys.exit(1);

pipe = subprocess.Popen(["./ft_display_file", "T", "T"], stdout=subprocess.PIPE)
output = pipe.communicate()[0]

if output != "Too many arguments.\n":
	print("Error on ex00")
	print("I GOT: " + output.replace("\n", "\\n"))
	print("WHAT I EXPECTED: Too many arguments.\\n")
	print("DUM DUM DUM DUM DUM DUM!")
	sys.exit(1);

pipe = subprocess.Popen(["./ft_display_file", "Makefile"], stdout=subprocess.PIPE)
output = pipe.communicate()[0]

if output != "*contenu du Makefile*\n":
	print("Error on ex00")
	print("I GOT: " + output.replace("\n", "\\n"))
	print("WHAT I EXPECTED: *contenu du Makefile*\\n")
	print("DUM DUM DUM DUM DUM DUM!")
	sys.exit(1);

#Actually test shit
pipe = subprocess.Popen(["./ft_display_file", "test.txt"], stdout=subprocess.PIPE)
output = pipe.communicate()[0]

if output != text:
	print("Error on ex00")
	print("I GOT: \n" + output.replace("\n", "\\n"))
	print("WHAT I EXPECTED: \n" + text.replace("\n", "\\n"))
	print("DUM DUM DUM DUM DUM DUM!")
	sys.exit(1);

#Clean up
pipe = subprocess.Popen(["make", "clean"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = pipe.communicate()[0]

if "ft_display_file" in os.listdir("."):
	print("Erorr on ex00")
	print(output)
	print("DUM DUM DUM DUM DUM DUM: Make FAILED. ft_display_file still found! " + ' '.join(os.listdir(".")))
	sys.exit(1)

print("ex00 GOOD!!! One smart for you!")
#--------------------------ex01--------------------------
def check_diff(str1, str2):
	j = 0
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			return (i)
	return (-1)
os.chdir("../ex01")
file = open("test.txt", "w")
file.write(text);
file.close()

#Make
pipe = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = pipe.communicate()[0]

if "ft_cat" not in os.listdir("."):
	print("Erorr on ex01")
	print(output)
	print("DUM DUM DUM DUM DUM DUM: Make FAILED. File ft_cat not found. " + ' '.join(os.listdir(".")))
	sys.exit(1)

subprocess.call(["chmod", "u+x", "ft_cat"])
#Test opening files
pipe = subprocess.Popen(["./ft_cat", "test.txt"], stdout=subprocess.PIPE)
output = pipe.communicate()[0]

if output != text:
	print("Erorr on ex01")
	print(len(output), len(text))
	print("I GOT: \n" + output.replace("\n", "\\n"))
	print("WHAT I EXPECTED: \n" + text.replace("\n", "\\n"))
	print("DUM DUM DUM DUM DUM DUM!")
	sys.exit(1);

#Test reading from stdin
pipe = subprocess.Popen(["echo", text], stdout=subprocess.PIPE)
pipe = subprocess.Popen(["./ft_cat"], stdin=pipe.stdout, stdout=subprocess.PIPE)
output = pipe.communicate()[0]

if output[0:len(output)-1] != text:
	print("Erorr on ex01")
	print(len(output), len(text))
	print("I GOT: \n" + output.replace("\n", "\\n"))
	print("WHAT I EXPECTED: \n" + text.replace("\n", "\\n"))
	print("DUM DUM DUM DUM DUM DUM!")
	sys.exit(1);

#Clean up
pipe = subprocess.Popen(["make", "clean"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = pipe.communicate()[0]

if "ft_cat" in os.listdir("."):
	print(output)
	print("DUM DUM DUM DUM DUM DUM: Make FAILED. ft_cat still found! " + ' '.join(os.listdir(".")))
	sys.exit(1)

print("ex01 GOOD!!! One smart for you!")
