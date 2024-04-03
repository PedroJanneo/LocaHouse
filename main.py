
from funcoes_locacoes import *

print("Ola, seja bem vindo(a) a LocaHouse")
print( ''''
      1. Apartamento (com 1 quarto);
      2. Casa (com 1 quarto);
      3. Estudio
''')

tipo_lugar = escolha(input("Digite o numero da sua escolha: "))
num_quarto = 0
if tipo_lugar in ['1','2']:
    num_quarto = int(input("Quantos quartos adicionais? "))
    garagem = input("Gostaria de adicionar uma garagem ? S|N: ").upper()
    num_veiculos = 0
elif tipo_lugar in ['3']:
    garagem = input("Gostaria de adicionar uma garagem (com 2 vagas) ? S|N: ").upper()
    if garagem == 'S':
        num_veiculos = 0
        num_veiculos = (int(input("Quantos veiculos adicionais? (contando com as vagas já liberadas): ")))

aluguel_total = calcular_aluguel( tipo_lugar, num_quarto, garagem, num_veiculos) #aq ele vai calcular o aluguel
print("Sua escolha foi", tipo_lugar, ",vc pagará R$", aluguel_total)
