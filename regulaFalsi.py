import math

ERROR = math.pow(5, -17)
VACIO = None
# PADRON = 99093
# L0 = 2*100000/PADRON
L0 = 2.02
G = 9.81
K = 10
# M0 = 100000/PADRON
M0 = 1.01
M = 0*M0
A = 1

def regula_falsi (inicio,fin):
	a = []
	b = []
	raiz = []
	absError = []
	relError = []

	k = 0

	if regula_falsi_rec(k, inicio, fin, raiz, a, b, absError, relError):
		print ("HAY RAIZ")
	else:
		print ("NO HAY RAIZ")

	print a
	print calcular_f_en_arreglo(a)
	print b
	print calcular_f_en_arreglo(b)
	print raiz
	print absError
	print relError
	p = calcular_exp_p(absError)
	print p
	print calcular_lambda(absError, p)

	
def regula_falsi_rec(k, inicio, fin, raiz, a, b, absE, relE):
	medio = calcular_medio(inicio, fin)
	raiz.append(medio)
	
	a.append(inicio)
	b.append(fin)

	if k == 0:
		absE.append(VACIO)
		relE.append(VACIO)

	else:
		absE.append(abs(raiz[k]-raiz[k-1]))
		relE.append(abs(absE[k]/(raiz[k])))

		if relE[k] < ERROR:
			return True

	k += 1

	if f(inicio)*f(medio) < 0:
		regula_falsi_rec(k, inicio, medio, raiz, a, b, absE, relE)

	if f(medio)*f(fin) < 0:
			regula_falsi_rec(k, medio, fin, raiz, a, b, absE, relE)

	else:
		return False
	
	return True	
	
def calcular_medio( inicio, fin):
	return inicio-((fin-inicio)/(f(fin)-f(inicio)))*f(inicio)

def calcular_f_en_arreglo(arreglo):
	f_en_arreglo = []

	for a in arreglo:
		f_en_arreglo.append(f(a))

	return f_en_arreglo

def f(y):
	return -2*K*y*(1 - L0/math.sqrt(math.pow(y, 2) + math.pow(A, 2))) - M*G

def calcular_exp_p(absE):
	p = []

	for k in range(len(absE)-1):
		if k > 1:
			p.append(math.log((absE[k+1]/absE[k]), math.e) / math.log((absE[k]/absE[k-1]), math.e))

		else:
			p.append(VACIO)

	return p

def calcular_lambda(absE, p):
	y = []

	for k in range(len(absE)-1):
		if k > 1:
			y.append(absE[k+1] / math.pow(absE[k], p[k]))

		else:
			y.append(VACIO)

	return y

def main():
	regula_falsi(1, 2)
	
main()
