#Liberia "random"|
import random

#Variables
numbers = []
highestScore = []



#Creación de los pares de numeros aleatorios
def createPairs():
    for i in range(1,20):
        num = random.randint(1,200)
        pair = num
        numbers.append(num)
        numbers.append(pair)
    random.shuffle(numbers)
    print(numbers)

def checkNumbers(a,b):
    for i in numbers:
        if a == b:
            print("+5 puntos")


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
    elif answer == "2":
        print("Tu puntaje máximo es de: ",highestScore)
    elif answer == "3":
        print("Gracias por haber jugado")
        break




