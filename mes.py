'''Me va pedir el numero de un mes'''
def mes():
    abreviaMes="EneFebMarAbrJunJulAgoSepOctNovDic"
    numeroMes=input("Introduce mes: ")
    pos=(numeroMes-1)*3
    print("El mes es: ", abreviaMes[pos:pos+3])

mes()
