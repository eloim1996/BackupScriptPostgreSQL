import menus.menu_bem_vindo
import menus.menu_conexao
import tratamentos.tratamento_opcao
import tratamentos.tratamento_servidor
import tratamentos.tratamento_porta
import tratamentos.tratamento_senha
import tratamentos.tratamento_servidor
import tratamentos.tratamento_usuario
import pwinput
import os
import psycopg2


def conexao_banco():
    limpar = lambda: os.system('cls')
    menus.menu_bem_vindo.boas_vindas()

    global servidor_origem
    servidor_origem = 'win-dsp-banco01'#input("Nome ou ip do servidor origem: ")
    while not servidor_origem:
        limpar()
        menus.menu_bem_vindo.boas_vindas()
        tratamentos.tratamento_servidor.servidor_vazio()
        servidor_origem = input("\nNome ou ip do servidor origem: ")

    global usuario
    usuario = 'postgres'#input("Nome do usuário: ")
    while not usuario:
        limpar()
        menus.menu_bem_vindo.boas_vindas()
        tratamentos.tratamento_usuario.usuario_vazio()
        usuario = input("\nNome do usuário: ")

    global senha_usuario
    senha_usuario = 'abc123!'#pwinput.pwinput("Insira a senha do usuário: ")
    while not senha_usuario:
        limpar()
        menus.menu_bem_vindo.boas_vindas()
        tratamentos.tratamento_senha.senha_vazia()
        senha_usuario = pwinput.pwinput("\nInsira a senha do usuário: ")
        

    global porta_postgres
    tratamentos.tratamento_porta.menu_porta()
    opcao = input("Selecione uma opção: ")
    while not opcao:
        limpar()
        tratamentos.tratamento_opcao.opcao_branco()
        tratamentos.tratamento_porta.menu_porta()
        opcao = input("Selecione uma opção: ")
            
    while opcao.isdigit() == False:
        if not opcao:
            limpar()
            tratamentos.tratamento_opcao.opcao_branco()
            tratamentos.tratamento_porta.menu_porta()
            opcao = input("Selecione uma opção: ")       
        else:    
            limpar()
            tratamentos.tratamento_opcao.opcao_letra()
            tratamentos.tratamento_porta.menu_porta()
            opcao = input("Selecione uma opção: ")

    while int(opcao) < 1 or int(opcao) > 2:
        limpar()
        tratamentos.tratamento_opcao.opcao_invalida()
        tratamentos.tratamento_porta.menu_porta()
        opcao = input("Selecione uma opção: ")           
        while not opcao:
            limpar()
            tratamentos.tratamento_opcao.opcao_branco()
            tratamentos.tratamento_porta.menu_porta()
            opcao = input("Selecione uma opção: ")
        while opcao.isdigit() == False:
            if not opcao:
                limpar()
                tratamentos.tratamento_opcao.opcao_branco()
                tratamentos.tratamento_porta.menu_porta()
                opcao = input("Selecione uma opção: ")       
            else:    
                limpar()
                tratamentos.tratamento_opcao.opcao_letra()
                tratamentos.tratamento_porta.menu_porta()
                opcao = input("Selecione uma opção: ")

                                                            
    if opcao == "1":
        porta_postgres = 5432
    elif opcao == "2":
        porta_postgres = input("Insira a porta por favor: ")
        while not porta_postgres:
            limpar()
            tratamentos.tratamento_porta.porta_nula()
            porta_postgres = input("Insira a porta por favor: ")

        while porta_postgres.isdigit() == False:
            if not porta_postgres:
                limpar()
                tratamentos.tratamento_porta.porta_nula()
                porta_postgres = input("Insira a porta por favor: ")
                limpar()
            else:
                limpar()    
                tratamentos.tratamento_porta.porta_com_letra()
                porta_postgres = input("Insira a porta por favor: ")

    global database_origem
    database_origem = input("\nBanco de dados onde será rodado o procedimento: ").upper()
    while not database_origem:
        database_origem = input("Banco de dados onde será rodado o procedimento: ").upper()

def tentativa_conexao():
    try:
        conectar = psycopg2.connect(host=f'{servidor_origem}', database=f'{database_origem}',user=f'{usuario}', password=f'{senha_usuario}', port =f'{porta_postgres}')
        global opcao_reconect
        opcao_reconect = 0
    except psycopg2.OperationalError as e:
        limpar = lambda: os.system('cls')
        limpar()
        print(f'''Conexão falhou!!\n
{e}\n
Deseja tentar novamente
[1] - Sim 
[2] - Não    
        ''') 
        opcao_reconect = input("Selecione uma opção: ")
        #tratamento opção      
        while opcao_reconect.isdigit() == False:
            if not opcao_reconect:
                limpar()
                tratamentos.tratamento_opcao.opcao_branco()
                menus.menu_conexao.try_conect()
                opcao_reconect = input("Selecione uma opção: ")       
            else:    
                limpar()
                tratamentos.tratamento_opcao.opcao_letra()
                menus.menu_conexao.try_conect()
                opcao_reconect = input("Selecione uma opção: ")

        while int(opcao_reconect) < 1 or int(opcao_reconect) > 2:
            limpar()
            tratamentos.tratamento_opcao.opcao_invalida()
            menus.menu_conexao.try_conect()
            opcao_reconect = input("Selecione uma opção: ")           
            while not opcao_reconect:
                limpar()
                tratamentos.tratamento_opcao.opcao_branco()
                menus.menu_conexao.try_conect()
                opcao_reconect = input("Selecione uma opção: ")
            while opcao_reconect.isdigit() == False:
                if not opcao_reconect:
                    limpar()
                    tratamentos.tratamento_opcao.opcao_branco()
                    menus.menu_conexao.try_conect()
                    opcao_reconect = input("Selecione uma opção: ")       
                else:    
                    limpar()
                    tratamentos.tratamento_opcao.opcao_letra()
                    menus.menu_conexao.try_conect()
                    opcao_reconect = input("Selecione uma opção: ")

        while opcao_reconect == "1":
            try:
                limpar()
                conexao_banco()
                conectar = psycopg2.connect(host=f'{servidor_origem}', database='postgres',user=f'{usuario}', password=f'{senha_usuario}', port =f'{porta_postgres}')
                opcao_reconect = "0"
            except psycopg2.OperationalError as e:
                limpar = lambda: os.system('cls')
                limpar()
                print(f'''Conexão falhou!!\n
{e}\n
Deseja tentar novamente?
[1] - Sim 
[2] - Não    
                ''') 
                opcao_reconect = input("Selecione uma opção: ")
                #tratamento opção      
                while opcao_reconect.isdigit() == False:
                    if not opcao_reconect:
                        limpar()
                        tratamentos.tratamento_opcao.opcao_branco()
                        menus.menu_conexao.try_conect()
                        opcao_reconect = input("Selecione uma opção: ")       
                    else:    
                        limpar()
                        tratamentos.tratamento_opcao.opcao_letra()
                        menus.menu_conexao.try_conect()
                        opcao_reconect = input("Selecione uma opção: ")

                while int(opcao_reconect) < 1 or int(opcao_reconect) > 2:
                    limpar()
                    tratamentos.tratamento_opcao.opcao_invalida()
                    menus.menu_conexao.try_conect()
                    opcao = input("\nSelecione uma opção: ")           
                    while not opcao_reconect:
                        limpar()
                        tratamentos.tratamento_opcao.opcao_branco()
                        menus.menu_conexao.try_conect()
                        opcao_reconect = input("Selecione uma opção: ")
                    while opcao_reconect.isdigit() == False:
                        if not opcao_reconect:
                            limpar()
                            tratamentos.tratamento_opcao.opcao_branco()
                            menus.menu_conexao.try_conect()
                            opcao_reconect = input("Selecione uma opção: ")       
                        else:    
                            limpar()
                            tratamentos.tratamento_opcao.opcao_letra()
                            menus.menu_conexao.try_conect()
                            opcao_reconect = input("Selecione uma opção: ")


        if int(opcao_reconect) == 2:
            print("##################")
            print("# Fim do sistema #")
            print("##################")
        