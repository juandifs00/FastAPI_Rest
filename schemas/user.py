from pydantic import BaseModel

class Vehiculos(BaseModel):
    id: str | None = None
    marca: str
    cilindraje: int
    combustible: str
    ano: int

class Concesionarios(BaseModel):
    id: str | None = None
    idVehiculo: str | None = None
    tipo_vehiculo: str
    tipo_combustible: str
    estado_vehiculo: str
