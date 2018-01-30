from subprocess import Popen, PIPE
from sys import exit
from os import chdir
import ctypes

main = ["int main() {\n\t", "\n\treturn 0;\n}"]

#--------------ex00-----------------#
try:
	chdir("work/ex00")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -shared -o ft_ft ft_ft.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex00.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
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
pipe = Popen("gcc -o ft_ultimate_ft ft_ultimate_ft.c main.c".split(" "), stderr=PIPE)
err = pipe.communicate()[1]

if err != "":
	print("Compiling failed on ex01!")
	print(err)
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

pipe = Popen(["./ft_ultimate_ft"], stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()
if output != "42":
	print("Error: ex01 failed!\nI got " + output + "\nI expected 42")
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)
print("ex01 RIGHT! One smart for you!")
#--------------ex02-----------------#
try:
	chdir("../ex02")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -shared -o ft_swap ft_swap.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex02.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
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
	exit(1)
print("ex02 RIGHT! One smart for you!")
#--------------ex03-----------------#
try:
	chdir("../ex03")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -shared -o ft_div_mod ft_div_mod.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex03.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
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

if div.value != 6 or mod.value != 3:
	print("Error: ex03 failed!\nI got x:" + str(div.value) + " y: " + str(mod.value) + "\nI expected 6 2")
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)
print("ex03 RIGHT! One smart for you!")