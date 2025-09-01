
def busquedaLineal(arreglo, numeroABuscar):
  comparaciones = 0
  for i in range(len(arreglo)):
    comparaciones += 1
    if arreglo[i] == numeroABuscar:
      return comparaciones,i
  return comparaciones,-1



# Probamos el programa
# if __name__ == "__main__":
#   casos = [
#     {"array": [1,2,8,9,6,19,3,4,300],
#     "numero": 19},
#     {"array": [1,2,8,9,6,19,3,4,300,600,434,1234,4335,3,0,132321,33322,34444332,22333244],
#     "numero": 22333244},

#   ]

#   for i in range(len(casos)):
#     arrayDePrueba = casos[i]["array"]
#     numeroDePrueba = casos[i]["numero"]

#     busqueda = busquedaLineal(arrayDePrueba,numeroDePrueba)

#     print(f"Se busca el numero {numeroDePrueba} en el array {arrayDePrueba}" )

#     if(busqueda[1] != -1):
#       print(f"el numero ha sido hallado en la posicion {busqueda[1]} y se han realizado {busqueda[0]} comparaciones")
#     else:
#       print(f"No se encontro el numero pero se realizaron {busqueda[0]} comparaciones")
  









