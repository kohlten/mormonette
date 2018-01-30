from subprocess import Popen, PIPE
from os import listdir, chdir
from ctypes import CDLL
from sys import exit
from hashlib import md5

text_putchar = "#include <unistd.h>\n\nvoid ft_putchar(char c)\n{\n\twrite(1, &c, 1);\n}"
main = ["int main() {\n\t", "\n\treturn 0;\n}"]

#--------------ex00-----------------#
try:
	chdir ("work/ex00")
except OSError:
	print("Done")
	exit(0)

open("ft_putchar.c", "w").write(text_putchar)
open("main.c", "w").write("void ft_print_alphabet();\n\n" + main[0] + "ft_print_alphabet();" + main[1])

#compile the file with the main
pipe = Popen("gcc -o ft_print_alphabet ft_print_alphabet.c ft_putchar.c main.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Compilation failed on ex00:")
	print(err)
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

#run ft_print_alphabet
pipe = Popen(["./ft_print_alphabet"], stdout=PIPE)
output = pipe.communicate()[0]
if output != "abcdefghijklmnopqrstuvwxyz":
	print("Error:\nex00 is not right:\n" + output)
	print("Expected: abcdefghijklmnopqrstuvwxyz")
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

print("ex00 RIGHT! One smart for you!")
#--------------ex01-----------------#
try:
	chdir ("../ex01")
except OSError:
	print("Done")
	exit(0)

open("ft_putchar.c", "w").write(text_putchar)
open("main.c", "w").write("void ft_print_reverse_alphabet();\n\n" + main[0] + "ft_print_reverse_alphabet();" + main[1])

pipe = Popen("gcc -o ft_print_reverse_alphabet ft_print_reverse_alphabet.c ft_putchar.c main.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Compilation failed on ex01:")
	print(err)
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

pipe = Popen(["./ft_print_reverse_alphabet"], stdout=PIPE)
output = pipe.communicate()[0]
if output != "zyxwvutsrqponmlkjihgfedcba":
	print("Error:\nex01 is not right:\n" + output)
	print("Expected: zyxwvutsrqponmlkjihgfedcba")
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

print("ex01 RIGHT! One smart for you!")
#--------------ex02-----------------#
try:
	chdir ("../ex02")
except OSError:
	print("Done")
	exit(0)

open("ft_putchar.c", "w").write(text_putchar)
open("main.c", "w").write("void ft_print_numbers();\n\n" + main[0] + "ft_print_numbers();" + main[1])

pipe = Popen("gcc -o ft_print_numbers ft_print_numbers.c ft_putchar.c main.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Compilation failed on ex02:")
	print(err)
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

pipe = Popen(["./ft_print_numbers"], stdout=PIPE)
output = pipe.communicate()[0]
if output != "0123456789":
	print("Error: ex02 is not right:\n" + output)
	print("Expected: 0123456789")
	print("Can't you count?")
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

print("ex02 RIGHT! One smart for you!")
#--------------ex03-----------------#
try:
	chdir ("../ex03")
except OSError:
	print("Done")
	exit(0)

open("ft_putchar.c", "w").write(text_putchar)
open("main.c", "w").write("void ft_is_negative(int n);\n\n" + main[0] + "ft_is_negative(15);\n\tft_is_negative(-25);\n\tft_is_negative(12345678);\n\tft_is_negative(0);" + main[1])

pipe = Popen("gcc -o ft_is_negative ft_is_negative.c ft_putchar.c main.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Compilation failed on ex03:")
	print(err)
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

pipe = Popen(["./ft_is_negative"], stdout=PIPE)
output = pipe.communicate()[0]
if output != "PNPP":
	print("Error: ex03 is not right:\n" + output)
	print("Expected: PNPP")
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

print("ex03 RIGHT! One smart for you!")
#--------------ex04-----------------#
try:
	chdir ("../ex04")
except OSError:
	print("Done")
	exit(0)
comb = "012, 013, 014, 015, 016, 017, 018, 019, 023, 024, 025, 026, 027, 028, 029, 034, 035, 036, 037, 038, 039, 045, 046, 047, 048, 049, 056, 057, 058, 059, 067, 068, 069, 078, 079, 089, 123, 124, 125, 126, 127, 128, 129, 134, 135, 136, 137, 138, 139, 145, 146, 147, 148, 149, 156, 157, 158, 159, 167, 168, 169, 178, 179, 189, 234, 235, 236, 237, 238, 239, 245, 246, 247, 248, 249, 256, 257, 258, 259, 267, 268, 269, 278, 279, 289, 345, 346, 347, 348, 349, 356, 357, 358, 359, 367, 368, 369, 378, 379, 389, 456, 457, 458, 459, 467, 468, 469, 478, 479, 489, 567, 568, 569, 578, 579, 589, 678, 679, 689, 789"

open("ft_putchar.c", "w").write(text_putchar)
open("main.c", "w").write("void	ft_print_comb();\n\n" + main[0] + "ft_print_comb();" + main[1])

pipe = Popen("gcc -o ft_print_comb ft_print_comb.c ft_putchar.c main.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Compilation failed on ex04:")
	print(err)
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

pipe = Popen(["./ft_print_comb"], stdout=PIPE)
output = pipe.communicate()[0]
if output != comb:
	print("Error: ex04 is not right:\n" + output)
	print("Expected: " + comb)
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

print("ex04 RIGHT! One smart for you!")
#--------------ex05-----------------#
try:
	chdir ("../ex05")
except OSError:
	print("Done")
	exit(0)

comb = '022b798edf04ce89f0c19ca1ea305534'
open("ft_putchar.c", "w").write(text_putchar)
open("main.c", "w").write("void	ft_print_comb2(void);\n\n" + main[0] + "ft_print_comb2();" + main[1])

pipe = Popen("gcc -o ft_print_comb2 ft_print_comb2.c ft_putchar.c main.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Compilation failed on ex05:")
	print(err)
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

pipe = Popen(["./ft_print_comb2"], stdout=PIPE)
output = pipe.communicate()[0]
hash = md5(output)
if hash.hexdigest() != comb:
	print("Error: ex05 is not right:\n" + output[0: 40])
	print("Expected: 00 01, 00 02, 00 03, 00 04, 00 05, ..., 00 99, 01 02, ..., 97 99, 98 99")
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

print("ex05 RIGHT! One smart for you!")
#--------------ex06-----------------#
try:
	chdir ("../ex06")
except OSError:
	print("Done")
	exit(0)

open("ft_putchar.c", "w").write(text_putchar)
open("main.c", "w").write('''void ft_putnbr(int nb);\nvoid ft_putchar(char c);\n''' + main[0] + '''ft_putnbr(42);\n\tft_putchar('\\n');\n\tft_putnbr(-1);\n\tft_putchar('\\n');\n\tft_putnbr(-25);
	ft_putchar('\\n');\n\tft_putnbr(0);\n\tft_putchar('\\n');\n\tft_putnbr(2147483647);\n\tft_putchar('\\n');\n\tft_putnbr(-2147483647);''' + main[1])

#compile the file with the main
pipe = Popen("gcc -o ft_putnbr ft_putnbr.c ft_putchar.c main.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Compilation failed on ex06:")
	print(err)
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

#run ft_print_alphabet
pipe = Popen(["./ft_putnbr"], stdout=PIPE)
output = pipe.communicate()[0]
if output != "42\n-1\n-25\n0\n2147483647\n-2147483647":
	print("Error: ex06 is not right:\n" + output)
	print("Expected: \n42\n-1\n-25\n0\n2147483647\n-2147483647")
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

print("ex06 RIGHT! One smart for you!")
#--------------ex07-----------------#
try:
	chdir ("../ex07")
except OSError:
	print("Done")
	exit(0)

comb = ["0, 1, 2, 3, 4, 5, 6, 7, 8, 9", "01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89", "012, 013, 014, 015, 016, 017, 018, 019, 023, 024, 025, 026, 027, 028, 029, 034, 035, 036, 037, 038, 039, 045, 046, 047, 048, 049, 056, 057, 058, 059, 067, 068, 069, 078, 079, 089, 123, 124, 125, 126, 127, 128, 129, 134, 135, 136, 137, 138, 139, 145, 146, 147, 148, 149, 156, 157, 158, 159, 167, 168, 169, 178, 179, 189, 234, 235, 236, 237, 238, 239, 245, 246, 247, 248, 249, 256, 257, 258, 259, 267, 268, 269, 278, 279, 289, 345, 346, 347, 348, 349, 356, 357, 358, 359, 367, 368, 369, 378, 379, 389, 456, 457, 458, 459, 467, 468, 469, 478, 479, 489, 567, 568, 569, 578, 579, 589, 678, 679, 689, 789"]
open("ft_putchar.c", "w").write(text_putchar)
open("main.c", "w").write("void	ft_print_combn(int n);\nvoid ft_putchar(char c);\n\n" + main[0] + "ft_print_combn(1);\n\tft_putchar('\\n');\nft_print_combn(2);\n\tft_putchar('\\n');\n\tft_print_combn(3);" + main[1])

pipe = Popen("gcc -o ft_print_combn ft_print_combn.c ft_putchar.c main.c".split(" "), stdout=PIPE, stderr=PIPE)
output, err = pipe.communicate()

if err != "":
	print("Compilation failed on ex07:")
	print(err)
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

pipe = Popen(["./ft_print_combn"], stdout=PIPE)
output = pipe.communicate()[0]
if output != '\n'.join(comb):
	print("Error: ex07 is not right:\n" + output)
	print("Expected: " + '\n'.join(comb))
	print("DUM DUM DUM DUM DUM DUM")
	exit(1)

print("ex07 RIGHT! One smart for you!")
print("You are SMART SMART SMART SMART SMART SMART!")