from ejercicio1.main1 import main1
from ejercicio2.main2 import main2

def main():
    ejr = input("Escribe el numero del ejercicio que desea ejecutar: ") 
    if ejr == '1':
        main1()
    elif ejr == '2':
        main2()