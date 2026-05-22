from time import sleep

from lib.interface import *
from lib.arquivo import *
lista = ["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sitema"]

arq = "nomes_cadastro.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(lista)

    if resposta == 1:
        cabecalho("Lista de pessoas")
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho("Cadastro pessoas")
        nome_pessoa = input("Digite o nome da pessoa: ")
        idade_pessoa = input("Digite idade da pessoa: ")
        cadastrar(arq, nome_pessoa, idade_pessoa)
    elif resposta == 3:
        cabecalho("Saindo do sistema")
        break
    else:
        print("Digite opção válida!")
    sleep(2)