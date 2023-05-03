# Funciones con las opciones principales que tendra el usuario al ingresar al programa

# Importaciones
import pandas as pd
import csv
import opciones_usuario
import re

# Función que busca un usuario por su correo y si existe devuelve true, sino false
def user_exists(username):
    users=pd.read_csv('./usuarios.csv')
    usuario_encontrado = users.loc[users['Correo']==username, 'Correo']
    if  len(usuario_encontrado)==0:
        return False
    else:
        return True

# Función para registrar un nuevo usuario para el programa
def registrarse():
    print('\nIngrese los siguientes datos:')
    nombre = input('Nombre: ')
    correo = input('Correo: ')
    password = input('Contraseña: ')
    telefono = ''
    peso = ''
    altura = ''
    edad = ''
    alergias = ''
    complejidad = ''
    costo = ''
    tiempo = ''

    if user_exists(correo) == True:
       print('El correo que deseas registrar ya esta en uso')
    else:
        if es_correo_valido(correo):
            # El ingreso fue correcto
            archivo = open('./usuarios.csv', mode='a', newline='')
            writer = csv.writer(archivo)
            writer.writerow([nombre, correo, password, telefono, peso, altura, edad, alergias, complejidad, costo, tiempo])
            print('El usuario fue registrado con exito!')
        else:
            print()
            print("Intente otra vez con un correo válido, por favor.")

# Función para que los usuarios pueda iniciar sesión 
def login():
    users=pd.read_csv('./usuarios.csv')
    correo = input('\nCorreo:')
    password = input('Contraseña:')
    
    usuario_encontrado = None

    # Validacion de correo y contraseña
    for indice_fila in range(len(users)):
        usuario_actual = users.iloc[indice_fila]

        if usuario_actual["Correo"] == correo: 
            if str(usuario_actual["Password"]) == password:
                usuario_encontrado = usuario_actual
    
    nombre_usuario = users.loc[(users['Correo']==correo) & (users['Password']==password), 'Nombre']
    #user = users.loc[(users['Correo']==correo) & (users['Password']==password)] 
    if usuario_encontrado is not None:
        nombre_usuario = usuario_encontrado["Nombre"]
        opciones_usuario.menu(nombre_usuario, usuario_encontrado)

    # En tal caso no pueda iniciar sesión
    else:
        print('El correo o la contraseña son incorrectos')

# Funcion para verificar que el correo ingresado por el usuario sea valido
def es_correo_valido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None
