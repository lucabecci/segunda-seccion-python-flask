### CREANDO UNA LISTA ###
lista = [1, 2, 3, 2, 22]

### METODOS PARA LISTAS ###

# lista.append(2) agregar mas datos
# lista.clear() elimina todos los elementos
# lista2 = lista.copy() copia de la lista
# lista.count(2) => 3 se utiliza para ver cuantas veces se repite un valor de la lista
# len(lista) => 5 muestra la longitud de la lista

### ACCEDER A ELEMENTOS DE UNA LISTA ###
#print(lista[4])   accedo al ultimo valor de la lista
# las listas se indexan desde 0

### ELIMINANDO ELEMENTOS DE UNA LISTA ###
#lista.pop() elimina el  ultimo valor de la lista
#lista.remove(1) elimina un elemento especifico de la lista

### REVERSE Y SORT ###
#lista.reverse() cambia la lista y da vuelta los valores 
lista.sort() #se utiliza para ordenar lista (deben de ser del mismo tipo de dato)
print(lista)