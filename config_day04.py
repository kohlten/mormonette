from subprocess import Popen, PIPE
from ctypes import *
from os import chdir

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
	exit(1)

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
	exit(1)

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
	exit(1)

lib = CDLL("./ft_iterative_power")
ft_iterative_power = lib.ft_iterative_power
ft_iterative_power.argstypes = [c_int, c_int]
ft_iterative_power.restype = c_int
tests = []
awnsers = [0, 0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, -2147483648]
for i in range(-2, 32):
	tests.append(ft_iterative_power(2, i))

print(tests)

if tests != awnsers:
	print('''Error: ex02 failed!\nI got:
-2! -1!  0!  1!  2!  3!  4!    5!    6!    7!      8!      9!       10!        11!        12!     13! 14!
 '''+ str(tests).replace(", ", ",  ") + "\nI expected:\n" + str(awnsers).replace(", ", ",  "))
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)
print("ex02 RIGHT! One smart for you!")'''
