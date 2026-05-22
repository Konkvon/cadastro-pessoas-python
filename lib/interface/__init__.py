def linha(tam=42):
    return '-' * tam

def leiaInt(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print("Erro! Digite um numero inteiro valido")
      continue
    except KeyboardInterrupt:
      print("Entrada de dados interrompida pelo usuario")
      return 0
    else:
      return n

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for i in lista:
        print(f"{c} --- {i}")
        c += 1
    print(linha())
    opc = leiaInt("Sua opção: ")
    return opc