def escolha(opcao): # escolher a opcao, caso seja uma invalida, fica no loop
    while opcao not in ['1','2','3']:
        opcao = input('''INVALIDO, escolha uma opção valida:  
        1. Apartamento (com 1 quarto);
        2. Casa (com 1 quarto); 
        3. Estudio: ''')
    return opcao

def calcular_aluguel(tipo_lugar, num_quarto ,garagem, num_veiculos):
    if tipo_lugar == '1':    #OPÇÃO DO APARTAMENTO
        aluguel_base = 700
        if num_quarto >1:
            aluguel_base += 200 * (num_quarto -1)
        if garagem.upper() == 'S':
             aluguel_base += 300
        if num_quarto == 1 or num_quarto == 0:
            desconto = input("Vc possui filhos? S|N ").upper() # desconto caso NAo haja filho
            if desconto == 'N':
                aluguel_base *= 0.85
    elif tipo_lugar == '2': #OPÇÃO DA CASA
        aluguel_base = 900
        if num_quarto >1 :
            aluguel_base += 250 * (num_quarto-1)
        if garagem.upper() == 'S':
            aluguel_base += 300
    elif tipo_lugar == '3': # OPÇÃO DO ESTUDIO
        aluguel_base = 1200
        if garagem.upper() == 'S':
            aluguel_base += 250
        if num_veiculos == 2 or num_veiculos == 0:
            aluguel_base = aluguel_base
        elif num_veiculos > 2:
            aluguel_base += 60 * (num_veiculos-2)
    return aluguel_base


    


