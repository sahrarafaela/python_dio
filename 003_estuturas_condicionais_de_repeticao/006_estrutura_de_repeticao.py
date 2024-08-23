"""
O QUE SÃO E COMO USAR ESTRUTURAS DE REPETIÇÃO

- estruturas para repetir um trecho de código determinado números de vezes

* for
* for else: executa no final
"""

texto = input ("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
        
        if letra.upper() in VOGAIS: 
               letra, end=" "


# não muito utilizado
for letra in texto:
        
    if letra.upper() in VOGAIS: 
        print(letra, end=" ")
else: 
    "executa no final do laço"
