from ejr1 import *

raiz = huffman(tabla)  
comprimir(input('Escriba el mensaje que quiere que se codifique: '), raiz)
descomprimir(raiz[0], raiz[0], input("Escribe el mensaje que quiere que se descodifique: "), 0)