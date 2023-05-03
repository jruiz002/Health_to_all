# Jose Gerardo Ruiz Garcia
# Humberto Alexander de la Cruz Chanchavac
# Daniel Oswaldo Juarez Herrera
# Juan Diego Solís Martínez
# Diego Oswaldo Flores Rivas

# Programa que ayudará a las personas a encontrar dietas personalizadas según su estado fisico y posiblidades económicas; además permitirá
# generar dietas segun el tiempo de comida que desee el usuario y se le brindadrán los ingredientes y pasos. Esto con el fin de atacar
# el ODS de salud y bienestar.

# Importaciones
import pagina

repetir_menu = True

# Menu incial del programa
while repetir_menu == True:
    print('\nHEALTH TO ALL')
    print('1. Registrarse')
    print('2. Iniciar Sesión')
    print('3. Salir')

    opcion = input('Ingrese la opción que desee:')

    # Ingresar al registro del programa
    if opcion == '1':
        pagina.registrarse()

    # Ingresar al login del programa
    elif opcion == '2':
        pagina.login()

    # Salir del programa
    elif opcion == '3':
        repetir_menu = False
    else:
        print('La opción ingresada no es válida')