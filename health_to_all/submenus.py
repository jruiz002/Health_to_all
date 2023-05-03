# Jose Gerardo Ruiz Garcia
# Humberto Alexander de la Cruz Chanchavac
# Daniel Oswaldo Juarez Herrera
# Juan Diego Solís Martínez
# Diego Oswaldo Flores Rivas

# Funciones para los submenus de las opciones del formulario de la personalizacion de dietas

# Funcion para mostrar el menu de tipo de alergia de la receta
def tipo_alergia():
    repetir = True
    while repetir == True:
        print('\nAlergias:')
        print('1. Carnes')
        print('2. Mariscos')
        print('3. Frutos secos')
        opcion = input('Ingresa el tipo de alergia que tienes:')
        
        if opcion.isdigit():

            opcion = int(opcion)
            alergia = ''

            if opcion>0 and opcion<4:
                repetir = False
                if opcion == 1:
                    alergia = 'Carnes'
                elif opcion == 2:
                    alergia = 'Mariscos'
                elif opcion == 3:
                    alergia = 'Frutos secos'
                else:
                    print('Error')
                
                return alergia
            else:
                print('La opción seleccionada no es válida')

        else:
            print('La opción seleccionada no es valida, asegurese de que sea un valor numerico')


# Funcion para mostrar el menu de tipo de complejidad de la receta
def tipo_complejidad():
    repetir = True
    while repetir == True:
        print('\nComplejidad de las recetas:')
        print('1. Facil')
        print('2. Media')
        print('3. Dificil')
        opcion = input('Ingresa la complejidad de las recetas que deseas:')

        if opcion.isdigit():
            opcion = int(opcion)
            complejidad = ''

            if opcion>0 and opcion<4:
                repetir = False
                if opcion == 1:
                    complejidad = 'Facil'
                elif opcion == 2:
                    complejidad = 'Media'
                elif opcion == 3:
                    complejidad = 'Dificil'
                else:
                    print('Error')
                
                return complejidad
            else:
                print('La opción seleccionada no es válida')

        else:
            print('La opción seleccionada no es valida, asegurese de que sea un valor numerico')


# Funcion para mostrar el tiempo de comida de la receta
def tipo_tiempo_de_comida():
    repetir = True
    while repetir == True:
        print('\nTiempo de comida:')
        print('1. Desayuno')
        print('2. Almuerzo')
        print('3. Cena')
        opcion = input('Ingresa el tiempo de comida para el cual seran las dietas:')

        if opcion.isdigit():

            opcion = int(opcion)
            tiempo = ''

            if opcion>0 and opcion<4:
                repetir = False
                if opcion == 1:
                    tiempo = 'Desayuno'
                elif opcion == 2:
                    tiempo = 'Almuerzo'
                elif opcion == 3:
                    tiempo = 'Cena'
                else:
                    print('Error')
                
                return tiempo
            else:
                print('La opción seleccionada no es válida')

        else:
            print('La opción seleccionada no es valida, asegurese de que sea un valor numerico')