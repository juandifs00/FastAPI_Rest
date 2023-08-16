from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED
from config.db import engine
from uuid import uuid4
from models.user import Vehiculo, Concesionario
from schemas.user import Vehiculos, Concesionarios

user = APIRouter()

@user.get('/users', response_model=list[Vehiculos], tags=['Vehiculos'])
def obtener_vehiculos():
    with engine.connect() as conn:
        return conn.execute(Vehiculo.select()).fetchall()

#Vehiculos model_dump() para volverlo un diccionario

@user.post('/vehiculos/', response_model=list[Vehiculos], tags=['Vehiculos'])
def crear_vehiculo(vehiculo: Vehiculos):
    with engine.connect() as conn:
        nuevo_vehiculo = vehiculo.model_dump()
        nuevo_vehiculo["id"] = str(uuid4())
        xd = conn.execute(Vehiculo.insert().values(nuevo_vehiculo))
        return conn.execute(Vehiculo.select().where(Vehiculo.c.id == xd.lastrowid)).first()
        #return Response(status_code=HTTP_201_CREATED)

@user.get('/vehiculos/{vehiculo_id}', response_model=list[Vehiculos], tags=['Vehiculos'])
def obtener_vehiculo(vehiculo_id: str):
    with engine.connect() as conn:
        return conn.execute(Vehiculo.select().where(Vehiculo.c.id == vehiculo_id)).first()

@user.delete('/vehiculos/{vehiculo_id}', response_model=list[Vehiculos], tags=['Vehiculos'])
def eliminar_vehiculo(vehiculo_id: str):
    with engine.connect() as conn:
        conn.execute(Vehiculo.delete().where(Vehiculo.c.id == vehiculo_id))
        return Response(status_code=HTTP_204_NO_CONTENT)

@user.put('/vehiculos/{vehiculo_id}', response_model=list[Vehiculos], tags=['Vehiculos'])
def actualizar_vehiculo(vehiculo_id: str, vehiculo: Vehiculos):
    with engine.connect() as conn:
        conn.execute(Vehiculo.update().values(marca = vehiculo.marca, 
                                            cilindraje = vehiculo.cilindraje, 
                                            combustible = vehiculo.combustible, 
                                            ano = vehiculo.ano).where(Vehiculo.c.id == vehiculo_id))
        return conn.execute(Vehiculo.select().where(Vehiculo.c.id == vehiculo_id)).first()

#Concesionarios

@user.get('/concesionarios/', response_model=list[Concesionarios], tags=['Concesionarios'])
def obtener_concesionarios():
    with engine.connect() as conn:
        return conn.execute(Concesionario.select()).fetchall()

@user.post('/concesionarios/', response_model=list[Concesionarios], tags=['Concesionarios'])
def crear_concesionario(concesionario: Concesionarios):
    with engine.connect() as conn:
        nuevo_concesionario = concesionario.model_dump()
        nuevo_concesionario["id"] = str(uuid4())
        xd = conn.execute(Concesionario.insert().values(nuevo_concesionario))
        return conn.execute(Concesionario.select().where(Concesionario.c.id == xd.lastrowid)).first()
        #return Response(status_code=HTTP_201_CREATED)

@user.get('/concesionarios/{concesionario_id}', response_model=list[Concesionarios], tags=['Concesionarios'])
def obtener_concesionario(concesionario_id: str):
    with engine.connect() as conn:
        return conn.execute(Concesionario.select().where(Concesionario.c.id == concesionario_id)).first()

@user.delete('/concesionarios/{concesionario_id}', response_model=list[Concesionarios], tags=['Concesionarios'])
def eliminar_concesionario(concesionario_id: str):
    with engine.connect() as conn:
        conn.execute(Concesionario.delete().where(Concesionario.c.id == concesionario_id))
        return Response(status_code=HTTP_204_NO_CONTENT)

'''
@user.put('/concesionarios/{concesionario_id}', tags=['Concesionarios'])
def actualizar_concesionario(concesionario_id: str, concesionario: Concesionario):
    with engine.connect() as conn:
        conn.execute(Concesionario.update().values(idVehiculo = concesionario.idVehiculo, 
                                                tipo_vehiculo = concesionario.tipo_vehiculo,
                                                tipo_combustible = concesionario.tipo_combustible, 
                                                estado_vehiculo = concesionario.estado_vehiculo)).where(Concesionario.c.id == concesionario_id)
        return conn.execute(Concesionario.select().where(Concesionario.c.id == concesionario_id)).first()
'''