def menu():
    print "Introduce dos numeros enteros"
    numero1=input("numero 1= ")
    numero2=input("numero 2= ")
    print "****************************************"
    print "*               MENU                   *"
    print "****************************************"
    print "1.SUMA"
    print "2.RESTA"
    print "3.MULTIPLICACION"
    print "4.DIVISION"
    opcion= input ("Teclee la opcion elegida= ")
    if(opcion==1):
        resultado=numero1+numero2
    if(opcion==2):
        resultado=numero1-numero2
    if(opcion==3):
        resultado=numero1*numero2
    if(opcion==4):
        resultado=numero1/numero2
    print "el resultado es",resultado
menu()
