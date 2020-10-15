'''Dime un numero al azar entre el 1 y 10 y lo adivino'''
def adivino():
    numero=input("dime un numero del 1 al 10: ")
    intento=input("intentalo: ")
    while intento!=numero:
        if intento>numero:
            print "Demasiado grande"
        if intento<numero:
            print "Demasiado pequeño"
        intento=input("intentalo: ")
    print "Has acertado"
        
    


adivino()
