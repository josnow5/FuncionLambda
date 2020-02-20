def areaTriangulo(base, altura):
	return (base*altura)/2

print(areaTriangulo(4, 3))

areaTrianguloLambda = lambda base, altura: (base*altura)/2

print(areaTrianguloLambda(4, 3))

def doblar(num):
    resultado = num*2
    return resultado

doblar(2)

doblar1 = lambda num: num*2

doblar1(2)

impar = lambda num: num%2 != 0

impar(5)
