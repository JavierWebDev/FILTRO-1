import os
import func.peliculas as pl
import func.corefiles.corePeliculas as cf

blockbuster = {
    'blockbuster':{
        'peliculas':{
            
        }
    }
}
cf.MY_DATABASE='data/blockbuster.json'

def New(peli : dict):
    cf.addData(peli["id"],peli)
    
def Del():
    id = input("[-] Ingrese el ID a eliminar: ")
    cf.Eliminar(id, blockbuster)
    
def search():
    idBusqueda = str(input("Ingrese el ID a Buscar (PXX): "))
    return blockbuster.get(idBusqueda, {})

def modifyMovie(llave:int, idBuscar):
    for key, item in idBuscar.items():
        if (key != "actores") and (key != "formato"):
            if bool(input(f"[?] Desea editar el campo ({key}) ? (SI [ENTER] | NO [DIGITO])\n >)")) == False:
                idBuscar[key] = input(f"[-] Ingrese {key.capitalize()}: ")
    blockbuster["blockbuster"]["peliculas"][str(llave)].update(idBuscar)