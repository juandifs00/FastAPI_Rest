from sqlalchemy import create_engine, MetaData

#docker_ip = '172.17.0.2'
#engine = create_engine(f"mysql+pymysql://root:admin@{docker_ip}:3306/myfastapi")

engine = create_engine("mysql+pymysql://root:admin@localhost:3306/myfastapi")

meta = MetaData()

conn = engine.connect()