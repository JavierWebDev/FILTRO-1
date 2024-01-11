import os
import ui.mainMenu as mmenu
import ui.menuGeneros as mgeneros
import ui.menuActores as mactores
import ui.menuFormatos as mformatos
import ui.menuPeliculas as mpeliculas

def main():
    isActive = True
    
    while isActive:
        op = mmenu.MainMenu()
        
        if op == 1:
            mgeneros.MenuGeneros()
        elif op == 2:
            mactores.MenuActores()
        elif op == 3:
            mformatos.MenuFormatos()
        elif op == 4:
            mpeliculas.MenuPeliculas()
        else:
            print("[!] SALIENDO DEL PROGRAMA")
            isActive = False
    
    
if __name__ == "__main__":
    main()
