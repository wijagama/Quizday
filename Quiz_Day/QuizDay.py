from Pandas import jugar_quiz,animate_text,Score_G,top3_from_csv #Aca se referencia el archivo Pandas_pre y exportamos, y en el import usamos las funciones de cada uno





def main():
   
    #Asci_art un recurso alfanumerico que muestra imagenes de forma secuencial.
    ascii_art = r"""

            ██████╗░██╗███████╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗██╗██████╗░░█████╗░  ░█████╗░
            ██╔══██╗██║██╔════╝████╗░██║██║░░░██║██╔════╝████╗░██║██║██╔══██╗██╔══██╗  ██╔══██╗
            ██████╦╝██║█████╗░░██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║██║██║░░██║██║░░██║  ███████║
            ██╔══██╗██║██╔══╝░░██║╚████║░╚████╔╝░██╔══╝░░██║╚████║██║██║░░██║██║░░██║  ██╔══██║
            ██████╦╝██║███████╗██║░╚███║░░╚██╔╝░░███████╗██║░╚███║██║██████╔╝╚█████╔╝  ██║░░██║
            ╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░░╚════╝░  ╚═╝░░╚═╝

            ░██████╗░██╗░░░██╗██╗███████╗  ██████╗░░█████╗░██╗░░░██╗
            ██╔═══██╗██║░░░██║██║╚════██║  ██╔══██╗██╔══██╗╚██╗░██╔╝
            ██║██╗██║██║░░░██║██║░░███╔═╝  ██║░░██║███████║░╚████╔╝░
            ╚██████╔╝██║░░░██║██║██╔══╝░░  ██║░░██║██╔══██║░░╚██╔╝░░
            ░╚═██╔═╝░╚██████╔╝██║███████╗  ██████╔╝██║░░██║░░░██║░░░
            ░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░
                                                
            """
    #Aca se anima el ascii_art para que se muestre en la terminal
    animate_text(ascii_art)
    print("¡Hola! Bienvenido a esta emocionante aventura.")

    # Se solicita al usuario que ingrese su nombre del usuario que esta jugando
    

    # Bucle principal que muestra el menú de opciones y gestiona la interacción del usuario
    while True:
        print("\nOpciones:")
        print("1) Iniciar Quiz")
        print("2) Top 3")
        print("3) Salir")

        # Se solicita al usuario que elija  una opción
        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == "1":
            # Inicia curses y ejecuta el cronómetro en una ventana de curses
            
# El resto de tu juego de preguntas puede continuar desde aquí sin bloquear el cronómetromamos la funcion de las preguntas para que puedas recorrerse en el menu principal

            nombre = input("Por favor, introduce tu nombre: ")
            print(f"\n¡Hola, {nombre}!")
            resultado_quiz = jugar_quiz(nombre)
            tema_seleccionado,  Score = resultado_quiz
            Score_G(nombre, tema_seleccionado,  Score)
            
            #Aca se utiliza se guarda el nombre del usuario, para poder imprimirlo en el txt
            

        elif opcion == "2":
            
            top3_result = top3_from_csv("resultados.csv", "Puntuacion")
            print("Los 3 mejores resultados basados en la Puntuacion son:")
            print(top3_result)
            break
           # 3 resultado, top 3 de los que mas puntuacion tengan
        

        elif opcion == "3":
            # Opción para salir del programa
            print("\n¡Gracias por jugar! ¡Hasta la próxima!")
            break  # Se sale del bucle while

        else:
            # Opción inválida
            print("\nOpción inválida. Por favor, selecciona una opción válida.")

# Bloque de ejecución principal que verifica si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()  # Llama a la función principal "main" para co



