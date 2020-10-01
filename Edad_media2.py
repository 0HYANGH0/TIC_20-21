def edad_media():
    print "introduce numero: "
    numero=input ()
    mayor=numero
    menor=numero
    for cont in range (1, 11):
        print "Nuevo numero: "
        numero= input ();
        if (numero < menor):
            menor = numero
    print "Menor", menor
    print "Mayor", mayor

edad_media()



