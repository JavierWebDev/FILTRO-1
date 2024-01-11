import os
import func.actores as ac
import func.corefiles.coreActores as cf

opcactors = ["Crear actor", "Listar actores", "Volver"]

actores = {}    

def MenuActores():
    header = '''
    ******************************
    *  ADMINISTRADOR DE ACTORES  *
    ******************************
    '''
    isActiveActores = True
    while isActiveActores:
        cf.checkFile(ac.actores)
        data = cf.ReadFile()
        try:
            os.system("cls")
            print(header)
            
            for i, item in enumerate(opcactors):
                print(f"{i+1}. {item}")
            opActors = int(input("\n >) "))
        except ValueError:
            print("[!] VALOR INCORRECTO")
            os.system("pause")
        else:
            if opActors == 1:
                titulo = '''
                    *******************
                    *  AGREGAR ACTOR  *
                    *******************
                '''
                isActiveCreActor = True
                while isActiveCreActor:
                    os.system("cls")
                    print(titulo)
                    
                    nombre = input("[-] Ingresa nombre del actor: ")
                    
                    actor = {
                        'id':'',
                        'nombre':nombre
                    }
                    
                    idAu = str(f"A0{len(data)+1}")
                    
                    actor["id"] = idAu

                    actor.update(actor)
                    ac.New(actor)
                    rta = input("[?] Deseas ingresar otro actor? ([S] - SI | [N] - NO\n >)").upper
                    if rta != "S":
                        isActiveCreActor = False
            
            elif opActors == 2:
                os.system("cls")
                idBus = str(input("[-] Ingresa el ID a buscar (GXX): "))

                if idBus in data:
                    os.system("cls")
                    print(f"[*] ID DEL ACTOR:          {data[idBus]["id"]}")
                    print(f"[*] NOMBRE DEL ACTOR:      {data[idBus]["nombre"]}")
                    os.system("pause")
                else:
                    print("[!] CODIGO NO ENCONTRADO")
                    os.system("pause")
            
            else:
                isActiveActores = False
                    
                    
                
                
                
                