#Liberia "random"
import random
import math

#Variables
highestScore = 0



#Creación de los pares de numeros aleatorios
def createPairs():
    numbers = []
    numberOfPairs = random.randint(0,12)
    for _ in range(numberOfPairs):
        num = random.randint(1,30)
        numbers.append(num)
        numbers.append(num)
    random.shuffle(numbers)
    return numbers
    

#función para chequear los pares de números dados por el usuario
def checkNumbers():
    global highestScore
    numbers = createPairs()
    score = 0 
#Comprobar si los indices dados contienen el mismo números
    while len(numbers) > 0 :
        
        
        try:
            a = int(input("Elige un número entre 0 y {}: \n \n".format(len(numbers) - 1)))
            b = int(input("Elige otro número entre 0 y {}: \n \n".format(len(numbers) - 1)))

            if a < 0 or b < 0 or a >= len(numbers) or b >= len(numbers):
                print("Índices fuera de rango. Intenta de nuevo.")
                continue
            if a == b:
                print("Debes elegir 2 posiciones diferentes")
                continue


            num1 = numbers[a]
            num2 = numbers[b]
    
            if num1 == num2:
        
                print("El número es:", num1)
                print("El número es:",num2)
                score += 10
                print("has encontrado una pareja! \n")
                print("puntaje" , score ,"puntos \n")
                print("has ganado 10 puntos")
    
    
    
    
        #Se remueven las parejas encontradas
                numbers[a] = None
                numbers[b] = None
        #se iteran los números y elimina los elementos ya encontrados
                numbers = [n for n in numbers if n is not None]
                print("debes encontrar", round(len(numbers)/2), "parejas más")
            
                
    
            elif num1 != num2:
                print("El número es:",num1)
                print("El número es:",num2)
                print("Los numeros no coinciden vuelve a intentar")
        except ValueError:
            print("Debes digitar números")
        
    ##puntuación maxima
    if score > highestScore:
        highestScore = score
    
    
      
    
        


while(True):
    print("\n Bienvenido a tu juego 'Memory Numbers' \n")
    print("Elige una opción:\n")
    print("Opción 1: Partida Nueva")
    print("Opción 2: Ver Puntuación Máxima")
    print("Opción 3: salir")
    
    answer = input("Elige tu opción: \n" )

    if answer == "1":
        checkNumbers()


    elif answer == "2":
        print("Tu puntaje máximo es de: ",highestScore, "puntos")
    elif answer == "3":
        print("Gracias por haber jugado")
        break



