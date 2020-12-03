Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def salario():
	p=30
	h=input("Inserte las horas trabajadas: ")
	if h>40:
		print "Cobrará", (30*40)+(h-40)*45, "euros."
	else:
		print "Cobrará", h*p, "euros."

		
>>> salario()
