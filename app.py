from utilidades import apresentar_programa, verde, vermelho, amarelo, azul, separar_por_linha
import json
from os import sys
from pathlib import Path
from playsound import playsound

def salvar_alteracoes(investimentos):
    investimento_json = json.dumps(investimentos)
    Path('investimentos.json').write_text(investimento_json)

def criar_investimentos_iniciais():
    lista_de_investimentos =  [

        {
            "id":1,
            "nome":"Computador",
            "valor": 3000
        },
        
        {
            "id":2,
            "nome":"Playstation",
            "valor": 2500
        },
        {
            "id":3,
            "nome":"Carta de Motorista",
            "valor": 1500
        },
        {
            "id":4,
            "nome":"Entrada p/ Casa Própria",
            "valor": 10000
        },
        {
            "id":5,
            "nome":"Carro",
            "valor": 18000
        },
        {
            "id":6,
            "nome":"Teclado",
            "valor": 600
        }

    ]
    investimentos_json = json.dumps(lista_de_investimentos)
    Path('investimentos.json').write_text(investimentos_json)



def ler_investimentos_existentes():
    investimentos_json = Path('investimentos.json').read_text()
    investimentos = json.loads(investimentos_json)
    return investimentos


def exibir_investimento_total():
    investimentos = ler_investimentos_existentes()
    total = 0
    for investimento in investimentos:
        total = investimento['valor'] + total

    verde('O total investido até o momento foi de: ' + 'R$' + str(total))


def listar_investimentos(exibir_todos=False):
    from tabulate import tabulate
    investimentos = ler_investimentos_existentes()
    lista_de_investimentos = []
    if exibir_todos == False:
        for investimento in investimentos[0:5]:
         lista_de_investimentos.append(
            [investimento['id'],investimento['nome'],investimento['valor']])
        print(tabulate(lista_de_investimentos, headers=['id','nome','valor']))
    else:
        for investimento in investimentos:
            lista_de_investimentos.append(
                [investimento['id'],investimento['nome'],investimento['valor']])
        print(tabulate(lista_de_investimentos, headers=['id','nome','valor']))

def apresentar_menu():
    separar_por_linha()
    verde('1 - Listar todos os investimentos')
    amarelo('2 - Editar investimento existente')
    vermelho('3 - Excluir investimento existente')
    azul('4 - Criar investimento')
    vermelho('5 - Sair do Programa')
    opcao = input('Digite uma opção: ')
    separar_por_linha()
    return opcao

def editar_investimento_existente(investimento_id):
    investimentos = ler_investimentos_existentes()
    nome = input('Digite o novo nome: ')
    valor = input('Digite o novo valor: ')
    for investimento in investimentos:
        if investimento['id'] == int(investimento_id):
            if nome != '':
                investimento.update({'nome':nome})
            if valor != '':
                investimento.update({'valor': int(valor)})
            salvar_alteracoes(investimentos)
            amarelo('Seu novo investimento e foi atualizado e sua identificação esta como: '),verde(investimento)

def excluir_investimento(investimento_id):
    investimentos = ler_investimentos_existentes()
    for indice,item in enumerate(investimentos):
        if item['id'] == int(investimento_id):
            vermelho(f'O investimento {item} foi excluído com sucesso!')
            del investimentos[indice]
            salvar_alteracoes(investimentos)

def obter_ultimo_id(investimentos):
    ultimo_investimento = investimentos[-1:]
    ultimo_id = ultimo_investimento[0]['id']
    ultimo_id += 1
    return ultimo_id

def criar_novo_investimento(nome,valor):
    investimentos = ler_investimentos_existentes()
    ultimo_id = obter_ultimo_id(investimentos)
    novo_investimento = {'id':ultimo_id, 'nome': nome, 'valor': valor}
    investimentos.append(novo_investimento)
    salvar_alteracoes(investimentos)
    azul(f'O investimento acaba de ser criado com as seguintes propriedades: {novo_investimento}')


if __name__ == '__main__':

    playsound('4-wheeler-dealer.wav',block=False)
    apresentar_programa()
    exibir_investimento_total()
    listar_investimentos()

    # Menu para listar todos, editar, excluir e criar investimentos
    while True:
        opcao = apresentar_menu()
        if opcao == '1':
            listar_investimentos(exibir_todos=True)
        if opcao == '2':
            investimento_id = input('Qual investimento deseja alterar?: ')
            editar_investimento_existente(investimento_id)
        if opcao == '3':
            investimento_id = input('Digite o id do investimento a excluir: ')
            excluir_investimento(investimento_id)
        if opcao == '4':
            nome = input('Nome do investimento a ser criado: ')
            valor = int(input('Valor do novo investimento: '))
            criar_novo_investimento(nome,valor)
        if opcao == '5':
            sys.exit(0)

