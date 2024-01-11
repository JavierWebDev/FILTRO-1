import os
import func.formatos as fm
import func.corefiles.coreFormatos as cf

opcFormatos = ["Crear actor", "Listar actores", "Volver"]

formatos = {}    

def MenuFormatos():
    header = '''
    *******************************
    *  ADMINISTRADOR DE FORMATOS  *
    *******************************
    '''
    isActiveFormato = True
    while isActiveFormato:
        cf.checkFile(fm.formatos)
        data = cf.ReadFile()
        try:
            os.system("cls")
            print(header)
            
            for i, item in enumerate(opcFormatos):
                print(f"{i+1}. {item}")
            opformato = int(input("\n >) "))
        except ValueError:
            print("[!] VALOR INCORRECTO")
            os.system("pause")
        else:
            if opformato == 1:
                titulo = '''
                    *********************
                    *  AGREGAR FORMATO  *
                    *********************
                '''
                isActiveCreFormat = True
                while isActiveCreFormat:
                    os.system("cls")
                    print(titulo)
                    
                    nombre = input("[-] Ingresa nombre del formato: ")
                    
                    formato = {
                        'id':'',
                        'nombre':nombre
                    }
                    
                    idAu = str(f"F0{len(data)+1}")
                    
                    formato["id"] = idAu

                    formato.update(formato)
                    fm.New(formato)
                    rta = input("[?] Deseas ingresar otro formato? ([S] - SI | [N] - NO\n >)").upper
                    if rta != "S":
                        isActiveCreFormat = False
            
            elif opformato == 2:
                os.system("cls")
                idBus = str(input("[-] Ingresa el ID a buscar (GXX): "))

                if idBus in data:
                    os.system("cls")
                    print(f"[*] ID DEL FORMATO:          {data[idBus]["id"]}")
                    print(f"[*] NOMBRE DEL FORMATO:      {data[idBus]["nombre"]}")
                    os.system("pause")
                else:
                    print("[!] CODIGO NO ENCONTRADO")
                    os.system("pause")
            
            else:
                isActiveFormato = False
                    
                    
                
                
                
                