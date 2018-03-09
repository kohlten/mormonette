#!/usr/bin/python
from subprocess import Popen, PIPE
from os import listdir, chdir
from ctypes import *
from sys import exit, argv, settrace

settrace
option_i = 0
main = ["int main() {\n\t", "\n\treturn 0;\n}"]
text_putchar = "#include <unistd.h>\n\nvoid ft_putchar(char c)\n{\n\twrite(1, &c, 1);\n}"
if len(argv) > 1:
	if "-i" in argv:
		option_i = 1

#--------------ex00-----------------#
try:
	chdir ("work/ex00")
except OSError:
	print("Done")
	exit(0)

open("ft_putchar.c", "w").write(text_putchar)
open("main.c", "w").write("void ft_putstr(char *str);\n\n" + main[0] + "ft_putstr(\"Hello world!!!!!!!!!!\");" + main[1])

#compile the file with the main
pipe = Popen("gcc -o ft_putstr ft_putstr.c ft_putchar.c main.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Compilation failed on ex00:")
	print(err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	pipe = Popen(["./ft_putstr"], stdout=PIPE)
	output = pipe.communicate()[0]
	if output != "Hello world!!!!!!!!!!":
		print("Error:\nex00 is not right:\n" + output)
		print("Expected:\nHello world!!!!!!!!!!")
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)

	print("ex00 RIGHT! One smart for you!")
#--------------ex01-----------------#
try:
	chdir ("../ex01")
except OSError:
	print("Done")
	exit(0)

open("ft_putchar.c", "w").write(text_putchar)
open("main.c", "w").write("void ft_putnbr(int nb);\nvoid ft_putchar(char c);\n\n" + main[0] + "ft_putnbr(42);\n\tft_putchar(' ');\n\tft_putnbr(-42);\n\tft_putchar(' ');\n\tft_putnbr(0);\n\tft_putchar(' ');\n\tft_putnbr(2147483647);\n\tft_putchar(' ');\n\tft_putnbr(-2147483648);" + main[1])

#compile the file with the main
pipe = Popen("gcc -o ft_putnbr ft_putnbr.c ft_putchar.c main.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Compilation failed on ex01:")
	print(err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	pipe = Popen(["./ft_putnbr"], stdout=PIPE)
	output = pipe.communicate()[0]
	if output != "42 -42 0 2147483647 -2147483648":
		print("Error:\nex01 is not right:\n" + output)
		print("Expected:\n42 -42 0 2147483647 -2147483648")
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)

	print("ex01 RIGHT! One smart for you!")
#--------------ex02-----------------#
try:
	chdir("../ex02")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_atoi ft_atoi.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex02.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_atoi")
	ft_atoi = lib.ft_atoi
	ft_atoi.argstypes = [c_char_p]
	ft_atoi.restype = c_int
	awnsers = [42, -42, 0, 0, 2147483647, -2147483648, 123]
	tests = []
	strings = ["42", "-42", "0", "abc42abc", "2147483647", "-2147483648", "    \t\n\v\r\f+123"]
	for string in strings:
		tests.append(ft_atoi(string))

	if tests != awnsers:
		print("Error: ex02 failed!\nI got:\n" + str(tests))
		print("I expected:\n" + str(awnsers))
		print("My strings were:\n" + str(strings))
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex02 RIGHT! One smart for you!")
#--------------ex03-----------------#
try:
	chdir("../ex03")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_strcpy ft_strcpy.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex03.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_strcpy")
	val = create_string_buffer(7)
	ft_strcpy = lib.ft_strcpy
	ft_strcpy.argstypes = [c_char_p, c_char_p]
	ft_strcpy.restype = c_char_p
	val = ft_strcpy(val, "Jello!")
	if val != "Jello!":
		print("Error: ex03 failed!\nI got:\n" + val)
		print("I expected:\nJello!")
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex03 RIGHT! One smart for you!")
#--------------ex04-----------------#
try:
	chdir("../ex04")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_strncpy ft_strncpy.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex04.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_strncpy")
	val = create_string_buffer(7)
	ft_strncpy = lib.ft_strncpy
	ft_strncpy.argstypes = [c_char_p, c_char_p, c_uint]
	ft_strncpy.restype = c_char_p
	val = ft_strncpy(val, "Jello World!", 5)
	if val != "Jello":
		print("Error: ex04 failed!\nI got:\n" + val)
		print("I expected:\nJello!")
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex04 RIGHT! One smart for you!")
#--------------ex05-----------------#
try:
	chdir("../ex05")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_strstr ft_strstr.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex05.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_strstr")
	ft_strstr = lib.ft_strstr
	ft_strstr.argstypes = [c_char_p, c_char_p]
	ft_strstr.restype = c_char_p
	tests = ""
	tests += ft_strstr("Jello World!", "W") + '\n'
	tests += ft_strstr("Jello World!", "e")
	test1 = ft_strstr("", "W")
	test0 = ft_strstr("Jello World!", "Z")
	if tests != "World!\nello World!" or test0 != None or test1 != None:
		print("Error: ex05 failed!\nI got:\n" + tests + " " + str(test0) + " " + str(test1))
		print("I expected:\nWorld!\nello World! " + str(test0) + " " + str(test1))
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex05 RIGHT! One smart for you!")
#--------------ex06-----------------#
try:
	chdir("../ex06")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_strcmp ft_strcmp.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex06.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_strcmp")
	ft_strcmp = lib.ft_strcmp
	ft_strcmp.argstypes = [c_char_p, c_char_p]
	ft_strcmp.restype = c_int
	tests = []
	awnsers = [0, 32, 111, -1]
	tests.append(ft_strcmp("Jello World!", "Jello World!"))
	tests.append(ft_strcmp("Jello World!", "Jello"))
	tests.append(ft_strcmp("Jello World!", "Jello W"))
	tests.append(ft_strcmp("A", "B"))
	if tests != awnsers:
		print("Error: ex06 failed!\nI got:\n" + str(tests))
		print("I expected:\n" + str(awnsers))
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex06 RIGHT! One smart for you!")
#--------------ex07-----------------#
try:
	chdir("../ex07")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_strncmp ft_strncmp.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex07.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_strncmp")
	ft_strncmp = lib.ft_strncmp
	ft_strncmp.argstypes = [c_char_p, c_char_p, c_uint]
	ft_strncmp.restype = c_int
	tests = []
	awnsers = [0, 0, 111, -1]
	tests.append(ft_strncmp("Jello World!", "Jello World!", 13))
	tests.append(ft_strncmp("Jello World!", "Jello", 5))
	tests.append(ft_strncmp("Jello World!", "Jello W", 8))
	tests.append(ft_strncmp("A", "B", 1))
	if tests != awnsers:
		print("Error: ex07 failed!\nI got:\n" + str(tests))
		print("I expected:\n" + str(awnsers))
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex07 RIGHT! One smart for you!")
#--------------ex08-----------------#
try:
	chdir("../ex08")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_strupcase ft_strupcase.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex08.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_strupcase")
	ft_strupcase = lib.ft_strupcase
	ft_strupcase.argstypes = [c_char_p, c_char_p, c_uint]
	ft_strupcase.restype = c_char_p
	tests = []
	awnsers = ["JELLO WORLD!", "JELLO WORLD!", "JELLO WORLD!"]
	tests.append(ft_strupcase("Jello World!"))
	tests.append(ft_strupcase("JeLlO WoRlD!"))
	tests.append(ft_strupcase("jello world!"))
	if tests != awnsers:
		print("Error: ex08 failed!\nI got:\n" + str(tests))
		print("I expected:\n" + str(awnsers))
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex08 RIGHT! One smart for you!")
#--------------ex09-----------------#
try:
	chdir("../ex09")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_strlowcase ft_strlowcase.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex09.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_strlowcase")
	ft_strlowcase = lib.ft_strlowcase
	ft_strlowcase.argstypes = [c_char_p, c_char_p, c_uint]
	ft_strlowcase.restype = c_char_p
	tests = []
	awnsers = ["jello world!", "jello world!", "jello world!"]
	tests.append(ft_strlowcase("Jello World!"))
	tests.append(ft_strlowcase("JeLlO WoRlD!"))
	tests.append(ft_strlowcase("jello world!"))
	if tests != awnsers:
		print("Error: ex09 failed!\nI got:\n" + str(tests))
		print("I expected:\n" + str(awnsers))
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex09 RIGHT! One smart for you!")
#--------------ex10-----------------#
try:
	chdir("../ex10")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_strcapitalize ft_strcapitalize.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex10.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_strcapitalize")
	ft_strcapitalize = lib.ft_strcapitalize
	ft_strcapitalize.argstypes = [c_char_p]
	ft_strcapitalize.restype = c_char_p
	tests = []
	awnsers = ["Hello World!", "Salut, Comment Tu Vas ? 42mots Quarante-Deux; Cinquante+Et+En", "Hello World, I'm Currently Developing At The 42 Campus!"]
	tests.append(ft_strcapitalize("hello world!"))
	tests.append(ft_strcapitalize("salut, comment tu vas ? 42mots quarante-deux; cinquante+et+un"))
	tests.append(ft_strcapitalize("hello WORLD, i'm currently developing at the 42 campus!"))
	if tests != awnsers:
		print("Error: ex10 failed!\nI got:")
		for test in tests:
			print(test)
		print("I expected:")
		for awnser in awnsers:
			print(awnser)
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex10 RIGHT! One smart for you!")
#--------------ex11-----------------#
try:
	chdir("../ex11")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_str_is_alpha ft_str_is_alpha.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex11.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_str_is_alpha")
	ft_str_is_alpha = lib.ft_str_is_alpha
	ft_str_is_alpha.argstypes = [c_char_p]
	ft_str_is_alpha.restype = c_int
	tests = []
	awnsers = [1, 0, 0]
	tests.append(ft_str_is_alpha("HelloWorld"))
	tests.append(ft_str_is_alpha("12334abs"))
	tests.append(ft_str_is_alpha("!+DSJDHSADA!+"))
	if tests != awnsers:
		print("Error: ex11 failed!\nI got:")
		for test in tests:
			print(test),
		print("\nI expected:")
		for awnser in awnsers:
			print(awnser),
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex11 RIGHT! One smart for you!")
#--------------ex12-----------------#
try:
	chdir("../ex12")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_str_is_numeric ft_str_is_numeric.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex12.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_str_is_numeric")
	ft_str_is_numeric = lib.ft_str_is_numeric
	ft_str_is_numeric.argstypes = [c_char_p]
	ft_str_is_numeric.restype = c_int
	tests = []
	awnsers = [0, 1, 0]
	tests.append(ft_str_is_numeric("HelloWorld"))
	tests.append(ft_str_is_numeric("12334"))
	tests.append(ft_str_is_numeric("!+DSJDHSADA!+"))
	if tests != awnsers:
		print("Error: ex12 failed!\nI got:")
		for test in tests:
			print(test),
		print("\nI expected:")
		for awnser in awnsers:
			print(awnser),
		print("\nDUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex12 RIGHT! One smart for you!")
#--------------ex13-----------------#
try:
	chdir("../ex13")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_str_is_lowercase ft_str_is_lowercase.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex13.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_str_is_lowercase")
	ft_str_is_lowercase = lib.ft_str_is_lowercase
	ft_str_is_numeric.argstypes = [c_char_p]
	ft_str_is_numeric.restype = c_int
	tests = []
	awnsers = [1, 0, 0]
	tests.append(ft_str_is_lowercase("helloworld"))
	tests.append(ft_str_is_lowercase("13334"))
	tests.append(ft_str_is_lowercase("!+DSJDHSADA!+"))
	if tests != awnsers:
		print("Error: ex13 failed!\nI got:")
		for test in tests:
			print(test),
		print("\nI expected:")
		for awnser in awnsers:
			print(awnser),
		print("\nDUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex13 RIGHT! One smart for you!")
#--------------ex14-----------------#
try:
	chdir("../ex14")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_str_is_uppercase ft_str_is_uppercase.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex14")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_str_is_uppercase")
	ft_str_is_uppercase = lib.ft_str_is_uppercase
	ft_str_is_uppercase.argstypes = [c_char_p]
	ft_str_is_uppercase.restype = c_int
	tests = []
	awnsers = [1, 0, 0]
	tests.append(ft_str_is_uppercase("HELLOWORLD"))
	tests.append(ft_str_is_uppercase("13334"))
	tests.append(ft_str_is_uppercase("!+DSJDHSADA!+"))
	if tests != awnsers:
		print("Error: ex14 failed!\nI got:")
		for test in tests:
			print(test),
		print("\nI expected:")
		for awnser in awnsers:
			print(awnser),
		print("\nDUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex14 RIGHT! One smart for you!")
#--------------ex15-----------------#
try:
	chdir("../ex15")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_str_is_printable ft_str_is_printable.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex15")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_str_is_printable")
	ft_str_is_printable = lib.ft_str_is_printable
	ft_str_is_printable.argstypes = [c_char_p]
	ft_str_is_printable.restype = c_int
	tests = []
	awnsers = [0, 1, 1]
	tests.append(ft_str_is_printable("\nHEY\n\v\t\f"))
	tests.append(ft_str_is_printable("13334"))
	tests.append(ft_str_is_printable("!+DSJDHSADA!+"))
	if tests != awnsers:
		print("Error: ex15 failed!\nI got:")
		for test in tests:
			print(test),
		print("\nI expected:")
		for awnser in awnsers:
			print(awnser),
		print("\nDUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex15 RIGHT! One smart for you!")
#--------------ex16-----------------#
try:
	chdir("../ex16")
except OSError:
	print("Done")
	if option_i == 0:
		exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_strcat ft_strcat.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex16")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_strcat")
	ft_strcat = lib.ft_strcat
	ft_strcat.argstypes = [c_char_p, c_char_p]
	ft_strcat.restype = c_char_p
	tests = []
	awnsers = ["Hello World!", "SFDJKHFKSJDHFKJSHDKJFHSD1234\n"]
	tests.append(ft_strcat("Hello ", "World!"))
	tests.append(ft_strcat("SFDJKHFKSJD" , "HFKJSHDKJFHSD1234\n"))
	if tests != awnsers:
		print("Error: ex16 failed!\nI got:")
		for test in tests:
			print(test),
		print("\nI expected:")
		for awnser in awnsers:
			print(awnser),
		print("\nDUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex16 RIGHT! One smart for you!")
#--------------ex17-----------------#
#WIP
#try:
#print "got"
#chdir("../ex17")
#print "Here"
#except OSError:
#	print("Done")
#	if option_i == 0:
#		exit(1)
#pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_strncat ft_strncat.c".split(" "), stdout=PIPE, stderr=PIPE)
#output, err = pipe.communicate()

#if err != "":
#	print("Failed to compile on ex17")
#	print("Heres the error:\n " + err)
#	print("DUM DUM DUM DUM DUM DUM")
#	if option_i == 0:
#		exit(1)
'''else:
	lib = CDLL("./ft_strncat")
	ft_strncat = lib.ft_strncat
	ft_strncat.argstypes = [c_char_p, c_char_p, c_int]
	ft_strncat.restype = c_char_p
	tests = []
	awnsers = ["Hello W", "SFDJKHFKSJDHFKJ"]
	tests.append(ft_strncat("Hello ", "World!", 1))
	tests.append(ft_strncat("SFDJKHFKSJD" , "HFKJSHDKJFHSD1234\n", 20))
	print tests, "HI"
	if tests != awnsers:
		print("Error: ex17 failed!\nI got:")
		for test in tests:
			print(test),
		print("\nI expected:")
		for awnser in awnsers:
			print(awnser),
		print("\nDUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	else:
		print("ex17 RIGHT! One smart for you!")'''