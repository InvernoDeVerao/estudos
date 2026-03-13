"""
\033[0;33;44m]
(33 = text) 
30 = branco
31 = vermelho
32 = verde  
33 = amarelo
34 = azul
35 = magenta
36 = ciano
37 = cinza

(0 = style ) 
0 = normal
1 = negrito
4 = sublinhado
7 = invertido

(44 = background)
40 = branco
41 = vermelho
42 = verde
43 = amarelo
44 = azul
45 = magenta
46 = ciano
47 = cinza
"""

print ("\033[0;31;46mOlá, mundo!\033[m")
a = 10
b = 20
print(f"os valores são a = \033[33m{a}\033[0m e b = \033[34m{b}\033[0m")

cores= {
    'azul': "\033[34m",
    'vermelho': "\033[31m",
    'verde': "\033[32m"
}
print(f"o valor de a é {cores['verde']}{a}\033[0m e o valor de b é {cores['azul']}{b}\033[0m")