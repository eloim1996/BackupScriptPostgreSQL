import classes.conexao_postgresql
import os
import funcoes.backup

limpar = lambda: os.system('cls')

classes.conexao_postgresql.conexao_banco()
classes.conexao_postgresql.tentativa_conexao()

if int(classes.conexao_postgresql.opcao_reconect) == 0:
    limpar()
    funcoes.backup.dump_postgres()
else:
    limpar()
    print("################################################")
    input("# Sistema encerrado. Aperte enter para fechar: #")
    print("################################################")
    