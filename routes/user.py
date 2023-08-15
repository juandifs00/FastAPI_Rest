from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from uuid import uuid4
from models.user import Vehiculo, Concesionario
from schemas.user import Vehiculos, Concesionarios

user = APIRouter()

@user.get('/users', response_model=list[Vehiculos], tags=['Vehiculos'])
def obtener_vehiculos():
    return conn.execute(Vehiculo.select()).fetchall()

#Vehiculos model_dump()

@user.post('/vehiculos/', response_model=Vehiculos, tags=['Vehiculos'])
def crear_vehiculo(vehiculo: Vehiculos):
    nuevo_vehiuclo = {"marca":vehiculo.marca, "cilindraje":vehiculo.cilindraje, "combustible":vehiculo.combustible, "ano":vehiculo.ano}
    nuevo_vehiuclo["id"] = str(uuid4())
    result = conn.execute(Vehiculo.insert().values(nuevo_vehiuclo))
    print(result.lastrowid)
    #return conn.execute(Vehiculo.select().where(Vehiculo.c.id == result.lastrowid)).first()
    return "Vehiculo insertado correctamente"

@user.get('/vehiculos/{vehiculo_id}', response_model=Vehiculos, tags=['Vehiculos'])
def obtener_vehiculo(vehiculo_id: str):
    return conn.execute(Vehiculo.select().where(Vehiculo.c.id == vehiculo_id)).first()

@user.delete('/vehiculos/{vehiculo_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Vehiculos'])
def eliminar_vehiculo(vehiculo_id: str):
    conn.execute(Vehiculo.delete().where(Vehiculo.c.id == vehiculo_id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put('/vehiculos/{vehiculo_id}', response_model=Vehiculos, tags=['Vehiculos'])
def actualizar_vehiculo(vehiculo_id: str, vehiculo: Vehiculos):
    conn.execute(Vehiculo.update().values(marca = vehiculo.marca, cilindraje = vehiculo.cilindraje, 
                                          combustible = vehiculo.combustible, 
                                          ano = vehiculo.ano).where(Vehiculo.c.id == vehiculo_id))
    return conn.execute(Vehiculo.select().where(Vehiculo.c.id == vehiculo_id)).first()

'''
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