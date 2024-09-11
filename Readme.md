# LocaHouse

## Descrição

O LocaHouse é um programa simples em Python desenvolvido para calcular o custo de aluguel de propriedades com base nas opções fornecidas pelo usuário. O programa oferece três tipos de imóveis: Apartamento, Casa e Estúdio. Dependendo das escolhas do usuário, o custo do aluguel é ajustado com base em fatores como número de quartos, garagem e veículos.

## Funcionalidades

1. **Escolha do Tipo de Imóvel**:
    - Apartamento (com 1 quarto)
    - Casa (com 1 quarto)
    - Estúdio

2. **Configurações de Imóvel**:
    - Número de quartos adicionais
    - Garagem (sim/não)
    - Número de veículos adicionais (apenas para Estúdio)

3. **Cálculo do Aluguel**:
    - Ajuste do valor base do aluguel com base nas configurações fornecidas pelo usuário.
    - Aplicação de desconto caso o usuário não tenha filhos e escolha um apartamento com um quarto.

## Arquivos

### `funcoes_locacoes.py`

Este arquivo contém as funções principais utilizadas pelo programa:

- `escolha(opcao)`: Solicita ao usuário que escolha uma opção válida entre 1, 2 e 3. Se a opção fornecida for inválida, o usuário será solicitado a tentar novamente.

- `calcular_aluguel(tipo_lugar, num_quarto, garagem, num_veiculos)`: Calcula o valor do aluguel com base no tipo de imóvel, número de quartos, presença de garagem e número de veículos. Aplica ajustes e descontos conforme necessário.

### `main.py`

Este é o script principal que executa o programa:

1. Exibe uma mensagem de boas-vindas e as opções disponíveis.
2. Solicita ao usuário que escolha o tipo de imóvel e outras configurações.
3. Calcula o valor do aluguel utilizando as funções do arquivo `funcoes_locacoes.py`.
4. Exibe o valor total do aluguel com base nas escolhas do usuário.

## Como Executar

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Clone o repositório ou faça o download dos arquivos `funcoes_locacoes.py` e `main.py`.
3. Navegue até o diretório onde os arquivos estão localizados.
4. Execute o script principal usando o seguinte comando:

   ```bash
   python main.py
Olá, seja bem vindo(a) a LocaHouse
'''
      1. Apartamento (com 1 quarto);
      2. Casa (com 1 quarto);
      3. Estúdio
'''

Digite o número da sua escolha: 1
Quantos quartos adicionais? 2
Gostaria de adicionar uma garagem? S|N: S
Vc possui filhos? S|N N
Sua escolha foi 1 , você pagará R$ 1400.0
