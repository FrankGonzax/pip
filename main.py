import random

choice = "1"
options = ("1", "2", "3")

while(choice != "4"):
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijera")
    print("4) Salir del juego")
    choice = input("Ingrese una opcion (1/2/3): ")

    if(choice != "1" and choice != "2" and choice != "3" and choice != "4"):
        print("Opcion invalida.")
    else:
        choiceComputer = random.choice(options)

        if(choice == choiceComputer):
            print("Eligieron lo mismo, por lo tanto es empate.")
        if(choice == "1" and choiceComputer == "2"):
            print("Papel gana a piedra, gana el computador")
        elif(choice == "1" and choiceComputer == "3"):
            print("Piedra gana a tijera, ganas tu.")
        if(choice == "2" and choiceComputer == "1"):
            print("Papel gana a piedra, ganas tu.")
        elif(choice == "2" and choiceComputer == "3"):
            print("Tijera gana a papel, gana el computador")
        if(choice == "3" and choiceComputer == "1"):
            print("Piedra gana a tijera, gana el computador.")
        elif(choice == "3" and choiceComputer == "2"):
            print("Tijera gana a papel, ganas tu.")