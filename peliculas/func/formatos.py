import func.corefiles.coreFormatos as cf
import os

formatos = {}
cf.MY_DATABASE='data/formatos.json'

def New(formato : dict):
    cf.addData(formato["id"],formato)
    
# def Del():
#     id = input("[-] Ingrese el ID a eliminar: ")
#     cf.Eliminar(id, actores)
    
# def search():
#     idBusqueda = str(input("Ingrese el ID a Buscar (PXX): "))
#     return actores.get(idBusqueda, {})
