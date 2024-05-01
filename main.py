#PASOS PARA USAR PANDAS POR PRIMERA VEZ
#1. Importar Pandas donde lo quiera usar

import pandas as pd

#2. Traer los datos
tablaEncicla=pd.read_csv("./data/EstacionesEnCicla_DatosAbiertos2_1.csv")
print(tablaEncicla)

tablaSiembras=pd.read_csv("./data/PlanSiembra_dic2019.csv")
print(tablaSiembras.describe())