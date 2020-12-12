def separar_por_linha():
        print('-'*82)
# Criada funções para colorir strings de modo mais facil

def vermelho(palavra):
    print(f'\u001b[31m{palavra}\u001b[0m')

def verde(palavra):
    print(f'\u001b[32m{palavra}\u001b[0m')

def amarelo(palavra):
    print(f'\u001b[33m{palavra}\u001b[0m')

def azul(palavra):
    print (f'\u001b[34m{palavra}\u001b[0m')

# Apresentando o programa
def apresentar_programa():


    separar_por_linha()
    print ('''\u001b[32m]
               
            
                ██ ███    ██ ██    ██ ██ ███████ ████████  █████        ███    ███ ███████ 
                ██ ████   ██ ██    ██ ██ ██         ██    ██   ██       ████  ████ ██      
                ██ ██ ██  ██ ██    ██ ██ ███████    ██    ███████ █████ ██ ████ ██ █████   
                ██ ██  ██ ██  ██  ██  ██      ██    ██    ██   ██       ██  ██  ██ ██      
                ██ ██   ████   ████   ██ ███████    ██    ██   ██       ██      ██ ███████ 
                                                                           
                                                                           

    
    \u001b[0m''')

    print(' '*35 + 'Pronto para investir?')
    separar_por_linha()




