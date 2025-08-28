
def encontrarParesAnidado(arr, numero):
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] + arr[j] == numero:
        return True
  return False


def encontrarParesHash(arr, numero):
  dic = {}
  for i in range(len(arr)):
    complemento = numero - arr[i]
    if complemento in dic:
      return True
    
    dic[arr[i]] = True

  return False

casos = [
    ([1, 2, 3, 4, 5, 6, 7, 8], 10),   # 4+6, 2+8
    ([1, 2, 3], 5),                   # 2+3
    ([1, 2, 3], 10),                  # no existe
    ([5, 5, 5], 10),                  # 5+5
    ([], 4),                          # lista vacía
    ([0, -1, 2, -3, 1], -2),          # -3 + 1 = -2
    ([10], 20),                       # un solo número
    ([2, 4, 6, 8], 12),               # 4+8 o 6+6 (pero ojo, necesita dos distintos índices)
]


for arr,numero in casos:
  print(f"array : {arr}, numero: {numero}")
  print(f"Anidado: ",encontrarParesAnidado(arr, numero))
  print(f"Hash: ",  encontrarParesHash(arr, numero))
  print("-" * 40)