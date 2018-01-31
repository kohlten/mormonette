#!/usr/bin/python
from subprocess import Popen, PIPE
from sys import exit, argv
from os import chdir
import ctypes

option_i = 0
main = ["int main() {\n\t", "\n\treturn 0;\n}"]
text_putchar = "#include <unistd.h>\n\nvoid ft_putchar(char c)\n{\n\twrite(1, &c, 1);\n}"
if len(argv) > 1:
	if "-i" in argv:
		option_i = 1

#--------------ex00-----------------#
try:
	chdir("work/ex00")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_ft ft_ft.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex00.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)

val = ctypes.c_int(9)
lib = ctypes.CDLL("./ft_ft")
ft_ft = lib.ft_ft
ft_ft.argstypes = [ctypes.POINTER(ctypes.c_int)]
ft_ft.restype = None
ft_ft(ctypes.byref(val))

if val.value != 42:
	print("Error: ex00 failed!\nI got " + str(val.value) + "\nI expected 42")
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
print("ex00 RIGHT! One smart for you!")
#--------------ex01-----------------#
try:
	chdir("../ex01")
except OSError:
	print("Done")
	exit(1)

#Pleasssssssseeee, dont actually check this one yourself. It is cancer incarnate! I'm dying on the inside writing this.
open("main.c", "w").write("#include <stdio.h>\nvoid ft_ultimate_ft(int *********nbr);\n\n" + main[0] + "int a = 15;\n\tint* b = &a;\n\tint** c = &b;\n\tint*** d = &c;\n\tint**** e = &d;\n\tint***** f = &e;\n\tint****** g = &f;\n\tint******* h = &g;\n\tint******** i = &h;\n\tint********* j = &i;\n\tft_ultimate_ft(j);\n\tprintf(\"%d\", a);" + main[1])
pipe = Popen("gcc -Wall -Wextra -Werror -o ft_ultimate_ft ft_ultimate_ft.c main.c".split(" "), stderr=PIPE)
err = pipe.communicate()[1]

if err != "":
	print("Compiling failed on ex01!")
	print(err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)

pipe = Popen(["./ft_ultimate_ft"], stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()
if output != "42":
	print("Error: ex01 failed!\nI got " + output + "\nI expected 42")
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

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_swap ft_swap.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex02.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)

x = ctypes.c_int(10)
y = ctypes.c_int(20)
lib = ctypes.CDLL("./ft_swap")
ft_swap = lib.ft_swap
ft_swap.argstypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
ft_swap.restype = None
ft_swap(ctypes.byref(x), ctypes.byref(y))

if x.value != 20 and y.value != 10:
	print("Error: ex02 failed!\nI got x:" + str(x.value) + " y: " + str(y.value) + "\nI expected 20 10")
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
print("ex02 RIGHT! One smart for you!")
#--------------ex03-----------------#
try:
	chdir("../ex03")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_div_mod ft_div_mod.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex03.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)

x = ctypes.c_int(20)
y = ctypes.c_int(3)
div = ctypes.c_int(0)
mod = ctypes.c_int(0)
lib = ctypes.CDLL("./ft_div_mod")
ft_div_mod = lib.ft_div_mod
ft_div_mod.argstypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
ft_div_mod.restype = None
ft_div_mod(x, y, ctypes.byref(div), ctypes.byref(mod))

if div.value != 6 or mod.value != 2:
	print("Error: ex03 failed!\nI got div: " + str(div.value) + " mod: " + str(mod.value) + "\nI expected div: 6 mod: 2")
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
print("ex03 RIGHT! One smart for you!")
#--------------ex04-----------------#
try:
	chdir("../ex04")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_ultimate_div_mod ft_ultimate_div_mod.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex04.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)

x = ctypes.c_int(20)
y = ctypes.c_int(3)
lib = ctypes.CDLL("./ft_ultimate_div_mod")
ft_ultimate_div_mod = lib.ft_ultimate_div_mod
ft_ultimate_div_mod.argstypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
ft_ultimate_div_mod.restype = None
ft_ultimate_div_mod(ctypes.byref(x), ctypes.byref(y))

if x.value != 6 or y.value != 2:
	print("Error: ex04 failed!\nI got x: " + str(x.value) + " x: " + str(x.value) + "\nI expected x: 6 y: 2")
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
print("ex04 RIGHT! One smart for you!")
#--------------ex05-----------------#
try:
	chdir("../ex05")
except OSError:
	print("Done")
	exit(1)

open("ft_putchar.c", "w").write(text_putchar)
open("main.c", "w").write("\nvoid ft_putstr(char *str);\n\n" + main[0] + "ft_putstr(\"Hello world!\\n\");\n\tft_putstr(\"test1\\n\");\n\tft_putstr(\"test2\\n\");\n\tft_putstr(\"\");\n\tft_putstr(\"\");" + main[1])
pipe = Popen("gcc -Wall -Wextra -Werror -o ft_putstr ft_putstr.c ft_putchar.c main.c".split(" "), stderr=PIPE)
err = pipe.communicate()[1]

if err != "":
	print("Compiling failed on ex05!")
	print(err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)

pipe = Popen(["./ft_putstr"], stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()
if output != "Hello world!\ntest1\ntest2\n":
	print("Error: ex05 failed!\nI got: \n" + output + "\nI expected:\nHello world!\ntest1\ntest2\n")
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
print("ex05 RIGHT! One smart for you!")
#--------------ex06-----------------#
try:
	chdir("../ex06")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_strlen ft_strlen.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex06.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)

lib = ctypes.CDLL("./ft_strlen")
ft_strlen = lib.ft_strlen
ft_strlen.argstypes = [ctypes.c_char_p]
ft_strlen.restype = ctypes.c_int
len1 = ft_strlen("Hey")
len2 = ft_strlen("")
len3 = ft_strlen("THE WORLD!")

if len1 != 3 or len2 != 0 or len3 != 10:
	print("Error: ex06 failed!\nI got len1: " + str(len1) + " len2: " + str(len2) + " len3: " + str(len3) + "\nI expected len1: 3 len2: 0 len3: 10")
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
print("ex06 RIGHT! One smart for you!")
#--------------ex07-----------------#
try:
	chdir("../ex07")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_strrev ft_strrev.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex07.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)

lib = ctypes.CDLL("./ft_strrev")
ft_strrev = lib.ft_strrev
ft_strrev.argstypes = [ctypes.c_char_p]
ft_strrev.restype = ctypes.c_char_p
test1 = ft_strrev("abc")
test2 = ft_strrev("9876543210")

if test1 != "cba" or test2 != "0123456789":
	print("Error: ex07 failed!\nI got:\n" + test1 + " " + test2)
	print("I expected:\ncba 01234567890")
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
print("ex07 RIGHT! One smart for you!")
#--------------ex08-----------------#
try:
	chdir("../ex08")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_atoi ft_atoi.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex08.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)

lib = ctypes.CDLL("./ft_atoi")
ft_atoi = lib.ft_atoi
ft_atoi.argstypes = [ctypes.c_char_p]
ft_atoi.restype = ctypes.c_int
awnsers = [42, -42, 0, 0, 2147483647, -2147483648, 123]
tests = []
strings = ["42", "-42", "0", "abc42abc", "2147483647", "-2147483648", "    \t\n\v\r\f+123"]
for string in strings:
	tests.append(ft_atoi(string))

if tests != awnsers:
	print("Error: ex08 failed!\nI got:\n" + str(tests))
	print("I expected:\n" + str(strings))
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
print("ex08 RIGHT! One smart for you!")
#--------------ex09-----------------#
try:
	chdir("../ex09")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_sort_integer_table ft_sort_integer_table.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex09.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)

lib = ctypes.CDLL("./ft_sort_integer_table")
ft_sort_integer_table = lib.ft_sort_integer_table
ft_sort_integer_table.argstypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
ft_sort_integer_table.restype = None
arr = (ctypes.c_int * 3)
array = arr(3, 2, 1)
test1 = ft_sort_integer_table(array, 3)

if array[0] != 1 or array[1] != 2 or array[2] != 3:
	print("Error: ex09 failed!\nI got:\n" + str(array[0]) + str(array[1]) + str(array[2]))
	print("I expected:\n123")
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
print("ex09 RIGHT! One smart for you!")
if option_i == 0:
	print("You got everything right!\nYou are SMART SMART SMART SMART SMART SMART")