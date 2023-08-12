from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

class Vehiculo(BaseModel):
    id: Optional[str] = None
    marca: str
    cilindraje: int
    combustible: str
    año: int
    '''
    concesionario_id: Optional[str] = None
    '''

class Concesionario(BaseModel):
    id: Optional[str] = None
    vehiculos: List[Vehiculo] = []
    tipo_vehiculo: str
    tipo_combustible: str
    estado_vehiculo: str

vehiculos = []
concesionarios = []

@app.get('/')
def read_root():
    return {'Welcome': 'Welcome to my REST API'}

#Vehiculos

@app.post('/vehiculos/')
def crear_vehiculo(vehiculo: Vehiculo):
    vehiculo.id = str(uuid4())
    vehiculos.append(vehiculo)
    return {'message' : f'El vehiculo {vehiculo.marca}, con cilindraje {vehiculo.cilindraje} del año {vehiculo.año} y con combustible {vehiculo.combustible} ha sido creado exitosamente'}

@app.get('/vehiculos/')
def obtener_vehiculos():
    return vehiculos

@app.get('/vehiculos/{vehiculo_id}')
def obtener_vehiculo(vehiculo_id: str):
    for vehiculo in vehiculos:
        if vehiculo.id == vehiculo_id:
            return vehiculo
    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")

@app.put('/vehiculos/{vehiculo_id}')
def actualizar_vehiculo(vehiculo_id: str, vehiculo_actualizado: Vehiculo):
    for index, vehiculo in enumerate(vehiculos):
        if vehiculo.id == vehiculo_id:
            vehiculos[index] = vehiculo_actualizado
            vehiculos[index].id = vehiculo_id
            return {"message": "Vehiculo actualizado exitosamente"}
    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")

@app.delete('/vehiculos/{vehiculo_id}')
def eliminar_vehiculo(vehiculo_id: str):
    for index, vehiculo in enumerate(vehiculos):
        if vehiculo.id == vehiculo_id:
            vehiculos.pop(index)
            return {"message": "Vehiculo eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")

#Concesionarios

@app.post('/concesionarios/')
def crear_concesionario(concesionario: Concesionario):
    concesionario.id = str(uuid4())
    concesionarios.append(concesionario)
    return concesionario

'''
@app.post('/concesionarios/{concesionario_id}/agregar_vehiculo/')
def agregar_vehiculo_a_concesionario(concesionario_id: str, vehiculo_id: str):
    for concesionario in concesionarios:
        if concesionario.id == concesionario_id:
            for vehiculo in vehiculos:
                if vehiculo.id == vehiculo_id:
                    vehiculo.concesionario_id = concesionario.id
                    concesionario.vehiculos.append(vehiculo)
                    return {'message': 'Vehiculo agregado al concesionario exitosamente'}
            raise HTTPException(status_code=404, detail='Vehiculo no encontrado')
    raise HTTPException(status_code=404, detail='Concesionario no encontrado')
'''

@app.get('/concesionarios/')
def obtener_concesionarios():
    return concesionarios

@app.get('/concesionarios/{concesionario_id}')
def obtener_concesionario(concesionario_id: str):
    for concesionario in concesionarios:
        if concesionario.id == concesionario_id:
            return concesionario
    raise HTTPException(status_code=404, detail="Concesionario no encontrado")

@app.put('/concesionarios/{concesionario_id}')
def actualizar_concesionario(concesionario_id: str, concesionario_actualizado: Concesionario):
    for index, concesionario in enumerate(concesionarios):
        if concesionario.id == concesionario_id:
            concesionarios[index] = concesionario_actualizado
            concesionarios[index].id = concesionario_id
            return {"message": "Concesionario actualizado exitosamente"}
    raise HTTPException(status_code=404, detail="Concesionario no encontrado")

@app.delete('/concesionarios/{concesionario_id}')
def eliminar_concesionario(concesionario_id: str):
    for index, concesionario in enumerate(concesionarios):
        if concesionario.id == concesionario_id:
            concesionarios.pop(index)
            return {"message": "Concesionario eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Concesionario no encontrado")