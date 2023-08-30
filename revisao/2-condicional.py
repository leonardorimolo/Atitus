A = False
B = True
C = False

if A:
	if B:
		print("Comando 1")
	else:
		print("Comando 2")
	print("Comando 3")
else:
	print("Comando 4")
	if C:
		print("Comando 5")
	elif B:	
		print("Comando 6")
		
'''
Quais comandos serão executados se:
a) A = True, B = False e C = True 
b) A = False, B = True e C = True  
c) A = True, B = True e C = False  
d) A = False, B = False e C = False  
e) Quais os valores de A, B e C para que somente os comandos 4 e 6 sejam executados? 
'''