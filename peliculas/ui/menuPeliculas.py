import os 
import func.peliculas as pl
import func.corefiles.corePeliculas as cf

opcPelis = ["Agregar pelicula","Editar pelicula","Eliminar pelicula","Eliminar actor","Buscar Pelicula","Listar peliculas","Volver"]

def MenuPeliculas():
    IsActivePeli = True
    header = '''
    ********************************
    *  ADMINISTRADOR DE PELICULAS  *
    ********************************
    '''

    while IsActivePeli:
        cf.checkFile(pl.blockbuster)
        data = cf.ReadFile()
        try:
            for i, item in enumerate(opcPelis):
                print(f"{i+1}. {item}")
            opPelis = int(input("\n >) "))
        except ValueError:
            print("[!] VALOR INCORRECTO")
            os.system("pause")

        else:
            if opPelis == 1:
                titulo = '''
                    **********************
                    *  AGREGAR PELICULA  *
                    **********************
                '''

                pass