import pandas as pd
import random # Para selecionar aleatoriamente las preguntas de los temas 
import time
from pygame import mixer # audios del quiz,Importa el módulo 'mixer' de la biblioteca pygame para gestionar la reproducción de audio. 
from datetime import datetime #importa la hora exacta del pc para imprimirlo en codigo 

# Obtener la fecha y hora actual
fecha = datetime.now()

# Formatea la fecha y hora como una cadena sin microsegundos (score)
tiempo = fecha.strftime("%Y-%m-%d %H:%M:%S")   #?

def jugar_quiz(nombre):
    # Lista para registrar las respuestas y retroalimentación del usuario
    registro_preguntas = []
    # Cargar las preguntas desde un archivo CSV(leyendo archivo desde pandas)
    df = pd.read_csv('preguntas.csv')
     # Mensaje de bienvenida al juego
    print(f"¡Bienvenido al juego de preguntas y respuestas, {nombre}!")
    print("Responde las preguntas correctamente para ganar puntos.")
    print("!!AVISO!!\n Si se demoran mas de 10 Segundos en Responder una pregunta Se le descontara 5 Punto, Cada pregunta tiene valor de 10 Puntos") 

    # Preguntar al usuario si quiere seleccionar un tema o elegir uno aleatoriamente
    tema_elegido = input("¿Quieres seleccionar un tema (S) o elegir uno aleatorio (A)? ").strip().lower() #  elimina los espacios en blanco iniciales y finales/ y que coloque en minuscula en el CSV
    # Obtener solo a la columna de temas disponibles  del archivo csv        
    temas_disponibles = df['Tema'].unique() 
    # de acuerdo a  la opcion elegida del usuario sucede lo siguiente:            
    if tema_elegido == 's':
        # Si el usuario elige seleccionar un tema
        print("Temas disponibles:")
        #Hace una busqueda en la columna tema y los escala para poder imprimirlos 
        for i, tema in enumerate(temas_disponibles, 1): #recorre los temas,enumera desde la posicion 1  los temas que esten en el archivo csv y se va actualizando  e incrementando  a medida que va
            print(f"{i}. {tema}")
                    
        tema_seleccionado = None  # Inicializamos la variable con None(no hay valor)
        # se  crea otro bucle con while  ya que el usuario debe elegir el tema de interes y cuando  lo elija esa variable  se llenara con el tema elegido
        while tema_seleccionado is None:
            try:
                # solicitar al usuario el número del tema de acuerdo al archivo .csv
                numero_tema = int(input("Escribe el número del tema que deseas jugar: ")) -1 #el -1 se coloca para que tome el orde adecuado de los temas, no filtraba bien con las preguntas. 
                # aqui determina que de acuerdo al numero que escoja es el que va realizar las preguntas
                if 0 <= numero_tema < len(temas_disponibles): # los temas que estan entre 0 y la cantidad de temas(5)
                    tema_seleccionado = temas_disponibles[numero_tema] # y entre 0-5  sera el tema seleccionado
                    #si se dijita un numero diferente automaticamente va soltar la alerta
                else:
                    print("Por favor, ingresa un número válido.")
            except ValueError: #?
                print("Por favor, ingresa un número válido.")
        #aca hace el filtrado del tema que se seleciono del archivo  y se iguala al  numero digitado por el usuario(pasa saber si coincide)
        df_filtrado = df[df['Tema'] == tema_seleccionado]
     #En caso de que el usuario elija preguntas al azar, con la funcion random el programa elije uno.
    else:
        print("Has elegido un tema aleatorio.")
        #aca usa la funcion randon para escoger el tema al azar
        tema_seleccionado = random.choice(temas_disponibles)
        #aca se seleciona el tema al azar
        df_filtrado = df[df['Tema'] == tema_seleccionado]  # independientemente sea al azar o escogido, para  que lo frilte bien se hace nuevamente este codigo,
        #para que siga comparando  el tema  y no tome valores erroneos

     # Aca se determina que la puntuacion es 0            
    puntuacion = 0
    score_t = 100
    score = 0

    # Barajar las preguntas
    df_barajado = df_filtrado.sample(frac=1) #que me muestre el dataframe  del tema todas las pregutas de manera aleatoria pero sin repetirlas  ?

    # Limitar el número de preguntas a 10
    numero_preguntas = 10
    #Aca se recorreria las preguntas de acuerdo el tema selecionado
    for i, pregunta in df_barajado.iterrows(): #recorre todas las filas donde estan las pregutnas  del tema  en el csv
        if numero_preguntas == 0: #se inicialziza con 0 
            break  # Salir del bucle después de 10 preguntas
        tiempo_inicio = time.time()
        #Se utiliza para enumerar las preguntas.
        numero_pregunta = 11 - numero_preguntas # inicia desde 11 ya que hay una capa de titulo, y para que no comience  en 0
        print(f"\nPregunta {numero_pregunta} :")
        print("\n" + pregunta['Pregunta'])
        print("a) " + pregunta['Opción A'])
        print("b) " + pregunta['Opción B'])
        print("c) " + pregunta['Opción C'])
        print("d) " + pregunta['Opción D'])

        #Aca el usuario digita las opciones de acuerdo a la pregunta sin espacio y minusculas
        respuesta_usuario = input("Escribe la letra de tu respuesta (a, b, c o d): ").strip().lower()
        tiempo_transcurrido = time.time() - tiempo_inicio
        if tiempo_transcurrido > 10:
            print("¡Te has demorado demasiado! Se descontó 5 punto.")
            score -= 5
        # Validar que la respuesta sea 'a', 'b', 'c' o 'd'
        while respuesta_usuario not in ['a', 'b', 'c', 'd']: # si el usuario no coloca estas opciones  aparecera el mensaje de alerta
            print("Respuesta inválida. Por favor, ingresa 'a', 'b', 'c' o 'd'.")
            respuesta_usuario = input("Escribe la letra de tu respuesta (a, b, c o d): ").strip().lower()
        #Si la respuesta fue correcta automaticamente entra este if y te muestra el mensaje y lo almacena en una variable llamada retroalimentacion
        if respuesta_usuario == pregunta['Respuesta Correcta']:
            #va mostrar el mensaje(respuesta correcta) y la respuesta que digitaste
            retroalimentacion =  f"Respuesta Correcta {respuesta_usuario}" # cuando responda bien aparece este mensaje
            #Aca se almacena las preguntas  y su respectiva retroalimentacion al diccionario llamado registro preguntas,respuesta de usuario, y retroalimentacion
            registro_preguntas.append((pregunta['Pregunta'], respuesta_usuario, retroalimentacion))
            print(f"¡Respuesta correcta! {respuesta_usuario}") # aqui otro print de respuesta correcta para  el registro final 
            #para contar las preguntas correctas
            puntuacion += 1 # para que sume las respuestas correctas
            #Si la respuesta no  fue correcta automaticamente entra este else y te muestra el mensaje y lo almacena en una variable llamada retroalimentacion
        else: #basicamente hace lo mismo que en el if(respuestas correctas) pero en este caso con las incorrectas
            retroalimentacion = f"Respuesta incorrecta. La respuesta correcta es {pregunta['Respuesta Correcta']}."
            registro_preguntas.append((pregunta['Pregunta'], respuesta_usuario, retroalimentacion))
            print(retroalimentacion)  # Aquí imprimimos si la respuesta fue incorrecta
            score -=10
        
        # Restar 1 al número de preguntas que se han  realizado hasta llegar a 10(limite)
        numero_preguntas -= 1
    result = score_t + score
    # (init)Inicializa el módulo 'mixer', preparándolo para su uso
    mixer.init()
    # Aquí puedes proporcionar retroalimentación basada en la puntuación del usuario
    #Si la puntuacion es menor o igual a 5 te va mostrar el mensaje de perdiste y las caritas triste de acuerdo a cuantas preguntas correctas respondiste            
    if puntuacion <= 5:
        #Esto son los unicode que se utilizan para mostrar el emoticon y se multiplica de acuerdo a cuantas preguntas correctas
        total = puntuacion * "\U0001F622"
        print(f"¡Perdiste! Has respondido {puntuacion} de las 10 preguntas correctamente {total}, Score {result}/{score_t}.")
        retro = f"¡Perdiste! Has respondido {puntuacion} de las 10 preguntas correctamente.\U0001F622"
        # Carga el archivo de audio "Fail.wav" ubicado en la ruta especificada.
        mixer.music.load(r"Music\Fail.wav")
        #mixer.music.load(r"C:\Users\ASUS\Desktop\proyecto final\Fail.wav")
        
        # Reproduce el archivo de audio cargado.
        mixer.music.play()
        #Si la puntuacion es mayor o igual a 6 se imprimira la puntuacion y el tema selecionado que se eligio o que se tomo al azar
    elif puntuacion >= 6 :
        #Esto son los unicode que se utilizan para mostrar el emoticon y se multiplica de acuerdo a cuantas preguntas correctas
        total = puntuacion * "\U0001F604"
        print(f"¡Muy bien!. Tu puntuación es: {puntuacion} de 10 para el tema {tema_seleccionado} {total}, Score {result}/{score_t}.")
        retro = f"¡Muy bien!. Tu puntuación es: {puntuacion} de 10 para el tema {tema_seleccionado} {total}."
        # Carga el archivo de audio "Win.wav" ubicado en la ruta especificada.
        mixer.music.load(r"Music\Win.wav")
        #mixer.music.load(r"C:\Users\ASUS\Desktop\proyecto final\Win.wav")
        
        # Reproduce el archivo de audio cargado.
        mixer.music.play()
   # else:
       # print("Dijite un numero valido") #? 
    Score= f"{result}/{score_t}"
   #Aqui se le pregunta al usuario si Desea imprimir su retroalimentacion en un archivo txt
    a = input("¿Quieres imprimir en un archivo de texto tu retroalimentación? (Si o No): ")
    if a == 'si' or a =='Si':
        # Escribe las preguntas y retroalimentación en un archivo de texto
        with open('Registro_preguntas.txt', 'w', encoding='utf-8') as file:
            file.write("Registro de Preguntas y Retroalimentación:\n")
            file.write(f"Retroalimentacion de {nombre}\n")            
            file.write(retro + "\n") # retro es la variable que muestra si la pregunta es correcta o incorrecta con su puntuacion
            file.write("\n")
            file.write("###################\n")
            file.write("#     SCORE     #\n")
            file.write(f"###{result}/{score_t}###")
            file.write("\n###################\n")
            file.write("\n")
            for i, (pregunta, respuesta, retroalimentacion) in enumerate(registro_preguntas, 1):
                file.write(f"Pregunta {i}:\n")#escriba en el archivo  las pregutnas y respuestas 
                file.write(f"Pregunta: {pregunta}\n")
                file.write(f"Tu respuesta: {respuesta}\n")
                file.write(f"a) {df.loc[df['Pregunta'] == pregunta, 'Opción A'].values[0]}\n")
                file.write(f"b) {df.loc[df['Pregunta'] == pregunta, 'Opción B'].values[0]}\n")
                file.write(f"c) {df.loc[df['Pregunta'] == pregunta, 'Opción C'].values[0]}\n")
                file.write(f"d) {df.loc[df['Pregunta'] == pregunta, 'Opción D'].values[0]}\n")
                #El df.loc es para que me muestre tanto la fila como la columna de las preguntas.
                file.write(f"Retroalimentación: {retroalimentacion}\n\n")   
         #Este mensaje sale cada vez que el txt del registro de preguntas digitas por el usuario ha creado.
        print("El registro de preguntas y retroalimentación se ha guardado en 'Registro_preguntas.txt'.")
    else:
        print("No se guardará la retroalimentación en un archivo de texto.")
    result_Score = (tema_seleccionado,Score)
    return result_Score
    

#Esta funcion sirve para que Ascci art pueda recorrer  espacio por espacio( fraccion por fraccion)
def animate_text(texto): 
    #aqui recorre uno por uno cada bloque de texto de izquierda a derecha
    for caracter in texto:
        #Aqui imprimimos cada bloque de texto
        print(caracter, end='') # end indica que  no se agreguen caracteres adicionales al final, ni nuevas lineas  ni espacios, basicamente que lo imprima tal cual como esta
        #Aca se controla la rapidez con la que se debe imprimir cada bloque
        time.sleep(0.001)
    print()


#def Del_resul():
    #df = pd.read_csv('resultados.csv')
    #print(df)


def Score_G(nombre, tema_seleccionado, Score):
   
    
    archivo_csv = 'resultados.csv' # es un archivo que genera el programa,donde muesra los resultados de los jugadores
    
# Intenta cargar los resultados anteriores desde el archivo CSV (si existe)
    try:
        dp = pd.read_csv(archivo_csv)
    except FileNotFoundError: #?
        # Si el archivo CSV no existe, crea un DataFrame vacío con ese nombre
        dp = pd.DataFrame()

    # Crea un diccionario con el resultado actual,datos de usuario, puntuacion y tiempo
    nuevo_resultado = {
        'Nombre': [nombre],
        'Tema_Seleccionado': [tema_seleccionado],
        'Puntuacion': [Score],
        'Tiempo':[tiempo] #Fecha y la hora
    }

    # Convierte el nuevo resultado(los datos proporcionados y todo lo digitado por el usuario, y la informacion  del programa interno) en un DataFrame
    nuevo_resultado_df = pd.DataFrame(nuevo_resultado)

    # Concatena el nuevo DataFrame de resultados con el DataFrame existente (si lo hay), basicamente guarda los resultados de los jugadores en un df,
    dp = pd.concat([dp, nuevo_resultado_df], ignore_index = True) #gnore_index es para que no se restablezcan los indices,no se borren,que no haya duplicados cuando se  #inicie una nueva partida ?

    # Guarda el DataFrame actualizado en el archivo CSV
    dp.to_csv(archivo_csv, index=False) #index false, va a ocultar los indice 
    #diseño de score para diferenciarlo 
    print("\n")
    print("\n============================================================= SCORE ===============================================")
    # Muestra el DataFrame actualizado (opcional)
    print(dp)
    print("===================================================================================================================\n")
    print("\n")

def top3_from_csv(csv_file, Top_Ordenado):
    try:
        # Leer el archivo CSV en un DataFrame
        df = pd.read_csv(csv_file)
        
        # Ordenar el DataFrame por la columna especificada de forma descendente (mayor a menor)
        df_sorted = df.sort_values(by=Top_Ordenado, ascending=False)
        
        # Tomar los primeros 3 registros del DataFrame ordenado
        top3 = df_sorted.head(3).reset_index(drop=True) #Al usar reset_index(drop=True) después de head(3), eliminarás el índice original y asignarás un nuevo índice numérico secuencial.
        
        return top3
    except Exception as e:
        # Manejar cualquier error que pueda ocurrir durante la lectura del archivo CSV
        return f"Error: {str(e)}"