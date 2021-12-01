import os
import hashlib
import time

from pygame import mixer




print('''
//                                _                    _         _                  _
//                               | |                  | |       | |                | |
//   __ _   ___  _ __   __ _   __| |  ___   _ __    __| |  ___  | |__    __ _  ___ | |__   ___
//  / _` | / _ \| '__| / _` | / _` | / _ \ | '__|  / _` | / _ \ | '_ \  / _` |/ __|| '_ \ / __|
// | (_| ||  __/| |   | (_| || (_| || (_) || |    | (_| ||  __/ | | | || (_| |\__ \| | | |\__ \\
//  \__, | \___||_|    \__,_| \__,_| \___/ |_|     \__,_| \___| |_| |_| \__,_||___/|_| |_||___/
//   __/ |
//  |___/
//
#By. MrArthurEmanuel
''')

print(f'''--------------------------------------------------------------------------
            \n*se é a primeira vez que usa essa aplicação, é recomendado que abra o menu de ajuda para mais informações*

                                        OBSERVAÇÃO: 
            TODOS OS COMÂNDOS TERÃO QUE SER INSERIDOS COM LETRAS MINÚSCULAS, EX (--init) 
            E NÃO COM LETRAS MAIÚSCULAS, EX (--INIT). 
            SE FOR INSERIDO COM LETRAS MAIÚSCULAS, A APLICAÇÃO FECHARÁ.
            
//Digite --help para ver o menu de ajuda ou --init para iniciar o programa.''')
entrada1 = input('\n> ')

while entrada1 == '--help':
    print(f'''           GERADOR DE HASHS SIMPLES

    --------- AVISO IMPORTANTE ----------
    A APLICAÇÃO AINDA ESTÁ EM FASE DE TESTES,
    SENDO ASSIM, AINDA PODE APRESENTAR ALGUNS ERROS
    INESPERADOS. 
    ----------------------------------------------------------------------------------
                    MODO DE USO

    1 - EXISTEM 10 MODOS DE CRIPTOGRAFIA HASH DISPONIVEIS PARA USO,
    ESCOLHA A CRIPTOGRAFIA DESEJADA NO MENU E CRIE SEU HASH.

    2 - VOCÊ PODE ENCERRAR O PROGRAMA A QUALQUER MOMENTO APERTANDO CTRL + C OU 
    DANDO O COMANDO (--exit).

    3 - VOCÊ PODE CRIAR UM HASH DE QUALQUER STRING, NOME OU NUMEROS.

    4 - NÃO TENTE EXECUTAR UM COMANDO MAIS DE UMA VEZ PARA QUE O PROGRAMA NÃO FECHE.

    5 - AO FINAL DO MENU DE AJUDA, IRÁ ABRIR A NOVA LINHA PARA ENTRADA DO COMANDO 
    DESEJADO, DIGITE (--init) PARA DAR INICIO AO PROGRAMA OU (--exit) PARA ENCERRAR.

    6 - AO FINAL DO PROGRAMA, SERÁ PERGUNTADO SE VOCÊ DESEJA SALVAR O HASH GERADO EM 
    UM ARQUIVO .TXT; ESSE ARQUIVO FICA SALVO LOCALMENTE NA SUA MÁQUINA. ESSE PROGRAMA 
    NÃO SALVA AS HASHS GERADAS EM NUVEM OU SERVIDORES.

    ----------------------------------------------------------------------------------''')
    

    entrada1 = input('> ')

if entrada1 == '--exit':
    print('A aplicação será encerrada. Obrigado por usar!')
    time.sleep(1)
    os.system('pause')
    exit()


if entrada1 == '--init':

    def Prog():

            string = input(f'''\nDigite o texto/string a ser gerado o HASH
> ''')

            
            if string == '--exit':
                print('A aplicação sera encerrada. Obrigado por usar!')
                time.sleep(1)
                os.system('pause')
                exit()     

            menu = int(input('''### MENU DOS HASHES ###
--------------------------------------------
1) MD5
2) SHA-1 
3) SHA-224
4) SHA-256
5) SHA-384
6) SHA-512
7) SHA3-224
8) SHA3-256
9) SHA3-384
10) SHA3-512
--------------------------------------------
Digite o numero do tipo de hash a ser gerado: '''))

            

            if menu == 1:
                resultado = hashlib.md5(string.encode('utf-8'))
                print("\nO Hash MD5 de",string, "é:", resultado.hexdigest())
            elif menu == 2:
                resultado = hashlib.sha1(string.encode('utf-8'))
                print("\nO Hash SHA-1 de",string,"é:", resultado.hexdigest())
            elif menu == 3:
                resultado = hashlib.sha224(string.encode('utf-8'))
                print("\nO Hash SHA-224 de",string,"é:", resultado.hexdigest())
            elif menu == 4:
                resultado = hashlib.sha256(string.encode('utf-8'))
                print("\nO Hash SHA-256 de",string,"é:", resultado.hexdigest())
            elif menu == 5:
                resultado = hashlib.sha384(string.encode('utf-8'))
                print("\nO Hash SHA-384 de",string,"é:", resultado.hexdigest())
            elif menu == 6:
                resultado = hashlib.sha512(string.encode('utf-8'))
                print("\nO Hash SHA-512 de",string,"é:", resultado.hexdigest())
            elif menu == 7:
                resultado = hashlib.sha3_224(string.encode('utf-8'))
                print("\nO Hash SHA3-224 de",string,"é:", resultado.hexdigest())
            elif menu == 8:
                resultado = hashlib.sha3_256(string.encode('utf-8'))
                print("\nO Hash SHA3-256 de",string,"é:", resultado.hexdigest())
            elif menu == 9:
                resultado = hashlib.sha3_384(string.encode('utf-8'))
                print("\nO Hash SHA3-384 de",string,"é:", resultado.hexdigest())
            elif menu == 10:
                resultado = hashlib.sha3_512(string.encode('utf-8'))
                print("\nO Hash SHA3-512 de",string,"é:", resultado.hexdigest()) 
            

            else:
                menu = int(input('''\nA opção digitada não existe. Digite uma das opções de Hash abaixo:
       --------------------------------------------
1) MD5
2) SHA-1 
3) SHA-224
4) SHA-256
5) SHA-384
6) SHA-512
7) SHA3-224
8) SHA3-256
9) SHA3-384
10) SHA3-512
--------------------------------------------
Digite o numero do hash a ser gerado: '''))



            if menu == 1:
                resultado = hashlib.md5(string.encode('utf-8'))
                print("\nO Hash MD5 de",string, "é:", resultado.hexdigest())
            elif menu == 2:
                resultado = hashlib.sha1(string.encode('utf-8'))
                print("\nO Hash SHA-1 de",string,"é:", resultado.hexdigest())
            elif menu == 3:
                resultado = hashlib.sha224(string.encode('utf-8'))
                print("\nO Hash SHA-224 de",string,"é:", resultado.hexdigest())
            elif menu == 4:
                resultado = hashlib.sha256(string.encode('utf-8'))
                print("\nO Hash SHA-256 de",string,"é:", resultado.hexdigest())
            elif menu == 5:
                resultado = hashlib.sha384(string.encode('utf-8'))
                print("\nO Hash SHA-384 de",string,"é:", resultado.hexdigest())
            elif menu == 6:
                resultado = hashlib.sha512(string.encode('utf-8'))
                print("\nO Hash SHA-512 de",string,"é:", resultado.hexdigest())
            elif menu == 7:
                resultado = hashlib.sha3_224(string.encode('utf-8'))
                print("\nO Hash SHA3-224 de",string,"é:", resultado.hexdigest())
            elif menu == 8:
                resultado = hashlib.sha3_256(string.encode('utf-8'))
                print("\nO Hash SHA3-256 de",string,"é:", resultado.hexdigest())
            elif menu == 9:
                resultado = hashlib.sha3_384(string.encode('utf-8'))
                print("\nO Hash SHA3-384 de",string,"é:", resultado.hexdigest())
            elif menu == 10:
                resultado = hashlib.sha3_512(string.encode('utf-8'))
                print("\nO Hash SHA3-512 de",string,"é:", resultado.hexdigest()) 

            
 

            enter = input('Deseja salvar o hash em um arquivo de texto? (s/n) > ')

            if enter == 's':
                arquivo = open('HashGerado.txt', 'a')
                arquivo.write(f'''\n---------------------------------------\n{resultado.hexdigest(), string}''')
                print('Arquivo salvo com o nome: HashGerado.txt. Obrigado por usar!')
                time.sleep(1)
                os.system('pause')
                exit() 

            if enter == 'n':
                enter2 = input('Tem certeza que não quer salvar (s/n) > ')

            if enter2 == 's':
                arquivo = open('HashGerado.txt', 'a')
                arquivo.write(f'''\n---------------------------------------\n{resultado.hexdigest(), string}''')
                print('Boa escolha!\nArquivo salvo com o nome: HashGerado.txt. Obrigado por usar!')
                time.sleep(1)
                os.system('pause')
                exit()  

            if enter2 == 'n':
                print('Ok. Encerrando aplicação! Obrigado por usar!')
                time.sleep(1)
                os.system('pause')
                exit()     

    Prog()
mixer.init()
mixer.music.load('musiquinha.mp3')
mixer.music.play()
time.sleep(2)
os.system('pause')