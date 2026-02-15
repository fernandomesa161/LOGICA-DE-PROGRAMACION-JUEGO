
#creamos la interfas para que pueda ingresar de una forma interactiva y damos la bienvenida
jugar = None
opciones = ("","no")

while True:
    jugar =input("Para iniciar el juego preciona enter ,y para cerrar ingresa no: ").lower()
    if jugar == "":
        print("bienvenido y que la pases super bien :)")
    if jugar == "no":
        print("gracias por tu tiempo")
        break
        
    
     
    # se importa una lista random
    import random
    #ponemos nuestros elementos en una lista ademas de preguntar el numero de rondas por jugar

    lista = ("tijera","papel","piedra")
    i = 0
    rondas= int(input("¿cuantas rondas deceas jugar?: "))
    while  i < rondas :
    #Hacemos que el usuario escoja una opcion de la lista sino la repetimos asta que la escoja
             contricante = random.choice(lista)
             jugador = None
             print("VAMOS AVER QUIEN GANA ESCOGE LA MEJOR OPCION!!")
             while jugador not in lista:
                   jugador = input("tijera,papel o piedra?: ").lower() 
         # Damos la reglas del juego ademas de incluir un mensaje en cada resultado 
                   if jugador == contricante:
                           print("contricante :",contricante)
                           print("jugador: ",jugador)
                           print("Empate!!")

                   elif jugador == "papel" :
                       if contricante == "tijera":
                            print("contricante : ",contricante)
                            print("jugador: ", jugador)
                            print("perdiste!!:C")

                       if contricante == "piedra":
                           print("contricante: ",contricante)
                           print("jugador: ",jugador)
                           print("ganaste!>.<")

                   elif jugador == "piedra":
                       if contricante == "papel":
                            print("contricante : ",contricante)
                            print("jugador: ", jugador)
                            print("perdiste!!:C")

                       if contricante == "tijera":
                           print("contricante: ",contricante)
                           print("jugador: ",jugador)
                           print("ganaste!>.<")

                   elif jugador == "tijera":
                       if contricante == "piedra":
                            print("contricante : ",contricante)
                            print("jugador: ", jugador)
                            print("perdiste!!:C")

                       if contricante == "papel":
                           print("contricante: ",contricante)
                           print("jugador: ",jugador)
                           print("ganaste!>.<")
                  
                #colocamos i+= 1 para que el bucle sepa cuando debe de termninar
                   i+= 1
               # mensaje de felicitacion jjj
                   print("jugaste muy bien!:)")   
      
    
    

         
    
    
    
    


    

