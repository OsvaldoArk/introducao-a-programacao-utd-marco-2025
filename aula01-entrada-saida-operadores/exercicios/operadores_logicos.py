'''
Sendo v1 = 15, v2 = 10, v3 = 5, v4 = 0, defina qual será a resposta (VERDADEIRO OU FALSO) para as sentenças lógicas abaixo.
a) (v1 = 10) E (v2 = 10) 			b) (v1 = 15) E (v2 = 10) 	c) (v1 = 15) E (v3 = 10)
d) (v2 > 5) OU (v3 < 10) 			e) (v4 = 1) OU (v3 = 4) 	f) (v2 = 10) OU (v4 = 5)
g) (v1 > 10 E v2 < 15) E (v3 < 10 E v4 = 0) 	h) (v1 < 10 E v2 > 15) OU (v3 > 5 OU v4 = 0)
'''

v1 = 15
v2 = 10
v3 = 5
v4 = 0
proposicao01 =  v1 > 10 and v2 < 15
proposicao02 =  v3 < 10 and v4 == 0

resultado_g = proposicao01 and proposicao02

resultado_g_direto = (v1 > 10 and v2 < 15) and (v3 < 10 and v4 == 0)

resultado_h =  (v1 < 10 and v2 > 15) or (v3 > 5 or v4 == 0)

print(resultado_h)