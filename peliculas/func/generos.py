import func.corefiles.coreGeneros as cf
import os

generos = {}
cf.MY_DATABASE='data/generos.json'

def New(genero : dict):
    cf.addData(genero["id"],genero)
    
# def Del():
#     id = input("[-] Ingrese el ID a eliminar: ")
#     cf.Eliminar(id, generos)
    
# def search():
#     idBusqueda = str(input("Ingrese el ID a Buscar (PXX): "))
#     return generos.get(idBusqueda, {})

