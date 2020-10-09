Contenidos:

## 1. Tipos de datos.

Los tipos de datos básicos en python son los siguientes:

- Tipos numéricos
- Booleanos
- Cadena de caracteres

A continuación se muestra un ejemplo de estos.

```python
#variables de cadena de caracteres
var1 = 'my str' #string
#o
var2 = "my str"# string
print(var1)

##variables numericas
entero = 20 #integer
con_decimales = 20.2 #float
complejo = 2j #complex number
print(entero, con_decimales, complejo)

##variables booleanas
falso = false
verdadero = true
```

## 2. Listas en python.

Las listas en python son un conjunto de valores en una misma variables, ya sean integers, strings y booleans. Se pueden almacenar distintos tipos de datos en una misma lista. A continuación explico cada método:

**Metodos para listas:**

- **.append()** ⇒ Se utiliza para agregar un dato al final de la lista.
- **.clear()**  ⇒ Elimina todos los elementos de la lista.
- **lista2 = lista.copy()** ⇒ podemos guardar en una var una copia de la lista.
- **.count()** ⇒ Se utiliza para contar cuantas veces se repite un valor de la lista.
- **lent(lista)** ⇒ Muestra la longitud de la lista pasada como parámetro.

**Acceder a valores de una lista:**

- **lista[X]** ⇒ Donde X es el index de la lista para el valor que queremos ver de ese index. Las listas se indexan desde el valor 0.

**Eliminando elementos de una lista:**

- lista.pop() ⇒ Elimina el ultimo valor indexado de la lista.
- **lista.remove(x)** ⇒ Elimina el index pasado como parametro X.

**Reverse y Sort:** 

- **lista.reverse()** ⇒ Cambia la lista y da vuelta sus valores, es decir, lo del index 0 pasa al ultimo index y el del ultimo index pasa al index0, y asi para los demás valores.
- **lista.sort()** ⇒ Se utiliza para ordenar una lista de mayor a menor( IMPORTANTE => los datos deben de ser del mismo tipo, si no son del mismo tipo python nos mostrara un error).

```python
### CREANDO UNA LISTA ###
lista = [1, 2, 3, 2, 22]

### METODOS PARA LISTAS ###

lista.append(2) #agregar mas datos
lista.clear() #elimina todos los elementos
lista2 = lista.copy() #copia de la lista
lista.count(2) => 3 #se utiliza para ver cuantas veces se repite un valor de la lista
len(lista) => 5 #muestra la longitud de la lista

### ACCEDER A ELEMENTOS DE UNA LISTA ###
print(lista[4]) #accedo al ultimo valor de la lista
# las listas se indexan desde 0

### ELIMINANDO ELEMENTOS DE UNA LISTA ###
lista.pop() #elimina el  ultimo valor de la lista
lista.remove(1) #elimina un elemento especifico de la lista

### REVERSE Y SORT ###
lista.reverse() #cambia la lista y da vuelta los valores 
lista.sort() #se utiliza para ordenar lista (deben de ser del mismo tipo de dato)
print(lista)
```

## 3. Tuplas.

Las tuplas son una lista con datos con la diferencia de que una vez que se crean no pueden ser alteradas.

**Métodos de tuplas:**

- **tupla.count(''hello")** ⇒ Busca y cuenta los valores que sean iguales al valor como parámetro.
- **tuplas.index("world")** ⇒ Busca la posición del elemento pasado como parámetro.

**¿Como transformamos una tupla a una lista?**

Para transformar una tupla a una lista tenemos que usar el método: list(*`aca va el nombre de nuestra tupla`*). A continuación se muestra un ejemplo.

```python
listToTuple = list(tuple)
```

```python
### TUPLAS ###
#Definicion:Las tuplas son una lista con datos con la diferencia de que
#           una vez que se crean no pueden ser alteradas.

tuple = ('hello', 'world', 'we are', 'a tupla')

### METODOS DE TUPLAS ###
#print(tupla.count('hello')) busca y cuentas los valores que sean iguales al parametro
#print(tupla.index('world')) busca la posicion de un elemento

### TRANSFORMANDO UNA TUPLA A LISTA ### 
listToTuple = list(tuple)
listToTuple.append('IS A JOKE IM A FUCKING LISTTTTT HAHAHA')
print(listToTuple)
```

## 4. Range

Nos permiten tener un numero de elementos desde un cierto numero inicial hasta un cierto numero final. A continuación veremos un ejemplo

```python
### CREANDO UN RANGO ###
rango = range(6)
print(rango)
```

## 5. Diccionarios

Son bastantes similares a la listas pero con la diferencia de que nosotros en vez de acceder a el index con números vamos a utilizar strings para esto.

### **Creando un diccionario:**

```python
 diccionario = {
     "nombre": "Luca",
     "pais": "Argentina",
     "edad": 20
 }
```

### **Métodos para diccionarios y formas de mostrar atributos:**

```python
print(diccionario) #mostrando el diccionario completo

print(diccionario["pais"])#de esta forma accedemos 
#al atributo que queramos del diccionario
#o
print(diccionario.get('nombre')) #esta es otra forma de acceder a un 
#atributo del diccionario

diccionario['nombre'] = 'LucaSSS' #de esta forma cambiamos un atributo 
#del diccionario

print(len(diccionario))#de esta forma vemos la longitud de 
#nuestro diccionario
```

### **Agregando y eliminando atributos de un diccionario:**

```python
diccionario['postal'] = 1663 # agregando un atributo al diccionario

diccionario.pop('pais') #eliminando un atributo del diccionario.
# o podemos:
diccionario.popitem()# elimina el ultimo atributo agregado o 
#el de la ultima posicion.
# tambien podemos:
del(diccionario['edad'])# es igual que pop solo que con otra syntaxis.

diccionario.clear() #elimina todos sus atributos.
```

### **Copiando un diccionario en otro:**

```python
copiaDiccionario = diccionario.copy() #copiamos el diccionario en 
#una nueva variable.
# o podemos:
copiaDiccionario2 = dict(diccionario)

#ambas formas son validas para la copia de un diccionario.
print(diccionario, copiaDiccionario, diccionario)
```

## 7. Diccionarios anidados:

....