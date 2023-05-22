import getpass
from time import strftime
import os
from datetime import date
import pyperclip
import classes.conexao_postgresql
import menus.menu_bem_vindo

def dump_postgres():

    menus.menu_bem_vindo.boas_vindas()

    data = strftime("%d-%m-%Y-%H-%M-S")
    time = str(data)
    host = classes.conexao_postgresql.servidor_origem
    user = classes.conexao_postgresql.usuario
    password = classes.conexao_postgresql.senha_usuario
    database_name = classes.conexao_postgresql.database_origem
    diretorio_bin =input("Diretório Bin do PostgreSQL: ").rstrip('"')
    diretorio =input("Diretório onde será salvo o backup: ").rstrip('"')
    role = input("Nome da role(OWNER): ").upper()


    dumper = f'"{diretorio_bin}\\pg_dump.exe" --host={host} --username "{user}" --role "{role}" --blobs --verbose --file="{diretorio}\\{database_name}_{time}.backup_postgresql" -F c "{database_name}" \n\nECHO Backup feito com sucesso Verifique o arquivo {database_name}_{time}.backup_postgresql em {diretorio}! \n\n\npause'


    os.putenv('PGPASSWORD', password)

    print(f'{data}: backup iniciado para base {database_name}')   


    pyperclip.copy(dumper)

    #pegar o nome do usuário do pc
    usuario = getpass.getuser()

    #criar arquivo bat com as infos corretas e na área de trabalho
    criar_arquivo = open("C:\\Users\\" + usuario + "\\Desktop\\Backup.bat", "w")
    criar_arquivo.write(f"{dumper}")
    criar_arquivo.close()

    os.startfile("C:\\Users\\" + usuario + "\\Desktop\\Backup.bat")


    print(f'{data}: fim')

