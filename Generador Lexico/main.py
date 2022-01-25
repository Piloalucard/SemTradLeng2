from lexico import  Lexico
import os

def clear():
    if os.name == "posix":
       os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")

def main():
    sal=0
    while(sal==0):
        print("")
        print("  /A N A L I Z A D O R   L E X I C O/")
        print("")
        lex = Lexico("if string agua123+pc*+/>")
        lex.leerSimb()
        print(lex.obtLexico())

        
        print("")
        print("")
        sal = int(input("    [D]igite 0 para repetir el programa si lo desea: "))
        clear()

main()