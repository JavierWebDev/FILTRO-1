import os

opcmenu = ["Administrador de generos","Administrador de actores", "Administrador de Formatos","Gestor de peliculas","Informes","SALIR"]

def MainMenu():
    isMainActive = True
    header = '''
    ******************
    *   BLOCKBUSTER  *
    *****************
    '''
    while isMainActive:
        os.system("cls")
        print(header)        
        
        try:
            for i,item in enumerate(opcmenu):
                print(f"{i+1}. {item}")
            op = int(input("\n >) "))
        except ValueError:
            print("[!] VALOR INCORRECTO")
            os.system("pause")
        else:
            return op
    
    