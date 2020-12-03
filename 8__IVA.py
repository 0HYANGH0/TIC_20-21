Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def iva():
	i=1
	p=input("Inserte precio sin I.V.A.: ")
	while i==1:
		print "********************"
		print "*       MENU       *"
		print "********************"
		print "Escoja el tipo de I.V.A. entre los siguientes: "
		print "1.General, 16%"
		print "2.Reducido, 7%"
		print "3.Superreducido 4%"
		o=input("Introduzca 1, 2 o 3: ")
		if o==1:
			print p*(1+0.16), "euros."
			i=0
		else:
			if o==2:
				print p*(1+0.07), "euros."
				i=0
			else:
				if o==3:
					print p*(1+0.04), "euros."
					i=0
				else:
					print "Escoja entre 1, 2 o 3"
					i=1

					
>>> iva()
