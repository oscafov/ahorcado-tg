from random import randint
fallos = 0
lista_palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()
print('\n\n █████╗ ██╗  ██╗ ██████╗ ██████╗  ██████╗ █████╗ ██████╗  ██████╗')
print('██╔══██╗██║  ██║██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗')
print('███████║███████║██║   ██║██████╔╝██║     ███████║██║  ██║██║   ██║')
print('██╔══██║██╔══██║██║   ██║██╔══██╗██║     ██╔══██║██║  ██║██║   ██║')
print('██║  ██║██║  ██║╚██████╔╝██║  ██║╚██████╗██║  ██║██████╔╝╚██████╔╝')
print('╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝\n')
ahorcado = ['''
      +-----+
      |     |
            |
            |
            |
            |
    ===========''', '''
      +-----+
      |     |
      O     |
            |
            |
            |
    ===========''', '''
      +-----+
      |     |
      O     |
      |     |
            |
            |
    ===========''', '''
      +-----+
      |     |
      O     |
     /|     |
            |
            |
    ===========''', '''
      +-----+
      |     |
      O     |
     /|\    |
            |
            |
    ===========''', '''
      +-----+
      |     |
      O     |
     /|\    |
     /      |
            |
    ===========''', '''
      +-----+
      |     |
      O     |
     /|\    |
     / \    |
            |
    ===========     f''']
palabra = lista_palabras[randint(0,len(lista_palabras)-1)]
resultado = list("_"*len(palabra))
mostrar = []
print("Hola, bienvenido al juego del ahorcado, a continuación se mostrará la palabra que debes adivinar, para resolver puedes escribir 'resuelvo', si fallas, perderás! \n")
while True:
  mostrar = []
  for caracteres in resultado:
    mostrar.append(caracteres)
    mostrar.append(" ")
  print("".join(mostrar))
  if "".join(resultado) == palabra:
    break
  letra = str(input("Introduce una letra: ").lower())
  if letra.isalpha() and len(letra) == 1:
    if letra in palabra:
      num_letra = palabra.count(letra)
      if num_letra == 1:
        resultado[palabra.index(letra)] = letra
      else:
        for k in range(len(palabra)):
          if letra == list(palabra)[k]:
            resultado[k] = letra
    else:
      fallos = fallos +1
      print(ahorcado[fallos-1])
  else:
    print("La letra introducida no es valida")
  if fallos == len(ahorcado):
    break