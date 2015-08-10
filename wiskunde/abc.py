from time import sleep
import math
def main():
	a = input('a: ')
	b = input('b: ')
	c = input('c: ')
	dis = b*b-4*a*c
	print (dis)
	if dis > 0:
		snij1 = (-b+math.sqrt(dis))/(2*a)
		snij2 = (-b-math.sqrt(dis))/(2*a)
		print snij1, 'V', snij2
	elif dis == 0:
		print (-b+math.sqrt(dis))/(2*a)
	else: print ('ERROR!')	
	hjk()
def hjk():
	cont = raw_input('press enter to start over or y to exit ')
	if cont == 'y': exit()
	else: main()
main()