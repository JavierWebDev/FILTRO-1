import os 
import func.peliculas as pl
import func.corefiles.corePeliculas as cf

opcPelis = ["Agregar pelicula","Editar pelicula","Eliminar pelicula","Eliminar actor","Buscar Pelicula","Listar peliculas","Volver"]

peliculas = {}

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

                nombre = input("[-] Ingrese el nombre de la pelicula: ")
                duracion = input("[-] Ingrese el duracion de la pelicula: ")
                sinopsis = input("[-] Ingrese el sinopsis de la pelicula: ")

                pelicula = {
                    'id':'',
                    'nombre':nombre,
                    "duracion":duracion,
                    'sinopsis':sinopsis,
                    'generos':{},
                    'actores':{},
                    'formatos':{}
                }
                idAu = str(f"A0{len(data)+1}")
                    
                pelicula["id"] = idAu

                peliculas.update(pelicula)
                pl.New(pelicula)

                isActiveRegGenero = True
                while isActiveRegGenero:
                    os.system("cls")
                    print("*************")
                    print("REGISTRO GENERO")


                    genero = {
                        'id': '',
                        'nombre':nombre
                    }
                    isActiveRegGenero = False


                    