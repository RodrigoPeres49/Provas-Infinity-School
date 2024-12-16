from models import *
from db import db

veiculo_existente = db.session.query(Veiculo).first()

if not veiculo_existente:
    veiculo1 = Veiculo(marca='Volkswagen', modelo='Gol 2003 1.0', tipo_combustivel='Gasolina', bomba=0, limite=55, consumo=13)
    veiculo2 = Veiculo(marca='Fiat', modelo='Siena 2013 1.0', tipo_combustivel='Gasolina', bomba=0, limite=48, consumo=12)
    veiculo3 = Veiculo(marca='Chevrolet', modelo='Onix 2024', tipo_combustivel='Flex', bomba=0, limite=44, consumo=14)
    veiculo4 = Veiculo(marca='Ferrari', modelo='SF90 Spider', tipo_combustivel='Gasolina', bomba=0, limite=68, consumo=8)
    
    db.session.add_all([veiculo1, veiculo2, veiculo3, veiculo4])
    db.session.commit()

combustivel_existente = db.session.query(Combustivel).first()

if not combustivel_existente:
    alcool = Combustivel(tipo='Alcool', valor=4.09, tanque=0)
    gasolina = Combustivel(tipo='Gasolina', valor=5.99, tanque=0)
    
    db.session.add_all([alcool, gasolina])
    db.session.commit()    