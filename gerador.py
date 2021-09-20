import os
import hashlib
import time
print('#' *25)
print('### Gerador de HASHES ###')
print('#' *25)
print('\nBy. Mr.Arthur (EU MESMO)')
string = input('\nDigite o texto a ser gerado o HASH: ')

menu = int(input('''### MENU DOS HASHES ###
--------------------------------------------
1) MD5
2) SHA1 
3) SHA256
4) SHA512
--------------------------------------------
Digite o numero do hash a ser gerado: '''))


if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print("\nO Hash MD5 de",string, "é:", resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("\nO Hash SHA1 de",string,"é:", resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("\nO Hash SHA256 de",string,"é:", resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("\nO Hash SHA512 de",string,"é:", resultado.hexdigest())

else:
    menu = int(input('''\nA opção digitada não existe. Digite uma das opções de Hash abaixo:
--------------------------------------------
1) MD5
2) SHA1 
3) SHA256
4) SHA512
--------------------------------------------
Digite o numero do hash a ser gerado: '''))


    if menu == 1:
        resultado = hashlib.md5(string.encode('utf-8'))
        print("\nO Hash MD5 de", string, "é:", resultado.hexdigest())
    elif menu == 2:
        resultado = hashlib.sha1(string.encode('utf-8'))
        print("\nO Hash SHA1 de", string, "é:", resultado.hexdigest())
    elif menu == 3:
        resultado = hashlib.sha256(string.encode('utf-8'))
        print("\nO Hash SHA256 de", string, "é:", resultado.hexdigest())
    elif menu == 4:
        resultado = hashlib.sha512(string.encode('utf-8'))
        print("\nO Hash SHA512 de", string, "é:", resultado.hexdigest())

time.sleep(2)
os.system('pause')