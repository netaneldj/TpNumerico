import math

G = 9.807
M = 87.464
L0 = 51.549
K1 = 49.366
K2 = 1

def ecuacion_iterativa_rungekutta(h,y0,f,v0):
	q1 = h*f(y0)
	q2 = h*f(y0+q1*(h/2))
	q3 = h*f(y0+q2*(h/2))
	q4 = h*f(y0+q3*h)
	return v0+(q1+2*q2+2*q3+q4)/6
	
def rungekutta4(h, y0, v0):

	posicion = []
	posicion.append(y0)

	velocidad = []
	velocidad.append(v0)

	aceleracion = []
	aceleracion.append(calcular_aceleracion(y0))

	oscilacion = 0
	n = 0
	cuarta_oscilacion = False

	tiempo = [0]

	while not cuarta_oscilacion:
		#for i in range(500):
		posicion.append(round(calcular_posicion(posicion, velocidad, h, n), 6))
		velocidad.append(round(calcular_velocidad(posicion, velocidad, h, n), 5))
		n+=1
		aceleracion.append(round(calcular_aceleracion(posicion[n]), 5))
		tiempo.append(round(n * h, 3))


		if hay_un_maximo(posicion, n):
			oscilacion+=1
			#print(posicion[n-1])
			if oscilacion == 4:
				cuarta_oscilacion = True
				
	return posicion, velocidad, aceleracion, tiempo


def calcular_posicion(y, v, h, n):
	return y[n]+h*calcular_velocidad(y,v,h,n)

def calcular_velocidad(y, v, h, n):
	return ecuacion_iterativa_rungekutta(h,y[n],calcular_aceleracion,v[n])

def calcular_aceleracion(y):
	if (y < L0): return G
	return G -(K1/M)*math.pow(y-L0,K2)

def hay_un_maximo(y, n):
	if (n > 1) and (y[n] < y[n-1]) and (y[n-1] > y[n-2]): return True
	return False

def main():
	y, v, a, t = rungekutta4(0.143,0,0) # intervalo h, posicion inicical, velocidad inicial

	print ("posicion:", y)
	print ("velocidad:", v)
	print ("aceleracion:", a)
	print ("tiempo:", t)

main()
