#!/usr/bin/python
from subprocess import Popen, PIPE
from ctypes import *
from os import chdir
from sys import argv

option_i = 0
main = ["int main() {\n\t", "\n\treturn 0;\n}"]
if len(argv) > 1:
	if "-i" in argv:
		option_i = 1

#--------------ex00-----------------#
try:
	chdir("work/ex00")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_iterative_factorial ft_iterative_factorial.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex00.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		if option_i == 0:
			exit(1)
else:
	lib = CDLL("./ft_iterative_factorial")
	ft_iterative_factorial = lib.ft_iterative_factorial
	ft_iterative_factorial.argstypes = [c_int]
	ft_iterative_factorial.restype = c_int
	tests = []
	awnsers = [0, 0, 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 0, 0]
	for i in range(-2, 15):
		tests.append(ft_iterative_factorial(i))

	if tests != awnsers:
		print('''Error: ex00 failed!\nI got:
	-2! -1!  0!  1!  2!  3!  4!    5!    6!    7!      8!      9!       10!        11!        12!     13! 14!
	''' + str(tests).replace(", ", ",  ") + "\nI expected:\n" + str(awnsers).replace(", ", ",  "))
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			if option_i == 0:
				exit(1)
	print("ex00 RIGHT! One smart for you!")
#--------------ex01-----------------#
try:
	chdir("../ex01")
except OSError:
	print("Done")
	exit(1)

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_recursive_factorial ft_recursive_factorial.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex01.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_recursive_factorial")
	ft_recursive_factorial = lib.ft_recursive_factorial
	ft_recursive_factorial.argstypes = [c_int]
	ft_recursive_factorial.restype = c_int
	tests = []
	awnsers = [0, 0, 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 0, 0]
	for i in range(-2, 15):
		tests.append(ft_recursive_factorial(i))

	if tests != awnsers:
		print('''Error: ex01 failed!\nI got:
	-2! -1!  0!  1!  2!  3!  4!    5!    6!    7!      8!      9!       10!        11!        12!     13! 14!
	''' + str(tests).replace(", ", ",  ") + "\nI expected:\n" + str(awnsers).replace(", ", ",  "))
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

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_iterative_power ft_iterative_power.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex02.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_iterative_power")
	ft_iterative_power = lib.ft_iterative_power
	ft_iterative_power.argstypes = [c_int, c_int]
	ft_iterative_power.restype = c_int
	tests = []
	awnsers = [0, 0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, -2147483648]
	for i in range(-2, 32):
		tests.append(ft_iterative_power(2, i))

	#print(tests)

	if tests != awnsers:
		print("Error: ex02 failed!\nI got:\n" + str(tests).replace(", ", ",  ") + "\nI expected:\n" + str(awnsers).replace(", ", ",  "))
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

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_recursive_power ft_recursive_power.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex03.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_recursive_power")
	ft_recursive_power = lib.ft_recursive_power
	ft_recursive_power.argstypes = [c_int, c_int]
	ft_recursive_power.restype = c_int
	tests = []
	awnsers = [0, 0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, -2147483648]
	for i in range(-2, 32):
		tests.append(ft_recursive_power(2, i))

	if tests != awnsers:
		print("Error: ex03 failed!\nI got:\n" + str(tests).replace(", ", ",  ") + "\nI expected:\n" + str(awnsers).replace(", ", ",  "))
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

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_fibonacci ft_fibonacci.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex04.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_fibonacci")
	ft_fibonacci = lib.ft_fibonacci
	ft_fibonacci.argstypes = [c_int]
	ft_fibonacci.restype = c_int
	tests = []
	awnsers = [-1, -1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
	for i in range(-2, 15):
		tests.append(ft_fibonacci(i))

	if tests != awnsers:
		print("Error: ex04 failed!\nI got:\n" + str(tests).replace(", ", ",  ") + "\nI expected:\n" + str(awnsers).replace(", ", ",  "))
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

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_sqrt ft_sqrt.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex05.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_sqrt")
	ft_sqrt = lib.ft_sqrt
	ft_sqrt.argstypes = [c_int]
	ft_sqrt.restype = c_int
	tests = []
	awnsers = [2, 1, 0, 0, 3, 4, 0, 12]
	test_nums = [4, 1, 0, 3, 9, 16, -5, 144]
	for num in test_nums:
		tests.append(ft_sqrt(num))

	if tests != awnsers:
		print("Error: ex05 failed!\nI got:\n" + str(tests).replace(", ", ",  ") + "\nI expected:\n" + str(awnsers).replace(", ", ",  "))
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

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_is_prime ft_is_prime.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex06.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_is_prime")
	ft_is_prime = lib.ft_is_prime
	ft_is_prime.argstypes = [c_int]
	ft_is_prime.restype = c_int
	tests = []
	awnsers = [2,  3,  5,  7,  11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97]
	for i in range(-4, 100):
		if ft_is_prime(i) == 1:
			tests.append(i)

	if tests != awnsers:
		print("Error: ex06 failed!\nI got:\n" + str(tests).replace(", ", ",  ") + "\nI expected:\n" + str(awnsers).replace(", ", ",  "))
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

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_find_next_prime ft_find_next_prime.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex07.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./ft_find_next_prime")
	ft_find_next_prime = lib.ft_find_next_prime
	ft_find_next_prime.argstypes = [c_int]
	ft_find_next_prime.restype = c_int
	tests = []
	awnsers = [2,  2,  2,  2,  2,  2,  2,  3,  5,  5,  7,  7,  11,  11,  11,  11,  13,  13,  17,  17,  17,  17,  19,  19]
	for i in range(-4, 20):
		tests.append(ft_find_next_prime(i))
	if tests != awnsers:
		print("Error: ex07 failed!\nI got:\n" + str(tests).replace(", ", ",  ") + "\nI expected:\n" + str(awnsers).replace(", ", ",  "))
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

pipe = Popen("gcc -Wall -Wextra -Werror -shared -o ft_eight_queens_puzzle ft_eight_queens_puzzle.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex08.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	lib = CDLL("./fft_eight_queens_puzzle ")
	ft_eight_queens_puzzle = lib.ft_eight_queens_puzzle
	ft_eight_queens_puzzle.argstypes = None
	ft_eight_queens_puzzle.restype = c_int
	val = ft_eight_queens_puzzle()

	if val != 92:
		print("Error: ex08 failed!\nI got:\n" + str(val) + "\nI expected:\n92")
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	print("ex08 RIGHT! One smart for you!")
#--------------ex08-----------------#
try:
	chdir("../ex09")
except OSError:
	print("Done")
	exit(1)
open("main.c", "w").write("void ft_eight_queens_puzzle_2(void);\n\n" + main[0] + "ft_eight_queens_puzzle_2();" + main[1])
pipe = Popen("gcc -Wall -Wextra -Werror -o ft_eight_queens_puzzle_2 ft_eight_queens_puzzle_2.c main.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Failed to compile on ex09.")
	print("Heres the error:\n " + err)
	print("DUM DUM DUM DUM DUM DUM")
	if option_i == 0:
		exit(1)
else:
	awnser = "15863724\n16837425\n17468253\n17582463\n24683175\n25713864\n25741863\n26174835\n26831475\n27368514\n27581463\n28613574\n31758246\n35281746\n35286471\n35714286\n35841726\n36258174\n36271485\n36275184\n36418572\n36428571\n36814752\n36815724\n36824175\n37285146\n37286415\n38471625\n41582736\n41586372\n42586137\n42736815\n42736851\n42751863\n42857136\n42861357\n46152837\n46827135\n46831752\n47185263\n47382516\n47526138\n47531682\n48136275\n48157263\n48531726\n51468273\n51842736\n51863724\n52468317\n52473861\n52617483\n52814736\n53168247\n53172864\n53847162\n57138642\n57142863\n57248136\n57263148\n57263184\n57413862\n58413627\n58417263\n61528374\n62713584\n62714853\n63175824\n63184275\n63185247\n63571428\n63581427\n63724815\n63728514\n63741825\n64158273\n64285713\n64713528\n64718253\n68241753\n71386425\n72418536\n72631485\n73168524\n73825164\n74258136\n74286135\n75316824\n82417536\n82531746\n83162574\n84136275"
	pipe = Popen(["./ft_eight_queens_puzzle_2"], stdout=PIPE, stderr=PIPE)
	output, err = pipe.communicate()
	if output != "" or err != "":
		print("Error: ex09 failed!\nI got:\n" + str(output) + "\nI expected:\n" + awnser.replace('\n', "\\n"))
		print(err)
		print("DUM DUM DUM DUM DUM DUM")
		if option_i == 0:
			exit(1)
	print("ex09 RIGHT! One smart for you!")
	if option_i == 0:
		print("All are right!\nYou are smart smart smart smart smart smart")
