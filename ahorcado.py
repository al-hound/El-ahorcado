import os
import random

def inici():
    print("Antes de empezar, ¿Como te llamas? ")
    global nom
    nom = input().capitalize()
    print("Bienvenido", nom,", tus decisiones condenaran o salvaran a alguien")
    print("         ")

def menu():
    print("Escoge una opción")
    print("         ")
    print("1.  Preparar juego")
    print("2.  Jugar")
    print("3.  Resultado final del juego")
    print("4.  Salir")
    a = input()
    return a

def prepararJoc():
    global abecedari
    abecedari = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f",
                 "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l",
                 "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r",
                 "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x",
                 "Y", "y", "Z", "z", "salir"]
    paraules = ["inquisicion", "brian", "python",
                "monty", "spam", "flying", "circus", "exloro",
                "pijus", "magnificus", "romanus", "domum",
                "queseros","lancelot", "supercalifragilisticoespialidoso"]
    global paraula
    paraula = random.choice(paraules)
    global palUsuari
    palUsuari = []
    global num
    num = len(paraula)
    for p in range(num):
        palUsuari.append(' _ ')
    global numJugades
    numJugades = 0
    global numLletres
    numLletres = 0
    global numErrades
    numErrades = 0


def mostrarFallida():
    if numErrades == 0:
        print("             ")
        print("Su destino está en tus manos... ")
        print("             ")
        print("--------     ")
        print("|/           ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|__________  ")
        print("             ")
    elif numErrades == 1:
        print("             ")
        print("Comenzamos mal!")
        print("             ")
        print("--------|    ")
        print("|/           ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|__________  ")
        print("             ")
    elif numErrades == 2:
        print("             ")
        print("Te recuerdo que su vida está en TUS manos")
        print("             ")
        print("--------|    ")
        print("|/      |    ")
        print("|            ")
        print("|            ")
        print("|            ")
        print("|__________  ")
        print("             ")
    elif numErrades == 3:
        print("             ")
        print("No lo lograras salvar si sigues asi")
        print("             ")
        print("             ")
        print("--------|    ")
        print("|/      |    ")
        print("|       O    ")
        print("|            ")
        print("|            ")
        print("|__________  ")
        print("             ")
    elif numErrades == 4:
        print("             ")
        print("Tiene mujer e hijos...")
        print("             ")
        print("--------|    ")
        print("|/      |    ")
        print("|       O    ")
        print("|       |    ")
        print("|            ")
        print("|__________  ")
        print("             ")
    elif numErrades == 5:
        print("             ")
        print("¿Quieres dejar una viuda y un herfano?")
        print("             ")
        print("--------|    ")
        print("|/      |    ")
        print("|       O    ")
        print("|      /|    ")
        print("|            ")
        print("|__________  ")
        print("             ")
    elif numErrades == 6:
        print("             ")
        print("también tiene un perrito rescatado, cojo y ciego el pobre...")
        print("             ")
        print("--------|    ")
        print("|/      |    ")
        print("|       O    ")
        print("|      /|\   ")
        print("|            ")
        print("|__________  ")
        print("             ")
    elif numErrades == 7:
        print("             ")
        print("su madre sufre una enfermedad terminal...")
        print("             ")
        print("--------|    ")
        print("|/      |    ")
        print("|       O    ")
        print("|      /|\   ")
        print("|       |    ")
        print("|__________  ")
        print("             ")
    elif numErrades == 8:
        print("             ")
        print("es hijo único, su madre depende de él")
        print("             ")
        print("--------|    ")
        print("|/      |    ")
        print("|       O    ")
        print("|      /|\   ")
        print("|       |    ")
        print("|______/___  ")
        print("             ")
    elif numErrades == 9:
        print("             ")
        print("¡Haz algo! ¡esta es su última oportunidad...! ")
        print("¡SALVALO POR FAVOR!")
        print("             ")
        print("--------|    ")
        print("|/      |    ")
        print("|       O    ")
        print("|      /|\   ")
        print("|       |    ")
        print("|______/_\_  ")
        print("             ")
    elif numErrades == 10:
        print("             ")
        print("!LO MATASTE!")
        print("!MONSTRUO!")
        print("               ")
        print("--------|      ")
        print("|/      |      ")
        print("|       X      ")
        print("|      /|\     ")
        print("|       |      ")
        print("|      / \     ")
        print("|__________    ")
        print("               ")

def llegirLletra():
    global lletra
    lletra = ""
    print("para acabar antes, escribe 'salir'")
    while lletra not in abecedari:
        lletra = input("escribe una letra: ")
    lletra = lletra.lower()
     
def buscarLletra():
    os.system("cls")      
    indxparaula = 0
    global lletra
    global numLletres
    global palUsuari2
    global numErrades
    global numJugades
    concideix = 0
    for a in paraula:
        if a == lletra and a != palUsuari2[indxparaula]:
            numLletres = numLletres + 1
            palUsuari2[indxparaula] = lletra
        if a == lletra:
            concideix += 1
        indxparaula += 1
    if concideix == 0:
        numErrades = numErrades + 1
    numJugades = numJugades + 1
    

def mostrarResultats():
    global palUsuari2
    palUsuari2 = palUsuari
    print(*palUsuari2)
    print("         ")
    print("         ")

def resultatFinal():
    print("Jugaste", numJugades, "veces")
    print("La palabra era", paraula, "y tenía", num, "letras, de las cuales acertaste", numLletres)
    print("Fallaste", numErrades, "veces")
    print("         ")
    print("Un agujero de gusano hizo que tus respuestas viajen en el tiempo")
    if numErrades == 10:
        print(nom, ", mataste a tu nieto!")
    elif numLletres == num:
        print(nom, ", salvaste a tu nieto")
    elif lletra == "salir":
        print("te condenaste a tí mismo,", nom)
    mostrarFallida()
    mostrarResultats()
    print("         ")
    print("         ")
    
    
    
x = ""
pre = ""
inici()
while x != "4":
    x = menu()
    if x == "1":
        os.system("cls")
        print("Has escogido 'Preparar juego'")
        prepararJoc()
        pre = "1"
    elif x == "2":
        if x == "2" and pre == "1":
            print("Has escogido 'Jugar'")
            pre = "2"
            os.system("cls")
            while numErrades != 10 and num != numLletres:
                mostrarFallida()
                mostrarResultats()
                llegirLletra()
                if lletra == "salir":
                    os.system("cls")
                    break
                buscarLletra()
            mostrarFallida()
        else:
            if x == "2" and pre != "1":
                os.system("cls")
                print("Primero debes preparar el juego!")
    elif x == "3":
        if x == "3" and pre == "2":
            os.system("cls")
            resultatFinal()
            print("Has escogido 'Resultado final del juego'")
            pre = "3"
        else:
            if x == "3" and pre != "2":
                os.system("cls")
                print("Primero debes Jugar!")
    elif x == "4":
        os.system("cls")
        print("Has escogido 'Salir'")
    else:
        os.system("cls")
        print("opción no valida")

     
