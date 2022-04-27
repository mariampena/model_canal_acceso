# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:17:52 2022

@author: pmayaduque
"""
from opt import create_model, solve_model
from utilities import read_data
import ast

# data paths
# data_filepath = r"https://raw.githubusercontent.com/mariampena/model_canal_acceso/main/data/data.json"
data_filepath = "../data/data.json"

# read data from file
data = read_data(data_filepath)

Buques = data["Buques"]
Nodos = data["Nodos"]
Puertos = data["Puertos"]
Arcos = data["Arcos"]
Rutas = data["Rutas"]
t_viaje = data["t_viaje"]
puerto = data["puerto"]
tiempo_programado = data["tiempo_programado"]
tiempo_seguridad = data["tiempo_seguridad"]
tiempodescarga =  data["tiempodescarga"]
tiempoliberacion =  data["tiempoliberacion"] 

M=1000 #Valor muy grande que despues calcularemos bien con base en los datos del problema

model=create_model(Buques, 
                 Nodos, 
                 Puertos, 
                 Arcos,
                 Rutas,
                 t_viaje,
                 puerto,
                 tiempo_programado,
                 tiempo_seguridad,
                 tiempodescarga,
                 tiempoliberacion,
                 M)

results, termination =solve_model(model,
                optimizer='gurobi',
                mipgap=0.02,
                tee=False)

print(termination)
