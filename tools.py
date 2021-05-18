from getpass import getpass

def logo():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print ('''
░██████╗███████╗████████╗██╗░█████╗░░░░░░░██████╗░██████╗░
██╔════╝██╔════╝╚══██╔══╝██║██╔══██╗░░░░░░██╔══██╗██╔══██╗
╚█████╗░█████╗░░░░░██║░░░██║██║░░╚═╝█████╗██████╔╝██████╔╝
░╚═══██╗██╔══╝░░░░░██║░░░██║██║░░██╗╚════╝██╔═══╝░██╔══██╗
██████╔╝███████╗░░░██║░░░██║╚█████╔╝░░░░░░██║░░░░░██║░░██║
╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░╚════╝░░░░░░░╚═╝░░░░░╚═╝░░╚
    ''')
    print('Seção de Tecnologia da Informação e Comunicação')
    print('''
Olá, este é um script criado pela equipe da SETIC-PR, em
modo precário, que tem como finalidade auxiliar os colegas
do NULOG-PR nos lançamentos de acautelamento de material.''')

def login():
    print('''
====================== Login SIPAC ======================    
    ''')

