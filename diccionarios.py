# Son bastantes similares a la listas pero con la diferencia de que
# nosotros en vez de acceder a el index con numeros vamos a ultilizar
# strings para esto.

# diccionario = {
#     "nombre": "Luca",
#     "pais": "Argentina",
#     "edad": 20
# }

#print(diccionario)mostrando el diccionario completo
#print(diccionario["pais"])#de esta forma accedemos al atributo que queramos del diccionario
#o
#print(diccionario.get('nombre'))#esta es otra forma de acceder a un atributo del diccionario
#diccionario['nombre'] = 'LucaSSS'#de esta forma cambiamos un atributo del diccionario
#print(len(diccionario))#de esta forma vemos la longitud de nuestro diccionario

diccionario = {
    "nombre": "Luca",
    "pais": "Argentina",
    "edad": 20
}

diccionario['postal'] = 1663 # agregando un atributo al diccionario
# print(diccionario)
diccionario.pop('pais') #eliminando un atributo del diccionario
# o podemos:
diccionario.popitem()# elimina el ultimo atributo agregado o el de la ultima posicion
# tambien podemos:
del(diccionario['edad'])# es igual que pop solo que con otra syntaxis
#copiaDiccionario.clear() elimina todos sus atributos

copiaDiccionario = diccionario.copy() #copiamos el diccionario en una nueva variable
# o podemos:
copiaDiccionario2 = dict(diccionario)

print(diccionario, copiaDiccionario, diccionario)
