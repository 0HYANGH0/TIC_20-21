'''Dime un numero al azar entre el 1 y 10 y lo adivino'''
import random

def adivino_2():
    maxn=1000000000
    numero=random.randint(1,maxn)
    intento=input("intentalo: ")
    while intento!=numero:
        if intento>numero:
            print "Demasiado grande"
        if intento<numero:
            print "Demasiado pequeño"
        intento=input("intentalo: ")
    print "Has acertado"
        
    


adivino_2()
