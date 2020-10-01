'''escribe un programa que genere'''
def contrasena():
    nombre=raw_input("introduce el nombre: ")
    apellido=raw_input("intrduce el apellido: ")
    print nombre,"",apellido, " eres el impostor?"
    print"las tres letras iniciales ",3*nombre+2*apellido
    
contrasena() 
