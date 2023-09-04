import os
import os.path
import sys
import string
os.system('cls')


#analisador lexico

#tok1 - Palavras Reservadas
# tok0 - varINTidade
# tok1 - varFLTpeso
# tok2 - varFLTaltura
# tok3 - LEIA
# tok4 - PRINT
# tok3 - varINTresultado
# tok4 - IF
# tok5 - ELSE

# tok1 - Operador
#   tok100 - .
#   tok101 - +
#   tok102 - -
#   tok103 - *
#   tok104 - /
#   tok105 - ++
#   tok106 - --
#   tok107 - ==
#   tok108 - !=
#   tok109 - >
#   tok110 - >=
#   tok111 - <
#   tok112 - <=
#   tok113 - &&
#   tok114 - ||
#   tok115 - =

# tok3 - Delimitador
#   tok - ;
#   tok200 - ,
#   tok201 - (
#   tok202 - )
#   tok203 - {
#   tok204 - }
#   tok205 - [
#   tok206 - ]

# tok404 - Cadeia constante
# ========================== ERROS LEXICOS
# Simbolo nao pertencente ao conjunto de simbolos terminais da linguagem
# Identificador Mal formado
# Tamanho do identificador
# Numero mal formado
# Fim de arquivo inesperado (comentario de bloco nao fechado)
# Caractere ou string mal formados
# ==============================================================================