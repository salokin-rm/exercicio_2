"""
Programa: Armazenamento de Números
Descrição: Este programa armazena os números 2 e 3, calcula a sua soma e imprime na tela o resultado.
Autor: Nikolas Martins
Data: 21/06/2023
Versão: 0.0.1
"""

# Atribuição de variáveis

variavel = []
tamanho = [0, 0]
x=0

# Entrada de dados

print("Digite os numeros 2 e 3 separados por enter: ")

# Processamento de dados

for y in range(len(tamanho)):
    x=x+1
    coringa = float(input(f"{x}º numero: ")) #variável transição
    variavel.append(coringa)
    
# Saída de dados
   
if len(variavel)==2:
    print("Números digitados:",variavel,".")
    
    