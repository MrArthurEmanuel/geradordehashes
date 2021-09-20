import hashlib

resultado = hashlib.md5(b'Arthur')

print("A hash é: ", resultado.hexdigest())