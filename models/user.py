from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

Vehiculo = Table("Vehiculo", meta, 
    Column("id", String(255), primary_key=True),
    Column("marca", String(255)), 
    Column("cilindraje", Integer), 
    Column("combustible", String(255)) ,
    Column("ano", Integer))

Concesionario = Table("Concesionario", meta, 
    Column("id", String(255)), 
    Column("idVehiculo", String(255)), 
    Column("tipo_vehiculo", String(255)), 
    Column("tipo_combustible", String(255)),
    Column("estado_vehiculo", String(255)))

meta.create_all(engine)