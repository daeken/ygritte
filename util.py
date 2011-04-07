from math import cos, sin, pi

def rotatePoint(a, factor=1, point=None):
	a = a*pi/180
	sa = sin(a)
	ca = cos(a)
	if point == None:
		return factor * sa, factor * ca
	else:
		return (
			factor*(point[0]*ca - point[1]*sa), 
			factor*(point[1]*ca + point[0]*sa))
