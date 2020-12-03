def ejercicio_9():
    horas_totales=input("Cuantas horas extras: ")
    precio_normal=30
    precio_extra=1.5*precio_normal
    if(horas_totales<=40):
        salario=horas_totales*precio_normal
    else:
        salario=40*precio_normal+(horas_totales-40)*precio_extra
    print "SALARIO= ",salario

ejercicio_9()
