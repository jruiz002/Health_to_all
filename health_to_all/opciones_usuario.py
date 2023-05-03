# Funciones para las opciones que tendra el usuario luego de registrarse e iniciar sesion

# Importaciones
import submenus
import pagina
import csv
import pandas as pd
import sys

# Funcion para mostrar el menu principal del programa
def menu_principal():
    repetir_menu = True
    while repetir_menu == True:
        print('\nHEALTH TO ALL')
        print('1. Registrarse')
        print('2. Iniciar Sesión')
        print('3. Salir')

        opcion = input('Ingrese la opción que desee:')

        if opcion == '1':
            pagina.registrarse()

        elif opcion == '2':
            pagina.login()

        elif opcion == '3':
            repetir_menu = False
            sys.exit()
        else:
            print('La opción ingresada no es válida')

# Funcion para mostrar el menu del usuario
def menu(usuario, user_found):
    print('\nBienvenido '+ usuario)
    print('1. Llenar formulario')
    print('2. Dietas pesonalizadas')
    print('3. Cerrar sesión')

    opcion = input('Ingrese la opción que desee:')

    # Llenar el formulario
    if opcion == '1':
        formulario(usuario, user_found)

    # Ver dietas
    elif opcion == '2':
        dietas(usuario)

    # Salir y regresar al menu principal del programa
    elif opcion == '3':
        menu_principal()

    else:
        print('La opción ingresada no es es válida')


# Funcion para el formulario de personalizacion de dietas
def formulario(usuario, user_found):
    print('\nIngresa los siguientes datos para mostrarte dietas personalizadas:')

    # Datos personales
    telefono = input('Número de telefono:')
    peso = input('Peso:')
    altura = input('Altura(cm):')
    edad = input('Edad:')
    costo = input('Presupuesto para la receta (Q):')

    # Tipo de alergia
    alergia = submenus.tipo_alergia()

    # Complejidad de la receta
    complejidad = submenus.tipo_complejidad()

    # Tiempo de comida
    tiempo = submenus.tipo_tiempo_de_comida()


    if telefono != '' and peso != '' and altura != '' and edad != '' and costo != '':

        # Modo lectura para ver los datos
        with open('usuarios.csv', mode='r', newline='') as archivo:
            reader = csv.reader(archivo)
            row_general = [row for row in reader]
        # Buscar al usuario y actualizarle los datos con los filtros para sus dietas personalizadas
        for i in range(len(row_general)):
            if row_general[i][0] == usuario:
                row_general[i][3] = telefono
                row_general[i][4] = peso
                row_general[i][5] = altura
                row_general[i][6] = edad
                row_general[i][7] = alergia
                row_general[i][8] = complejidad
                row_general[i][9] = costo
                row_general[i][10] = tiempo
                break
        # Modo escritura para guardar los cambios de datos
        with open('usuarios.csv', mode='w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerows(row_general)

        # Regresar al menu del usuario
        print('Ya puede ver sus recetas personalizadas!')

    else:
        print('No se pudo crear la personalizacion de dietas, asegurese de llenar todos los datos solicitados')
    
    menu(usuario, user_found)

# Funcion para mostrarle las dietas personalizadas al usuario
def dietas(nombreEncontrado):
    users_csv = pd.read_csv("./usuarios.csv")
    new_user = users_csv.loc[users_csv["Nombre"] == nombreEncontrado]
    
    if list(new_user['Alergias'].isna())[0]:
        print()
        print("¡Llena el formulario para poder visualizar tus dietas!")
        print()
        menu(list(new_user["Nombre"])[0], new_user)
    else:
        reader_csv_dietas = pd.read_csv("./recetas.csv", encoding='latin-1')
        
        print()
        print("A continuación se le muestran las dietas personalizadas: ")
        print()
        if len(reader_csv_dietas.loc[(reader_csv_dietas["Alergias"] == list(new_user["Alergias"])[0]) & 
                                        (reader_csv_dietas["Complejidad_receta"] == list(new_user["Complejidad_receta"])[0]) &
                                        (reader_csv_dietas["Costo_receta"] <= list(new_user["Costo_receta"])[0]) &
                                        (reader_csv_dietas["Tiempo_de_comida"] == list(new_user["Tiempo_de_comida"])[0]), "Nombre"]) > 0:
            
            print("#----" + "Nombre dieta")
            dietas_encontradas = reader_csv_dietas.loc[(reader_csv_dietas["Alergias"] == list(new_user["Alergias"])[0]) & 
                                        (reader_csv_dietas["Complejidad_receta"] == list(new_user["Complejidad_receta"])[0]) &
                                        (reader_csv_dietas["Costo_receta"] <= list(new_user["Costo_receta"])[0]) &
                                        (reader_csv_dietas["Tiempo_de_comida"] == list(new_user["Tiempo_de_comida"])[0]), "Nombre"]
            print(dietas_encontradas)
            
            list_index = []
            for i in dietas_encontradas.index:
                list_index.append(i)

            print()

            id_dieta = int(input("Seleccione la dieta que desea para saber sus ingredientes y pasos: "))
            if id_dieta in list_index:
                print()
                print("Ingredientes:")

                #Ingredientes
                ingredientes = (list(reader_csv_dietas.loc[reader_csv_dietas["#"] == (int(id_dieta)+1), "Ingredientes"])[0]).split("/")

                for index, ingrediente in enumerate(ingredientes):
                    print("- ", ingrediente)

                print()

                #Pasos
                print("Pasos")
                pasos = (list(reader_csv_dietas.loc[reader_csv_dietas["#"] == (int(id_dieta)+1), "Pasos"])[0]).split("/")
            
                for index, paso in enumerate(pasos):
                    print("- ", paso)

                print()
            else:
                print("Dieta no válida.")


        # Si en tal caso no existen dietas segun los filtros ingresados por el usuario
        else:
            print('No existen dietas para lo que solicitas')

        menu(list(new_user["Nombre"])[0], new_user)
        