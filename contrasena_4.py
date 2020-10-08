'''escribe un programa que genere una contrasena
con 3 letras de tu nombre y 3 de tu apellido'''
def contrasena_4():
    nombre=raw_input("introduce el nombre: ")
    apellido=raw_input("introduce el apellido: ")
    print nombre[-3:]+apellido[-3:]

contrasena_4()
