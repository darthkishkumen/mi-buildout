
lista2 = [-1, 0, 8, 10000, -30,]
lista = [7,2,8, 10000, 330,]
# // menor(2)
# >> 2
#longitud = len(lista)
#print (longitud)

def minimoN(n):
	#Llamamos la funcion para que ejecute una serie de setencias
    lista.sort()  #Usare el metodo sort para ordenarlo desde el menor elemento
    
    #if n > len(lista) or n < 1:
    #	raise ValueError('N debe estar entre 1 y' + str(len(lista)))

    #Use Sort para ordenar la lista, ya que al usar este algoritmo de ordeanmiento
    #  de python
    #esta optimizado, para que tenga rapidez, al ejecutar la instrucción, 
    #para ordenar una arreglo
    #Existen otros algoritmo que su implementación pueden ordenar pero pueden
    #tener sus desventajas en la velocidad al leer la lista o arreglo
    #(buuble sort (1956 hablar un poco), shellsort, mergesort, heapsort entre otros)
    # En python los arreglos comienzan desde cero hago
    #esta modificación haciendo que la posición uno sea el valor minimo.
    #En cambio el que usa la funcion Python por defecto es lineal.
    return lista[n-1]

print ("test")
print(minimoN(2))


#funcion el n menor elemento de una lista elemento
