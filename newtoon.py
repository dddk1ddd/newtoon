import sys, getopt, time
import random
from random import randint

year = int(time.strftime('%Y'))
day = int(time.strftime('%d'))
rmonth = int(time.strftime('%m'))


def usage():
	print('usage: newme --gender <arg> --state <arg> --age <arg>')
	print(' * optional arguments')
	print(' --gender : Male or Female')
	print(' --state  : Country or City or State')
	print(' --age    : child, teen, adult, elderly')
	sys.exit()

def gen_gender():
	gender = ['Male','Female']
	x = randint(0,len(gender)-1)
	return gender[x]
def gen_country():
	country = ['USA']
	x = randint(0,len(country)-1)
	return country[x]

g = gen_gender()
y = gen_country()
a = randint(2,85)
month = rmonth
while month == rmonth: month = randint(1,12)
if month == 1:
	nmonth = 'Jan'
	ndays = randint(1,31)
elif month == 2:
	nmonth = 'Feb'
	ndays = randint(1,28)
elif month == 3:
	nmonth = 'Mar'
	ndays = randint(1,31)
elif month == 4:
	nmonth = 'Apr'
	ndays = randint(1,30)
elif month == 5:
	nmonth = 'May'
	ndays = randint(1,31)
elif month == 6:
	nmonth = 'Jun'
	ndays = randint(1,30)
elif month == 7:
	nmonth = 'Jul'
	ndays = randint(1,31)
elif month == 8:
	nmonth = 'Aug'
	ndays = randint(1,31)
elif month == 9:
	nmonth = 'Sep'
	ndays = randint(1,30)
elif month == 10:
	nmonth = 'Oct'
	ndays = randint(1,31)
elif month == 11:
	nmonth = 'Nov'
	ndays = randint(1,30)
elif month == 12:
	nmonth = 'Dec'
	ndays = randint(1,31)

try:
	opts, args = getopt.getopt(sys.argv[1:], 'g:s:a', ['gender=', 'state=', 'age=', 'help'])
except getopt.GetoptError: 
	usage()
	sys.exit(2)

for opt, arg in opts:
	if opt in ('--gender'):
		g = arg
	elif opt in ('--state'):
		y = arg
	elif opt in ('--age'):
		if arg == 'adult':
			a = randint(18,55)
		elif arg == 'child':
			a = randint(2,12)
		elif arg == 'teen':
			a = randint(13,19)
		elif arg == 'elderly':
			a = randint(55,85)

year = (year - a)
if month >= rmonth: a = a-1
# todo: more countries
# if y == ('usa'):
if g in ['Male','male','M','m']:
	line = random.choice(open('./USA/male-first.txt').readlines())
else:
	line = random.choice(open('./USA/female-first.txt').readlines())
sline = random.choice(open('./USA/surnames.txt').readlines())
sline = sline.split(',')
cline = random.choice(open('./USA/cities.txt').readlines())
cline = cline.split(',')
# else:
#	line = 'xxx'
#	sline = ['xxx']
#	cline = ['xxx xxx']
print('\n')
print('-[First Name]-')
print(line)
print('-[Surname]-')
print(sline[0])
print('\n')
print(str(a) + ' year old ' + g + ' from ' + y)
print('born on ' + str(ndays) + ' of ' + nmonth + ', ' + str(year))
print('\n')
print("City, State, County")
print(cline[0])	