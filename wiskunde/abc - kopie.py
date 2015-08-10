from time import sleep
import math
fo = open("answers.txt", "wb")
def main():
	a = input('a: ')
	b = input('b: ')
	c = input('c: ')
	dis = b*b-4*a*c
	print (dis)
	fo.write(repr(a) + 'X^2+' + repr(b) + 'X+' + repr(c) + '\r\n')
	fo.write('discriminant: ' + repr(dis) + '\r\n')
	fo.write('snijpunt Y as: ' + repr(b*0+b*0+c) + '\r\n')
	print 'snijpunt Y as:', b*0+b*0+c
	if dis > 0:
		snij1 = (-b+math.sqrt(dis))/(2*a)
		snij2 = (-b-math.sqrt(dis))/(2*a)
		print snij1, 'V', snij2
		fo.write('snijpunt X as: ' + repr(snij1) + 'V' + repr(snij2) + '\r\n')
	elif dis == 0:
		print (-b+math.sqrt(dis))/(2*a)
		fo.write('snijpunt X as: ' + repr(-b+math.sqrt(dis)) + '\r\n')
	else: 
		print ('ERROR!')
		fo.write('snijpunt X as: geen \r\n')
	hjk()
def hjk():
	cont = raw_input('press enter to start over or y to exit ')
	if cont == 'y': 
		fo.close()
		exit()
	else: main()
main()
