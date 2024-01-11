import os
import func.generos as gn
import func.corefiles.coreGeneros as cf

opcGeneros = ["Crear Genero", "Listar Generos", "Volver"]

generos = {}    

def MenuGeneros():
    header = '''
    ******************************
    *  ADMINISTRADOR DE GENEROS  *
    ******************************
    '''
    isActiveGeneros = True
    while isActiveGeneros:
        cf.checkFile(gn.generos)
        data = cf.ReadFile()
        try:
            os.system("cls")
            print(header)
            
            for i, item in enumerate(opcGeneros):
                print(f"{i+1}. {item}")
            opGeneros = int(input("\n >) "))
        except ValueError:
            print("[!] VALOR INCORRECTO")
            os.system("pause")
        else:
            if opGeneros == 1:
                titulo = '''
                    ******************
                    *  CREAR GENERO  *
                    ******************
                '''
                isActiveCreGenre = True
                while isActiveCreGenre:
                    os.system("cls")
                    print(titulo)
                    
                    nombre = input("[-] Ingresa nombre del genero: ")
                    
                    genero = {
                        'id':'',
                        'nombre':nombre
                    }
                    
                    idAu = str(f"G0{len(data)+1}")
                    
                    genero["id"] = idAu

                    generos.update(genero)
                    gn.New(genero)
                    rta = input("[?] Deseas ingresar otro genero? ([S] - SI | [N] - NO\n >)").upper
                    if rta != "S":
                        isActiveCreGenre = False
            
            elif opGeneros == 2:
                os.system("cls")
                idBus = str(input("[-] Ingresa el ID a buscar (GXX): "))

                if idBus in data:
                    os.system("cls")
                    print(f"[*] ID DEL GENERO:          {data[idBus]["id"]}")
                    print(f"[*] NOMBRE DEL GENERO:      {data[idBus]["nombre"]}")
                    os.system("pause")
                else:
                    print("[!] CODIGO NO ENCONTRADO")
                    os.system("pause")
                    
            else:
                isActiveGeneros = False
                    
                
                
                
                