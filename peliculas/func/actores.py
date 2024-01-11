import func.corefiles.coreActores as cf
import os

actores = {}
cf.MY_DATABASE='data/actores.json'

def New(actor : dict):
    cf.addData(actor["id"],actor)
    
# def Del():
#     id = input("[-] Ingrese el ID a eliminar: ")
#     cf.Eliminar(id, actores)
    
# def search():
#     idBusqueda = str(input("Ingrese el ID a Buscar (PXX): "))
#     return actores.get(idBusqueda, {})
