#!/usr/bin/python
import os, sys, subprocess

location = ""
if len(sys.argv) > 1:
	location = sys.argv[1]
else: 
	for loc in os.listdir("."):
		if "day" in loc and len(loc) == 5:
			location = loc
			break

if location == "":
	print("Failed to find a dayXX folder!")
	sys.exit(1)
folders = os.listdir(location)
folders_to_be_copied = []
files_to_be_copied = []

if "work" not in os.listdir("."):
	os.mkdir("work")

if "ex00" in os.listdir("./work"):
	f = os.listdir("work")
	for i in range(len(f)):
		subprocess.call(["rm", "-Rf", "work/" + f[i]])

for i in range(len(folders)):
	if folders[i][0:2] == "ex":
		folders_to_be_copied.append(folders[i])
		files = os.listdir(location + '/' + folders[i])

		for j in range(len(files)):
			files_to_be_copied.append(folders[i] + '/' + files[j])

for i in range(len(folders_to_be_copied)):
	os.mkdir("work/" + folders_to_be_copied[i])

files_data = []
for i in range(len(files_to_be_copied)):
	file = open(location + '/' + files_to_be_copied[i], 'r')
	files_data.append(file.read())
	file.close()

for i in range(len(files_data)):
	file = open("work/" + files_to_be_copied[i], "w")
	file.write(files_data[i])
	file.close()
	file = "work/" + files_to_be_copied[i][:len(files_to_be_copied[i]) - 1]

subprocess.call(["python", "config_" + location + ".py"])
