#Liberia "random"
import random

#Variables
numbers = []
highestScore = []
score = []



#Creación de los pares de numeros aleatorios
def createPairs():
    for i in range(1,5):
        num = random.randint(1,10)
        pair = num
        numbers.append(num)
        numbers.append(pair)
    random.shuffle(numbers)
    print(numbers)
    print("Debes encontrar", len(numbers), "parejas")
    



#función para chequear los pares de números dados por el usuario
def checkNumbers():

    a = int(input("Elige un número \n"))
    b = int(input("Elige otro número"))
    num1 = numbers[a]
    num2 = numbers[b]
    print(num1,num2)


#Comprobar si los indices dados contienen el mismo números
    while len(numbers) > 0 :
        if num1 == num2:
            puntos = 10
            print("has encontrado  una pareja")
            score.append(puntos)
            print("has ganado 4 puntos")
            
        #Se remueven las parejas encontradas
            numbers.remove(numbers[num1])
            numbers.remove(numbers[num2])
        elif num1 != num2:
            print("Los numeros no coinciden vuelve a intentar")
        elif num1 == "salir":
            print("terminaste la partida")
            print("tu puntaje fue", score)
            score.clear()
            print(score)
            break
    
            

            



while(True):
    print("Bienvenido a tu juego de memoria de números \n")
    print("Elige una opción:\n")
    print("Opción 1: Partida Nueva")
    print("Opción 2: Ver Puntuación Máxima")
    print("Opción 3: salir")
    
    answer = input("Elige tu opción: \n" )

    if answer == "1":
        print("La partida ha empezado \n")
        createPairs()
        checkNumbers()


    elif answer == "2":
        print("Tu puntaje máximo es de: ",highestScore)
    elif answer == "3":
        print("Gracias por haber jugado")
        break



