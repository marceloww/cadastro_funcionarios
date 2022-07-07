# # Projeto 1
# #     Estamos criando um módulo de login do nosso aplicativo, e você deve obter as seguintes informações do funcionário

# # Módulo 1 - Gerar registro do funcionario

# Funcionalidades do módulo 1
#     1. Obtenha o nome do usuario
#     2. Obtenha idade do usuário
#     3. Registra de forma automática a data do cadastro do usuário, usando a data do registro como data de registro
#     4. Para cada novo funcionario que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:
#     cartões = ['R$50,00' , 'R$250,00' , 'R$120,00']
#     5. Guarde informações sobre a data de aniversário do funcionário (dd/mm/aaaa)

# Modulo 2 - Gerar apresentação do usuário
#Funcionalidades do módulo 2 - Mensagem de boas vindas!
#Usando os dados obtidos no módulo 1 exiba as seguintes informações:
    # 1.Olá (nome do usuário), seu registro foi concluído com sucesso no dia (data de cadastro no formato dd/mm/aaaa).
    #  Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).

from datetime import datetime
import random

print('----------- Olá, bem vindo a nossa empresa -----------')
nome_funcionario = input('Digite seu nome completo: ')
idade_funcionario = int(input('Digite sua idade: '))
data_cadastro = datetime.now()
cartoes = ['R$50,00' , 'R$250,00' , 'R$120,00' , 'R$130,00' , 'R$180,00']
cartao = random.choice(cartoes)
aniversario = datetime.strptime(
    input('Digite sua data de aniversário no formato dia/mês/ano: '), '%d/%m/%Y')

print(f'Ola {nome_funcionario}, seu registro foi concluído com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}.\nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}')


# Nesse projeto foi criado um mini-sistema de cadastro de nome e idade e um sorteio posteriormente.
# Foi usado strings dinâmicas, datetime e tempo, além da biblioteca random para realização do sorteio.