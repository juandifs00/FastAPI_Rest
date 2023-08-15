from fastapi import HTTPException, APIRouter
from config.db import conn
from uuid import uuid4
from models.user import Vehiculo, Concesionario
from schemas.user import Vehiculos, Concesionarios

user = APIRouter()

@user.get('/users')
def get_data():
    return conn.execute(Vehiculo.select()).fetchall()

#Vehiculos model_dump()

@user.post('/vehiculos/')
def crear_vehiculo(vehiculo: Vehiculos):
    nuevo_vehiuclo = {"marca":vehiculo.marca, "cilindraje":vehiculo.cilindraje, "combustible":vehiculo.combustible, "ano":vehiculo.ano}
    nuevo_vehiuclo["id"] = str(uuid4())
    result = conn.execute(Vehiculo.insert().values(nuevo_vehiuclo))
    print(result)
    return "Vehiculo insertado correctamente"


'''
@user.get('/vehiculos/')
def obtener_vehiculos():
    return vehiculos

@user.get('/vehiculos/{vehiculo_id}')
def obtener_vehiculo(vehiculo_id: str):
    for vehiculo in vehiculos:
        if vehiculo.id == vehiculo_id:
            return vehiculo
    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")

@user.put('/vehiculos/{vehiculo_id}')
def actualizar_vehiculo(vehiculo_id: str, vehiculo_actualizado: Vehiculo):
    for index, vehiculo in enumerate(vehiculos):
        if vehiculo.id == vehiculo_id:
            vehiculos[index] = vehiculo_actualizado
            vehiculos[index].id = vehiculo_id
            return {"message": "Vehiculo actualizado exitosamente"}
    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")

@user.delete('/vehiculos/{vehiculo_id}')
def eliminar_vehiculo(vehiculo_id: str):
    for index, vehiculo in enumerate(vehiculos):
        if vehiculo.id == vehiculo_id:
            vehiculos.pop(index)
            return {"message": "Vehiculo eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")

#Concesionarios

@user.post('/concesionarios/')
def crear_concesionario(concesionario: Concesionarios):
    concesionario.id = str(uuid4())
    concesionarios.userend(concesionario)
    return concesionario


@user.get('/concesionarios/')
def obtener_concesionarios():
    return concesionarios

@user.get('/concesionarios/{concesionario_id}')
def obtener_concesionario(concesionario_id: str):
    for concesionario in concesionarios:
        if concesionario.id == concesionario_id:
            return concesionario
    raise HTTPException(status_code=404, detail="Concesionario no encontrado")

@user.put('/concesionarios/{concesionario_id}')
def actualizar_concesionario(concesionario_id: str, concesionario_actualizado: Concesionario):
    for index, concesionario in enumerate(concesionarios):
        if concesionario.id == concesionario_id:
            concesionarios[index] = concesionario_actualizado
            concesionarios[index].id = concesionario_id
            return {"message": "Concesionario actualizado exitosamente"}
    raise HTTPException(status_code=404, detail="Concesionario no encontrado")

@user.delete('/concesionarios/{concesionario_id}')
def eliminar_concesionario(concesionario_id: str):
    for index, concesionario in enumerate(concesionarios):
        if concesionario.id == concesionario_id:
            concesionarios.pop(index)
            return {"message": "Concesionario eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Concesionario no encontrado")
'''