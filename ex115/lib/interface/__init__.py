def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[031mERRO: por favor, digite um número inteiro válido\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[031mEntrada de dados interrompida pelo usuário\033[m")
            return 0
        else:
            return ndef leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[031mERRO: por favor, digite um número inteiro válido\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[031mEntrada de dados interrompida pelo usuário\033[m")
            return 0
        else:
            return n

def linha(tam=42):
    return '_' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc

def linha(tam=42):
    return '_' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc